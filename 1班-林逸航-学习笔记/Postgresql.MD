#  Postgresql
##  概念
关系型数据库  
基本sql类型：int、smallint、real、double precision、char、varchar、date、time、timestamp、interval
地理sql类型:json、jsonb、line、lseg、point、polygon      
##     类型
###  real
浮点数类型，可以存储单精度浮点数（32位）  
###  double precision
更高精度的浮点数类型，占用8个字节  
###  circle
CIRCLE(point,radius),point是一个二元组(x,y)，表示圆心坐标，radius表示圆半径  
###  json|jsonb
json存储非结构化数据，jsonb存储二进制的json数据
查询json
```
SELECT json_column->>'name' AS name, json_column->>'age' AS age, json_column->'address'->>'city' AS city
FROM example_table
WHERE json_column @> '{"name": "John Smith"}';
```
```
 name        | age |   city
-------------+-----+----------
 John Smith  | 30  | New York
```
### line
line 类型表示在二维平面中的一条直线，包括其方向和位置等信息  
line可以存储空间数据，如地图上的道路、边界等  
line可以计算几何关系，使用postgis扩展，可以对line数据类型进行各种几何计算，如计算两条线交点、计算线段长度等  
line可以进行数据分析  
```
CREATE TABLE example_table (
    id SERIAL PRIMARY KEY,
    line_column LINE
);

INSERT INTO example_table (line_column)
VALUES ('{1, 1, 2, 2}');
```
```
SELECT ST_AsText(line_column) AS line, ST_Length(line_column) AS length
FROM example_table;
```
```
        line         |    length
---------------------+--------------
 LINESTRING(1 1,2 2) | 1.4142135624
```
### lseg
lseg 类型表示在二维平面中的一条线段，包括其起点和终点的坐标信息    
```
CREATE TABLE example_table (
    id SERIAL PRIMARY KEY,
    lseg_column LSEG
);

INSERT INTO example_table (lseg_column)
VALUES ('[(1, 1), (2, 2)]');
```
###    point
```
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    position POINT
);
INSERT INTO locations (position) VALUES (point(1.0, 2.0));
INSERT INTO locations (position) VALUES (point(3.0, 4.0));
或者按照上面的其他的写法一样
insert into locations(position) values('(1.0,2.0)');
```
###    polygon
```
CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    shape POLYGON
);
INSERT INTO areas (shape) VALUES
    ('((0,0),(0,10),(10,10),(10,0),(0,0))'),
    ('((5,5),(5,15),(15,15),(15,5),(5,5))');
```
```
SELECT id, ST_Area(shape) AS area FROM areas;
```
```
 id |   area
----+----------
  1 | 100.0000
  2 | 100.0000
```
###    serial  
自动递增序号
```
CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   email VARCHAR(255) NOT NULL
);
```


##  基本操作
###  进入docker的postgresql内部
```
docker exec -it postgres bash  在容器内启动一个交互式终端  
psql -U postgres  连接数据库
```
###  插入
```
CREATE TABLE weather (
    city            varchar(80),
    temp_lo         int,           -- 最低温度
    temp_hi         int,           -- 最高温度
    prcp            real,          -- 湿度
    date            date
);
```
###    查询所有表
```
select * from pg_tables;
```

##    schema    
在SQL环境下，schema就是数据库对象的集合，所谓的数据库对象也就是常说的表，索引，视图，存储过程等。在schema之上的，就是数据库的实例，也就是通常create databases获得的东西。也就是说一个schema 实例 可以有多个schema, 可以给不同的用户创建不同的schema,并且他们都是在同一数据库实例下面。    
PostgreSQL schema是其独有的一个强大的功能，它可以使一个单独的数据库实例中包含多个独立的、命名空间互相隔离的区域。这个功能让多个应用程序可以在同一个数据库实例中运行，而不会相互干扰。    
schema是由一组表、视图、序列、函数、索引等对象组成的，这些对象也被称为schema中的命名空间。   
###     创建schema    
```
create schema schema_name;
```
###    选择schema    
```
set schema_path to schema_name;
```
###    schema控制权限
```
grant privilege on schema_name to role_name;
```
privilege可以是select、insert、update、delete、usage等权限    
###    创建用户    
```
create user user_name with password '123456';
```
###    查看所有schema
```
\dn
```
##    基本用法    
和mysql差不多    
###    Like中的%和_
like '100%'    找出开头为100的    
like '100_'    找出前面三位为100的四位数
###    Limit和offset    
select * from user limit 4 offset 2;    
找出user表中，从第三条开始读取四条数据    


