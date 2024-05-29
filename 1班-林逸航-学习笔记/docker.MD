#  docker  
##  基本操作  
docker search xxx  查询版本  
docker pull xxx  拉取镜像  
docker images  查看镜像  
docker run --name xxx (-p 80:80) xxx  运行镜像  
选项：
> –name mysql	 启动容器的名字  
> -d	 后台运行  
> -p 3306:3306	 将容器的 3306 (后面那个) 端口映射到主机的 3306 (前面那个) 端口  
> –restart unless-stopped	 容器重启策略  
> -v /mydata/mysql/log:/var/log/mysql	将日志文件夹挂载到主机  
> -v /mydata/mysql/data:/var/lib/mysql	将mysql储存文件夹挂载到主机  
> -v /mydata/mysql/conf:/etc/mysql	将配置文件夹挂载到主机  
> -e MYSQL_ROOT_PASSWORD=root	 设置 root 用户的密码  
docker stop  
docker rm  
docker ps  
docker ps -a   
docker exec -it  进入容器内部  

