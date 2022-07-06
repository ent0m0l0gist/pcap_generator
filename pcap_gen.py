from scapy.all import * 

pcap_file = "http.pcap"

smac = "12:34:56:ab:cd:ef"
dmac = "ab:cd:ef:12:34:56"

sip = "1.2.3.4"
dip = "5.6.7.8"

#modify the dp as per protocol
sp = 12345
dp = 80

#modify the data as per requirement
data="HEAD / HTTP/1.1\r\n\r\nGET /index.html HTTP/1.1\r\n\r\n"

#3-way handshake
pkt1 = Ether(src=smac, dst=dmac)/IP(src=sip, dst=dip)/TCP(sport=sp, dport=dp, flags= "S", seq=0)
pkt2 = Ether(src=dmac, dst=smac)/IP(src=dip, dst=sip)/TCP(sport=dp, dport=sp, flags= "SA", seq=0, ack=1)
pkt3 = Ether(src=smac, dst=dmac)/IP(src=sip, dst=dip)/TCP(sport=sp, dport=dp, flags= "A", seq=1, ack=1)

#data packet
pkt4 = Ether(src=smac, dst=dmac)/IP(src=sip, dst=dip)/TCP(sport=sp, dport=dp, flags= "A", seq=1, ack=1)/data
#if you have multiple data packets, add pkt5, pkt6...and so on

#write the packets to file
wrpcap(pcap_file, pkt1, append=1)
wrpcap(pcap_file, pkt2, append=1)
wrpcap(pcap_file, pkt3, append=1)
wrpcap(pcap_file, pkt4, append=1)