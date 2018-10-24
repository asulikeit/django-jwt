create role testusr LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
create database "TestusrDb" with owner = testusr ENCODING = 'UTF8' CONNECTION LIMIT = -1;
alter role testusr with password 'password1!';