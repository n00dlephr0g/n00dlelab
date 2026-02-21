---
tags:
  - machine
  - virtual
  - core
Interfaces:
  - "[[scallop-vmbr0|vmbr0]]"
  - "[[scallop-vmbr1|vmbr1]]"
IP:
  - 10.10.0.1
  - 192.168.0.x/24
Host: "[[thinkcentre-m710s_1|scallop]]"
Hostname: router
OS: "[[opnsense]]"
---
# Function
Gateway and router for [[scallop-vmbr1|vmbr1]]
Static:
- `10.10.0.2 -> 10.10.0.254`
DHCP:
- `10.10.1.1` -> `10.10.1.254`
