import socket
import selectors

selector = selectors.DefaultSelector()
def server():
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_s.bind(("localhost", 5000))
    server_s.listen()

    selector.register(fileobj=server_s, events=selectors.EVENT_READ, data=acc_connection)

def acc_connection(server_s):
    client_s, addr = server_s.accept()
    print('Connection from', addr)

    selector.register(fileobj=client_s, events=selectors.EVENT_READ, data=send_m)

def send_m(client_s):
    try:
        client_s.recv(4096)
        resp = "Hi MotherFucker\n".encode()
        client_s.send(resp)
    except:
        selector.unregister(client_s)
        client_s.close()

def loop():
    while True:
        events = selector.select()

        for k, _ in events:
            callback = k.data
            callback(k.fileobj)


if __name__ == '__main__':
    server()
    loop()

