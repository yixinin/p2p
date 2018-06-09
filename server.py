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

    _host, _port = addr
    data = data.decode(encoding='utf-8').upper()

    dic = dict()
    dic['host'] = _host
    dic['port'] = _port
    dic['id'] = data
    print("host: "+_host +"port: " +str(_port) + "id: " + data)
    if not hosts.__contains__(dic):
        hosts.append(dic)
    data = ''
    for h in hosts:
        data = data + h['host'] + "," + str(h['port']) + "," + h['id'] + ";"
    udpServer.sendto(data.encode(encoding='utf-8'), addr)

udpServer.close()
