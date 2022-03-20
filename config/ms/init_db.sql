create table Dep -- отношение описывающее отделы (департаменты) которым принадлежат АС
(
    Code  int primary key,      -- код отдела
    Name  varchar(50) not null, -- название отдела
    Chief varchar(15)           -- глава (начальник) отдела
);

create table Emp -- отношение описывающее сотрудников компании
(
    Family Varchar(15) primary key, -- Фамилия сотрудника
    Dep    int not null,            -- отдел, где работает сотрудник
    Salary int,                     -- оклад
    CONSTRAINT FK_EDep FOREIGN KEY (Dep) REFERENCES Dep (Code) on update cascade on delete cascade
);

create table ASt -- отношение описывающее автоматизированные системы
(
    Code    int primary key, -- код системы (униклаьный)
    Name    varchar(50),     -- наименование/название системы
    Cost_in float,           -- стомость внедрения системы (единовременная)
    Cost_pm float,           -- стоимость поддержки системы (ежемесячная)
    UPSys   int,             -- система, в которую входит данная. Отражает вложенность АС друг в друга
    Dep     int,             -- отдел, к которому относится система
    CONSTRAINT FK_UPSys FOREIGN KEY (UPSys) REFERENCES ASt (Code),
    CONSTRAINT FK_SDep FOREIGN KEY (Dep) REFERENCES Dep (Code) on update cascade on delete cascade
);

create table Vun -- отношение описывающее риски в автоматизированной системе
(
    Code     int primary key, -- код уязвимости (уникальный)
    ASt      int,             -- код автоматизированной системы, к которой относится риск
    Discript varchar(50),     -- описание риска
    Cost     int,             -- численная оценка риска
    CONSTRAINT FK_ASt FOREIGN KEY (ASt) REFERENCES ASt (Code) on update cascade on delete cascade
);

create table Emp_Sys -- отношение описывающее сотрудников компании
(
    Emp Varchar(15) not null, -- Фамилия сотрудника
    ASt int         not null, -- название осистемы, с которой он работает
    PRIMARY KEY (Emp, ASt),
    CONSTRAINT FK_ES FOREIGN KEY (Emp) REFERENCES Emp (Family),
    CONSTRAINT FK_SE FOREIGN KEY (ASt) REFERENCES ASt (Code)
);

insert into Dep
values (1, 'D1', 'Ivanov'),
       (2, 'D2', 'Petrov'),
       (3, 'D3', null),
       (4, 'D4', 'Ivanov'),
       (5, 'D5', 'Ivanov'),
       (6, 'D6', 'Smirnov'),
       (7, 'D7', null);

insert into Emp
values ('Ivanov', 4, 150000),
       ('Petrov', 2, null),
       ('Smirnov', 5, 120000),
       ('Kuznetsov', 1, 70000),
       ('Losev', 1, null),
       ('Semenov', 4, 80000);

alter table Dep
    add CONSTRAINT FK_DEmp FOREIGN KEY (Chief) REFERENCES Emp (Family);

insert into ASt
values (1, 'AS 1', 50000, 9000, null, 4),
       (2, 'AS 2', null, 3000, null, 4),
       (3, 'AS 1.1', 30000, null, 1, 4),
       (4, 'AS 1,2', null, 7000, 1, 5),
       (5, 'AS 1.3', 70000, 9000, 1, 5),
       (6, null, 10000, 12000, 3, 5),
       (7, null, 20000, null, 6, 2),
       (8, 'AS 1.1.2', 10000, null, 3, null);

insert into Vun
values (1, null, 'V1', 5),
       (2, 1, 'V2', 2),
       (3, 1, 'V3', 3),
       (4, 2, 'V4', null),
       (5, null, 'V5', 5),
       (6, 3, 'V4', null),
       (7, 2, 'V1', null);

insert into Emp_Sys
values ('Ivanov', 1),
       ('Ivanov', 2),
       ('Ivanov', 3),
       ('Petrov', 1),
       ('Petrov', 3),
       ('Kuznetsov', 1),
       ('Kuznetsov', 2),
       ('Semenov', 1);

create table S
(
    SN    int,
    STAT  varchar(255) NOT NULL,
    SNAME varchar(255) NOT NULL,
    CITY  varchar(255),
    PRIMARY KEY (SN)
);

create table P
(
    PN     int,
    PNAME  varchar(255) NOT NULL,
    COLOR  varchar(255),
    WEIGHT float        NOT NULL,
    CITY   varchar(255),
    PRIMARY KEY (PN)
);

create table J
(
    JN    int,
    JNAME varchar(255) NOT NULL,
    CITY  varchar(255),
    PRIMARY KEY (JN)
);

create table SPJ
(
    SN  int,
    PN  int,
    JN  int,
    QTY int NOT NULL,
    PRIMARY KEY (SN, PN, JN),
    FOREIGN KEY (SN) references S (SN),
    FOREIGN KEY (PN) references P (PN),
    FOREIGN KEY (JN) references J (JN)
);

create table SPJ2
(
    SN  int,
    PN  int,
    JN  int,
    QTY int NOT NULL,
    PRIMARY KEY (SN, PN, JN),
    FOREIGN KEY (SN) references S (SN),
    FOREIGN KEY (PN) references P (PN),
    FOREIGN KEY (JN) references J (JN)
);

INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('1', 'headlight', 'red', '2000', 'London');
INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('2', 'Cowling', 'gray', '15000', 'Moscow');
INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('3', 'alarm', 'black', '3000', 'Harbin');
INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('4', 'phone', 'red', '3000', 'Harbin');
INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('5', 'panel', 'red', '3000', 'London');
INSERT INTO P (PN, PNAME, COLOR, WEIGHT, CITY)
VALUES ('6', 'alarm', 'gray', '3000', 'Saint-Petersburg');


INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('111', 'post_1', 'Manufacturer of products', 'Saint-Petersburg');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('222', 'post_2', 'Official dealer', 'Harbin');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('333', 'post_3', 'Innovative product', 'Voronezh');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('444', 'post_4', 'Official dealer', 'Moscow');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('555', 'post_5', 'Innovative product', 'Saint-Petersburg');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('666', 'post_6', 'Dealer', 'London');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('000', 'post_0', 'StartUP', 'London');
INSERT INTO S (SN, SNAME, STAT, CITY)
VALUES ('777', 'post_7', 'Manufacturer of products', 'London');


INSERT INTO J (JN, JNAME, CITY)
VALUES ('11', 'zakaz_1', 'Berlin');
INSERT INTO J (JN, JNAME, CITY)
VALUES ('22', 'zakaz_2', 'Saint-Petersburg');
INSERT INTO J (JN, JNAME, CITY)
VALUES ('33', 'zakaz_3', 'London');
INSERT INTO J (JN, JNAME, CITY)
VALUES ('44', 'zakaz_4', 'Harbin');
INSERT INTO J (JN, JNAME, CITY)
VALUES ('55', 'zakaz_5', 'London');
INSERT INTO J (JN, JNAME, CITY)
VALUES ('66', 'zakaz_6', 'London');


INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('111', '2', '66', 400);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('111', '3', '22', 5000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('111', '3', '66', 250);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('222', '2', '11', 3500);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('222', '3', '11', 700);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('222', '3', '22', 200);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('222', '4', '44', 500);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('222', '6', '33', 500);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('333', '1', '33', 1000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('333', '4', '55', 250);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('444', '1', '11', 400);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('444', '2', '22', 15000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('444', '3', '22', 15000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('555', '3', '22', 350);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('555', '2', '33', 1000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('666', '6', '33', 400);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('666', '4', '44', 300);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '1', '44', 500);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '1', '55', 250);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '2', '33', 750);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '2', '44', 600);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '2', '55', 1000);
INSERT INTO SPJ (SN, PN, JN, QTY)
VALUES ('777', '3', '22', 3500);

INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('111', '1', '66', 400);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('111', '2', '22', 400);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('111', '3', '22', 5000);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('111', '3', '66', 250);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('222', '2', '44', 3500);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('222', '3', '22', 200);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('222', '4', '44', 500);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('222', '6', '33', 500);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('333', '1', '33', 1000);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('333', '4', '55', 250);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('444', '3', '22', 15000);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('555', '3', '22', 350);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('666', '6', '33', 400);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('666', '4', '44', 300);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('777', '1', '44', 500);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('777', '1', '55', 250);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('777', '2', '33', 750);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('777', '2', '55', 1000);
INSERT INTO SPJ2 (SN, PN, JN, QTY)
VALUES ('777', '3', '22', 3500);

create table Wr
(
    Code   int primary key,
    Fio    varchar(50) not null unique,
    City   varchar(15),
    Salary int
);

create table Fr
(
    Code   int primary key,
    Name   varchar(50) not null unique,
    Fio    varchar(50),
    City   varchar(15),
    Bugjet int
);

create table Works -- отношение описывающее сотрудников компании
(
    W      int,
    F      int,
    Cost   int,
    Status varchar(15),
    PRIMARY KEY (W, F),
    CONSTRAINT FK_ES FOREIGN KEY (F) REFERENCES Fr (Code),
    CONSTRAINT FK_SE FOREIGN KEY (W) REFERENCES Wr (Code)
);

create table Works1 -- отношение описывающее сотрудников компании
(
    W      int,
    F      int,
    Cost   int,
    Status varchar(15),
    PRIMARY KEY (W, F),
    CONSTRAINT FK_ES1 FOREIGN KEY (F) REFERENCES Fr (Code),
    CONSTRAINT FK_SE1 FOREIGN KEY (W) REFERENCES Wr (Code)
);

insert into Wr
values (1, 'A', 'Msc', 20000),
       (2, 'B', 'Spb', Null),
       (3, 'C', Null, 10000),
       (4, 'D', 'Msc', 50000),
       (5, 'E', 'Msc', 10000),
       (6, 'F', 'Spb', 20000),
       (7, 'G', 'Tver', 10000);

insert into Fr
values (111, 'FA', 'B', 'Msc', 500000),
       (222, 'FB', 'K', 'Spb', 300000),
       (333, 'FC', 'A', 'Msc', Null),
       (444, 'FD', 'G', 'Msc', 400000),
       (555, 'FE', 'E', Null, 600000),
       (666, 'FG', Null, 'Ekb', 100000);

insert into Works
values (1, 111, 10000, 'End'),
       (1, 333, 10000, 'In progress'),
       (1, 222, null, 'In progress'),
       (2, 111, 10000, null), --!!!
       (3, 111, null, 'End'),
       (3, 333, 10000, 'Plan'),
       (4, 111, 10000, null),
       (4, 333, 10000, null),
       (6, 555, null, 'Before'),
       (4, 555, 20000, 'End'),
       (2, 555, 10000, 'In progress');

insert into Works1
values (1, 111, 10000, 'End'),
       (1, 333, 10000, 'In progress'),
       (1, 222, null, 'In progress'),
       (2, 111, 10000, null),
       (3, 111, null, 'End'),
       (3, 333, 10000, 'Plan'),
       (4, 111, 10000, null),
       (4, 333, 10000, null);
