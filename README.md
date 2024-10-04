# chat_room
This project implements a simple multi-client chat server using Python's socket and threading libraries. This chat server can be used for simple group chats and small scale applications

Functionality: The server accepts connections from multiple clients, allowing them to send and receive messages in real time.

Server Setup:

The server binds to a specified IP address (127.0.0.1) and port (12345) and listens for incoming client connections.
Client Management:

Two lists (clients and nicknames) are maintained to keep track of connected clients and their respective nicknames.
Broadcasting Messages:

The broadcast function sends messages to all connected clients, ensuring that everyone can see messages from others.
Handling Client Connections:

When a client connects, a dedicated thread is started to handle its interactions.
The server sends a request for the client's nickname, which is then stored.
Receiving Messages:

In the handle function, the server continuously listens for messages from the client and broadcasts them to all others.
If a client disconnects, it removes them from the lists, notifies other clients, and ends the thread.
Connection Feedback:

The server informs clients of successful connections and broadcasts messages indicating when clients join or leave the chat.
