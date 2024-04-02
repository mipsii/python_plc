import socket
import sys
import random
import time
import signal

# Funkcija za hvatanje signala SIGINT (Ctrl + C)
def signal_handler(sig, frame):
    print("\nPrekid izvršavanja programa.")
    if client_socket:
        client_socket.close()
    sys.exit(0)

# Postavljanje hvatača signala
signal.signal(signal.SIGINT, signal_handler)

# Function for starting state of sensors
def generate_initial_sensor_states():
    return [random.randint(0, 1) for _ in range(8)]

# Function change state
def simulate_sensor_change(sensor_states):
    index = random.randint(0, 7)
    sensor_states[index] = 1 - sensor_states[index]
    return sensor_states

# connect on socket
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)
    print("PLC Server is started.")
except Exception as e:
    print(f"error on start server: {e}")
    sys.exit(1)

# connected client
try:
    client_socket, client_address = server_socket.accept()
    print(f"Client {client_address} is connected")
except Exception as e:
    print(f"error {e}")
    sys.exit(1)

# Simulate change state of sensors
try:
    sensor_states = generate_initial_sensor_states()
    while True:
        sensor_states = simulate_sensor_change(sensor_states)
        sensor_data = ','.join(map(str, sensor_states))
        client_socket.sendall(sensor_data.encode())
        time.sleep(1)
except Exception as e:
    print(f"Error simulate change of senzora: {e}")
finally:
    client_socket.close()
    server_socket.close()
