#encoding:utf-8
import socket,sys
port_default=[22,80,8080,135,139,445,1433,3306,3389,1212]   #默认要扫描的端口

def is_open(ip,port):       #使用socket连接端口来判断端口是否打开
    s = socket.socket()
    try:
        s.connect((ip, port))
        print '%s host %s open' % (ip, port)
    except:
        print '%s host %s close' % (ip, port)

#扫描默认端口
def scan_default(ip):
    for i in port_default:
        is_open(ip,i)

#扫描所有端口
def scan_all(ip):
    for i in range(0,65535):
        is_open(ip,i)

#扫描用户自定义端口
def scan_define(ip,port_define):
    for i in port_define:
        #如果导入的端口字典最后一行有换行，则得到的列表最后一个字符串为''，这边是为了防报错
        if i == '':
            return 0
        else:
            is_open(ip,int(i))

#输出帮助文档
def help_info():
    print """TRUE:
    1.default: python scan_port.py ip;
    2.All:python scan_port.py ip -a;
    3.Custom:python scan_port.py ip -p port1,port2,port3;
    4.Custom by file:python scan_port.py ip -f 'filepath';
    4.--help || -h :print help infomation;
    5.--version || -v:print version infomation."""

#输出版本信息
def version_info():
    print 'python_sacn_port_tools-1.0'


try:
    len = len(sys.argv)
    #如果只有一个参数，sys.argv[0]为程序自身
    if len == 2:
        if sys.argv[1]=='--help' or sys.argv[1]=='-h':
            help_info()
        elif sys.argv[1]== '--version' or sys.argv[1]== '-v':
            version_info()
        else:
            scan_default(sys.argv[1])
    #如果有两个参数
    elif len == 3 :
        if sys.argv[2] == '-a':
            scan_all(sys.argv[1])
    #如果有三个参数
    elif len == 4:
        if sys.argv[2] == '-p':
            #sys.argv[3].split(',')，将第三个参数按','分割，形成要扫描的列表
            scan_define(sys.argv[1],sys.argv[3].split(','))
        elif sys.argv[2] == '-f':
            with open(sys.argv[3],'r') as f:
                read_file_port=f.read().split('\n')
                scan_define(sys.argv[1],read_file_port)
except:
    help_info()