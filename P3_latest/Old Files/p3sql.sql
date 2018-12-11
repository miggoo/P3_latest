
create database clia0918_db;

use clia0918_db;
select * from allposdata201809 As JSON;


use clia0918_db;
select * from caallfacsdata201809edited1cafacs20181;
select * from caallfacsdata201809edited1 As JSON;

use clia0918_db;
select * from cacensusdata2018upper4;

SELECT * FROM cacensusdata2018upper4 FULL LEFT JOIN cafacs2018 ON cafacs2018.CITY_NAME LIKE CONCAT('%', cacensusdata2018upper4.Geography, '%');