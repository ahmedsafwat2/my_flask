import socket

def listen_broadcast(port=12345):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    
    # Enable broadcasting mode
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Bind to the broadcast address and port
    s.bind(("", port))
    
    print(f"Listening for broadcast messages on port {port}")
    
    while True:
        # Receive messages
        data, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")

if __name__ == "__main__":
    listen_broadcast()
