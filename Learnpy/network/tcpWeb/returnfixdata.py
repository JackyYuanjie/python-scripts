# -*- coding:utf-8 -*-

# 第二个.
# 返回固定数据 return fixed data
"""
TCP服务端
1. 导入模块
2. 创建套接字
3. 设置地址重用
4. 绑定端口
5. 设置监听,让套接字由主动变被动接收.
6. 接受客户端连接
7. 接收客户端浏览器发送的请求协议.
8. 判断请求协议是否为空.
9. 拼接响应报文.
   - 响应行
   - 响应头
   - 响应空行
   - 响应主体
10. 发送响应报文.
11. 关闭和当前客户端的连接.
"""

import socket


def request_handler(new_client_socket,ip_port):
    """接收信息,并且做出响应"""
    # 7. 接收客户端浏览器发送的请求协议.
    request_data = new_client_socket.recv(1024)
    print(request_data)
    # 8. 判断请求协议是否为空.
    if not request_data:
        print("{}客户端已经下线.".format(str(ip_port)))
        new_client_socket.close()
        return 
    # 9. 拼接响应报文.
    # 9.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 9.2 响应头
    response_header = "Server:Python3-vscodeIDE/2.1\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应主体
    response_body = "test tcp web applications"
    response_data = response_line + response_header + response_blank + response_body

    # 10. 发送响应报文.
    new_client_socket.send(response_data.encode())

    # 11. 关闭连接.
    new_client_socket.close()

def main():
    """主函数"""
    fix_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #3.设置地址重用,          当前套接字         地址重用
    fix_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #4.绑定端口
    fix_socket.bind(("18.18.23.254",8822))
    # 5.设置监听, 让套接字由主动变为被动接收.
    fix_socket.listen(128)
    # 6.接受客户端连接.
    new_client_socket,ip_port = fix_socket.accept()
    # 调用功能函数处理请求并且响应
    request_handler(new_client_socket,ip_port)

    # 11 关闭操作
    fix_socket.close()

if __name__=="__main__":
    main()
