from scapy.all import sniff, TCP,IP

def packet_capture(packet):
    if packet.haslayer(TCP):
        ip_layer = packet.getlayer(IP)
        tcp_layer = packet.getlayer(TCP)
        print(f"[+] New Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
sniff(prn=packet_capture,count=10)

