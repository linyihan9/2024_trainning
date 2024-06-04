#  Postgresql
##  概念
关系型数据库  
基本sql类型：int、smallint、real、double precision、char、varchar、date、time、timestamp、interval
地理sql类型:json、jsonb、line、lseg、point、polygon
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
