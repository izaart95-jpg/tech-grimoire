# Installing Linux (Ubuntu) on Android using Termux + proot-distro  
## With GUI (TigerVNC + LXQt/LXDE + optional SDDM)

---

## 1. Overview

This guide explains how to install **Ubuntu Linux** inside Android using:

- **Termux**
- **proot-distro**
- **Ubuntu**
- GUI via:
  - `tigervnc-standalone-server`
  - `dbus-x11`
  - `lxqt` or `lxde`
  - (Optional) `sddm`

⚠️ Note:
- This does NOT require root.
- It runs in a **proot container**, not a real kernel-level Linux.
- Performance depends on your device.

---

## 2. Install Termux

⚠️ Recommended: Install Termux from **F-Droid** or **GitHub** (maintained Play Store builds returned in June 2024, but they only support Android 11+).

After installation, open Termux and update packages:

```bash
pkg update && pkg upgrade -y
```
### Installing Required Packages
```bash
pkg install proot-distro  -y
```
## 3. Install Ubuntu using proot-distro
### List installed containers / search for installable images:
```bash
proot-distro list                 # containers you have installed
proot-distro search ubuntu        # search Docker Hub for images
```
### Install Ubuntu:
```bash
proot-distro install ubuntu:24.04
```
### Login into Ubuntu:
```bash
pd login ubuntu
```
### You are now inside Ubuntu.

## 4. Update Ubuntu
### Inside Ubuntu
```bash
apt update && apt upgrade -y
```
### Install Common Tools
```bash
apt install sudo nano wget curl -y
```
# 5. Install GUI Components

## 5.1 Install X11 + VNC Server
```bash
apt install tigervnc-standalone-server dbus-x11 -y
```
## 5.2 Install Desktop Environment

### Option 1: LXQt (Recommended)
```bash
apt install lxqt sddm -y
```
### Option 2: LXDE (Alternative)
```bash
apt install lxde -y
```
####  ⚠️ Note:
Inside proot, SDDM usually does NOT work properly because systemd is not running.
You can install it, but VNC method is recommended.
# 6. Configure VNC
### Set VNC password:
```bash
vncserver :1
```
#### It will ask to create a password.
### Kill initial VNC session:
```bash
vncserver -kill :1
```
# 7. Start VNC Server
### Start VNC
```bash
vncserver :1 -geometry 1280x720  # Change Geometry Based On Display
```
# 8. Connect from Android
### Install a VNC Viewer app:
- RealVNC Viewer # Recommended
- VNC Viewer

We Will Go With RealVNC You Can get It On PlayStore
## Create new connection:
- Address: localhost:5901
- Name: Anything
- Click on connection
- IF IT ASKS CONNECTION IS UNENCRYPTED CLICK OK/CONTINUE
- Password: The One You Set Earlier
- Click Connect

#### Pro Tip 
If you are getting low quality video (RealVNC Viewer)
Click On I button and select picture quality to High From Automatic
# 9. Important Limitations

No hardware acceleration (no GPU)

No real systemd support

Some apps may not work

Slower than native Linux

# 10. Alternative: Use Termux:X11 (Better Performance)

Instead of VNC, you can use:

Termux:X11 app

Direct X server forwarding

It gives better performance and smoother GUI.

**Recommended lightweight setup:** Ubuntu + LXQt/LXDE + Termux:X11.

