
#1
# creating a database with the name incubyte
create database incubyte;
use incubyte;

#2
# Creating a staging table with the given records in mysql

create table records( Customer_name varchar(255), 
Cust_id varchar(18), 
Cust_open_dt date, 
Last_consulted_dt date, 
Vaccination_type char(5), 
Doctor char(255), 
state char(5), 
country char(5), 
dob date, 
active_cust char(1) );

#3
#Inserting the given value into the table

insert into records values ("Alex",123457,"20101012","20121013","MVD","PAUL","SA","USA","06031987","A"),
("Jhon",123458,"20101012","20121013","MVD","PAUL","TN","IND","06031987","A"),
("MATHEW",123459,"20101012","20121013","MVD","PAUL","WAS","PHIL","06031987","A"), 
("MATT",12345,"20101012","20121013","MVD","PAUL","BOS","NYC","06031987","A"),
("JACOB",1256,"20101012","20121013","MVD","PAUL","VIC","AU","06031987","A");

#4
# importing the staging table to hdfs by using sqoop import
sqoop import \ 
--connect jdbc:mysql://quickstart.cloudera:3306/incubyte
--username root \
--password cloudera \
--table records \ 
--m 1 \
--target-dir /recordsNew

#5
# querying and partitoning the dataset by using hive 

#Create a normal table without partitoning and have the data loaded
create table records_no_partition( Customer_name varchar(255), 
Cust_id varchar(18), 
Cust_open_dt date, 
Last_consulted_dt date, 
Vaccination_type char(5), 
Doctor char(255), 
state char(5), 
country char(5), 
dob date, 
active_cust char(1) )
row format delimited
fields terminated by ',';

load data inpath '/recordsNew/part-m-00000' into table records_no_partition

#Creating the partition table with partition on a column name
create table records( Customer_name varchar(255), 
Cust_id varchar(18), 
Cust_open_dt date, 
Last_consulted_dt date, 
Vaccination_type char(5), 
Doctor char(255), 
state char(5), 
dob date, 
active_cust char(1) )
partition by (Country char(5))
row format delimited
fields terminated by ',';

#transfer the data from normal table to the partitioned table
insert into table records
partition (Country)
select * from records_no_partition



