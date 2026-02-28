<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=35&pause=1000&color=1A1A1A&center=true&vCenter=true&width=500&height=70&lines=TECH+GRIMOIRE" alt="TECH GRIMOIRE" />

**A structured knowledge base covering systems fundamentals, networking, security, IoT, mobile, AI, dev tools, automation, deployment, media, mail, directories, Minecraft, torrenting, and reference material.**

---

</div>

## 📂 Documentation Index

### Fundamentals
| Document | Description |
|----------|-------------|
| [How a Computer Really Works](fundamentals/how-computers-work.md) | A full hardware-to-physics trace of one real scenario — opening YouTube on an Apple M-series MacBook: transistors, scheduler, WiFi, TLS, video decode, GPU, display, speaker |
| [HTTP vs HTTPS & TLS/SSL](fundamentals/http-https-tls.md) | How HTTPS actually works — TLS 1.3 handshake, cipher suites, X.509 certificates, PKI, HSTS, certificate transparency, known attacks |
| [CPU Architecture](fundamentals/cpu-architecture.md) | The CPU from silicon to software — pipelines, caches, out-of-order execution, branch prediction, NUMA, SIMD, privilege rings |
| [GPU Architecture](fundamentals/gpu-architecture.md) | How GPUs differ from CPUs — SM/warp execution, the graphics pipeline, rasterization vs ray tracing, CUDA/TPU compute, driver stack |
| [Compilers & Interpreters](fundamentals/compilers-and-interpreters.md) | What happens between source code and executing instructions — assembly, compiler stages, LLVM IR, JIT compilation |
| [Drivers & DLLs](fundamentals/drivers-and-dlls.md) | The glue layer between hardware and applications — device drivers, shared libraries (DLLs / .so), dynamic linker, services and daemons |
| [Linux Internals](fundamentals/linux-internals.md) | The kernel's moving parts — CFS scheduler, memory management, VFS, system calls, eBPF, cgroups |
| [Kernel Architecture](fundamentals/kernel-architecture.md) | How the big kernels differ — Linux, Windows NT, Darwin — architecture, syscall surface, debugging |
| [Operating Systems](fundamentals/operating-systems.md) | OS isolation theory tied to practice — chroot, proot, proot-distro, namespaces |
| [Linux Distributions](fundamentals/linux-distributions.md) | What distinguishes the major families — RHEL, Debian, Arch — package managers and release cycles |
| [Network Protocols](fundamentals/network-protocols.md) | Protocols organized by OSI/TCP-IP layer — what each is for, which port it uses, when it matters (TCP/UDP/QUIC, DNS, TLS, MQTT, BGP, WireGuard) |
| [Virtualization](fundamentals/virtualization.md) | The virtualization spectrum from lightweight subsystems (WSL) to full hypervisors — QEMU/KVM, VMware, VirtualBox, Hyper-V |
| [Wine Compatibility Layer](fundamentals/wine-compatibility.md) | How Windows apps run without emulation — Wine architecture, DXVK, Proton, Bottles, prefixes, macOS options (CrossOver/Whisky/GPTK) |
| [File Systems](fundamentals/file-systems.md) | On-disk data structures and the VFS layer — ext4, Btrfs, ZFS, XFS, NTFS, APFS, FUSE, procfs — plus the everyday commands |
| [Storage Technology](fundamentals/storage-technology.md) | Storage hardware from NAND cells to cable signaling — SD cards, DRAM, USB/Thunderbolt protocols, NVMe |
| [CGI & VFX](fundamentals/cgi-vfx.md) | How CGI/VFX production actually works — the rendering pipeline, path tracing, PBR shaders, compositing, simulation, mocap |
| [Ricing & Window Managers](fundamentals/ricing-window-managers.md) | Building a customized Linux desktop — tiling WMs (Hyprland, i3, bspwm, niri, sway, dwm), compositors, bars, dotfiles |

