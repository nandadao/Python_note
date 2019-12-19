## 新知识



### GIT 简介

svn也是一种代码管理

１．什么是git
git 是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件

２．git是分布式的项目管理工具(svn是集中式的)基本概念

- 工作区：项目所在操作目录，实际操作项目的区域
- 暂存区: 用于记录工作区的工作（修改）内容
- 仓库区: 用于备份工作区的内容
- 远程仓库: 远程主机上的GIT仓库

注意： 在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库区的内容才能和其他远程仓库交互。

３．统一用global配置

```shell
1.配置用户名
git config --global user.name Tedu
2.git config --global user.email lvze@tedu.cn
3.查看配置
cat .gitconfig
                    结果：
                    [user]
                        name = Tedu
                        email = lvze@tedu.cn
4.查看配置信息
git config --list
```

4.基本命令

注意：git add *：不能提交隐藏文件

```
1.初始化仓库
git　init
> 意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理

2.查看本地仓库状态
git status




```

7.分支管理

２．创建分支
git  branch   [branch_name]



### 注意：

### 如果把 .git　文件删除，那么这个文件就不再是git仓库，以及之前commit保存的文件都没了

git  branch -a :查看所有分支

ssh　　　linux第二天，下午课程找出ssh公钥
ssh-keygen：设置密钥
cd .ssh：进入目标地址
cat  id_rsa.pub：打开这个文件
复制公钥

### 作业：

把自己的笔记上传到github上























































