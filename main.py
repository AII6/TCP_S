import socket
import threading
import tkinter.scrolledtext
from tkinter import *

socket_list = []
s = socket.socket()
s.bind(('127.0.0.1', 30000))
s.listen()


#
# def accept():
def read_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    except:
        print(str(addr) + 'Left!')
        socket_list.remove(s)


def socket_target(s):
    try:
        while True:
            content = read_client(s)
            if content is None:
                break
            else:
                print(str(addr) + 'say:' + content)
                # chat.insert('2.0', str(addr) + 'say:' + content)
                for client in socket_list:
                    client.send((str(addr) + 'say:' + content).encode('utf-8'))
    except:
        print("Error!")


while True:
    conn, addr = s.accept()  # conn为socket对象，addr为ip地址
    socket_list.append(conn)
    print(str(addr) + ' Joined!')
    # chat.insert(END, addr)
    threading.Thread(target=socket_target, args=(conn,)).start()

#
# root = Tk()
# root.title("服务端")
# root.geometry("470x280")
# chat = tkinter.scrolledtext.ScrolledText(root)
# chat.pack()

# threading.Thread(target=accept).start()
# root.mainloop()
