-- drop database pokemones;
-- create database pokemones;

use pokemones;

-- create table pokemon (
--     id int not null primary key,
--     name varchar(20),
--     height int,
--     weight int,
--     picture varchar(150)

-- );

-- create table trainer(
--     name varchar(20) not null primary key,
--     town varchar(20)
-- );

-- create table trainer_of_pokemon(
--     id_pokemon int ,
--     id_trainer varchar(20),

--     foreign key (id_pokemon) references pokemon(id),
--     foreign key (id_trainer) references trainer(name),
--     primary key(id_pokemon,id_trainer)
-- );

-- create table types(
--     name varchar(20) primary key

-- );

-- create table type_pokemon(
--     type_id varchar(20),
--     pokemon_id int ,

--     foreign key (type_id) references types(name),
--     foreign key (pokemon_id) references pokemon(id),
--     primary key(type_id,pokemon_id)   
-- );

select * from pokemon;
-- -- select * from trainer;
-- select * from trainer_of_pokemon;
-- select *  from types;
-- select * from type_pokemon;
-- select * from trainer;