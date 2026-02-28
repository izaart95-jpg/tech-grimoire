# Minecraft Clients — Utility Mods, Ghost Clients & Addons

Client-side modifications come in three classes, defined by how visible they are and where they're acceptable:

- **Utility mods** (Meteor, Baritone) — openly visible features (ESP, flying, automation) used on anarchy servers and wherever the server permits modifications
- **Ghost clients** (Vape, Raven B+, Hydrogen, Vestige) — subtle PvP advantages engineered to mimic natural play, so spectators and recordings look normal
- **Meteor addons** (Glazed) — ordinary Fabric mods that bolt extra modules onto Meteor for a specific server's tasks

> **Server Rules Notice:** Using any of these on servers that prohibit them can result in bans — always check a server's rules first. Utility mods belong on single-player, anarchy servers (2b2t), or servers that explicitly allow client-side mods. Ghost clients are documented here as publicly known community topics, for educational and research purposes.

---

## Table of Contents
1. [Client Types & Anti-Cheat](#1-client-types--anti-cheat)
2. [Meteor Client](#2-meteor-client)
3. [Baritone](#3-baritone)
4. [Glazed — DonutSMP Meteor Addon](#4-glazed--donutsmp-meteor-addon)
5. [Ghost Clients](#5-ghost-clients)
6. [Comparison](#6-comparison)
7. [See Also](#7-see-also)

---

## 1. Client Types & Anti-Cheat

### 1.1 What Makes a Client "Ghost"

A ghost client provides advantages designed to imitate human play:

- **AimAssist** — subtle aim correction toward targets (micro-corrections, not the obvious snap of KillAura)
- **AutoClicker** — consistent high CPS with humanized timing variance
- **Reach** — extends attack range by a fraction of a block (e.g. 3.2 instead of 3.0)
- **Velocity** — reduces knockback received so positioning survives hits
- **WTap / FakeLag** — timing tricks that affect hit registration

### 1.2 Ghost vs Utility vs Addon

| Type | Examples | Visibility | Use Case |
|------|---------|-----------|---------|
| **Utility** | Meteor, Wurst | Visually obvious (ESP, flying) | Anarchy servers (2b2t) |
| **Ghost** | Vape, Raven B+ | Invisible to spectators | Competitive servers (Hypixel) |
| **Meteor addon** | Glazed | Runs inside Meteor | Server-specific automation (DonutSMP) |

### 1.3 Anti-Cheat Landscape

How much of this works depends on the server's anti-cheat:

| Anti-Cheat | Server | Detection Strength |
|-----------|--------|-------------------|
| **Watchdog** | Hypixel | Moderate (bans obvious cheats) |
| **Grim** | Many servers | Strong statistical analysis |
| **Intave** | Private servers | Strong |
| **Matrix** | Wide use | Moderate |
| **NCP** (NoCheatPlus) | Bukkit/Spigot | Weak, easily bypassed |

---

## 2. Meteor Client

- **Website:** https://meteorclient.com
- **Repository:** https://github.com/MeteorDevelopment/meteor-client
- **License:** GPL v3 (publicly auditable; forks must stay open source)
- **Type:** Fabric utility mod
- **Minecraft version:** latest stable (tracks Minecraft releases)

### 2.1 Overview

Meteor is the main open-source Fabric utility mod for anarchy servers. A customizable GUI/HUD drives a large module system, and a macro system lets one keypress reconfigure almost anything.

### 2.2 Installation

```
Prerequisites: Fabric Loader + Fabric API for the target Minecraft version

1. Install Fabric Loader from https://fabricmc.net/use/installer/
2. Download the Meteor .jar from https://meteorclient.com
3. Download the Baritone .jar alongside it (see §3 — Meteor no longer bundles it)
4. Place both .jar files in .minecraft/mods/
5. Launch Minecraft with the Fabric profile
6. In-game: press Right Shift to open the Meteor GUI
```

### 2.3 Module System

| Category | Examples |
|----------|---------|
| **Combat** | KillAura, CrystalAura, BedAura, AnchorAura, AutoTotem |
| **Movement** | Fly, NoFall, Speed, Sprint, Step, Jesus (walk on water) |
| **Render** | ESP, Xray, Fullbright, FreeLook, Tracers |
| **World** | AutoMine, InfinityMiner, Nuker, Timer |
| **Player** | AutoEat, AutoArmor, AutoFish, Freecam |
| **Misc** | AntiAFK, AutoReconnect, ChatFilter, FakePlayer |
| **HUD** | Customizable overlays (coords, speed, lag meter, inventory) |

### 2.4 Baritone Integration

Meteor requires Baritone as a separate mod — features depending on it stay disabled until it's installed in `.minecraft/mods/`. Meteor's own Baritone fork is downloadable alongside Meteor at meteorclient.com. Once installed, all Baritone commands (default prefix `#`) work directly inside Meteor.

### 2.5 Addons & Commands

Third-party addons extend Meteor with modules the team won't officially include (e.g. griefing-specific features) — placed in `.minecraft/meteor-client/addons/`. See [§4 Glazed](#4-glazed--donutsmp-meteor-addon).

```bash
# In-game commands (prefix: .)
.help                   # List all commands
.modules                # List all modules
.toggle <module>        # Toggle a module
.bind <module> <key>    # Bind a key to a module
.config <module> get    # View a module's settings
```

ViaFabric can be installed alongside Meteor to connect to servers running other Minecraft versions.

---

## 3. Baritone

- **Repository:** https://github.com/cabaletta/baritone
- **License:** LGPL v3
- **Author:** leijurv (cabaletta)
- **Type:** autonomous pathfinding bot — standalone mod or embedded in clients

### 3.1 Overview

Baritone is A* pathfinding adapted to Minecraft's actual movement costs. It navigates the world without player input: walking to coordinates, mining specific ores, building schematics, farming. It's the engine behind automation in utility clients (bundled with Impact, separate for Meteor).

### 3.2 Installation

```
Fabric (1.16.5+):   baritone-api-fabric-X.X.X.jar from GitHub Releases → .minecraft/mods/
Forge (legacy):     baritone-api-forge-X.X.X.jar from GitHub Releases → .minecraft/mods/
Impact client:      pre-installed (https://impactclient.net)
Meteor client:      separate download — see §2.4
```

### 3.3 Core Commands

```bash
# Navigation
#goto 1000 64 500        # Walk to X=1000, Y=64, Z=500
#goto 1000 500           # Walk to X=1000, Z=500 (ignores Y)
#goal 1000 500           # Set destination without starting
#path                    # Start pathing toward current goal
#stop                    # Stop all current tasks
#cancel                  # Cancel and clear goal

# Mining
#mine diamond_ore        # Find and mine diamond ore
#mine iron_ore gold_ore  # Mine multiple block types
#mining                  # Check mining progress

# Farming / Following
#farm                    # Auto-farm crops in an area
#follow playername       # Follow a player

# Building
#schematic load path/to/schematic.litematic
#build                   # Build loaded schematic at current position
#sel                     # Make a selection for building

# Elytra
#elytra                  # Fly in the Nether using fireworks

# Utilities
#come                    # Path back to start
#invert                  # Walk away from the current goal
#blacklist               # Blacklist the current block type from mining
#save name               # Save current location as a waypoint
#goto name               # Go to a saved waypoint
```

### 3.4 Key Settings

Over 100 settings exist; configured with `#set <setting> <value>`:

```bash
#set allowSprint true           # Sprint while pathfinding (default: true)
#set allowParkour true          # Jump across gaps (default: true)
#set allowBreak true            # Break blocks in the way (default: true)
#set allowPlace true            # Place blocks to bridge gaps (default: true)
#set chatDebug false            # Hide debug messages in chat
#set renderPath true            # Show planned path visually
#set followRadius 3             # Distance to maintain when following
#set mineScanDroppedItems true  # Pick up dropped items while mining
```

### 3.5 Java API

```java
// Set a pathfinding goal and start
BaritoneAPI.getSettings().allowSprint.value = true;
BaritoneAPI.getProvider()
    .getPrimaryBaritone()
    .getCustomGoalProcess()
    .setGoalAndPath(new GoalXZ(10000, 20000));

// Mine specific blocks
BaritoneAPI.getProvider()
    .getPrimaryBaritone()
    .getMineProcess()
    .mine(Blocks.DIAMOND_ORE, Blocks.DEEPSLATE_DIAMOND_ORE);

// Stop everything
BaritoneAPI.getProvider()
    .getPrimaryBaritone()
    .getPathingBehavior()
    .cancelEverything();
```

### 3.6 The Pathfinding Model

The cost function is what makes Baritone practical — it weighs Minecraft-specific costs:

- Block breaking time (tool, enchantments, efficiency)
- Falling block awareness (gravel/sand above target blocks)
- Liquid avoidance (won't break blocks adjacent to lava/water by default)
- Fire and magma avoidance
- Fall damage calculation
- Parkour jumps across gaps
- Bridging when blocks are available

---

## 4. Glazed — DonutSMP Meteor Addon

- **Website:** https://glazedclient.com
- **Repository:** https://github.com/realnnpg/Glazed
- **Type:** free, open-source Meteor Client addon (ordinary Fabric mod jar)
- **Minecraft versions:** 1.21.4, 1.21.11, 26.1.2
- **Requires:** Fabric Loader + Meteor Client + Baritone + Fabric API

### 4.1 Overview

Glazed exists because DonutSMP grinding is repetitive: shop ordering, selling, spawner farming. It packages that workflow as a Meteor addon — not a standalone or injected client. Modules appear inside Meteor's GUI, configs run through Meteor's profiles, and the whole thing is auditable and buildable from source like any Meteor addon.

### 4.2 Modules (65 across 3 categories)

**Economy automation (sample):** AH Sell (sell all hotbar items via /ah sell), AH Shield Seller (undercut cheapest listing, reclaim unsold), Auto Spawner Sell, Emergency Order/Seller (panic-move when a watched player approaches), Inv Sell, Iron AH Restocker, Shulker Dropper, Spawner Protect (break + store spawner on player detection), Order Dropper, Home Reset.

**ESP & detection (27 modules):** 1x1x1 Holes, Advanced Stash Finder, Amethyst ESP, Bedrock Void ESP, Beehive ESP, Block Notifier, Chunk Finder, Wandering ESP.

**Utility:** Coord Snapper (clipboard + webhook), Fake Pay, Fake Scoreboard, Glazed Freecam, No Block Interact (pearl through containers), Storage Stealer, TPA Macro (spam-send + auto-confirm).

*(Full module list: the GitHub README.)*

### 4.3 Installation

```
1. Install Fabric Loader from https://fabricmc.net/use/
2. Download Meteor Client from https://meteorclient.com → .minecraft/mods/
3. Download Baritone from https://meteorclient.com → .minecraft/mods/
4. Download Fabric API from https://modrinth.com/mod/fabric-api (required by
   Glazed's bundled ExploitPreventer) → .minecraft/mods/
5. Download the Glazed .jar (GitHub Releases or glazedclient.com) → .minecraft/mods/
6. Launch with the Fabric profile; Right Shift opens Meteor's GUI
```

No purchase, launcher, or injection — it installs like any Fabric mod and runs as a Meteor addon each session.

### 4.4 GUI & Configuration

Glazed ships no GUI of its own — everything plugs into Meteor:

- Modules grouped inside Meteor's click GUI (Right Shift)
- Meteor's module search covers Glazed modules
- Config save/load via Meteor profiles; binds via Meteor's bind system
- HUD elements edited in Meteor's HUD editor

---

## 5. Ghost Clients

### 5.1 Vape

- **Website:** https://www.vape.gg
- **Type:** injection-based ghost client
- **Price:** ~$35 one-time
- **Versions:** 1.7, 1.8.9, 1.12+
- **Developer:** Manthe (since 2015)

The oldest continuously active ghost client. Injection-based: no Forge or Fabric install — it injects into the running Minecraft process at launch. Marketing-design principle: modules built on long-term human-behavior emulation rather than bypasses that get patched out.

**Key modules:** AimAssist (subtle, retains full cursor control), humanized AutoClicker, configurable Reach, auto WTap for combo maintenance, AutoArmor, Velocity, Timer, HUD (keystrokes/FPS/CPS/coords/armor), Freelook, NoClickDelay.

```
1. Purchase at https://www.vape.gg
2. Download the Vape launcher from the client dashboard
3. Open Minecraft (any supported version)
4. Launch Vape — it injects into the running process
5. In-game: right-click the tray icon or the configured keybind opens the GUI
```

No installation process exists because injection modifies nothing on disk at runtime. Vape V4 is the current version; Vape Lite is a cheaper, reduced-module variant.

### 5.2 Raven B+

- **Type:** free Forge mod / ghost client
- **Minecraft version:** 1.8.9
- **Forks:** multiple open-source ones; primary maintained at https://k-ov.github.io/ (Raven B++)

Free, Forge-based ghost client for 1.8.9 focused on Hypixel PvP — Forge standard .jar mod with Feather client compatibility. Modules: AimAssist, AutoClicker, Reach, Velocity, Sprint-Scaffold, BowLongJump, legit aura (subtle KillAura within natural parameters), ClickGUI, custom HUD (keystrokes, CPS, FPS).

```
1. Install Forge 1.8.9 from https://files.minecraftforge.net
2. Download the Raven B++ jar from https://k-ov.github.io/download/
3. Place in .minecraft/mods/
4. Launch with the Forge 1.8.9 profile; GUI opens with Left Shift (default)
```

Notable forks: **Raven B++** (k-ov — most maintained), **Raven XD** (xia-mc — extended beyond Hypixel), **Raven B+** (xXxVPNxXx — basic 1.8.9).

### 5.3 Hydrogen

- **Website:** https://zpeanut.github.io
- **Repository:** https://github.com/zPeanut/Hydrogen
- **License:** open source
- **Type:** Forge ghost client
- **Minecraft version:** 1.8.9

Open-source Forge ghost client with 50+ modules across combat, render, movement, and utility plus pre-1.8 visual restorations (2D dropped items, old bow animation, armor damage visuals). Customizable GUI with font and theme options (Classic/Tephra layouts) and fuzzy module search. Popular as a code-quality study target for how ghost clients are structured.

**Module map:** combat (AimAssist, AutoClicker, Reach, Velocity, legit KillAura, Criticals) · render (ESP, Tracers, FullBright, ChestESP, Nametags) · movement (Sprint, NoFall, Step, LongJump) · utility (AutoArmor, AutoEat, FreeCam, NameProtect).

```bash
# Option 1: pre-built jar (recommended)
# https://github.com/zPeanut/Hydrogen/releases → hydrogen-X.X.X.jar → .minecraft/mods/
# Option 2: build from source
git clone https://github.com/zPeanut/Hydrogen.git
cd Hydrogen
./gradlew setupDecompWorkspace idea   # open in IntelliJ IDEA
./gradlew build                        # output in build/libs/
```

### 5.4 Vestige

- **Website:** https://vestige.my.canva.site
- **Type:** paid ghost client (free version deprecated)
- **Minecraft version:** 1.8.9
- **Developer:** YesCheatPlus

The multi-server ghost client: bypass profiles are per-server (Hypixel, RedesKy, MineMenClub, NCP, AAC) rather than Hypixel-only. Modules: Scaffold, SprintScaffold, BowLongJump, Hypixel strafe/timer disabler, AutoBlock, ghost modules, and a "blade mode" fast-attack configuration.

Distribution is via their Discord (linked on the Canva site) — the free version is no longer updated; the paid version receives updates.

---

## 6. Comparison

| Client | Class | Price | Type (loader/transport) | MC Version | Open Source | Primary Use |
|--------|-------|-------|-------------------------|-----------|-------------|-------------|
| **Meteor** | Utility | Free | Fabric mod | Latest | ✅ GPL v3 | Anarchy servers, visible utility |
| **Baritone** | Utility (bot) | Free | Fabric/Forge mod | 1.12.2 → latest | ✅ LGPL v3 | Autonomous navigation, mining, building |
| **Glazed** | Meteor addon | Free | Fabric mod (addon) | 1.21+ | ✅ | DonutSMP economy automation |
| **Vape** | Ghost | ~$35 | Injection | 1.7/1.8.9/1.12+ | ❌ | Hypixel ghost PvP |
| **Raven B+** | Ghost | Free | Forge mod | 1.8.9 | ✅ (forks) | Hypixel BedWars/SkyWars |
| **Hydrogen** | Ghost | Free | Forge mod | 1.8.9 | ✅ | Ghost PvP + source study |
| **Vestige** | Ghost | Free/Paid | Client | 1.8.9 | ❌ | Multi-server bypass |

Decision shortcuts:

| Scenario | Use |
|----------|-----|
| Anarchy / permitted servers, modern MC | **Meteor** (+ Baritone) |
| Server-specific automation on DonutSMP | **Glazed** (add-on for Meteor) |
| Budget-conscious ghost PvP, open source | **Hydrogen** or **Raven B++** |
| Maximum anti-cheat bypass (paid) | **Vape** |
| Multi-server bypass profiles | **Vestige** |
| Studying ghost client source code | **Hydrogen** |

---

## 7. See Also

- [Servers](servers.md) — FakePixel, 2b2t, Hypixel, MineMenClub
- [Frameworks & Libraries](../devtools/frameworks-and-libraries.md) — Mineflayer, minecraft-protocol, go-mc for headless bot development
