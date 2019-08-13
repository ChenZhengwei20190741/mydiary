# 常见问题解决方法汇总

---

### 安装完 python 插件后安装不了 pip

1. 在命令行进行以下操作：`sudo apt-get install python3-pip`
2. 如果第一种方法不行试一下下面这一种

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
$ pip -V　　#查看pip版本
```
