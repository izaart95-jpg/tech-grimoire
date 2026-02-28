# Kernel Architecture: Linux, Windows NT, and Darwin

## 1. What is a Kernel?

The **kernel** is the core component of an operating system that acts as a bridge between applications and hardware. It has complete control over everything in the system.

### Core Responsibilities
- **Process Management**: Creating, scheduling, and terminating processes
- **Memory Management**: Allocating and deallocating memory space
- **Device Management**: Controlling hardware through device drivers
- **File System Management**: Managing data storage and retrieval
- **Security & Access Control**: Enforcing permissions and isolation
- **System Calls**: Providing interface between applications and hardware

---

## 2. Computer Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER SPACE                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  Application│  │  Application│  │  Application│             │
│  │   (Browser) │  │   (Editor)  │  │   (Terminal)│             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│  ┌──────┴────────────────┴──────────────────────┐             │
│  │              System Call Interface             │             │
│  │         (libc, API, POSIX, Win32)             │             │
│  └─────────────────────┬─────────────────────────┘             │
└────────────────────────┼────────────────────────────────────────┘
                         │ TRAP / SYSCALL
┌────────────────────────┼────────────────────────────────────────┐
│                       KERNEL SPACE                               │
│  ┌─────────────────────▼──────────────────────────┐             │
│  │                    KERNEL                       │             │
│  │  ┌─────────────────────────────────────────┐  │             │
│  │  │         System Call Handler             │  │             │
│  │  └─────────────┬───────────────────────────┘  │             │
│  │  ┌─────────────▼───────────────────────────┐  │             │
│  │  │  Process │  Memory  │   File   │  Net  │  │             │
│  │  │Scheduler │ Manager  │  System  │ Stack │  │             │
│  │  └────────────────────┴──────────┴───────┘  │             │
│  │  ┌─────────────────────────────────────────┐  │             │
│  │  │         Device Drivers                   │  │             │
│  │  │  (GPU, Disk, USB, Network, Audio, etc.) │  │             │
│  │  └─────────────────────────────────────────┘  │             │
│  └───────────────────────────────────────────────┘             │
└────────────────────────┬────────────────────────────────────────┘
                         │ Hardware Abstraction
