
## 配置
在安装Stuoe，你的服务器/电脑 需要安装这些东西

* [Python3.8+](https://www.python.org/downloads/release/python-383/)
* [pip](https://pypi.org/)
* [Nginx](https://nginx.org)

拉取Stuoe源码

Github(国际访问速度较快)

``` bash
git clone https://github.com/stuoe/stuoe.git
cd stuoe
```
或者使用Gitee节点(中国大陆访问较快)

``` bash
git clone https://gitee.com/stuoe/stuoe.git
cd stuoe
```

如果你没有安装Git(分布式代码管理工具)，直接下载Zip

[在Github上下载最新分支](https://github.com/stuoe/stuoe/archive/stuoe-0.0.1Beta.zip)

下载后解压所有文件在Stuoe文件夹，然后在文件夹的根目录打开一个Microsoft Windows终端

# 运行

尽管需要配置的东西还很多，但还是先运行让你小赌为快

打开Microsoft Windows终端，运行stuoe.py
``` bash
python stuoe.py
```
如果运行失败或者报错，请检查排查以下问题

* 是否安装了需要的 环境/软件
* 环境变量是否配置正确
* python.exe是否拥有读写/监听端口等权限
* 是否有执行命令的权限？尝试切换Power Shell
* 是否解压了全部文件
* 端口是否被占用？

如果依然无法解决你的问题，尝试在Stuoe的[仓库](http://github.com/stuoe/stuoe/issues)问题区提出详细的问题

如果出现类似于以下输出，说明运行成功，并在服务器/电脑 的31端口监听
``` bash
* Serving Flask app "stuoe" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 190-981-669
 * Running on http://0.0.0.0:31/ (Press CTRL+C to quit)
 ```


现在，使用浏览器访问https://127.0.0.1:31   (本地)就可以看到Stuoe的首页

