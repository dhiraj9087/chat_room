
import threading
import socket

host = "127.0.0.1"
port = 55553

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except Exception as e:
            print(f"Failed to send message to a client: {e}")

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                decoded_message = message.decode('ascii')
                if "has left the chat!" in decoded_message:
                    index = clients.index(client)
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast(f'{nickname} left the chat!'.encode('ascii'))
                    nicknames.remove(nickname)
                    break
                else:
                    broadcast(message)
        except Exception as e:
            print(f"Error handling message: {e}")
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('ascii'))
                nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        try:
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)
            print(f"Nickname of the client is {nickname}")
            broadcast(f'{nickname} joined the chat!'.encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except Exception as e:
            print(f"Error during client setup: {e}")
            client.close()

print("Server is listening...")
receive()
