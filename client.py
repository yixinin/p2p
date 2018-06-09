from socket import *
import time

host  = '101.132.242.31' # 这是客户端的电脑的ip
port = 9999 #接口选择大于10000的，避免冲突
bufsize = 1024  #定义缓冲大小

addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM) #创建客户端
id="pc"
while True:

    data=id
    if not data:
        break
    data = data.encode(encoding="utf-8")
    udpClient.sendto(data,addr) # 发送数据
    data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
    str = data.decode(encoding="utf-8")
    print(str)
    datas=str.split(';')
    for d in datas:
        if d == "" or d == None or d == ' ':
            continue
        ds = d.split(',')
        _ip = ds[0]
        _port =ds[1]
        _id = ds[2]
        if id == _id:
            continue
        _addr=(_ip,int(port))
        _data="hello p2p".encode(encoding="utf-8")

        udpClient.sendto(_data, _addr)
    print(data.decode(encoding="utf-8"),'from',addr)
    print("done")
    time.sleep(10)
udpClient.close()