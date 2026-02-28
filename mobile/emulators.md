# Emulators on Android

Running other platforms on Android splits into three families, each with a different architecture:

- **Android-on-Android virtualization** — a full virtual Android system inside your phone (VPhone OS, VMOS) or app-level container cloning (VirtualXposed, Parallel Space)
- **PC compatibility layers** — running Windows/DOS software through translation layers (Winlator, XoDos) or full OS images through QEMU (Vectras VM)
- **Console emulation** — recreating hardware like the PSP locally (PPSSPP)

---

## Table of Contents
1. [Android-on-Android Emulators](#1-android-on-android-emulators)
2. [Winlator — Windows Compatibility Layer](#2-winlator--windows-compatibility-layer)
3. [Horizon Emulator](#3-horizon-emulator)
4. [XoDos — DOS Emulation](#4-xodos--dos-emulation)
5. [Vectras VM — Full OS Virtualization](#5-vectras-vm--full-os-virtualization)
6. [GameHub — Winlator-Based Windows Emulator](#6-gamehub--winlator-based-windows-emulator)
7. [PPSSPP — PSP Emulation](#7-ppsspp--psp-emulation)
8. [Comparison](#8-comparison)
9. [Performance Requirements](#9-performance-requirements)
10. [Risks & Legal Notes](#10-risks--legal-notes)

---

## 1. Android-on-Android Emulators

### 1.1 The Concept

An Android-on-Android emulator creates a secondary Android system that runs like a separate phone inside your main phone. Two evolutions exist:

1. **Full virtual OS** — a complete Android environment with its own settings app, storage, and app stack (VPhone OS, VMOS, X8 Sandbox)
2. **App-level container cloning** — apps run in isolated sandboxes using techniques like containerized wrappers, without a visible second Android (VirtualXposed, Parallel Space)

| Feature | Full Virtual OS | App Cloner |
|---------|----------------|------------|
| Full Android system | Yes | No |
| Separate settings app | Yes | No |
| Root possible | Sometimes | No |
| Performance cost | Higher | Lower |
| Isolation level | Strong | Moderate |

### 1.2 The Apps

- **VPhone OS** — a fully isolated virtual Android environment inside the host phone; primarily used for multi-account gaming, app cloning, sandboxed testing, and automation. Features: separate Google Play login, independent storage/app installs, background running, game optimization modes, and in some builds root access and virtual GPS/IMEI parameters
- **VMOS** — virtual Android with root support and parallel app environment
- **X8 Sandbox** — game-oriented with macro/script automation tools
- **VirtualXposed** — app-level virtualization, no root required, module support
- **Parallel Space** — app cloning only, lightweight, not a full Android system

### 1.3 How the Isolation Works

Consumer Android-on-Android virtualization generally can't use hardware virtualization — stock Android restricts it. These apps approximate it with:

- Linux namespaces
- Binder virtualization
- Kernel-level hooks
- Modified ART runtime
- QEMU (rare on mobile)

### 1.4 Trade-offs

**Advantages:** no PC required, runs alongside Android, lighter than PC emulators, portable.

**Limitations:** high RAM usage, battery drain, thermal load, host-device-dependent performance, and real security exposure in unofficial builds (some request dangerous permissions, bypass app protections, or smuggle malware — see [§10](#10-risks--legal-notes)).

**vs PC emulators (BlueStacks, LDPlayer, NoxPlayer, MEmu):** more portable, but PC emulators win on gaming performance and multi-instance management.

---

## 2. Winlator — Windows Compatibility Layer

- **Platform:** Android
- **Purpose:** run Windows x86 applications and games on ARM devices
- **Architecture:** Wine + Box86/Box64 + DXVK/VKD3D

### 2.1 The Stack

```
Windows game → Wine (Windows API compatibility layer)
            → Box86/Box64 (x86 code translated to ARM)
            → DXVK / VKD3D (DirectX 9/10/11 translated to Vulkan)
            → Android device GPU
```

The whole chain runs locally on the device — no cloud streaming involved.

### 2.2 Features & Limitations

**Features:** DirectX 9/10/11 via DXVK, custom container system, selectable GPU drivers (Turnip, VirGL), on-screen controls, gamepad support, offline execution.

**Limitations:** needs a powerful device, per-game compatibility varies (some crash or need tweaks), high storage usage.

---

## 3. Horizon Emulator

- **Platform:** Android
- **Purpose:** Windows gaming via compatibility layers — same model as Winlator

Also Wine-based with a Windows game container system, touch control mapping, custom driver support, and performance profiles. Differences from Winlator are in UI, container management, and driver builds; compatibility varies per game from Winlator's.

---

## 4. XoDos — DOS Emulation

- **Platform:** Android
- **Purpose:** retro DOS gaming

XoDos is a DOSBox-style emulator packaged for easy Android use: Sound Blaster emulation, keyboard + mouse emulation over touch controls, and low hardware requirements. Best for 1990s DOS games and lightweight devices — no modern Windows game support and limited 3D acceleration.

---

## 5. Vectras VM — Full OS Virtualization

- **Platform:** Android
- **Purpose:** run full operating system images
- **Architecture:** QEMU

Vectras VM boots ISOs and disk images of Windows XP/7 (the practical sweet spot) and Linux distributions, with snapshot support. The architectural reality: it virtualizes CPU only — no serious GPU acceleration — so it's notably slower than Winlator for games and better suited to OS testing than 3D titles.

---

## 6. GameHub — Winlator-Based Windows Emulator

- **Platform:** Android
- **Purpose:** game library management and launching, not runtime execution

GameHub is GameSir's distribution of a customized Winlator fork: it bundles its own Wine, Box86/Box64 and DXVK/Turnip stack, so it is a full Windows compatibility layer rather than a launcher for other engines. It also integrates Steam sign-in and downloads.

---

## 7. PPSSPP — PSP Emulation

- **Full name:** PlayStation Portable Simulator Suitable for Playing Portably
- **Original author:** Henrik Rydgård (2012)
- **License:** GPL 2.0, written in C++, hosted on GitHub
- **Platforms:** Windows, Linux, macOS, Android, iOS, Switch, Xbox (community ports)

### 7.1 The Emulated Architecture

PPSSPP recreates the PSP's hardware stack: the MIPS R4000-based CPU (via a dynamic recompiler/JIT with interpreter fallback), the GPU (OpenGL/Vulkan/Direct3D backends), audio engine, memory, file system, controller input, and Ad-Hoc networking.

### 7.2 Features

**Graphics enhancements:** resolution upscaling up to 10× native, texture scaling and replacement, anisotropic filtering, post-processing shaders, anti-aliasing.

**Performance:** frameskipping, speed control, fast memory access, multi-threading, Vulkan backend.

**Formats:** ISO, CSO (compressed ISO), PBP (homebrew), ELF/ZIP (development).

**Multiplayer:** local Ad-Hoc and online via LAN tunneling and community servers — not all games support online play.

**Save states** plus standard PSP saves.

### 7.3 Legal Position

PPSSPP itself is legal and open source. The PSP has no protected BIOS to dump (unlike older consoles). Game ISOs must come from discs you own; downloading pirated ISOs is illegal.

---

## 8. Comparison

| Feature | Winlator / Horizon | XoDos | Vectras VM | GameHub | PPSSPP |
|---------|-------------------|-------|------------|---------|--------|
| Runs | Windows x86 apps | DOS games | Full OS images | Windows x86/x64 apps and games | PSP games |
| Full OS virtualization | ❌ | ❌ | ✅ | ❌ | ❌ |
| DirectX→Vulkan (DXVK) | ✅ | ❌ | ❌ | Depends | N/A |
| GPU acceleration | ✅ | ❌ (2D/sound only) | ❌ (CPU only) | Depends on backend | ✅ (Vulkan/GL) |
| Needs root | ❌ | ❌ | ❌ | ❌ | ❌ |
| Best for | Modern PC games | Retro DOS | OS testing | Managing game setups | PSP library |

Shortcut guide:

- Modern Windows games → **Winlator** or **Horizon**
- DOS-era games → **XoDos**
- Full Windows/Linux OS → **Vectras VM**
- Easiest all-in-one Windows-on-Android experience → **GameHub** (Winlator fork)
- PSP games → **PPSSPP**
- Virtual Android with a separate Play login → **VPhone OS** / **VMOS**
- Just cloning two accounts of an app → **VirtualXposed** / **Parallel Space**

---

## 9. Performance Requirements

For Android-on-Android emulators:

| Tier | Spec |
|------|------|
| **Recommended** | 6 GB+ RAM, Snapdragon 7xx+, good cooling, Android 10+ |
| **Minimum** | 4 GB RAM, mid-range processor |

For PC compatibility tooling (Winlator/Horizon/Vectras):

- Snapdragon 865+ for comfortable frames
- 6 GB+ RAM
- Vulkan-capable GPU (best performance path)
- Large internal storage

---

## 10. Risks & Legal Notes

- Android-on-Android virtualization may violate game/app Terms of Service; rooted and virtualized environments can be banned or fingerprinted by anti-cheat
- Unofficial builds of these emulators are a real malware vector — download only from trusted sources
- Game emulation software (PPSSPP, DOSBox) is legal; game images are not — own the original games/backups you play
- Pirated game images risk both legal consequences and account bans
