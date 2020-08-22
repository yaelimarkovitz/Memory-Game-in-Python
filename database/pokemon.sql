drop database pokemones;
create database pokemones;

use pokemones;


create table pokemon (
    id int not null primary key,
    name varchar(20),
    type varchar(20),
    height int,
    weight int

);


create table trainer(
    name varchar(20) not null primary key,
    town varchar(20)
);


create table trainer_of_pokemon(
    id_pokemon int ,
    id_trainer varchar(20),

    foreign key (id_pokemon) references pokemon(id),
    foreign key (id_trainer) references trainer(name)
);

-- select * from pokemon;
-- select * from trainer;
-- select * from trainer_of_pokemon;