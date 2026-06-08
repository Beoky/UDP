from scapy.all import * import time
ip = IP(dst='127.0.0.127', src='10.99.99.99') 
udp = UDP(sport=321,dport=123) 
payload = '\x01\x0f' 
packet = ip/udp/payload send(packet) 
while(True): 	send(packet) 	time.sleep(1)
