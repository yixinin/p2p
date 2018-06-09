from socket import *
from time import ctime

host = ''
port = 9999
bufsize = 1024
addr = (host, port)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(addr)
hosts = []
while True:
    print('Waiting for connection...')
    data, addr = udpServer.recvfrom(bufsize)   

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
