drop table if exists persons;
drop table if exists address_1;

create table persons(
id serial primary key,
name text,
date_of_birth date
);


insert into persons (name, date_of_birth) values
('Dan Scott', '1956-11-25'),
('Lisa Scott', '1999-11-25'),
('Lily Scott', '1998-11-25'),
('Ting','1979-09-03');

CREATE table address_1
    (friend_id int primary key not null,
    house_number varchar(20),
    street_name varchar(50),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    primary_address boolean);

update persons
set date_of_birth = '1997-09-08'
where name = 'Lisa Scott'
and date_of_birth = '1999-11-25'

insert into persons(name, date_of_birth) values
('Vivi', '2000-04-06'),
('Susan','1985-05-30');

delete from persons
where id in
	(
	select id from 
		(select id,
				row_number() OVER (PARTITION BY(name,date_of_birth) order by id) as row_num
		 from persons
		) as t
 	where row_num > 1
	)		

Alter table persons
      add column  "As of today's age" not null %s"years%smonth"%sdays"old"
	  where = today() - date_of_birth;

/*

select * from persons;
select * from address_1;

*/




