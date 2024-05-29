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

##  docker-compose  
https://docs.docker.com/reference/cli/docker/compose/config/
Docker Compose 就是为了**简化多容器配置和管理工作**而生的，可以简化大量重复的手动工作，具有以下主要特点：  
> 提供工具用于定义和运行多个docker容器应用  
> 使用yaml文件来配置应用服务( docker-compse.yml )  
> 可以通过一个简单的命令 docker-compse up 可以按照依赖关系启动所有服务  
> 可以通过一个简单的命令 docker-compose down 停止所有服务  
> 当一个服务需要的时候，可以很简单地通过 --scale 进行扩容  

使用 Compose 基本上只要三步:  
> 通过编辑 Dockerfile 定义应用程序发布所需的运行环境  
> 通过编辑 docker-compose.yml 文件定义多个容器一起运行的环境和相互关系  
> 运行 docker-compose up 开始你的整个应用系统  

