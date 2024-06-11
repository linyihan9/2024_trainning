#  留言板设计  
##  功能
1.发布留言（留言内容、留言显示策略）
2.查看留言
3.删除留言
4.用户登录注册
5.回复留言
![](https://github.com/linyihan9/2024_trainning/blob/main/img/MessageBoardDetail.jpg)	
##    sql
###	用户	
create table user(user_id bigint,user_name varchar(50),user_pwd varchar(50));	
###	留言	
create table message(message_father_id bigint,message_son_id int,user_id bigint,user_name varchar(50),message_detail text,message_time datetime,message_authority int);	