### Networking
| Document | Description |
|----------|-------------|
| [SSH Tunneling](networking/ssh-tunneling.md) | Exposing local services with SSH reverse tunnels — Pinggy, Serveo, localhost.run |
| [VPN & ZTNA](networking/vpn-and-ztna.md) | The shift from traditional VPNs to zero-trust mesh networking — Tailscale, WireGuard, NetBird, ProtonVPN, Tor, Playit.gg |
| [Free DNS Services](networking/free-dns-services.md) | Pointing a domain at a changing IP — free Dynamic DNS (No-IP, Dynu, DuckDNS, Cloudflare) and free domain services |
| [Remote Access](networking/remote-access.md) | Display protocols explained, then the tools built on them — X11, VNC, RDP, SPICE, Win-KeX, Sunshine+Moonlight, RustDesk, Guacamole |
| [Tunneling Tools](networking/tunneling-tools.md) | Managed tunnels beyond plain SSH — Ngrok, LocalXpose, Cloudflared — dashboards, custom domains, authentication |
| [OnionShare](networking/onionshare.md) | Sharing files, sites, and chat as temporary Tor onion services — no accounts, no third parties |

### Security
| Document | Description |
|----------|-------------|
| [Penetration Testing Tools](security/penetration-testing-tools.md) | The standard pentest workflow by phase — scanning, exploitation, password cracking, wireless auditing (Nmap, Metasploit, Burp Suite, Hashcat) |
| [OSINT Platforms](security/osint-platforms.md) | Internet-wide scanning engines and when each applies — Shodan, Censys, ZoomEye, Netlas, CriminalIP, Onyphe |
| [OSINT CLI Tools](security/osint-cli-tools.md) | Command-line OSINT research — email breaches, phone lookups, onion search (GhostTrack, Holehe, PhoneInfoga) |
| [Web Application Security](security/web-application-security.md) | A structured learning path — OWASP Top 10 and tooling, OffSec certification track, HackTheBox practice |
| [Reverse Engineering](security/reverse-engineering.md) | The RE workflow — disassembly, decompilation, dynamic instrumentation (Ghidra, IDA, x64dbg, radare2, GDB, Frida) |
| [Binary Analysis](security/binary-analysis.md) | Framework-level analysis of compiled binaries — symbolic execution and emulation (angr, Qiling, PANDA, miasm), structured parsing (Kaitai, MemProcFS) |
| [Exploit Development](security/exploit-development.md) | Learning binary exploitation systematically — RPISEC MBE, HackSys HSEVD, exploitation techniques, mitigation bypasses |
| [Offensive Frameworks](security/offensive-frameworks.md) | Automation and post-exploitation frameworks — fsociety, AutoSploit, WinPwn, commix, SSH-Snake, AndroRAT |
| [Active Directory](security/active-directory.md) | AD exploitation concepts in operation — Kerberoasting, Pass-the-Hash, DCSync, lateral movement, persistence |
| [Network Analysis](security/network-analysis.md) | Traffic analysis with Zeek — recording, protocol logging, scriptable detection and threat hunting |
| [Hacker Roadmap](security/hacker-roadmap.md) | A structured entry into security — the sundowndev roadmap, Awesome Hacking and other curated resource hubs |
| [OPSEC & Proxies](security/opsec-and-proxies.md) | Staying private while researching — threat modeling, proxy chaining (ProxyChains), anti-fingerprint browsers (Camoufox), disposable identities |
| [Bootable USB Tools](security/bootable-usb-tools.md) | Writing bootable USB media and multi-toolkits — Rufus, Ventoy, BalenaEtcher |
| [DHCP Attacks](security/network-security-dhcp-attacks.md) | How DHCP starvation and spoofing work, and the mitigations for each |
| [FingerprintJS](security/fingerprintjs.md) | How browser fingerprinting works — the signals, spoofing methods, and defensive uses (fraud/bot detection) |
| [RE MCP Guide](security/reverse-engineering-mcp.md) | Driving Ghidra-class tooling from AI assistants via MCP servers (Claude Code, Cline, Cursor) |

### IoT
| Document | Description |
|----------|-------------|
| [ESP32](iot/esp32.md) | The ESP32 SoC and its variant families (S2/S3/C3/C6/H2), power modes, and the two programming paths — Arduino vs ESP-IDF |
| [ESP8266](iot/esp8266.md) | The cheaper predecessor — modules and the basics of WiFi programming |
| [Arduino](iot/arduino.md) | The platform: board families, the programming model, and IDE 1.x vs 2.x |
| [Offensive Firmware](iot/offensive-firmware.md) | Turning ESP32s into WiFi/BT testing tools — ESP32 Marauder, Bruce, GhostESP compared |
| [Flipper Zero](iot/flipper-zero.md) | The device's radios and interfaces — Sub-GHz, RFID, NFC, IR, BadUSB, GPIO — and custom firmware |
| [LilyGo, STM32 & CNC](iot/lilygo-stm32-cnc.md) | LilyGo ESP32 boards, the STM32 family, and G-code-driven CNC control with CAM software |
| [Espectre Project](iot/projects/espectre/ESPECTRE_README.md) | A working example: ESP32 CSI motion detection with a real-time WebSocket dashboard |

