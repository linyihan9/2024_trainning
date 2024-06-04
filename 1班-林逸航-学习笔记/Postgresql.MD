#  Postgresql
##  概念
关系型数据库  
基本sql类型：int、smallint、real、double precision、char、varchar、date、time、timestamp、interval、json、jsonb
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

