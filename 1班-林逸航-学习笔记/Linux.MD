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
**第一行是任务队列信息，跟 uptime 命令的执行结果类同，具体参数说明如下：**  
> 19:40:19 — 指当前系统时间  
> up 35 days, 20:32 — 表示系统已经运行了35天20小时32分钟（是指在这期间系统没有重新启动过，持续运行）  
> 1 users — 当前有1个用户登录系统  
> load average: 0.00, 0.00, 0.00 — load average后面的三个数分别是1分钟、5分钟、15分钟的负载情况。  
> load average数据是每隔5秒钟检查一次活跃的进程数，然后按特定算法计算出的数值。如果这个数除以逻辑CPU的数量，结果高于5的时候就表明系统在超负荷运转了。  

**第二行，Tasks — 任务（进程），具体信息说明如下：**  
> 系统现在共有81个进程，其中处于运行中的有1个，80个在休眠，stoped状态的有0个，zombie状态（僵尸）的有0个。  

**第三行，cpu状态信息，具体属性说明如下：**  
> us (user time)：用户空间程序的 CPU 使用率。  
> sy (system time)：内核空间的 CPU 使用率。  
> ni (nice time)：带有 nice 值的用户进程的 CPU 使用率。  
> id (idle time)：空闲时间，CPU 没有任务处理时的百分比。  
> wa (I/O wait time)：等待 I/O 操作完成的时间。  
> hi (hardware interrupt time)：硬件中断处理时间。  
> si (software interrupt time)：软件中断处理时间。  
> st (steal time)：被虚拟机管理程序偷走的时间。  

**第四行, Mem内存状态**  

**第五行，swap交换分区信息，具体信息说明如下：**  
> 0k total — 交换区总量（0K）  
> 0k used — 使用的交换区总量（0K）  
> 0k free — 空闲交换区总量（0K）  
> 401672k cached — 缓冲的交换区总量（383M）   

**第六行，空行。**

**第七行以下：各进程（任务）的状态监控，列信息说明如下：**
> PID — 进程id  
> USER — 进程所有者  
> PR — 进程优先级  
> NI — nice值。负值表示高优先级，正值表示低优先级  
> VIRT — 进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES  
> RES — 进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA  
> SHR — 共享内存大小，单位kb  
> S — 进程状态。D=不可中断的睡眠状态 R=运行 S=睡眠 T=跟踪/停止 Z=僵尸进程  I=空闲    
> %CPU — 上次更新到现在的CPU时间占用百分比  
> %MEM — 进程使用的物理内存百分比  
> TIME+ — 进程占用的CPU时间总计，单位1/100秒  
> COMMAND — 进程名称（命令名/命令行）  
![](https://github.com/linyihan9/2024_trainning/blob/main/img/Linux/topDetail.jpg)  

###  Swap  
Swap叫内存置换空间（swap space），是磁盘上的一块区域。作用是，当系统物理内存吃紧时，Linux 会将内存中不常访问的数据保存到 swap 上，这样系统就有更多的物理内存为各个进程服务，而当系统需要访问 swap 上存储的内容时，再将 swap 上的数据加载到内存中，也就是常说的 swap out 和 swap in。  

好处：一定程度的缓解内存空间紧张的问题  
缺点：CPU所读取的数据都来自于内存，交换分区则是存放在磁盘上的，磁盘的速度和内存比较起来慢了好几个数量级，如果不停的读写 swap，那么对系统的性能肯定有影响，尤其是当系统内存很吃紧的时候，读写 swap 空间发生的频率会很高，导致系统运行很慢。  

如果使用是桌面系统，由于系统会自动将不常用的内存数据移到 swap 上，对桌面程序来说，有可能会导致最小化一个程序后，再打开时小卡一下，因为需要将 swap 上的数据重新加载到内存中来。在部署了数据库的系统上，也不建议用交换分区，因为频繁地在内存和磁盘上相互导数据会影响数据库性能。


