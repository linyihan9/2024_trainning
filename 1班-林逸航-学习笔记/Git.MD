# Git
##  分区
工作区 暂存区 版本库 远程仓库   

##  Head
Head表示为当前选择的分支  
![](https://github.com/linyihan9/2024_trainning/blob/main/img/image.png)

##  分支
Git分支实际为一个包含所指对象校验和（40个字符长度的SHA-1字串）的文件   
大约2的51次方可能会发生哈希碰撞  

##  Merge
经过git merge hotfix，可能直接通过指针右移，也就是**Fast Forward**——快进

##  基本操作
git add   
git commit -a -m xxx  
git merge  
git checkout  选择分支  
git branch -d 删除分支
git push （远程仓库名） （分支名）   

##  实际应用
###  长期分支
在master分支中保留完全稳定的代码，与此同时，设置一个develop的平行分支，专门用于后续开发，一旦稳定，就可以合并到master中   
![](https://github.com/linyihan9/2024_trainning/blob/main/img/gitLongBranch.jpg)   
####  特性分支


