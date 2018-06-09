from socket import *
from time import ctime

host = ''  # 监听所有的ip
port = 13141  # 接口必须一致
bufsize = 1024
addr = (host, port)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(addr)  # 开始监听
hosts = []
while True:
    print('Waiting for connection...')
    data, addr = udpServer.recvfrom(bufsize)  # 接收数据和返回地址

    host, port = addr
    data = data.decode(encoding='utf-8').upper()

    dic = dict()
    dic['host'] = host
    dic['port'] = port
    dic['id'] = data
    if not hosts.__contains__(dic):
        hosts.append(dic)
    data = ''
    for h in hosts:
        data = data + h['host'] + "," + str(h['port']) + "," + h['id'] + ";"
    data = "at %s :%s" % (ctime(), data)
    udpServer.sendto(data.encode(encoding='utf-8'), addr)

    print('...recevied from and return to :', addr)

udpServer.close()
