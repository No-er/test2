import socket
from select import select

sockets_list = []

server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_s.bind(("localhost", 5000))
server_s.listen()

def acc_connection(server_s):
    client_s, addr = server_s.accept()
    print('Connection from', addr)
    sockets_list.append(client_s)

def send_m(client_s):
    try:
        client_s.recv(4096)
        resp = "Hi MotherFucker\n".encode()
        client_s.send(resp)
    except:
        sockets_list.remove(client_s)
        client_s.close()

def loop():
    while True:
        ready_to_read, _, _ = select(sockets_list, [], [])
        for socket in ready_to_read:
            if socket is server_s:
                acc_connection(socket)
            else:
                send_m(socket)

if __name__ == '__main__':
    sockets_list.append(server_s)
    loop()

