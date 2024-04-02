import tkinter as tk
import socket
import signal
import sys


# Function for show states of sensor
def update_sensor_states():
    global sensor_labels
    try:
        data = client_socket.recv(1024).decode()
        sensor_states = list(map(int, data.split(',')))
        for i, state in enumerate(sensor_states):
            sensor_labels[i].configure(text=f"Sensor {i+1}: {state}")
    except Exception as e:
        print(f"Greška pri primanju podataka: {e}")

# Connection on PLC server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    print("Klijent je povezan na server.")
except Exception as e:
    print(f"Greška pri povezivanju na server: {e}")
    sys.exit(1)

#  GUI
root = tk.Tk()
root.title("Stanje senzora")

sensor_frames = []
sensor_labels = []

for i in range(8):
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, padx=10, pady=5)
    sensor_frames.append(frame)
    label = tk.Label(frame, text=f"Sensor {i+1}: ")
    label.pack(side=tk.LEFT)
    sensor_labels.append(label)

# Function for update states
def update_states():
    update_sensor_states()
    root.after(1000, update_states)

update_states()

root.mainloop()
