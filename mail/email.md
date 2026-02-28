# Email — Privacy Providers & Desktop Clients

Email has two halves, and muddling them causes bad decisions:

- The **provider** stores, receives, and transports your mail — its business model and jurisdiction decide who can read it. Yahoo still uses mail content for ad targeting (Google stopped scanning Gmail content for ads in 2017); encrypted providers mathematically can't.
- The **client** is the app you read/write with — it can be a browser tab, or a desktop application talking to the provider over IMAP/SMTP, storing mail locally and working offline.

This document covers privacy-first encrypted providers (Proton Mail, Tuta) and desktop clients (Thunderbird, Canary Mail), including how they interlock — e.g. using Thunderbird with Proton via Bridge, or why Tuta can't be used with *any* standard client.

---

## Table of Contents
1. [Fundamentals](#1-fundamentals)
2. [Proton Mail](#2-proton-mail)
3. [Tuta Mail](#3-tuta-mail)
4. [Provider Comparison & Migration](#4-provider-comparison--migration)
5. [Thunderbird](#5-thunderbird)
6. [Canary Mail](#6-canary-mail)
7. [Client Comparison](#7-client-comparison)
8. [See Also](#8-see-also)

---

## 1. Fundamentals

### 1.1 Why Provider Choice Matters

Standard providers (Gmail, Outlook, Yahoo) store messages in plaintext the provider can read, can be compelled by government requests broadly, and scan mail for spam filtering (Yahoo still uses mail content for ad targeting — Google stopped scanning Gmail content for ads in 2017 and Microsoft does not scan Outlook mail for advertising). Privacy providers answer this with:

- **End-to-end encryption (E2EE)** — messages encrypted so only sender and recipient can read them
- **Zero-knowledge architecture** — the provider holds encrypted data but not the keys
- **Subscription business model** — revenue from users, not from reading your data
- **Stronger jurisdictions** — Switzerland (Proton) and Germany (Tuta) rather than the US

**The caveat that matters:** E2EE only applies between users of the same provider, or when using PGP with external contacts. Mail to and from Gmail is standard unencrypted SMTP regardless of your provider.

### 1.2 IMAP vs POP3 vs SMTP

Email protocols are how clients reach providers:

| Protocol | Port | Role |
|----------|------|------|
| **IMAP** | 993 (SSL) / 143 | Receive — syncs email between server and client; messages stay on server |
| **POP3** | 995 (SSL) / 110 | Receive — downloads email locally, typically deletes from server |
| **SMTP** | 465 (SSL) / 587 (STARTTLS) | Send outgoing email |

Use IMAP for modern setups: the server is the source of truth and every device sees the same mailbox. POP3 is for single-device setups.

### 1.3 Client Connection Security

When configuring any email client:

| Setting | Value |
|---------|-------|
| **IMAP Port** | 993 with SSL/TLS |
| **SMTP Port** | 587 with STARTTLS, or 465 with SSL/TLS |
| **Authentication** | Normal password or OAuth2 |
| **Security** | Never use plain/unencrypted on port 143 or 25 |

### 1.4 Common Provider IMAP/SMTP Servers

| Provider | IMAP Server | SMTP Server |
|----------|-------------|-------------|
| Gmail | `imap.gmail.com:993` | `smtp.gmail.com:587` |
| Outlook/Hotmail | `outlook.office365.com:993` | `smtp.office365.com:587` |
| Proton Mail | `127.0.0.1:1143` (via Bridge) | `127.0.0.1:1025` (via Bridge) |
| Tuta | Not supported (own apps only) | Not supported |
| FastMail | `imap.fastmail.com:993` | `smtp.fastmail.com:587` |
| Zoho | `imappro.zoho.com:993` | `smtppro.zoho.com:587` |

Note the pattern: standard providers expose raw IMAP/SMTP; Proton exposes them only through a paid local proxy (Bridge); Tuta exposes them never — its encryption model requires its own apps.

---

## 2. Proton Mail

- **Website:** https://proton.me/mail
- **Company:** Proton AG — founded 2013 at CERN (Geneva, Switzerland)
- **Jurisdiction:** Switzerland
- **Encryption model:** E2EE between Proton accounts; PGP with external users; zero-access server-side encryption for all stored mail

### 2.1 Plans

| Feature | Free | Mail Plus (~€3.99/mo) | Proton Unlimited (~€9.99/mo) |
|---------|------|----------------------|------------------------------|
| **Storage** | 1 GB | 15 GB | 500 GB |
| **Email addresses** | 1 | 10 | 15+ |
| **Custom domain** | ❌ | ✅ | ✅ |
| **Folders/Labels** | Limited | Unlimited | Unlimited |
| **ProtonVPN** | Free tier | ❌ | ✅ |
| **ProtonDrive** | 5 GB | 15 GB | 500 GB |
| **ProtonCalendar** | ✅ | ✅ | ✅ |
| **Bridge (IMAP)** | ❌ | ✅ | ✅ |
| **Priority support** | ❌ | ✅ | ✅ |

### 2.2 Key Features

**Zero-access encryption.** All stored mail — including messages from non-Proton senders — is encrypted at rest with your key. Proton cannot read your inbox, only hand over encrypted blobs.

**Proton-to-Proton E2EE.** Mail between Proton accounts is end-to-end encrypted automatically, no setup.

**PGP.** Proton runs on PGP principles: import external keys, and outgoing mail to contacts with known PGP keys is encrypted automatically. This is the main path for encrypted mail with *external* correspondents.

**Password-protected emails.** Encrypted mail to non-Proton users — the recipient gets a link and enters a password (shared out-of-band) to read in their browser.

**Self-destructing messages.** Setting an expiry timer deletes messages automatically.

**Proton Bridge.** A local IMAP/SMTP proxy that lets regular desktop clients (Thunderbird, Apple Mail) talk to Proton — the standard client connection table shows it as `127.0.0.1`. Requires a paid plan.

```bash
# Install Proton Bridge (Linux — .deb, .rpm, or AppImage from https://proton.me/mail/bridge)

# After installing and logging in, configure any client:
# IMAP server: 127.0.0.1, port 1143
# SMTP server: 127.0.0.1, port 1025
# Username: your Proton email
# Password: Bridge-generated password (shown in Bridge app)
```

**Import Assistant.** Migrate existing Gmail/Outlook mail into Proton via OAuth: https://proton.me/support/import-assistant

### 2.3 The Proton Ecosystem

| Product | Function | Free |
|---------|---------|------|
| **Proton Mail** | Encrypted email | 1 GB |
| **Proton VPN** | VPN service | ✅ (limited servers) |
| **Proton Drive** | Encrypted cloud storage | 5 GB |
| **Proton Calendar** | Encrypted calendar | ✅ |
| **Proton Pass** | Password manager | ✅ (limited) |

**SimpleLogin** (acquired by Proton) generates throwaway aliases that forward to your inbox — decouples signup addresses from your real one.

### 2.4 Access Points

```bash
# Web app: https://mail.proton.me
# Desktop apps (Windows, macOS, Linux): https://proton.me/mail/download
# Mobile: iOS / Android app stores
# Tor hidden service (maximum anonymity):
#   protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion
```

### 2.5 Automation via Bridge (No Public API)

Proton has no public REST API for third-party mail access. The programmatic path is Bridge + IMAP:

```python
import imaplib, email

# Requires Proton Bridge running with a paid Proton account
mail = imaplib.IMAP4('127.0.0.1', 1143)
mail.login('your@proton.me', 'BRIDGE_PASSWORD')
mail.select('INBOX')

# Fetch recent emails
_, messages = mail.search(None, 'ALL')
for num in messages[0].split()[-5:]:
    _, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    print(f"From: {msg['From']}")
    print(f"Subject: {msg['Subject']}")
```

---

## 3. Tuta Mail

- **Website:** https://tuta.com
- **Company:** Tutao GmbH — founded 2011 (Hannover, Germany)
- **Jurisdiction:** Germany (GDPR)
- **Encryption model:** proprietary protocol — AES-256 + **TutaCrypt** post-quantum (Kyber-1024 + x25519); *not* PGP
- **Open source:** ✅ fully (client and server — https://github.com/tutao/tutanota)

### 3.1 Plans

| Feature | Free | Revolutionary (~€3/mo) | Legend (~€8/mo) |
|---------|------|------------------------|-----------------|
| **Storage** | 1 GB | 20 GB | 500 GB |
| **Email addresses** | 1 | 15 | 30 |
| **Custom domain** | ❌ | ✅ | ✅ |
| **Extra email addresses** | – | 15 | 30 |
| **Calendar** | ✅ | ✅ | ✅ |
| **Priority support** | ❌ | Email support | ✅ (priority) |
| **Multiple accounts** | ❌ | Family option, activated by contacting support (each extra member billed separately) | Family option, activated by contacting support (each extra member billed separately) |

Cheaper than Proton at comparable storage — the trade-off is interoperability (see §3.3).

### 3.2 Key Features

**Deeper metadata encryption than Proton.** Tuta encrypts subject lines, attachment names, and calendar/contact data by default — Proton encrypts subject lines only as an explicit setting on the paid tiers.

**Post-quantum by design.** Tuta replaced its AES-128 + RSA-2048 scheme with AES-256 + TutaCrypt (Kyber-1024 KEM + x25519 ECDH) — TutaCrypt rolled out from March 2024. The trade: no PGP compatibility (§3.3), but subject lines and greeting text are encrypted by default.

**No IP logging.** Tuta doesn't log user IPs by default — stronger stance than Proton (which logs IP for abuse prevention in some cases).

**Fully open source.** Client and code server are auditable on GitHub.

```bash
# Web: https://app.tuta.com
# Desktop: https://tuta.com/#download
# Mobile: iOS App Store / Google Play / F-Droid (Play-free installs)
```

### 3.3 Tuta's Design Trade-offs (vs Proton)

- **No IMAP/SMTP at all** — Tuta's encryption model requires its own apps; no Thunderbird, no Apple Mail, no Automation via standard protocols
- **No PGP** — encrypted exchange with external PGP users happens via the password-protected external-mail mechanism, not PGP
- **Official import exists** — the desktop clients import EML or MBOX files directly (Legend plan); One-Click Migration is in closed beta. Otherwise: Google Takeout → third-party converters, or forwarding during transition

Pick Tuta for: strongest default metadata encryption, open source, low price, no-IP-logging. Pick Proton for: ecosystem size, PGP interoperability, IMAP via Bridge, import tooling.

---

## 4. Provider Comparison & Migration

### 4.1 Comparison

| Feature | Proton Mail | Tuta Mail | Gmail | Outlook |
|---------|-----------|----------|-------|---------|
| **Free storage** | 1 GB | 1 GB | 15 GB | 15 GB |
| **E2EE (same provider)** | ✅ | ✅ | ❌ | ❌ |
| **E2EE subject line** | Optional | ✅ Default | ❌ | ❌ |
| **PGP support** | ✅ | ❌ | ❌ (via extension) | ❌ |
| **Open source** | Partial | ✅ Full | ❌ | ❌ |
| **IMAP/SMTP** | ✅ (paid, Bridge) | ❌ | ✅ | ✅ |
| **IP logging** | Some | ❌ | Yes | Yes |
| **Custom domain** | Paid | Paid | Paid (Workspace) | Paid |
| **Jurisdiction** | Switzerland | Germany | USA | USA |
| **Business model** | Subscriptions | Subscriptions | Advertising | Advertising |
| **Self-destructing mail** | ✅ | ❌ | ❌ | ❌ |
| **Tor .onion address** | ✅ | ❌ | ❌ | ❌ |

Decision shortcuts:

| Need | Pick |
|------|------|
| Best free privacy email, no IMAP needed | **Tuta** — deeper default encryption |
| IMAP/Thunderbird compatibility | **Proton** (Bridge, paid) |
| PGP with external contacts | **Proton** |
| Open-source auditable stack | **Tuta** (fully open) |
| Broadest privacy ecosystem (VPN/Drive) | **Proton** |
| Minimum IP logging | **Tuta** |
| Migrating an existing mailbox | **Proton** (Import Assistant) |

### 4.2 Migration

**Gmail → Proton:**
1. Proton Import Assistant (https://proton.me/support/import-assistant)
2. Connect Gmail via OAuth
3. Select folders/date range — Proton imports and encrypts everything

**Gmail → Tuta:** Tuta now ships an official import — the desktop clients can import EML or MBOX files directly (included on the Legend plan), and a One-Click Migration assistant is in closed beta. Otherwise, export via Google Takeout (`.mbox`), convert with third-party tools (clunky), or forward from Gmail to Tuta during a transition period and run both.

**Custom domain (both):** add MX records pointing to the provider's mail servers on a paid plan, then create addresses under your domain — this keeps your address portable across future provider switches.

---

## 5. Thunderbird

- **Website:** https://www.thunderbird.net
- **Developer:** Mozilla Foundation (MZLA Technologies Corporation)
- **License:** MPL 2.0 (open source)
- **Platforms:** Windows, macOS, Linux (+ Android via the K-9 successor)
- **Price:** Free

Thunderbird is the default open-source desktop email client: it connects over IMAP/SMTP to any provider, handles mail/calendar/tasks/chat in one app, supports OpenPGP natively (since version 78 — no Enigmail needed), and extends through add-ons.

### 5.1 Installation

```bash
# Ubuntu/Debian
sudo apt install thunderbird

# Fedora
sudo dnf install thunderbird

# Arch
sudo pacman -S thunderbird

# Flatpak (cross-distribution)
flatpak install flathub org.mozilla.Thunderbird

# macOS
brew install --cask thunderbird

# Windows — download from https://www.thunderbird.net
```

### 5.2 Account Setup

1. **Menu → Account Settings → Account Actions → Add Mail Account**
2. Enter name, email address, password
3. Thunderbird auto-detects server settings via Mozilla's ISPDB
4. For unknown providers: **Configure manually** and enter IMAP/SMTP values ([§1.3](#13-client-connection-security))

### 5.3 PGP Encryption (OpenPGP)

Built in since version 78:

```
Setup:
1. Account Settings → End-To-End Encryption
2. "Add Key" → Generate new key or import existing
3. Set the key for your account

Send encrypted email:
1. Compose new message
2. Click the lock icon → Enable encryption
3. Thunderbird encrypts to recipients' published PGP keys automatically

Import a contact's public key:
1. If they attached their key to an email → import it
2. Or: Tools → OpenPGP Key Manager → Import from keyserver
```

```bash
# Export your public key: Tools → OpenPGP Key Manager → right-click key → Export
# Import a .asc public key: OpenPGP Key Manager → File → Import Public Key(s)
```

### 5.4 Calendar with CalDAV

The Lightning calendar is built in and syncs bidirectionally over CalDAV/iCalendar:

1. **Calendar → New Calendar → On the Network → CalDAV**
2. Enter your CalDAV URL (Fastmail, Nextcloud, or Proton Calendar via Bridge)

### 5.5 Useful Add-ons

| Add-on | Function |
|--------|---------|
| **Thunderbird Conversations** | Gmail-style threaded conversations |
| **ImportExportTools NG** | Batch export/import .eml, .mbox |
| **Cardbook** | Advanced CardDAV contact management |
| **FileLink for Dropbox/NextCloud** | Large attachments as cloud links |

### 5.6 Configuration Tips

```javascript
// Advanced config: Settings → Advanced → Config Editor

mail.compose.autosave = true          // Auto-save drafts
mail.compose.autosaveinterval = 5     // Save every 5 minutes
mailnews.default_sort_order = 2       // Sort newest first
mailnews.mark_message_read.delay = 5  // Mark read after 5 seconds
mail.spam.manualMark = true           // Manual junk marking
```

### 5.7 Proton Bridge + Thunderbird Setup

Standard way to run Proton in a real desktop client (paid Proton plan required):

```
1. Install Proton Bridge and log in
2. Bridge shows: IMAP port 1143, SMTP port 1025, and a Bridge password
3. In Thunderbird → Add Mail Account → Manual setup:
   - IMAP: 127.0.0.1, port 1143, SSL: None, Auth: Normal
   - SMTP: 127.0.0.1, port 1025, SSL: None, Auth: Normal
   - Username: your@proton.me
   - Password: Bridge-generated password (NOT your Proton login password)
4. Mail flows through Proton with full E2EE preserved
```

The odd-looking "SSL: None" is correct — security is provided by the TLS tunnel between Bridge and Proton's servers; the local hop stays on localhost.

### 5.8 Thunderbird on Android

Thunderbird for Android is the continuation of K-9 Mail (Mozilla acquired K-9 in 2022): separate mobile-optimized codebase, same brand. Supports IMAP, POP3, multiple accounts, and OpenPGP.

```
Google Play / F-Droid: search "Thunderbird"
Or: https://www.thunderbird.net/en-US/mobile/
```

---

## 6. Canary Mail

- **Website:** https://canarymail.io
- **Developer:** Canary Mail Inc.
- **Platforms:** macOS, iOS (incl. iPadOS), Windows, Android
- **Price:** Free ($0), Growth ($36/year), Pro+ ($100/year) — annual or one-time lifetime; no month-to-month billing

Canary Mail is a modern commercial client aimed at the Apple ecosystem — polished UI, built-in AI features, and encryption (S/MIME, PGP, and its own SecureScan-free SecureSend E2EE) without plug-ins. It's the pick for Apple users who want more than Apple Mail offers natively.

### 6.1 Key Features

**AI assistant (Copilot).** Summarizes long threads, drafts replies, categorizes mail. Runs on-device for free users; cloud models in Pro.

**Encryption:** 
- **S/MIME** — request a free certificate (Actalis/Comodo), import the .p12, and Canary signs outgoing mail and encrypts to contacts whose certs you have
- **PGP** — full support for external encrypted mail
- **SecureSend** — Canary's own E2EE between Canary users with no key setup

```
S/MIME setup:
1. Settings → Encryption → S/MIME
2. Get a free personal certificate (Actalis or Comodo)
3. Import the .p12 certificate file
4. Canary auto-signs outgoing mail
```

**Workflow features:** read receipts (recipient-side setup not needed), send later, snooze, one-click unsubscribe for marketing mail, AI-focused inbox filtering.

**Accounts:** Gmail, Outlook, iCloud, Yahoo, custom IMAP, Proton (via Bridge), Fastmail — in one interface.

### 6.2 Plans

| Feature | Free | Growth ($36/yr) | Pro+ ($100/yr) |
|---------|------|------------------|------------------|
| **Accounts** | Unlimited | Unlimited | Unlimited |
| **Devices** | 2 | 5 | 5 |
| **AI features** | ❌ | AI Copilot | AI Copilot |
| **Read receipts** | Lite | ✅ | ✅ |
| **Snooze & Pin** | ✅ | ✅ | ✅ |
| **Send Later** | ❌ | ✅ | ✅ |
| **Email templates** | ✅ | ✅ | ✅ |
| **PGP encryption** | ❌ | ❌ | ✅ |
| **SecureSend (HIPAA)** | ❌ | ❌ | ✅ |
| **Priority support** | ❌ | ❌ | ✅ |

### 6.3 Canary vs Apple Mail

| Feature | Canary | Apple Mail |
|---------|--------|-----------|
| **AI assistant** | ✅ | ✅ (iOS 18+ / macOS Sequoia+) |
| **Read receipts** | ✅ | ❌ |
| **Send later** | ✅ | ✅ (macOS Sequoia 15+ / iOS 18+) |
| **PGP** | ✅ | ❌ (plugin needed) |
| **S/MIME** | ✅ | ✅ |
| **Snooze** | ✅ | ❌ |
| **Price** | Free/Growth/Pro+ | Free (built-in) |

---

## 7. Client Comparison

| Client | Platforms | Open Source | PGP | S/MIME | IMAP | Free | AI |
|--------|-----------|-------------|-----|--------|------|------|-----|
| **Thunderbird** | Win/Mac/Linux + Android | ✅ | ✅ | ✅ | ✅ | ✅ | Limited |
| **Canary Mail** | Mac/iOS/Win(beta) | ❌ | ✅ | ✅ | ✅ | Free/Pro | ✅ |
| **Apple Mail** | Mac/iOS | ❌ | ❌ | ✅ | ✅ | ✅ | Limited |
| **Outlook** | All | ❌ | ❌ | ✅ | ✅ | Paid | ✅ (Copilot) |
| **K-9 Mail** | Android | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| **FairEmail** | Android | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

Decision shortcuts:

| Need | Pick |
|------|------|
| Cross-platform open source | **Thunderbird** |
| Apple ecosystem, modern UI + AI | **Canary Mail** |
| Proton in a desktop client | **Thunderbird + Proton Bridge** |
| Android with PGP | **Thunderbird for Android** (K-9 successor) |
| Maximum privacy, auditable | **Thunderbird** |

---

## 8. See Also

- [OPSEC & Proxies](../security/opsec-and-proxies.md) — disposable email, temp addresses, anonymity practices
- [Network Protocols](../fundamentals/network-protocols.md) — SMTP, IMAP, POP3 protocol details
- [VPN & ZTNA](../networking/vpn-and-ztna.md) — ProtonVPN and other VPN services
