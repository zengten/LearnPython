# LearnPython
## python相关命令操作

安装包 `pip install packagename`

卸载包 `pip uninstall packagename`

查看已经安装的包 `pip list`

查看包介绍 `pip show packagename`

查看包更加详细的介绍 `pip show --verbose packagename`

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

  

