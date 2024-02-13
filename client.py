import socket,time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)
print('Connected to server')

# Recive ans for checkout
response = client_socket.recv(1024).decode('utf-8')
print('Server response Answer.')
ans = response

def send_request(message):
    request = f"{message}"
    client_socket.send(request.encode('utf-8'))
    print('Sent to server:', message)

    # Receive and print the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print('Server response:', response)

# Send messages to the server
print("type \"exit\" for exit")
while True :
    message_input = input("Guess a number 1 - 100: ")
    if(message_input == "exit" ) :
        break
    elif(message_input == "ans") :
        print(ans)
    elif(message_input == ans) :
        send_request(message_input)
        break
    else :
        send_request(message_input)

# Close the connection
client_socket.close()