┌────────────────────────┼────────────────────────────────────────┐
│                       HARDWARE                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────  ┌──────────┐       │
│  │   CPU    │  │   RAM    │  │   Disk   │  │  Network │       │
│  │ (Cores)  │  │ (Memory) │  │  (SSD)   │  │   Card   │       │
│  └──────────  └──────────┘  └──────────┘  └──────────┘       │
│  ┌──────────┐  ┌──────────  ┌──────────┐  ┌──────────┐       │
│  │   GPU    │  │   USB    │  │  Audio   │  │  Sensors │       │
│  │ (Graphics│  │Controller│  │  Codec   │  │          │       │
│  └──────────┘  └──────────  └──────────┘  └──────────┘       │
└─────────────────────────────────────────────────────────────────┘

         PRIVILEGE LEVELS:
         ─────────────────
         Ring 3: User Space (Applications)
         Ring 0: Kernel Space (OS Kernel)
         
         MODES:
         ──────
         User Mode: Limited access, restricted instructions
         Kernel Mode: Full hardware access, privileged instructions
```

---

## 3. Linux Kernel

### Overview
- **Type**: Monolithic kernel with modular design
- **License**: GPL v2 (Open Source)
- **Created**: 1991 by Linus Torvalds
- **Architecture**: C with some assembly
- **Used In**: Linux distributions, Android, ChromeOS, embedded systems

### Architecture
```
┌─────────────────────────────────────────────┐
│            Linux Kernel Space                │
│  ┌─────────────────────────────────────────┐│
│  │  System Call Interface (vsyscall/vDSO)  ││
│  └─────────────────┬───────────────────────┘│
│  ┌─────────────────▼───────────────────────┐│
│  │  Core Subsystems:                        ││
│  │  • Process Scheduler (EEVDF, was CFS)   ││
│  │  • Memory Manager (MM)                  ││
│  │  • Virtual File System (VFS)            ││
│  │  • Network Stack                        ││
│  │  • IPC (Signals, Pipes, Sockets)        ││
│  └─────────────────┬───────────────────────┘│
│  ┌─────────────────▼───────────────────────┐│
│  │  Loadable Kernel Modules (LKMs)          ││
│  │  • Device Drivers                        ││
│  │  • File Systems (ext4, XFS, Btrfs)      ││
│  │  • Network Protocols                     ││
│  └─────────────────────────────────────────┘│
└─────────────────────────────────────────────┘
```

### Key Features
- **Preemptive multitasking**
- **Virtual memory** with paging
- **Loadable kernel modules** (dynamic driver loading)
- **Namespaces** (containers support)
- **cgroups** (resource limiting)
- **Netfilter** (firewall/packet filtering)
- **KVM** (Kernel-based Virtual Machine)

### Common Usage & Commands

```bash
# Check kernel version
uname -r
cat /proc/version

# List loaded kernel modules
lsmod                      # /proc/modules
modinfo <module_name>      # Detailed module info

# Load/unload kernel modules
sudo modprobe <module_name>
sudo rmmod <module_name>

# View kernel messages (boot, drivers, errors)
dmesg
dmesg -w  # Follow in real-time

# Kernel parameters
cat /proc/sys/kernel/*
sudo sysctl -a
sudo sysctl -w vm.swappiness=10

# Build/install kernel (Debian/Ubuntu)
sudo apt install build-essential libncurses-dev bison flex
make menuconfig
make -j$(nproc)
sudo make modules_install
sudo make install

# Check kernel config
zcat /proc/config.gz | grep CONFIG_<OPTION>
cat /boot/config-$(uname -r) | grep CONFIG_<OPTION>
```

### System Calls Examples
```c
// C program making system calls
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    // open() - syscall to open file
    int fd = open("/tmp/test.txt", O_CREAT | O_WRONLY, 0644);
    
    // write() - syscall to write data
    write(fd, "Hello Kernel!", 14);
    
    // close() - syscall to close file
    close(fd);
    
    // fork() - syscall to create process
    pid_t pid = fork();
    
    return 0;
}

// Trace system calls
strace ./program
strace -e open,read,write ./program
```

---

## 4. Windows NT Kernel

### Overview
- **Type**: Hybrid kernel (microkernel design with monolithic implementation)
- **License**: Proprietary (Microsoft)
- **Created**: 1988-1993 by Dave Cutler
- **Architecture**: C and C++
- **Used In**: Windows NT, 2000, XP, Vista, 7, 8, 10, 11, Windows Server

### Architecture
```
┌─────────────────────────────────────────────────────┐
│              Windows User Mode (Ring 3)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Win32 API  │  │  .NET/CLR   │  │  POSIX/W SL │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         │                │                │         │
│  ┌──────▼────────────────▼────────────────▼──────┐ │
│  │           Subsystem DLLs (kernel32.dll)       │ │
│  └───────────────────────┬───────────────────────┘ │
└──────────────────────────┼──────────────────────────┘
                           │ NtCreateFile, etc.
┌──────────────────────────▼──────────────────────────┐
│              Windows Kernel Mode (Ring 0)            │
│  ┌─────────────────────────────────────────────────┐│
│  │              Executive Services                  ││
│  │  ┌─────────────────────────────────────────────┐││
│  │  │  Object Manager | Security Reference Monitor│││
│  │  │  Process/Thread Manager | Virtual Memory Mgr│││
│  │  │  I/O Manager | Cache Manager | Power Mgr    │││
│  │  └─────────────────────────────────────────────┘││
│  └─────────────────────┬───────────────────────────┘│
│  ┌─────────────────────▼───────────────────────────┐│
│  │              Kernel (ntoskrnl.exe)               ││
│  │  • Thread Scheduling | Interrupt/Exception Disp ││
│  │  • Multiprocessor Synchronization               ││
│  └─────────────────────┬───────────────────────────┘│
│  ┌─────────────────────▼───────────────────────────┐│
│  │           Hardware Abstraction Layer (HAL)       ││
│  │  • Abstracts hardware differences               ││
│  │  • hal.dll                                      ││
│  └─────────────────────┬───────────────────────────┘│
│  ┌─────────────────────▼───────────────────────────┐│
│  │              Device Drivers                      ││
│  │  • File system drivers (NTFS, FAT32, ReFS)     ││
│  │  • Hardware drivers (.sys files)                ││
│  │  • Filter drivers                               ││
│  └─────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

### Key Features
- **Object-based design** (everything is an object)
- **Hardware Abstraction Layer (HAL)**
- **I/O Ring buffers** for performance
- **Asynchronous I/O**
- **Security descriptors** and ACLs
- **Registry** (centralized configuration)
- **Driver Model** (WDM, WDF)
- **Hyper-V** (Type-1 hypervisor)

### Common Usage & Commands

```powershell
# Windows PowerShell / Command Prompt

# Check kernel/version info
systeminfo
ver
wmic os get BuildNumber, Version

# View loaded drivers
driverquery
driverquery /v  # Verbose
Get-WindowsDriver -Online  # PowerShell

# System Information
msinfo32  # GUI
systeminfo | findstr /C:"OS Name" /C:"OS Version"

# Event Viewer (kernel logs)
eventvwr.msc
# Kernel logs in: Windows Logs → System
wevtutil qe System /c:10 /rd:true /f:text

# Registry (kernel parameters)
regedit
reg query "HKLM\SYSTEM\CurrentControlSet\Control"

# Device Manager (drivers)
devmgmt.msc
pnputil /enum-drivers  # List drivers

# Check for kernel updates
start ms-settings:windowsupdate   # Windows Update settings (wuapp.exe is deprecated)
usoclient StartScan  # PowerShell

# Blue Screen logs
# Located in: C:\Windows\Minidump\
# Use WinDbg for analysis
```

### Windows Driver Development
```c
// Basic WDM Driver Skeleton (C)
#include <ntddk.h>

NTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath) {
    DbgPrint("Driver loaded!\n");
    
    // Create device
    UNICODE_STRING deviceName;
    RtlInitUnicodeString(&deviceName, L"\\Device\\MyDevice");
    
    PDEVICE_OBJECT deviceObject;
    IoCreateDevice(DriverObject, 0, &deviceName, FILE_DEVICE_UNKNOWN, 
                   0, FALSE, &deviceObject);
    
    return STATUS_SUCCESS;
}

NTSTATUS UnloadDriver(PDRIVER_OBJECT DriverObject) {
    DbgPrint("Driver unloaded!\n");
    return STATUS_SUCCESS;
}
```

---

## 5. Darwin Kernel (XNU)

### Overview
- **Type**: Hybrid kernel (XNU = "X is Not Unix")
- **License**: Apple Public Source License (Open Source core)
- **Created**: 1996, based on Mach 3.0 + BSD
- **Architecture**: C, C++, Objective-C
- **Used In**: macOS, iOS, iPadOS, watchOS, tvOS

### Architecture
```
┌─────────────────────────────────────────────────────┐
│              Darwin User Space (Ring 3)              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Cocoa/API  │  │  Unix CLI   │  │  iOS SDK    │ │
│  └──────┬──────┘  └──────┬──────┘  └────────────┘ │
│         │                │                │         │
│  ┌──────▼────────────────▼────────────────▼──────┐ │
│  │      libSystem (BSD libc, Mach APIs)          │ │
│  └───────────────────────┬───────────────────────┘ │
└──────────────────────────┼──────────────────────────┘
                           │ mach_trap, BSD syscalls
┌──────────────────────────▼──────────────────────────┐
│              XNU Kernel (Ring 0)                     │
│  ┌─────────────────────────────────────────────────┐│
│  │           BSD Layer (POSIX/BSD API)              ││
│  │  • Process model | Signals | Permissions        ││
│  │  • POSIX APIs | Sockets | File descriptors     ││
│  │  • VFS | APFS, HFS+, UFS, NTFS (read-only)    ││
│  └─────────────────────┬───────────────────────────┘│
│  ┌─────────────────────▼───────────────────────────┐│
│  │           I/O Kit (Device Drivers)               ││
│  │  • Object-oriented (C++ subset)                 ││
│  │  • Driver framework | Power management         ││
│  │  • USB, PCIe, Network, Graphics drivers        ││
│  └─────────────────────┬───────────────────────────┘│
│  ┌─────────────────────▼───────────────────────────┐│
│  │           Mach Microkernel                       ││
│  │  • IPC (Inter-Process Communication)            ││
│  │  • Virtual Memory (pagemap, copy-on-write)     ││
│  │  • Threads & Scheduling | Synchronization      ││
│  │  • Message passing (ports, messages)           ││
│  └─────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

### Key Features
- **Mach IPC** (message-based communication)
- **BSD compatibility layer** (POSIX compliance)
- **I/O Kit** (driver framework)
- **APFS** (Apple File System)
- **Grand Central Dispatch** (concurrency)
- **Sandboxing** (seatbelt)
- **Code signing** enforcement
- **System Integrity Protection (SIP)**

### Common Usage & Commands

```bash
# macOS Terminal / iOS (jailbroken)

# Check kernel version
uname -a
uname -r  # Darwin version
sw_vers   # macOS version

# Kernel information
sysctl kern.*
sysctl kern.version
sysctl hw.ncpu

# Loaded kernel extensions (kexts)
kextstat
kextstat | grep -v com.apple  # Show only 3rd party

# Load/unload kexts (requires SIP disabled)
sudo kextload /path/to/kext.kext
sudo kextunload -bundle-identifier com.example.driver

# System logs (kernel messages)
log show --predicate 'eventMessage contains "kernel"' --last 1h
dmesg  # Limited on modern macOS
log stream --level info

# Process info (Mach/BSD)
ps aux
top
vm_stat  # Virtual memory statistics

# I/O Kit registry
ioreg -l
ioreg -p IOUSB -l  # USB devices
ioreg -p IOService | grep -i battery

# System Integrity Protection status
csrutil status  # In Recovery Mode

# Build kernel from source (Apple Open Source)
# https://opensource.apple.com/
```

### XNU Kernel Development
```c
// Basic I/O Kit Driver Skeleton (C++)
#include <IOKit/IOService.h>
#include <IOKit/IOLib.h>

class com_example_driver : public IOService {
    OSDeclareDefaultStructors(com_example_driver)
    
public:
    virtual bool start(IOService *provider) override;
    virtual void stop(IOService *provider) override;
    virtual IOReturn someMethod(int arg);
};

bool com_example_driver::start(IOService *provider) {
    if (!super::start(provider))
        return false;
    
    IOLog("Example driver started\n");
    return true;
}

void com_example_driver::stop(IOService *provider) {
    IOLog("Example driver stopped\n");
    super::stop(provider);
}
```

---

## 6. Kernel Comparison Matrix

| Feature | Linux | Windows NT | Darwin (XNU) |
|---------|-------|------------|--------------|
| **Type** | Monolithic (modular) | Hybrid | Hybrid (Mach + BSD) |
| **License** | GPL v2 | Proprietary | APSL (core) |
| **Source** | Open source | Closed source | Partially open |
| **IPC** | Sockets, pipes, shared mem | LPC, ALPC, named pipes | Mach messages |
| **Drivers** | LKMs (Loadable Kernel Modules) | WDM/WDF drivers | I/O Kit (C++) |
| **File Systems** | ext4, XFS, Btrfs, ZFS | NTFS, ReFS, FAT32 | APFS, HFS+, UFS, NTFS (read-only) |
| **VM System** | Custom (mm/) | Custom | Mach VM |
| **Scheduler** | EEVDF (was CFS) | Multilevel feedback queue | Mach + BSD |
| **Security** | SELinux, AppArmor, capabilities | ACLs, Integrity Levels | Sandbox, SIP |
| **Virtualization** | KVM, Xen | Hyper-V | Hypervisor.framework |
| **Package Mgr** | apt, dnf, pacman | MSI, Winget, Chocolatey | Homebrew, pkg |

---

## 7. How Data Flows Through the System

### Example: Reading a File from Disk

```
┌─────────────────────────────────────────────────────────────┐
│ 1. APPLICATION LAYER                                         │
│    fopen("/home/user/file.txt", "r")                        │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 2. LIBRARY LAYER (User Space)                                │
│    libc: fopen() → open() syscall                            │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 3. SYSCALL INTERFACE                                         │
│    TRAP instruction (interrupt 0x80 / syscall)              │
│    Switch from User Mode (Ring 3) → Kernel Mode (Ring 0)   │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 4. KERNEL: VFS LAYER                                         │
│    open() → VFS lookup path "/home/user/file.txt"           │
│    Determine file system type (ext4/NTFS/APFS)              │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 5. KERNEL: FILESYSTEM DRIVER                                 │
│    ext4: Read inode, check permissions                      │
│    Translate file path to disk blocks                       │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 6. KERNEL: PAGE CACHE                                        │
│    Check if data in cache (RAM)                             │
│    If miss → request from block layer                       │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 7. KERNEL: BLOCK LAYER / I/O SCHEDULER                       │
│    Create I/O request (read blocks 12345-12350)             │
│    Schedule request (none, mq-deadline, bfq)                   │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 8. KERNEL: DEVICE DRIVER                                     │
│    SATA/NVMe driver converts to hardware commands           │
│    Program DMA (Direct Memory Access)                       │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 9. HARDWARE: STORAGE CONTROLLER                              │
│    SSD/HDD controller seeks and reads data                  │
│    DMA transfers data directly to RAM                       │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 10. HARDWARE: INTERRUPT                                      │
│    Disk raises IRQ (Interrupt Request)                      │
│    CPU pauses, executes Interrupt Service Routine (ISR)     │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 11. KERNEL: INTERRUPT HANDLER                                │
│    Acknowledge interrupt                                    │
│    Mark I/O request complete                                │
│    Wake up waiting process                                  │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 12. KERNEL: RETURN TO USER SPACE                             │
│    Copy data from kernel buffer to user buffer              │
│    Restore user context (registers, stack)                  │
│    Switch back to User Mode (Ring 3)                        │
│    ↓                                                         │
├─────────────────────────────────────────────────────────────┤
│ 13. APPLICATION LAYER                                        │
│    fread() receives data                                    │
│    Application processes file contents                      │
└─────────────────────────────────────────────────────────────┘

Total time: ~100 microseconds (SSD) to ~10 milliseconds (HDD)
Context switches: 2 (User→Kernel, Kernel→User)
Mode switches: Multiple (interrupts, scheduling)
```

---

## 8. Advanced Kernel Concepts

### Virtual Memory Translation
```
┌─────────────────────────────────────────────────────┐
│              VIRTUAL ADDRESS (48-bit)                │
│  ┌─────────┬─────────┬─────────┬─────────┬────────┐│
│  │ PML4    │ PDPT    │ PD      │ PT      │ Offset ││
│  │ (9 bit) │(9 bit)  │(9 bit)  │(9 bit)  │(12 bit)││
│  └────┬────┴────┬────┴────┬────┴────┬────┴────┬───│
│       │         │         │         │         │    │
│       ↓         ↓         ↓         ↓         ↓    │
│  ┌─────────┐┌─────────┐┌─────────┐┌─────────┐    │
│  │ PML4    ││ PDPT    ││ PD      ││ PT      │    │
│  │ Table   ││ Table   ││ Table   ││ Table   │    │
│  └────┬────┘└────┬────┘└────┬────┘└────┬────┘    │
│       │         │         │         │            │
│       └─────────┴─────────┴─────────┘            │
│                    │                              │
│                    ↓                              │
│         ┌──────────────────┐                     │
│         │   PHYSICAL RAM   │                     │
│         │   (Actual Data)  │                     │
│         └──────────────────┘                     │
└───────────────────────────────────────────────────┘

MMU (Memory Management Unit) performs this translation
TLB (Translation Lookaside Buffer) caches recent translations
```

### Interrupt Handling Flow
```
Hardware Event (Key press, Network packet, Disk I/O complete)
                    ↓
         Hardware raises IRQ line
                    ↓
    CPU finishes current instruction
                    ↓
         CPU saves context (registers, PC)
                    ↓
         CPU jumps to IDT entry (Interrupt Descriptor Table)
                    ↓
         Execute Interrupt Service Routine (ISR)
                    ↓
         Top Half (Hard IRQ) - Quick, time-critical
                    ↓
         Schedule Bottom Half (Soft IRQ, Tasklet, Workqueue)
                    ↓
         Send EOI (End of Interrupt) to PIC/APIC
                    ↓
         Restore context and resume interrupted task
```

---

## 9. Kernel Development & Debugging

### Linux Kernel Debugging
```bash
# Enable kernel debugging
dmesg -w    # debug_kmsg was removed from modern kernels

# Use KGDB (kernel gdb)
# Boot with: kgdboc=ttyS0,115200 kgdbwait
gdb vmlinux
(gdb) target remote /dev/ttyS0

# ftrace (function tracer)
echo function > /sys/kernel/debug/tracing/current_tracer
cat /sys/kernel/debug/tracing/trace

# perf (performance monitoring)
perf record -a
perf report
perf top

# SystemTap (dynamic tracing)
stap -e 'probe kernel.function("do_sys_open") { 
    printf("Opening: %s\n", user_string($arg2)) 
}'

# eBPF/BCC (modern tracing)
./opensnoop  # Trace file opens
./execsnoop  # Trace process execs
```

### Windows Kernel Debugging
```powershell
# WinDbg setup
# Enable kernel debugging:
bcdedit /debug on
bcdedit /dbgsettings net hostip:192.168.1.100 port:50000

# Connect from host WinDbg
windbg -k net:port=50000,target=192.168.1.50

# Common WinDbg commands
!analyze -v          # Analyze crash
lm                   # List modules
!process 0 0         # List processes
!thread              # Thread info
!irp                 # I/O Request Packet
kb                   # Stack trace

# Driver Verifier (stress test drivers)
verifier /standard /all
verifier /querysettings
verifier /reset
```

### Darwin/XNU Debugging
```bash
# Enable kernel debugging
# Boot args: nvram boot-args="kdp_match_name=en0"

# LLDB kernel debugging
lldb -c /Library/Developer/KDKs/*/System/Library/Kernels/kernel

# DTrace (dynamic tracing)
sudo dtrace -n 'syscall::open*:entry { printf("%s", copyinstr(arg0)); }'

# Instruments (GUI profiling)
open -a Instruments

# Kernel core dumps
# Located in /Library/Logs/DiagnosticReports/
```

---

## 10. Security Considerations

### Kernel Security Features

| Feature | Linux | Windows NT | Darwin |
|---------|-------|------------|--------|
| **ASLR** | ✓ (KASLR) | ✓ | ✓ |
| **DEP/NX** | ✓ | ✓ | ✓ |
| **SMEP/SMAP** | ✓ | ✓ | ✓ |
| **Stack Canaries** | ✓ | ✓ | ✓ |
| **Module Signing** | ✓ | ✓ (WHQL) | ✓ |
| **Sandboxing** | seccomp, AppArmor | AppContainer | Seatbelt, Sandbox |
| **Secure Boot** | ✓ | ✓ | ✓ |
| **Kernel Hardening** | grsecurity (was) | PatchGuard | SIP |

### Common Kernel Vulnerabilities
- **Buffer overflows** in drivers
- **Use-after-free** bugs
- **Privilege escalation** via syscalls
- **Race conditions** in synchronization
- **Side-channel attacks** (Spectre, Meltdown)
- **DMA attacks** via Thunderbolt/PCIe

---

## 11. Resources & Further Reading

### Linux Kernel
- **Source**: https://github.com/torvalds/linux
- **Docs**: https://www.kernel.org/doc/html/latest/
- **Books**: "Linux Kernel Development" by Robert Love
- **Courses**: Linux Foundation Kernel Development

### Windows NT
- **Docs**: https://docs.microsoft.com/windows-hardware/drivers/
- **Books**: "Windows Internals" by Pavel Yosifovich
- **Tools**: Windows Driver Kit (WDK), WinDbg

### Darwin/XNU
- **Source**: https://opensource.apple.com/
- **Docs**: https://developer.apple.com/library/archive/
- **Books**: "Mac OS X Internals" by Amit Singh

### General OS Theory
- **Books**: "Operating Systems: Three Easy Pieces"
- **Courses**: MIT 6.S081 (Operating System Engineering)
- **Papers**: Original Mach, Unix papers

---

## 12. Quick Reference: Kernel Commands

```bash
# ========== LINUX ==========
uname -a                    # All system info
lsmod                       # List modules
dmesg | tail                # Recent kernel messages
sysctl -a                   # All kernel params
modprobe <name>             # Load module
insmod <file.ko>            # Insert module
rmmod <name>                # Remove module

# ========== WINDOWS ==========
systeminfo                  # System information
driverquery                 # List drivers
msinfo32                    # System info GUI
bcdedit                     # Boot configuration
verifier                    # Driver verifier
winver                      # Windows version

# ========== DARWIN/macOS ==========
uname -a                    # System info
kextstat                    # List kexts
sysctl -a                   # System controls
ioreg -l                    # I/O Registry
log show --last 1h          # System logs
sw_vers                     # macOS version
```

---

> **💡 Pro Tip**: Understanding kernels is fundamental to systems programming, security research, and performance optimization. Always test kernel modifications in virtual machines first!

---

## 13. Linux Kernel Modules Management

### Listing & Inspecting Modules

```bash
# List all loaded modules
lsmod

# Detailed module information
modinfo <module_name>

# List available modules for current kernel
find /lib/modules/$(uname -r) -name "*.ko"

# Common module categories
lsmod | grep -E 'e1000|igb|ixgbe|iwlwifi|ath'     # Network drivers
lsmod | grep -E 'ext4|xfs|btrfs|vfat|ntfs'         # Filesystem modules
lsmod | grep -E 'kvm|kvm_intel|kvm_amd|vboxdrv'     # Virtualization
lsmod | grep -E 'i915|nvidia|amdgpu|radeon'         # Graphics
lsmod | grep -E 'usb_storage|xhci_hcd|ehci_hcd'     # USB modules
```

### Loading & Unloading

```bash
# Load a module
sudo modprobe <module_name>

# Remove a module
sudo modprobe -r <module_name>

# Blacklist a module (prevent loading)
echo "blacklist <module_name>" | sudo tee -a /etc/modprobe.d/blacklist.conf

# Auto-load module at boot
echo "<module_name>" | sudo tee -a /etc/modules-load.d/<module_name>.conf
```

---

## 14. Kernel Parameters & Tuning

### Viewing and Modifying Parameters

```bash
# View all kernel parameters
sysctl -a

# View specific parameter
sysctl kernel.hostname

# Temporarily change parameter
sudo sysctl -w vm.swappiness=10

# Permanently change parameter
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf

# Reload sysctl configuration
sudo sysctl -p

# Parameter filesystem layout
/proc/sys/
├── kernel/      # Core kernel parameters
├── vm/          # Virtual memory settings
├── net/         # Network stack parameters
├── fs/          # Filesystem settings
└── dev/         # Device-specific settings
```

### Important Parameters Reference

```bash
# Memory Management
vm.swappiness              # Swap usage tendency (0-100, default 60)
vm.dirty_ratio             # Max dirty pages before blocking writes (%)
vm.dirty_background_ratio  # Background writeback threshold (%)
vm.overcommit_memory       # Memory overcommit policy (0,1,2)

# Network Tuning
net.core.somaxconn         # Max listen queue backlog
net.ipv4.tcp_max_syn_backlog  # SYN backlog size
net.ipv4.ip_forward        # IP forwarding (0=off, 1=on)

# Security
kernel.randomize_va_space  # ASLR (0=off, 1=partial, 2=full)
kernel.dmesg_restrict      # Restrict dmesg access (0,1)
kernel.kptr_restrict       # Kernel pointer restriction (0,1,2)
```

### Example: High-Performance Web Server Tuning

```bash
# /etc/sysctl.d/99-webserver.conf
fs.file-max = 2097152
net.ipv4.ip_local_port_range = 1024 65535
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.ipv4.tcp_rmem = 4096 87380 16777216
net.ipv4.tcp_wmem = 4096 87380 16777216
net.ipv4.tcp_window_scaling = 1
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 8192

# Apply changes
sudo sysctl -p /etc/sysctl.d/99-webserver.conf
```

---

## 15. Kernel Compilation & Building

### Prerequisites

```bash
# Debian/Ubuntu
sudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev

# RHEL/Fedora
sudo dnf install gcc make ncurses-devel bison flex openssl-devel elfutils-libelf-devel
```

### Building from Source

```bash
# 1. Download kernel source (browse available releases in
#    https://cdn.kernel.org/pub/linux/kernel/)
cd /usr/src
sudo wget https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-7.3.tar.xz
sudo tar -xf linux-7.3.tar.xz
cd linux-7.3

# 2. Get current config
cp /boot/config-$(uname -r) .config

# 3. Update config for new version
make olddefconfig
# OR: Interactive configuration
make menuconfig

# 4. Compile kernel
make -j$(nproc)

# 5. Compile and install modules
make modules
sudo make modules_install

# 6. Install kernel
sudo make install

# 7. Update bootloader
sudo update-grub                                    # Debian/Ubuntu
sudo grub2-mkconfig -o /boot/grub2/grub.cfg         # RHEL/Fedora

# 8. Reboot
sudo reboot
```

---

## 16. Kernel Versioning & Lifecycle

### Version Number Format

```
Major.Minor.Patch-Extra
Example: 6.5.11-200.fc38.x86_64

• 6      = Major version
• 5      = Minor version
• 11     = Patch level
• 200    = Distribution-specific build number
• fc38   = Fedora 38
• x86_64 = Architecture
```

### Release Cycle

```
MAINLINE KERNEL
• Released every 9-10 weeks
• Latest features and drivers
• Maintained by Linus Torvalds
        ↓
STABLE KERNEL
• Bug fixes and security patches
• Maintained by Greg Kroah-Hartman
        ↓
LONGTERM (LTS)
• Maintained for 2-6+ years
• Critical fixes only
• Used by distributions (RHEL, Ubuntu LTS)
• Current LTS: 5.10, 5.15, 6.1, 6.6, 6.12, 6.18  (current stable: 7.3)
```

---

## 17. Advanced: eBPF, Namespaces & cgroups

### eBPF (Extended Berkeley Packet Filter)

```bash
# Install tools
sudo apt install bpfcc-tools linux-tools-$(uname -r)

# Trace exec() calls
sudo /usr/share/bcc/tools/execsnoop

# Trace file opens
sudo /usr/share/bcc/tools/opensnoop

# Trace TCP connections
sudo /usr/share/bcc/tools/tcpconnect
```

### Namespaces (Container Foundation)

```bash
# View namespaces
ls -la /proc/self/ns/

# Namespace types: pid, net, mnt, uts, ipc, user

# Create isolated namespace
unshare --pid --fork --mount-proc /bin/bash
```

### Control Groups (cgroups)

```bash
# View cgroups
cat /proc/<pid>/cgroup

# Modern cgroups v2
ls /sys/fs/cgroup/

# Limit memory for a process (cgroups v2)
mkdir /sys/fs/cgroup/mygroup
echo 512M > /sys/fs/cgroup/mygroup/memory.max
echo <pid> > /sys/fs/cgroup/mygroup/cgroup.procs
```

---

## 18. Kernel Hardening

```bash
# Enable lockdown mode
# Boot parameter: lockdown=confidentiality

# Disable module loading (maximum security)
echo 1 | sudo tee /proc/sys/kernel/modules_disabled

# Restrict ptrace
echo "kernel.yama.ptrace_scope = 2" | sudo tee -a /etc/sysctl.d/60-kernel-hardening.conf

# Enable strict reverse path filtering
echo "net.ipv4.conf.all.rp_filter = 1" | sudo tee -a /etc/sysctl.d/60-kernel-hardening.conf

# Check security features
cat /proc/sys/kernel/randomize_va_space    # ASLR
cat /proc/sys/kernel/kptr_restrict         # Kernel pointer restriction
cat /proc/sys/kernel/dmesg_restrict        # dmesg restriction
```

---

## 19. Best Practices

**Security:**
- Keep kernel updated with security patches
- Use signed kernel modules
- Enable SELinux/AppArmor
- Disable unnecessary kernel modules

**Performance:**
- Tune kernel parameters for workload
- Use appropriate I/O scheduler
- Monitor system resources regularly

**Stability:**
- Test new kernels in staging first
- Keep previous kernel for rollback
- Monitor kernel logs for errors
- Use LTS kernels for production

**Maintenance:**
- Document custom kernel parameters
- Backup kernel configurations
- Remove old unused kernels
