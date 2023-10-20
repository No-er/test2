import socket
from select import select

tasks = []

read_dic = {}
write_dic = {}

def server():
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_s.bind(("localhost", 5000))
    server_s.listen()

    while True:

        yield ('read', server_s)
        client_s, addr = server_s.accept() #read

        print('Connection from', addr)
        tasks.append(client(client_s))



def client(client_s):
    while True:

        try:
            yield ('read', client_s)
            client_s.recv(4096) #read

            resp = "Hi MotherFucker\n".encode()

            yield ('write', client_s)
            client_s.send(resp) #write

        except:
            try:
                tasks.remove(client_s)
                client_s.close()
            except:
                pass




def loop():
    while any([tasks, read_dic, write_dic]):

        while not tasks:
            ready_4_read, ready_4_write, _ = select(read_dic, write_dic, [])

            for sock in ready_4_read:
                tasks.append(read_dic.pop(sock))
            for sock in ready_4_write:
                tasks.append(write_dic.pop(sock))

        try:
            task = tasks.pop(0)

            mode, sock = next(task)

            if mode == 'read':
                read_dic[sock] = task
            if mode == 'write':
                write_dic[sock] = task
        except StopIteration:
            print('All Done')



if __name__ == '__main__':
    tasks.append(server())
    loop()