### Mobile
| Document | Description |
|----------|-------------|
| [Termux Setup](mobile/termux-setup.md) | Termux from zero — installation, package management, SSH, Tmux, FFmpeg |
| [Linux on Android](mobile/linux-on-android.md) | A full Ubuntu desktop on Android without root — proot-distro, TigerVNC, LXQt/LXDE |
| [Desktop Environments](mobile/desktop-environments.md) | Headless desktop setups: XFCE, LXDE, GNOME, KDE over VNC and Termux X11 |
| [Environment Isolation](mobile/environment-isolation.md) | How Android isolates Linux environments — chroot vs proot vs proot-distro |
| [Termux Pentesting](mobile/termux-pentesting.md) | Security distributions inside Termux — Kali NetHunter Rootless, Parrot OS, BlackArch |
| [Emulators](mobile/emulators.md) | Running other platforms on Android — Android-in-Android (VPhone OS, VMOS), Windows via Wine layers (Winlator), QEMU (Vectras VM), PSP via PPSSPP |
| [Android Automation](mobile/android-automation.md) | Automating a phone: Tasker, MacroDroid, and on-device Arduino development |
| [Android System](mobile/android-system.md) | Deeper system access without root — Shizuku, rootless debloating, the phantom process killer fix |
| [Termux GPU Acceleration](mobile/termux-gpu-accel.md) | GPU rendering inside proot desktops — VirGL, Zink, Turnip/Adreno drivers |
| [Android Rooting](mobile/android-rooting.md) | How rooting actually works — bootloader unlock, Magisk/KernelSU/APatch, custom ROMs, Play Integrity bypass |

### AI
| Document | Description |
|----------|-------------|
| [Platforms & APIs](ai/platforms-and-apis.md) | Hosting platforms, API aggregators, and free inference endpoints — OpenRouter, Hugging Face, Groq, Ollama, llama.cpp |
| [Chat Interfaces](ai/chat-interfaces.md) | The assistant landscape explained — commercial tiers, free/open platforms, prompt communities, self-hosted UIs (LibreChat, Open WebUI) |
| [AI Video Tools](ai/ai-video-tools.md) | AI video by capability family — identity swap, generative video, avatars, editing/restoration, video understanding — with tools as examples |

### Dev Tools
| Document | Description |
|----------|-------------|
| [Coding Agents](devtools/coding-agents.md) | Autonomous coding tools by shape — AI IDEs (Cursor, Windsurf, Kiro), CLI agents (Claude Code), VS Code extensions (Cline) |
| [Editors & IDEs](devtools/editors-and-ides.md) | Editor setups beyond local VS Code — browser-based code-server, remote development, and the (now deprecated) Void Editor |
| [Terminal Tools](devtools/terminal-tools.md) | Session persistence and comfort — Tmux in depth, Tabby, modern emulator features |
| [Docker Essentials](devtools/docker-essentials.md) | Containers from images to registries — Dockerfiles, volumes, Compose |
| [Figma](devtools/figma.md) | Design-to-development pipeline — collaboration model, dev mode, prototyping, plugins |
| [Frameworks & Libraries](devtools/frameworks-and-libraries.md) | Programmatic control libraries — PyTorch for deep learning; Mineflayer, minecraft-protocol, go-mc for Minecraft bots |
| [APIs & Resources](devtools/apis-and-resources.md) | API fundamentals — types, authentication methods, and useful public APIs |
| [Version Control](devtools/version-control.md) | The three Git hosting platforms compared — Bitbucket, GitHub, GitLab: APIs, pipelines, CLI tooling, self-hosting |

