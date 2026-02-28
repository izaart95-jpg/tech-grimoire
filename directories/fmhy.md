# FMHY — The Largest Collection of Free Stuff

This document covers [FMHY](https://fmhy.net) (*freemediaheckyeah*) — the tagline is theirs: "The largest collection of free stuff on the internet!" It is a community-maintained index of curated link lists covering free movies, video platforms, music, games, books, software, and tools. Where other documents in this knowledge base document individual sites, FMHY is the **upstream discovery layer** they were all sourced from — when a site here dies, its replacement is already indexed there.

> **Note:** FMHY itself hosts no files ("This site does not host any files" is in the site footer) — it indexes sites, many of which operate in legal gray areas (streaming mirrors, torrent trackers, DDL hubs). Legality varies by jurisdiction; the index also catalogs fully legal free alternatives everywhere. An index is not an endorsement.

---

## Table of Contents
1. [What It Is](#1-what-it-is)
2. [What's Inside](#2-whats-inside)
3. [Tooling Around the List](#3-tooling-around-the-list)
4. [How to Use It](#4-how-to-use-it)
5. [Caveats](#5-caveats)
6. [See Also](#6-see-also)

---

## 1. What It Is

- **Website:** https://fmhy.net
- **Edit repo:** https://github.com/fmhy/edit (formerly `nbats/FMHYedit` — the old URL redirects) — 12.5k stars, ~4,000 commits
- **Community:** [r/FREEMEDIAHECKYEAH](https://reddit.com/r/FREEMEDIAHECKYEAH) (the list began as a Reddit wiki), Discord, GitHub
- **Running since:** 2018
- **Model:** wiki-style index — anyone can suggest additions/corrections through the [contributing guide](https://fmhy.net/other/contributing); approved changes deploy to the site and all backups

The list is organized as one page per topic, each page a curated, annotated link list with a "Beginners Guide" box at the top (the safest starting points for that topic), emoji markers (⭐ community recommendations, 🌐 third-party indexes), and per-entry notes on mirrors, quality, and traps.

---

## 2. What's Inside

Thirteen top-level sections (verified from fmhy.net, October 2026):

| Section | Path | What it indexes |
|---------|------|-----------------|
| **Adblocking / Privacy** | [/privacy](https://fmhy.net/privacy) | Ad blockers, trackers, privacy tools |
| **Artificial Intelligence** | [/ai](https://fmhy.net/ai) | AI tools and models |
| **Streaming** | [/video](https://fmhy.net/video) | Movie & TV streaming/download sites — the layer where PRMovies/Nunflix-class aggregators live |
| **Listening** | [/audio](https://fmhy.net/audio) | Music, podcasts, audio tools |
| **Gaming** | [/gaming](https://fmhy.net/gaming) | Games + emulators for consoles past and present |
| **Reading** | [/reading](https://fmhy.net/reading) | Books, manga, comics |
| **Downloading** | [/downloading](https://fmhy.net/downloading) | Software, DDL hubs, file tools |
| **Torrenting** | [/torrenting](https://fmhy.net/torrenting) | Trackers and torrent tooling |
| **Educational** | [/educational](https://fmhy.net/educational) | Courses, textbooks, learning resources |
| **Android / iOS** | [/mobile](https://fmhy.net/mobile) | Mobile apps and content |
| **Linux / macOS** | [/linux-macos](https://fmhy.net/linux-macos) | Platform-specific tools |
| **Non-English** | [/non-english](https://fmhy.net/non-english) | Content in other languages |
| **Miscellaneous** | [/misc](https://fmhy.net/misc) | Food, travel, news, shopping, fun sites |

The sections map almost one-to-one onto categories in this knowledge base (Streaming, Torrenting, Educational, AI) — FMHY is effectively their shared upstream index.

---

## 3. Tooling Around the List

FMHY ships its own tooling, which is what makes the index *usable* rather than just big:

- **[FMHY Search](https://fmhy.net/posts/search)** — dedicated search over the list
- **Single-page API** — the entire list as one markdown document at `fmhy.net/single-page.md` and [`api.fmhy.net/single-page`](https://api.fmhy.net/single-page), plus a JSON API — scriptable for link audits (same technique as the [EverythingMoe](everythingmoe.md) JSON cache)
- **Backups** — site mirrors and markdown exports via the [backups wiki page](https://github.com/fmhy/FMHY/wiki/Backups)
- **Startpage** — a curated browser start page built from the list
- **SearXNG instance** — [searx.fmhy.net](https://searx.fmhy.net/)
- **[FMHY SafeGuard](https://github.com/fmhy/FMHY-SafeGuard)** — extension flagging untrusted domains
- **SFW FMHY** — [fmhy.xyz](https://fmhy.xyz/), a safe-for-work mirror; the main site keeps NSFW sections behind a toggle

---

## 4. How to Use It

1. Go to [fmhy.net](https://fmhy.net) and pick the section matching what you need (e.g. `/video` for movies & shows).
2. Start from the section's **Beginners Guide** box — the curated, community-vetted entry points.
3. `Ctrl+F` the [single-page version](https://fmhy.net/single-page.md) when you're looking for something specific by name.
4. Trust the markers: ⭐ entries are community recommendations; 🌐 entries are third-party indexes you can keep digging through.
5. Bookmark `fmhy.net` **from the official GitHub org or Discord** — the index's brand is cloned by lookalike sites the same way the sites it indexes are (see the clone-swarm pattern in [Torrent Sites](../torrenting/torrent-sites.md)).
6. If a link is dead or a site turned malicious, [contribute the correction upstream](https://fmhy.net/other/contributing) — the list stays current because hundreds of editors maintain it.

---

## 5. Caveats

- **Scale ≠ safety.** FMHY vets its entries, but indexed sites still serve aggressive ads, malware-ringed APK bundles, and legal gray areas. An ad blocker and the same hygiene rules from [EverythingMoe](everythingmoe.md) apply.
- **Links die fast.** Use the site search and the single-page/backup versions rather than stale copies floating around — the list itself is the only durable artifact.
- **Gray-zone content dominates** the Streaming/Torrenting/Downloading sections. The index also catalogs legal alternatives; what you click is your jurisdiction's problem, not the index's.
- This knowledge base previously documented individual free-content sites (movie streaming platforms, Dailymotion) as standalone pages — they were removed in favor of pointing at FMHY, the index those sites are cataloged in.

---

## 6. See Also

- [EverythingMoe](everythingmoe.md) — curated otaku-culture index (anime/manga/light-novel discovery layer)
- [Torrent Sites](../torrenting/torrent-sites.md) — the torrenting layer FMHY also indexes
- [Media Tools](../media/media-tools.md) — FFmpeg, VLC for what you end up downloading
