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
