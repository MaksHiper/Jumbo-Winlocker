import socket
import uuid
from requests import get

def get_mac_address():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

def get_location():
    response = get('https://ipinfo.io')
    data = response.json()
    return f"Location: {data['city']}, {data['region']}, {data['country']}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "0.0.0.0"  # Привязываем сервер ко всем доступным интерфейсам
server_port = 12345  # Порт для прослушивания

server.bind((server_ip, server_port))
server.listen()

print("Server is listening...")

while True:
    user, address = server.accept()
    ip_address = address[0]
    mac_address = get_mac_address()
    location = get_location()

    print("New user detected:")
    print(f"IP Address: {ip_address}")
    print(f"MAC Address: {mac_address}")
    print(location)

    user.close()

