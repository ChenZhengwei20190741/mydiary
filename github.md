# **github 使用总结**

## _个人 github 学习及使用总结性文档_

---

###远程库：

添加远程仓库
首先先创建 github 仓库<br>
然后把本地的仓库推送到远程仓库中

1.关联仓库 `git remote add origin <链接>`

2.推送仓库 `git push -u origin master`

---

###分支创建：

```
$git checkout -b dev
==
$ git branch dev
$ git checkout dev
```

表示切换并创建

`git branch`
会出现所有分支

`git checkout master`
切换回 master

`git merge dev`
把 dev 分支的修改合并到 master 上去

`git branch -d dev`
合并完后就可以删除 dev 了

---

###总结
查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`

创建+切换分支：`git checkout -b <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

查看分支合并图：`git log --graph`

合并分支并做记录：`git merge --no-ff -m "merge with no-ff" dev`

在你的分支<br>
存放现场：`git stash`
回来的时候<br>
查看存放列表：`git stash list`

> 恢复：`git stash apply`
> 删除`git stash drop`

恢复和删除同时操作：`git stash pop`

---

### 远程库操作

查看远程库信息`git remote -v`

本地新建的分支如果不推送到远程，对其他人就是不可见的；

从本地推送分支，使用`git push origin branch-name，`如果推送失败，先用`git pull`抓取远程的新提交；

在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；

建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；

从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。

---

### 标签管理

设置当前 HEAD：`git tag <tagname>`
指定某个 commit：`git tag v1.0 xxxxxx`
指定标签信息：`git tag -a <tagname> -m "message"`
查看标签：`git tag`
<br>
命令`git push origin <tagname>`可以推送一个本地标签；

命令`git push origin --tags`可以推送全部未推送过的本地标签；

命令`git tag -d <tagname>`可以删除一个本地标签；

命令`git push origin :refs/tags/<tagname>`可以删除一个远程标签。
