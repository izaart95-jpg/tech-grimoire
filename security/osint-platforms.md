# OSINT & Internet-Wide Scanning Tools Overview

## 1. **Shodan**
**What it is:**  
Shodan is a search engine for Internet-connected devices. Instead of indexing web pages like Google, it indexes services (HTTP, SSH, FTP, IoT protocols) and their metadata.

**Origin:**  
- Created by John Matherly  
- Launched in 2009

**Key Features:**  
- Scan results from global Internet scanning  
- Search by banner, port, IP, protocol, geolocation  
- Filters (port, hostname, OS, SSL certificate)  
- API access for automation  
- Monitor services & get alerts

**Use Cases:**  
- Discover exposed devices (cameras, routers)  
- Security research  
- Attack surface mapping

---

## 2. **ZoomEye**
**What it is:**  
ZoomEye is a Chinese Internet asset search engine similar to Shodan that scans for devices, web servers, and application banners.

**Origin:**  
- Created by KnownSec (中国安全公司)

**Key Features:**  
- Web and host search engines  
- Fingerprint recognition (products, services)  
- API available  
- Geolocation and tagging

**Use Cases:**  
- Identify vulnerable services  
- Asset discovery

---

## 3. **Netlas**
**What it is:**  
Netlas is a SaaS (hosted, subscription-based) internet scanning and search platform operated by Netlas LLC. It is not open source and has no self-hosted/on-prem release.

**Origin:**  
- Proprietary platform by Netlas LLC

**Key Features:**  
- Large dataset of Internet hosts and services (non-intrusive scanning)  
- Web app, CLI tool, and API access  
- DNS and WHOIS search, attack surface discovery tool  
- Search by banners, responses and metadata

**Use Cases:**  
- OSINT research  
- Attack surface discovery

---

## 4. **CriminalIP**
**What it is:**  
CriminalIP is a threat intelligence and attack surface monitoring platform.

**Origin:**  
- Enterprise product by a cybersecurity company

**Key Features:**  
- Internet asset discovery  
- Risk scoring  
- Network traffic context  
- Dark web and threat feeds integration

**Use Cases:**  
- Corporate security visibility  
- Threat hunting

---

## 5. **Onyphe**
**What it is:**  
Onyphe is a French OSINT search engine that indexes internet data (hosts, certificates, metadata) and provides API access.

**Origin:**  
- Built by cybersecurity researchers (France)

**Key Features:**  
- Search for hosts, IPs, domains, certificates  
- API for automation  
- Data correlations and enrichment

**Use Cases:**  
- Threat intelligence  
- Digital footprinting

---

## 6. **Censys**
**What it is:**  
Censys is an Internet-wide scanning platform and search engine for devices and certificates.

**Origin:**  
- Developed by University researchers (University of Michigan, University of Illinois)
  
**Key Features:**  
- Daily IPv4 and IPv6 scanning  
- TLS/SSL certificate indexing  
- Web UI and API  
- Data export and reports

**Use Cases:**  
- Discover vulnerable infrastructure  
- Monitor certificate deployments  
- Research internet protocol deployment

---

## 7. **Sarenka** (by KTZgraph)
**What it is:**  
Sarenka is an OSINT framework/utility (GitHub project) that helps with passive data collection and investigation workflows.

**Origin:**  
- Open source tool hosted on GitHub  
- Created by KTZgraph

**Key Features:**  
- Aggregates results from multiple OSINT sources  
- Self-hosted web app (Django + React)  
- Helpful for research automation

**Use Cases:**  
- Passive reconnaissance  
- Data consolidation

**Source:**  
https://github.com/pawlaczyk/sarenka

---

## 8. **CriminalIP vs Shodan vs ZoomEye vs Censys (Summary)**

| Feature | Shodan | ZoomEye | Censys | Onyphe | Netlas | CriminalIP | Sarenka |
|---------|--------|---------|--------|--------|--------|-------------|---------|
| Internet-wide scanning | ✔ | ✔ | ✔ | Partial | ✔ | Proprietary | Tool aggregator |
| API access | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | Uses APIs |
| Self-hostable | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ |
| Focus | IoT & services | Hosts & web | Hosts, certs | OSINT index | Internet scan DB | Threat intel | Recon workflow |
| Best for | Exposed devices | App & host search | Cert & host research | Metadata search | Attack surface discovery | Enterprise risk | Automated OSINT |

---

## 9. **Typical Use Cases Across Tools**
- **Asset discovery:** Shodan, ZoomEye, Censys  
- **IoT & exposed service detection:** Shodan  
- **Certificate & HTTPS research:** Censys  
- **Cyber threat intel:** CriminalIP, Onyphe  
- **Open source research workflows:** Sarenka  
- **Attack surface discovery:** Netlas

---

## 10. **Ethical and Legal Notes**
OSINT tools should be used responsibly:
- Respect target rights and privacy  
- Follow laws and terms of service  
- Do not scan or target networks without permission
