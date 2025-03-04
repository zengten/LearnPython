# LearnPython
## python相关命令操作

安装包 `pip install packagename`

卸载包 `pip uninstall packagename`

安装指定版本包 `pip install packagename==version`

包升级到指定版本 `pip install --upgrade packagename==version`

查看已经安装的包 `pip list`

查看包介绍 `pip show packagename`

查看包更加详细的介绍 `pip show --verbose packagename`

查看所有安装的包 `pip freeze`

- 将当前环境所有包信息输出到文件中，便于复制安装包到其他环境中
- 包信息输出到文件中命令`pip freeze > requirements.txt`
- 其他环境安装清单包命令`pip freeze -r path/to/requirements.txt`

## pyenv多版本环境
### windows版本
仓库地址：`https://github.com/pyenv-win/pyenv-win`
个人体验不太好用，换miniconda了
```shell
# 使用powershell安装
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
# 检查安装是否成功
pyenv --version 
# 检查 pyenv-win 支持的 Python 版本列表
pyenv install -l 
# 安装支持的版本
pyenv install <version> 
# 以设置全局 Python 版本
pyenv global <version> 
# 检查您正在使用的 Python 版本及其路径
pyenv version
# 当你切换 Python 版本或者安装、卸载 Python 版本之后，就需要运行这个命令，重新生成 pyenv 的 shims（垫片）文件
pyenv rehash
```
## miniconda多版本环境

### 下载和帮助
清华镜像conda帮助使用页面：`https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/`
软件下载：`https://mirrors.tuna.tsinghua.edu.cn/#` 右边的获取下载链接，选择`Conda`进行下载

### 设置环境变量
```
# 新增系统变量
MINICONDA_HOME=miniconda安装根路径
# path添加环境变量
%MINICONDA_HOME%
%MINICONDA_HOME%\Scripts
%MINICONDA_HOME%\Library\bin
```

### 更新镜像源
不同系统下的 .condarc 目录如下：
- Linux: ${HOME}/.condarc
- macOS: ${HOME}/.condarc
- Windows: C:\Users\<YourUserName>\.condarc
在**管理员cmd**窗口下，使用命令生成.condarc配置文件`conda config --set show_channel_urls yes`
然后编辑.condarc文件，设置镜像源
```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
验证源是否生效，cmd输入`conda config --show`即可看到镜像源地址

### 创建使用镜像

创建新环境`conda create --name 环境名称 python=python版本`
激活环境`conda activate 环境名称`，可能需要使用`conda init`初始化conda
**上面操作可能需要管理员cmd模式**

## venv虚拟环境

虚拟环境的出现是为了解决项目之间，包版本依赖以及包冲突问题

使用帮助命令`python -m venv -h`

创建一个虚拟环境，命令`python -m venv testVenv01`

- 创建虚拟环境最好不要指定可选参数，会降低虚拟环境的独立性

此时当前文件夹下会多出一个`testVenv01`虚拟环境目录

进入到该文件夹目录`testVenv01/Scripts/`下

- 输入`activate`命令进入到该虚拟环境
- 输入`deactivate`命令退出虚拟环境

此时使用`pip install packages`安装的包与系统环境无关

## 问题

### pip install numpy报错怎么处理？

- 更新pip，命令：`python.exe -m pip install --upgrade pip`

- 本地添加文件，系统盘下`C:\Users\用户名\AppData\Roaming`

  - 文件夹下有没有一个pip文件夹，无则创建
  - 然后创建pip.ini文件，编辑文件复制下面文字，粘贴保存

  ```ini
  [global]
  index-url = http://mirrors.aliyun.com/pypi/simple
  [install]
  trusted-host = mirrors.aliyun.com
  ```


### pip升级之后，原来版本安装的包，无法卸载/出现警告怎么处理？

- 使用`pip list`或`pip freeze`会出现warning

- 解决：在python包目录`C:\Python39\Lib\site-packages`删掉`~`号开头的文件夹
