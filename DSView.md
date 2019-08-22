# DSView

## 这是关于 DSView 相关协议编码器教程

---

### 1. 安装 DSView

#### step1

> 搭建 libsigrok4DSL

```shell
 $ cd libsigrok4DSL
 $ ./autogen.sh
 $ ./configure
 $ make
 $ sudo make install
 $ cd ..
```

#### step2

---

### 2. 如何加载协议解码器到 DSView 中

1. 修改或者新建 python 脚本

```
$cd libsigrokdecode4DSL/decoders   #到这个目录下,此目录存放的是协议解码器的脚本内容
$mkdir test_i2c
$cd test_i2c
$touch __init__.py pd.py   #新建或修改协议解码器
$cd ../..     #到libsigrokdecode4DSL目录下
$./autogen.sh
$./configure
$make
$sudo make install  #装载更新libsigrokdecode4DSL

$cd ..
$cd ./DSView
#cmake .            #装载到DSView里
```
