# 安装
clone repo 到本地.执行 setup 文件安装。windows用户请自行参考 setup 文件内容安装相关依赖。等我有空把 setup 也改成 python 的脚本。
# 使用
## 编写文章
文章添加请参考 [pelican](http://docs.getpelican.com/en/3.6.3/quickstart.html#create-an-article) 的手册。
## 更新博客内容
请在编写完你的文章之后或者修改博客设置之后，执行以下命令

	make github

该命令会执行下述步骤

* 提交所有的更改
* 将代码库内容推送到 github 的 pelican 分支
* 生成博客内容
* 将生成的博客内容推送到 github 的 master 分支

如果需要添加自己的commit message 请手动进行 git 相关操作。

