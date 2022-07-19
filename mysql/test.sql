
create database sql_test;

USE sql_tes;

/* Create table*/
CREATE TABLE Persons (
    PersonID int,
    UserName varchar(255),
    Email varchar(255),
);

show columns from Persons;

/* Add columm */
alter table Persons add edad int;

/* Delete columm */
alter table Persons drop column edad;

/* Modify column email and size for characters*/
alter table Persons modify email varchar(50);

insert into Persons (PersonID, UserName, Email);

values (1, 'Save', 'Salvador75WF@gmail.com')