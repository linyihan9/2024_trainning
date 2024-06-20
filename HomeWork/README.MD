#	数据清洗
1.数据下载		
2.数据清洗			
3.数据存储			
4.数据应用		
```mermaid
graph TD;
下载数据-->解压数据;
解压数据-->解析数据;
解析数据-->分析data_info.json;
解析数据-->根据data_info.json寻找相应data;
解析数据-->插入数据至数据库;	
分析data_info.json-->根据data_info.json寻找相应data;
根据data_info.json寻找相应data-->插入数据至数据库;	
插入数据至数据库-->查询相应数据;
```
##	数据下载	
url、button	
下载路径		
数据过大，采用分块下载	
多线程运行		
##	交互
数据下载	储存包名和hash	自增ID
后续使用ID进行管理	
##	数据存储
###	版本一	
jpg存路径、存时间戳		
点云二进制存路径、存文件大小、存时间戳		
四条json数据直接存json数据	
##	sql	
![](https://github.com/linyihan9/2024_trainning/blob/main/img/DataClean.jpg)	