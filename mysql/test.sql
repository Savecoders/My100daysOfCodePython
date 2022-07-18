
create database sql_test;

Select sql_test;

/* Create table*/
CREATE TABLE Persons (
    PersonID int,
    UserName varchar(255),
    Email varchar(255),
);

/* Add columm */
alter table Persons add edad int;

/* Delete columm */
alter table persons drop column edad;

/* Modify column email and size for characters*/
alter table persons modify email varchar(50);