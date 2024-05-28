# Git
##  test工具  

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

##  rebase  
###  rebase守则  
多人同时操作某个项目的时候，不要用rebase

##  merge和rebase区别
rebase 会把你当前分支的 commit 放到公共分支的最后面,所以叫变基。就好像你从公共分支又重新拉出来这个分支一样。  
而 merge 会把公共分支和你当前的 commit 合并在一起，形成一个新的 commit 提交  
优劣：  
git merge 优点是分支代码合并后不破坏原分支代码的提交记录，缺点是会产生额外的提交记录并进行两条分支的合并  
git rebase 优点是可以将对象分支的提交记录续道目标分支上，形成线性提交历史记录，review时更加直观  
  
合代码到公共分支上时用git merge  
合代码到个人分支时用git rebase，形成线性提交历史记录  

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

##  Git回退
###  reset和revert区别
reset:
版本1->版本2->版本3
回退后：
版本1->版本2

revert：
版本1->版本2->版本3  
发现版本2有问题，但是版本3想保留，就用rebase，保留了版本3，舍弃版本2  
版本1->版本2->版本3->版本4  
![](https://github.com/linyihan9/2024_trainning/blob/main/img/gitMergeAndRebase.jpg)  




