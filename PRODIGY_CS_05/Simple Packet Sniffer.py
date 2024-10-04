from scapy.all import sniff ,Raw, bytes_hex,IP, TCP, UDP, ICMP


def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        ProtocolsDic = {
            1 : "ICMP",
            6 : "TCP",
            8 : "EGP",
            9 : "IGP",
            17: "TCP",
            18: "MUX",
            58: "IPv6-ICMP",
            86: "DGP",
            88: "EIGRP",
            89: "OSPF"
            }
        
        if protocol in ProtocolsDic:
            proto_str = ProtocolsDic[protocol]
        else:
            proto_str = "Other"
            
        print("-------------------------------------------------------------------------------------------------------")        
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {proto_str}")
        print("\n########################################################################\n")
        print(f"Summary: {packet.summary()}")
        print("\n########################################################################\n")
        
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload in Hexa: {bytes_hex(payload)}")
            print("\n########################################################################\n")
            
        packet.show()
        print("-------------------------------------------------------------------------------------------------------")
            


if __name__ == "__main__":
    print("Starting packet sniffer... Press Ctrl+C to stop.")
    sniff(filter="ip", prn=process_packet)
