# Level 15 - DNS Tunnel Secrets

*Objective:*  
Extract the hidden flag sent through a DNS tunneling technique captured in dns_traffic.pcap.

---

## Challenge Description

The attacker exfiltrated data using DNS queries by embedding a base64-encoded flag into the domain name and sending it to a DNS server (like 8.8.8.8). The task is to inspect the packet capture and recover the original flag.

---

## How It Works

1. A flag is stored in a file:
   ```bash
   echo "CyberCrack{DNS_Tunnel_Hidden_Flag}" > flag.txt
