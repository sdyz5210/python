README# pycrypto安装问题
安装环境为macOS Sierra 版本号为10.12.3
直接使用 `pip install pycrypto` 安装一直不成功，提示c编译器不工作。
解决问题：通过命令行执行：`xcode-select --install`，安装完后，需要同意一下协议
最后直接使用`pip install pycrypto` 安装

# 提示No module named Crypto.Cipher

解决问题：

```
sudo pip uninstall crypto
sudo pip uninstall pycrypto
sudo pip install pycrypto

```
