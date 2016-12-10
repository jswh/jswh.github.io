Title: 初始化一个 Python 开发环境的正确姿势
Date: 2016-07-01 06:00
Category: 深夜鸡汤

在看这篇文章的时候，我需要两个假设，以避免做过多无关的解释。
1. 假设读者对 [Python](https://www.python.org/downloads/) 有最基本的了解，知道如何使用 [pip](https://pip.pypa.io/en/stable/installing/)。并且系统环境中已经安装有 Python 和 pip。
2. 假设读者对 [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) 有最基本的了解，知道为什么要用 virtualenv。

如果假设不成立，可以跟随上面的链接和 Google 来了解。

## 0x1 更换 pypi 源为豆瓣的源
如果网络环境好的话这一步也可以不做

    mkdir -p ~/.config/pip/
    touch ~/.config/pip/pip.conf

在pip.conf 文件中添加以下内容

    [global]
    timeout = 60
    index-url = https://pypi.doubanio.com/simple/
## 0x2 安装 virtualenv
    pip install virtualenv
## 0x3 使用 vritualenv 初始化应用目录
    virtualenv path/to/your/app/folder/
    source path/to/your/app/folder/bin/activate # 激活环境
virtualenv 初始化的时候可以有多种基本Python的环境选择。新版本默认是不会带上site-packages的干净环境。

## 0x4 安装依赖
比如 Flask 

    pip install flask
或者如果有`requirements.txt`的话

    pip install -r requirements.txt

## 0x5 把 virtualenv 环境导入编辑器/IDE
这里仅以 VSCode 为例。先安装 [python 的语言插件](https://code.visualstudio.com/docs/languages/python)，然后编辑 [workerspace settings](https://code.visualstudio.com/docs/customization/userandworkspace)
增加以下内容

    "python.autoComplete.extraPaths": [
        "path/to/your/app/folder/lib"
    ],
    "python.pythonPath":"path/to/your/app/folder/bin/python"

之后就可以愉快的使用了。