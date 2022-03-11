


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

alter table Dep add CONSTRAINT FK_DEmp FOREIGN KEY (Chief) REFERENCES Emp (Family);

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
