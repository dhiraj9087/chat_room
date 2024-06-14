# Chat Room Project

This project is a simple chat room application built with Python. It includes a server and client implementation using the `socket` and `threading` libraries. The client also features a graphical user interface (GUI) built with `tkinter`.

## Features

- Multiple clients can connect to the server and chat with each other in real-time.
- Each client is required to choose a unique nickname.
- Clients can send and receive messages.
- Clients can leave the chat, which notifies other clients.

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of networking and Python programming.

## Networking Fundamentals Used

- **Sockets**: Used for communication between the server and clients. The server uses `socket.AF_INET` and `socket.SOCK_STREAM` to establish a TCP connection.
- **Multithreading**: The server handles multiple clients simultaneously using threads.
- **IP Address and Port**: The server binds to a specific IP address and port to listen for incoming connections.
- **Message Encoding and Decoding**: Messages are encoded to bytes before sending and decoded back to strings upon receipt.
- **Client-Server Architecture**: The server listens for connections and processes messages, while clients connect to the server to participate in the chat.

## Getting Started

### Server Setup

1. Clone the repository and navigate to the directory containing the server script.
2. Run the server script:
   ```bash
   python server.py
### Client Setup

1. Run the client script:
   ```bash
   python client.py
2. for multiple clients repeat step 1 in different terminals 

### Usage
1. Start the server by running server.py.
2. Run one or more instances of client.py to join the chat.
3. Enter your nickname when prompted.
4. Send messages using the text entry box and the "Send" button.
5. Leave the chat by clicking the "Leave" button or closing the window.


### Notes
1. The server should be started before any clients attempt to connect.
2. Ensure that the IP address and port in client.py match those in server.py.

### License
This project is licensed under the MIT License.
