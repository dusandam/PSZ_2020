# Pronalazenje skrivenog znanja 2020 - projektni zadatak

## Zadatak 1: Prikupljanje podataka

Za realizaciju ove faze koriscena je skripta populate_database.py zajedno sa repository.py
Baza je kreirana uz pomoc skripte create_database.py, a njen sadrzaj se nalazi u fajlu /analysis.database.csv.

## Zadatak 2: Analiza podataka

Rezultati ovog zadatka dobijaju se pokretanjem skripte analysis.py, i nalaze se u direktorijumu analyisis 
u fajlovima na sledeci nacin:

### A) offer_count.csv

### B) listings_per_city.csv

### C) registered.csv, unregistered.csv

### D) expensive_houses.csv, expensive_appartments.csv

### E) expensive_houses_rent.csv, expensive_appartments_rent.csv

### F) bulit_in_2019.csv

### G) most_rooms.csv, most_bathrooms.csv, largest_land_area.csv
    
## Zadatak 3: Vizuelizacija podataka

Rezultati ovog zadatka dobijaju se pokretanjem skripte visual_analysis.py, i nalaze se u direktorijumu visualization 
u fajlovima na sledeci nacin:

### A) most_present_quarters.csv, most_present_quarters.png

### B) appartment_square_meters.csv, appartment_square_meters.png

### C) year_built_statistics.csv, year_built_statistics.png

### D) ratio.csv, ratio_listings_percentage.png, ratio_number_of_listings.png, ratio_ratio.png

### E) price_stats.csv, price_stats.png, price_stats_percentage.png

    
## Zadatak 4: Implementacija linearne regresije

Linearna regresija implementirana je skriptom linear_regression.py, a rezultati su dobijeni pokretanjem skripte
test_regression_py. Skripta prima obavezne argumente tipa float: -y (godina izgradnje stana, npr. 2009) 
i -s (kvadratura stana, npr. 150). 
Kao rezultat rada, ova skripta ce ispisati opste performanse regresije u 
vidu srednje kvadratne greske dobijene na osnovu uporedjivanja stvarnih vrednosti seta podataka za testiranje
sa vrednostima dobijenim predikcijom ovog modela. Greska je procenjena na normalizovanim vrednostima ovih podataka
(izmedju -1 i 1).
Drugi rezultat rada je predikcija cene stana za vrednosti unetih podataka.    

## Zadatak 5: Implementacija support vector machine algoritma

Support Vetor Machine algoritam sa dve kernel funkcije obavlja visestruku klasifikaciju nad ulaznim
skupom podataka (nekretnine na prodaju). Implementiran je uz koriscenje paketa sklearn.
Skripta prima obavezne argumente tipa float: -y (godina izgradnje stana, npr. 2009), -s (kvadratura stana, npr. 150)
i -t (ukupan broj soba, npr. 4).
Izlazne vrednosti podeljene su u vise klasa: 'under_50', '50_to_100', '100_to_150', '150_to_200', 'over_200', u 
zavisnosti od opsega u kome se cena nekretnine nalazi. 
Za ovaj algoritam koriscene su dve kernel funkcije, linearna i polinomijalna.
Kao rezultat ove faze dostavljaju se performanse algoritma sa svakom od kernel funkcija nad test setom podataka.
Drugi rezultat je klasifikacija na osnovu ulaznim podataka.



