SELECT
    *
FROM
    table1;

SELECT
    *
FROM
    table2;

SELECT
    *
FROM
    table3;

SELECT
    *
FROM
    table_mate_view_1;

SELECT
    *
FROM
    table_mate_view_2;

   
create materialized view joined as 
select t1.id,t1.column1,t1.column2,t1.column3 from table_mate_view_1 t1 inner join table_mate_view_2 t2 on t1.column2=t2.column2;

--
;

update table2 set column2='up';
update table1 set column2='upe';


refresh materialized view table_mate_view_1;
refresh materialized view table_mate_view_2;
refresh materialized view joined;

select * from joined where id in (1,3,5);