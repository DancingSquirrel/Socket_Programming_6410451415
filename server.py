import socket,random,time

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening for connections...')

# Accept a connection
connection, client_address = server_socket.accept()
print('Connection from', client_address)

def process_request(request):
    # Dummy processing, just append "Server Processed: " to the request
    processed_request = "Server Processed: " + request
    return processed_request

def send_response_ans(rand_number):
    response = f"{rand_number}"
    connection.send(response.encode('utf-8'))

def send_response(status_code, status_phrase, message):
    response = f"RES {status_code} {status_phrase} {message}"
    connection.send(response.encode('utf-8'))
    

rand_num = random.randint(1,100)
print(rand_num)
send_response_ans(rand_num)
# Receive and process messages from the client
while True:
    data = connection.recv(1024).decode('utf-8')
    if not data:
        break

    # Check if the received data follows the protocol
    if data.startswith(""):
        # Extract the message from the request
        message = data
        print('Received from client:', message)

        # Process the request
        processed_message = process_request(message)
        print(processed_message)
        try:
            time.sleep(2)
            # Attempt to convert the message to an integer
            message_as_int = int(message)

            if rand_num == message_as_int:
                send_response(200, "OK", "  HiT !!!!!! %d is correct" % rand_num)
                connection.close()
                server_socket.close()
                break
            else:
                send_response(200, "OK", "  Try again")
        except ValueError:
            # Handle the case where the message is not an integer
            if message == "exit":
                time.sleep(2)
                # Close the connection if "exit" is received
                connection.close()
                server_socket.close()
            else:
                send_response(200, "OK", " Invalid input. Please enter a number.")
