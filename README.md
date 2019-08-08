# mydiary

Introduce what I do every day

分支创建：

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

##总结
查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`

创建+切换分支：`git checkout -b <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

查看分支合并图：`git log --graph`

合并分支并做记录：`git merge --no-ff -m "merge with no-ff" dev`

存放现场：`git stash`
