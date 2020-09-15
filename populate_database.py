from bs4 import BeautifulSoup
import requests

from repository import Repository
from lxml.html import fromstring

from itertools import cycle


def get_proxies():
    url='https://free-proxy-list.net/'
    response=requests.get(url)
    parser=fromstring(response.text)
    proxies=set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy=":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def populate():
    total_pages=600
    variants=['https://www.nekretnine.rs/stambeni-objekti/stanovi/lista/po-stranici/10/stranica/',
              'https://www.nekretnine.rs/stambeni-objekti/kuce/lista/po-stranici/10/stranica/']
    proxies=get_proxies()
    proxy_pool=cycle(proxies)

    for variant in variants:
        for page in range(total_pages):
            print('Current page number: ' + str(page))
            search_results_url=variant + str(page + 1)
            try:
                proxy=next(proxy_pool)
                response=requests.get(search_results_url)
            except:
                try:
                    response=requests.get(search_results_url)
                except:
                    print('Skipping. Connnection error')
                    break
            soup=BeautifulSoup(response.content, "html.parser")
            properties=soup.findAll('div', {'class': 'placeholder-preview-box ratio-1-1'})

            for prop in properties:
                url='https://www.nekretnine.rs' + prop.contents[1].attrs['href']

                from threading import Thread
                import threading
                import sys
                from queue import Queue

                concurrent=len(properties)

                def run():
                    while True:
                        url=q.get()
                        realty=requests.get(url)
                        innerSoup=BeautifulSoup(realty.content, "html.parser")
                        realty_props=get_props(innerSoup)
                        try:
                            price=get_price(innerSoup)
                        except Exception as e:
                            price = None
                            print(e)
                        location_content=innerSoup.findAll('h3', {'class': 'stickyBox__Location'})
                        try:
                            location=location_content[0].contents[0]
                        except Exception as e:
                            print(e)
                            location = None
                        heating=get_heating(innerSoup)
                        num_of_bathrooms=get_bathrooms(innerSoup)
                        city=None
                        quarter=None
                        if (location is not None) and (',' in location):
                            location=location.split(',', 1)
                            city=location[0].strip()
                            quarter=location[1].strip()
                        else:
                            city=location
                            quarter = None
                        transaction=None
                        category=None
                        square_metrics=None
                        land_area=None
                        registered=None
                        number_of_rooms=None
                        total_floors=None
                        floor=None
                        year_built=None
                        try :
                            contents_=realty_props.contents[1::2]
                        except:
                            print('no content')
                            continue;
                        for content in contents_:
                            if 'Transakcija' in content.contents[0]:
                                if 'Prodaja' in content.contents[0]:
                                    transaction='prodaja'
                                else:
                                    transaction='izdavanje'
                            if 'Kategorija' in content.contents[0]:
                                # stanovi mogu biti i garsonjere i dupleksi
                                if 'kuća' in content.contents[0].lower():
                                    category='kuca'
                                else:
                                    category='stan'
                            if 'Kvadratura' in content.contents[0]:
                                square_metrics=content.contents[0]
                                square_metrics=square_metrics.replace('Kvadratura:', '')
                                square_metrics=square_metrics.replace('m²', '')
                                square_metrics=square_metrics.strip()
                                square_metrics=float(square_metrics)
                            if 'Površina zemljišta' in content.contents[0]:
                                land_area=content.contents[0]
                                land_area=land_area.replace('Površina zemljišta:', '')
                                land_area=land_area.replace('m²', '')
                                land_area=land_area.strip()
                                land_area=float(land_area)
                            if 'Uknjiženo' in content.contents[0]:
                                if 'Da' in content.contents[0]:
                                    registered=True
                                else:
                                    registered=False
                            if 'Ukupan broj soba' in content.contents[0]:
                                number_of_rooms=content.contents[0]
                                number_of_rooms=number_of_rooms.replace('Ukupan broj soba:', '')
                                number_of_rooms=number_of_rooms.strip()
                                try:
                                    number_of_rooms=float(number_of_rooms)
                                except ValueError:
                                    number_of_rooms=None
                            if 'Ukupan broj spratova' in content.contents[0]:
                                total_floors=content.contents[0]
                                total_floors=total_floors.replace('Ukupan broj spratova:', '')
                                total_floors=total_floors.strip()
                                try:
                                    total_floors=float(total_floors)
                                except ValueError:
                                    total_floors=None
                            if 'Godina izgradnje' in content.contents[0]:
                                year_built=content.contents[0]
                                year_built=year_built.replace('Godina izgradnje:', '')
                                year_built=year_built.strip()
                                year_built=int(year_built)
                            if 'Sprat' in content.contents[0]:
                                floor=content.contents[0]
                                if 'prizemlje' in content.contents[0].lower():
                                    floor=0
                                else:
                                    floor=floor.replace('Sprat:', '')
                                    floor=floor.strip()
                                    try:
                                        floor=float(floor)
                                    except ValueError:
                                        floor=None
                        data=(category,
                              transaction,
                              square_metrics,
                              year_built,
                              land_area,
                              total_floors,
                              floor,
                              registered,
                              heating,
                              number_of_rooms,
                              num_of_bathrooms,
                              price,
                              city,
                              quarter)
                        repository=Repository()
                        repository.insert_data(data)

                        q.task_done()
                        break

                def get_heating(innerSoup):
                    heating_content=innerSoup.findAll('div', {'class': 'property__main-details'})
                    try:
                        heating_content=heating_content[0].contents[1].contents
                    except Exception as e:
                        print(e)
                        return None
                    for content in heating_content[1::2]:
                        if 'Grejanje' in content.text:
                            heating=content.text.replace('Grejanje:', '')
                            heating=heating.replace('-', '')
                            heating=heating.strip()
                            if heating == '':
                                return None
                            return heating
                    return None

                def get_bathrooms(innerSoup):
                    heating_content=innerSoup.findAll('div', {'class': 'property__main-details'})
                    try:
                        heating_content=heating_content[0].contents[1].contents
                    except Exception as e:
                        print(e)
                        return None
                    for content in heating_content[1::2]:
                        if 'Kupatilo' in content.text:
                            heating=content.text.replace('Kupatilo:', '')
                            number=heating.strip()
                            if number == '-':
                                return None
                            try:
                                return float(number)
                            except ValueError:
                                return None
                    return None

                def get_price(innerSoup):
                    price_content=innerSoup.findAll('h4', {'class': 'stickyBox__price'})
                    try:
                        price=price_content[0].contents[0]
                    except Exception as e:
                        print(e)
                        return None
                    if 'dogovor' in price.lower():
                        return None
                    price=price.replace('EUR', '')
                    price=price.replace(' ', '')
                    try:
                        return float(price)
                    except ValueError:
                        return None

                def get_props(innerSoup):
                    amenities_props=innerSoup.findAll('div', {'class': 'property__amenities'})
                    for prop in amenities_props:
                        if prop.contents[1].text == 'Podaci o nekretnini':
                            return prop.contents[3]

                try:
                    threads=[]
                    q=Queue(concurrent)
                    t=Thread(target=run)
                    t.daemon=True
                    threads.append(t)
                    t.start()

                    try:
                        q.put(url)
                        q.join()
                    except KeyboardInterrupt:
                        sys.exit(1)

                    t.join()
                except Exception as e:
                    print(url)
                    print(e)
                    continue


repository=Repository()
# repository.empty_database()
populate()
print('SUCCESS')