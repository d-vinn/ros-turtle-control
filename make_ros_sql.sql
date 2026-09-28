create schema rosdb;
use rosdb;
create table turtlepos(
	id varchar(20),
    x int,
    y int,
    theta int,
    time datetime default current_timestamp
);
    
