select *
from table1 t;
SELECT *
from table2 t;
SELECT *
FROM table1 t1
WHERE exists(
        SELECT *
        FROM table2 t2
        WHERE t1.column1 = t2.column1
    );
select *
from table1 t1
    inner join table2 t2 on t1.column1 = t2.column1
    and t2.column2 = 'a';
select *
from table1 t1
where t1.column1 in(
        select t2.column1
        from table2 t2
        where t2.column2 = 'a'
    );