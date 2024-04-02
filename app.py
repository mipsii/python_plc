import signal
import tkinter as tk
import subprocess
import time
import os


server_process = None
client_process = None

def start_server_and_client():
    server_process =subprocess.Popen(["python", "serverPLC.py"])
    time.sleep(5)
    
    client_process = subprocess.Popen(["python", "clientPLC.py"])
    time.sleep(1)
   

start_server_and_client()

