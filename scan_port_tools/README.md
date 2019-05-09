# scan_port_tools
使用python2编写

使用方法：

1.default: 扫描指定ip的默认（脚本自带）端口号
python2.exe scan_port.py ip

2.All:扫描所有端口号，0~65535
python2.exe scan_port.py ip -a

3.Custom:自定义需要扫描的端口
python2.exe scan_port.py ip -p port1,port2,port3
    
4.Custom by file:导入端口字典文件扫描端口
python2.exe scan_port.py ip -f 'filepath';
    
5.--help || -h :获取帮助
python2.exe scan_port.py --help

6.--version || -v:输出版本信息
python2.exe scan_port.py --version
