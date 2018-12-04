# 服务端地址
SER_PORT = 10000
SER_IP = "127.0.0.1"
SER_ADDR = (SER_IP,SER_PORT)

# socket最大传输的数据包长度
BUFSIZE = 1024 
# 服务端返回可用的端口起始值
APP_PORT = 20000
# 客户端发送请求的端口
CLI_PORT = 30000

# 默认参数
OPERATION = "lget"
FILENAME = "test.txt"

# 客户端缓存大小
RecvBuffer = 200
# 服务端缓存大小
SER_RECV_BUF = 200

# 硬盘写操作时间间隔
FileWriteInterval = 0.1

# 发送报文数据字段最大字节长度
MSS = 500
# 发送方最大等待时延
senderTimeoutValue = 0.1
# 拥塞窗口大小
cwnd = 1
# 慢启动阈值
ssthresh = 20