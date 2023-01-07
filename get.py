from socket import *
import socket as abc
import uuid
import sys
import time # 导入包

#本程序使用Apache-2.0 license 开源
#原作者doupoa，项目地址https://github.com/doupoa/MinecraftBedrockServerStatuSquery
#由Xiaoxiaoyu 修改后继续以Apache-2.0 license 开源
print('本程序使用Apache-2.0 license 开源')
print('原作者doupoa，项目地址https://github.com/doupoa/MinecraftBedrockServerStatuSquery')
print('由Xiaoxiaoyu 修改后继续以Apache-2.0 license 开源')

userinput = sys.argv
usernumber = len(userinput)
if usernumber >= 5:
    print('已获取到需要信息')
    wowhost = userinput[1]
    print('目标服务器:' + wowhost)
    wowport = int(userinput[2])
    print('目标端口:'+str(wowport))
    localhost = userinput[3]
    print('本地服务器:'+localhost)
    localport = int(userinput[4])
    print('本地服务器端口:' + str(localport))
    time.sleep(0.5)
else:
    wowhost = input('请输入目标服务器')
    wowport = int(input('请输入目标端口'))
    
    
addr = (wowhost,wowport) #定义目标地址及端口

uuid = str(uuid.uuid1()).upper().split("-") # 生成GUID，在C++中此值称为GUID，在Python中却叫UUID
time = int((time.perf_counter())*10000000) # 获取程序已启动时间，精准至小数后5位
tickcounttime = '%016d' % time  # 将启动时间填充零至16字节
str2 = "01"+str(tickcounttime) + "00FFFF00FEFEFEFEFDFDFDFD12345678" + uuid[2]+uuid[4] # 缝合数据包
str1 = bytes.fromhex(str2) # 将数据包转换为16进制
eClient = abc.socket()
host = localhost
port = int(localport)
eClient.connect((host,port))
#msg = "fuckyou"
#eClient.send(bytes(msg.encode('gbk')))



#try: # 尝试连接
UDPC = socket(AF_INET, SOCK_DGRAM) #定义socket为UDP 内部大写字符为socket的特征码，详情请查阅相关资料
socket.settimeout(UDPC, 5) # 设置超时时间为5秒
socket.connect(UDPC, addr) # 连接远程地址
UDPC.sendto(str1, addr) # 发送数据包
rec = socket.recvfrom(UDPC, 1024) # 设置接收缓冲区
    #print(rec) #输出返回内容 内容仍为字节编码
    #---数据清洗---#
global sb
sb = rec
global Cleaning
Cleaning = str(rec).split(';')
  
    #print(len(Cleaning))
#except: # 尝试失败后执行
    #msg = "Error|Error"
    #print("连接超时")

cnm = 0
#print(len(Cleaning))
print('====================')
msg = ""
while cnm < len(Cleaning):
    if cnm == 0:
        pass
        print('useless data:' + Cleaning[cnm] + "\n \n \n")
    elif cnm == 1:
        wcnmd = Cleaning[cnm].split("\\")
        print(str(cnm)+"|" + wcnmd[0])
        msg= msg + str(cnm)+"|" + wcnmd[0] + '||'

    elif cnm == 5:
        wdnmd = Cleaning[cnm].split("'")
        print(str(cnm)+"|" + wdnmd[0])
        msg =msg + str(cnm)+"|" + wdnmd[0] + '||'

    else:
        print(str(cnm)+"|" + Cleaning[cnm])
        msg = msg + str(cnm)+"|" + Cleaning[cnm] + '||'

    cnm = cnm + 1
print(msg)
eClient.send(msg.encode('gbk'))
#eClient.send(str(sb).encode('gbk'))

UDPC.close() # 关闭socket
eClient.close()
