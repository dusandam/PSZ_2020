CREATE TABLE "realty"
(
 "realty_id"       integer NOT NULL GENERATED ALWAYS AS IDENTITY (
 start 1
 ),
 "type"            varchar(40) NULL,
 "offer_type"      varchar(40) NULL,
 "square_meters"   float NULL,
 "year_built"      int NULL,
 "land_area"       float NULL,
 "total_floors"    int NULL,
 "floor"           int NULL,
 "registered"     boolean NULL,
 "heating_type"    varchar(50) NULL,
 "total_rooms"     int NULL,
 "total_bathrooms" int NULL,
 "price"           float NULL,
 "city"        varchar(50) NULL,
 "quarter"     varchar(50) NULL,
 "webpage"     varchar(50) NULL,
 CONSTRAINT "PK_Supplier" PRIMARY KEY ( "realty_id" )
);






