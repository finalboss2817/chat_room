import threading
import socket
host= '127.0.0.1' 
port=12345

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            clients.close()
            nickname=nicknames[index]
            broadcast(f"{nickname} left the chat" .encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client,address=server.accept()
        print(f"connected with {str(address)} ")
        client.send('nick'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send('connected to server'.encode('ascii'))
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()
print("server is listening")
recieve()
