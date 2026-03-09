# main.py

from scapy.all import sniff
from collections import Counter
import matplotlib.pyplot as plt


# Capture packets
def capture_packets(interface):
    packets = sniff(iface=interface, count=100)
    return packets


# Analyze packets
def analyze_packets(packets):
    protocol_counts = Counter(pkt.proto for pkt in packets if hasattr(pkt, 'proto'))
    return protocol_counts


# Visualize results
def visualize_data(protocol_counts):
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.bar(protocols, counts)
    plt.xlabel("Protocols")
    plt.ylabel("Number of Packets")
    plt.title("Protocol Distribution Chart")
    plt.show()


# Main execution
def main():
    interface = input("Enter network interface (e.g., eth0 / wlan0): ")

    print("Capturing packets...")
    packets = capture_packets(interface)

    print("Analyzing packets...")
    protocol_counts = analyze_packets(packets)

    print("Protocol Statistics:")
    for proto, count in protocol_counts.items():
        print(f"Protocol {proto}: {count} packets")

    visualize_data(protocol_counts)


if __name__ == "__main__":
    main()
