#  Linux  
##  磁盘管理  
pwd  显示当前目录  
fdisk -l  查看新的分区  
ll  (-a all 显示隐藏的)纵向，包含组、权限等  
ls  (-a)横向  
df  (-h Human-Readable，即使用GB、MB等易读的)查看磁盘空间情况
du  (-h)查看文件和目录的磁盘空间使用情况  
##  文件管理
mkdir  
mkdir -p file1/file2  递归创建  
mkdir -v file显示信息  
mkdir -vp {file1,file2}  
rm (-f force 强制删除 -r递归删除)删除  
cat file  将文件内容输出到控制台  
more file  逐屏输出  
less file  逐屏输出  
head file  显示头十行
tail file  后十行  
cp (源文件)  (目标文件)  复制 
find (目标文件)  当前目录下查找  
which (目标文件)  在PATH下查找  t-b）、man说明文件（参数-m）和源代码文件（参数-s），如果省略参数，则返回所有信息  
##  系统设置  
ps -aux  |||||  ps -ef  查看系统进程  
kill (-9强制) pid  杀死进程  
date  
echo $LANG  查看当前语言环境  
###  top详解  
top  查看系统cpu、内存、运行时间、交换分区、执行的线程等信息  
![](https://github.com/linyihan9/2024_trainning/blob/main/img/Linux/top.jpg)  


