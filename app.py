import socket

# Configura el host y el puerto en el que deseas que escuche el servidor
host = '127.0.0.1' 
port = 5000

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula el socket al host y puerto especificados
server_socket.bind((host, port))

# Escucha conexiones entrantes
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

while True:
    # Acepta una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde {client_address}")
    
    # Lee datos del cliente
    data = client_socket.recv(1024)
    
    # Envía una respuesta de ejemplo
    response = b"HTTP/1.1 200 OK\nContent-Length: 12\n\nHello, World!"
    client_socket.sendall(response)
    
    # Cierra la conexión con el cliente
    client_socket.close()