### Automation
| Document | Description |
|----------|-------------|
| [Web Automation](automation/web-automation.md) | Browser automation and anti-bot countermeasures — Playwright, Selenium, Puppeteer, CAPTCHA solving, Camoufox |
| [Workflow Automation](automation/workflow-automation.md) | Event-driven pipelines — n8n for services, Tasker/MacroDroid for Android |
| [Discord Quest Completer](automation/discord-quest-completer.md) | How Discord Rich Presence can be faked to complete quests without installing games |
| [Userscripts](automation/userscripts.md) | Writing GM_ userscripts for Tampermonkey/Violentmonkey — intercepting XHR, modifying pages |

### Deployment
| Document | Description |
|----------|-------------|
| [Hosting Platforms](deployment/hosting-platforms.md) | Git-push deployment — Vercel, Netlify, Firebase Studio (sunsetting): functions, edge, CDNs |
| [Cloud Platforms](deployment/cloud-platforms.md) | Google Cloud and free notebook environments — Colab, Kaggle — for experimentation |
| [Kubernetes](deployment/kubernetes.md) | Container orchestration from first principles — deployments, services, ingress, Helm, managed GKE/EKS/AKS |

### Media
| Document | Description |
|----------|-------------|
| [Creative Software](media/creative-software.md) | Professional creative apps by workflow — Blender (3D), DaVinci Resolve (edit+color), Photoshop, Premiere, Filmora, CapCut |
| [Media Tools](media/media-tools.md) | Practical command recipes — FFmpeg conversion/streaming, VLC transcoding, GIMP editing |
| [Mobile Creative Tools](media/mobile-creative-tools.md) | Mobile editing — CapCut, Alight Motion — and hardware diagnostics with CPU-Z |
| [Image Upscalers](media/image-upscalers.md) | Neural upscaling vs classical interpolation — Real-ESRGAN, Upscayl, Waifu2x, web services |

### Mail
| Document | Description |
|----------|-------------|
| [Email — Providers & Clients](mail/email.md) | Privacy email end to end — zero-knowledge providers (Proton, Tuta) and desktop clients (Thunderbird, Canary), including Bridge/IMAP interop |

### Directories
| Document | Description |
|----------|-------------|
| [FMHY](directories/fmhy.md) | The largest collection of free stuff on the internet — the community-maintained index where free movies, video platforms, music, games, and books are cataloged |
| [EverythingMoe](directories/everythingmoe.md) | A curated index of ~1,000 otaku-culture sites — the discovery layer for anime/manga/light-novel categories |

### Minecraft
| Document | Description |
|----------|-------------|
| [Clients](minecraft/clients.md) | Client mods by class — utility (Meteor, Baritone), Meteor addons (Glazed), ghost clients (Vape, Raven B+, Hydrogen, Vestige) |
| [Servers](minecraft/servers.md) | Notable server networks — FakePixel, 2b2t, Hypixel, MineMenClub — game modes beyond vanilla |

### Torrenting
| Document | Description |
|----------|-------------|
| [BitTorrent Technology](torrenting/bittorrent-technology.md) | The protocol layer by layer — info hashes, piece verification, DHT, magnet links, PEX, MSE encryption |
| [Torrent Sites](torrenting/torrent-sites.md) | The indexing landscape and its domain churn — TPB, 1337x, YTS, TorrentGalaxy, Torrends.to |
| [Deluge](torrenting/deluge.md) | A seedbox-grade client — Deluge's daemon/client split, Web UI, plugins, VPN binding |

### Reference
| Document | Description |
|----------|-------------|
| [Archive.org](reference/archive-org.md) | The Internet Archive as infrastructure — Wayback Machine, software library, CDX API, uploading |
| [File Hosting & Transfer](reference/file-hosting.md) | The three hosted-sharing models compared — anonymous hosting (Gofile), persistent storage (MediaFire), encrypted storage (Mega), transfer (Smash) |
| [URL Shorteners](reference/url-shorteners.md) | How shorteners work end to end — earning-based services (Shrink.pe), analytics, self-hosting (YOURLS, Shlink, Kutt) |
| [Platforms & Communities](reference/platforms-and-communities.md) | Where cybersecurity people congregate — social platforms, news outlets, threat intel orgs, underground forums |

---

## 🛠 Maintenance

A link checker ships with the repo so the index and every cross-reference stay valid:

```bash
# Offline checks (fast): relative file links, intra-document anchors,
# and README index coverage
python3 tools/check-links.py

# Also probe every external URL (slower, needs network)
python3 tools/check-links.py --external
```

---

## ⚖️ Disclaimer

All security-related content is for **educational and authorized testing purposes only**.
