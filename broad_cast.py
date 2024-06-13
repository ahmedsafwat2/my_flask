import socket

def broadcast_message(message, port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(message.encode(), ('192.168.1.2', port))
    s.close()

message = "Hello, this is a broadcast message to all devices in the network!"
broadcast_message(message)
'''
import ipaddress

def calculate_broadcast(ip, subnet_mask):
    network = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False)
    return network.broadcast_address

ip = "192.168.1.10"
subnet_mask = "255.255.255.0"

broadcast_address = calculate_broadcast(ip, subnet_mask)
print(f"The broadcast address is: {broadcast_address}")
'''