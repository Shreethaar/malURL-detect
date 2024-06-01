import pyshark
capture = pyshark.LiveCapture(interface='wlan0')
for packet in capture.sniff_continuously(packet_count=10):
    print(f"[+] Packet: {packet.sniff_time} - {packet.highest_layer}")
    if 'IP' in packet:
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src} -> Destination IP: {ip_layer.dst}")

    if 'TCP' in packet:
        tcp_layer = packet['TCP']
        print(f"Source Port: {tcp_layer.srcport} -> Destination Port: {tcp_layer.dstport}")

