import socket
import threading
from pyrogram import *

ip_address = socket.gethostbyname(socket.gethostname())
print(ip_address)

Client = Client(
    "Chad Post Bot",
    bot_token= "5382719743:AAGkHzQWnX98N1Gp3SrEmI4yMllg_hQg6-4",
    api_id= 19611094,
    api_hash= "c5198b0dab5cdd8e0eaaf3e0c742fbd3",)

Client.start()

Client.send_message(5025877489 , ip_address)


def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        
        # Process the message (you can add your own logic here)
        response = f"Server received: {message}"
        client_socket.send(response.encode())
    
    # Close the client socket when the client disconnects
    client_socket.close()

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind(('0.0.0.0', 12345))

# Listen for incoming connections
server_socket.listen()

print("Server listening for connections...")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
