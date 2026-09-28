create schema rosdb;
use rosdb;
create table turtlepos(
	id varchar(20),
    x float,
    y float,
    theta float,
    time datetime default current_timestamp
);
    
