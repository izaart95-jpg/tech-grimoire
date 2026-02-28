# File Hosting & Transfer — Gofile, MediaFire, Mega & Smash

Hosted file sharing comes in three distinct models, and each service here represents one of them:

- **Hosting** (MediaFire, Gofile) — files live on remote storage and are accessible until deleted; downloaders just need a link
- **Encrypted cloud storage** (Mega.nz) — files are encrypted client-side before upload; the provider never holds a readable copy
- **Transfer** (Smash) — the file is a parcel: upload, send a link, recipient downloads, then the file is deleted

Picking the right model matters more than picking a "better" service — a 100 GB video deliverable, a ROM archive you link in a forum post, private backups, and a one-shot handoff are four different problems.

- **Related:** [Archive.org](archive-org.md) — permanent public archival; [OnionShare](../networking/onionshare.md) — anonymous local-first sharing over Tor

---

## Table of Contents
1. [Choosing a Service](#1-choosing-a-service)
2. [Gofile — Anonymous Unlimited Hosting](#2-gofile--anonymous-unlimited-hosting)
3. [MediaFire — Persistent Public Storage](#3-mediafire--persistent-public-storage)
4. [Mega.nz — End-to-End Encrypted Storage](#4-meganz--end-to-end-encrypted-storage)
5. [Smash — Large File Transfer](#5-smash--large-file-transfer)
6. [Comparison](#6-comparison)
7. [See Also](#7-see-also)

---

## 1. Choosing a Service

Four questions decide everything:

1. **Where should the file go at the end?** Stored indefinitely (hosting/storage) or deleted (transfer)?
2. **Who might read it?** Plain hosting stores plaintext — encrypt yourself or use Mega. Smuggling a link around a censored network is a different problem → OnionShare over Tor.
3. **Does the recipient need an account?** Gofile and MediaFire allow accountless downloads; Mega needs an account unless you share the URL *including* the encryption key fragment.
4. **Size and retention?** Gofile has no size cap but expires inactive guest uploads after 10 days; MediaFire keeps files indefinitely but caps free uploads at 5 GB; Smash's free tier caps transfers at 2 GB and deletes them after 7 days.

Practical defaults:

| Need | Use |
|------|-----|
| Large file sent once, no account | **Smash** |
| Public file that must not expire | **MediaFire** |
| Public file over 20 GB, no expiry needed forever | **Gofile** (free account) |
| Private storage only you can read | **Mega.nz** |
| Anonymous sharing, no third party at all | **OnionShare** |
| Permanent archival, public-domain content | **Archive.org** |

---

## 2. Gofile — Anonymous Unlimited Hosting

- **Website:** https://gofile.io
- **Model:** Free file hosting with guest upload — no account required to upload, no size limit, no download countdown
- **Retention:** 10 days without activity (guest) / indefinite (free account)
- **API:** Full REST API available

### 2.1 Free vs Account Usage

| Feature | Guest (No Account) | Account (Free) |
|---------|-------------------|----------------|
| **Upload** | ✅ | ✅ |
| **Max file size** | Unlimited | Unlimited |
| **File retention** | 10 days no activity | Indefinite |
| **Download password** | ❌ | ✅ |
| **File management** | ❌ | ✅ |
| **Folder organization** | ❌ | ✅ |
| **Direct links** | ✅ | ✅ |
| **API access** | ✅ (limited) | ✅ (full) |
| **Storage quota** | None stated | None stated |

The notable difference from most competitors: no file size cap, and direct download links work even without an account. Guest uploads use the 10-day no-activity clock; a free account extends retention indefinitely and unlocks password protection and file management.

### 2.2 Uploading Files

**Web upload:**

1. Visit https://gofile.io
2. Drag and drop files onto the page
3. Files upload immediately — no account needed
4. You receive a shareable folder link:

```
https://gofile.io/d/FOLDERID
```

Each upload creates a folder on Gofile, even for a single file — the folder link is what you share.

**CLI upload via API:**

```bash
# Step 1: Get a server to upload to
SERVER=$(curl -s "https://api.gofile.io/servers" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['data']['servers'][0]['name'])")
echo "Uploading to: $SERVER"

# Step 2: Upload the file (guest — no token needed)
curl -F "file=@/path/to/your/file.zip" "https://$SERVER.gofile.io/contents/uploadfile"

# Step 3: Response contains the download page link
# {"status":"ok","data":{"guestToken":"...","folderId":"...","folderCode":"abc123",...}}
```

```python
import requests

def upload_to_gofile(filepath: str, token: str = None) -> dict:
    """Upload a file to Gofile. Token optional (extends retention)."""
    # Get best server
    servers = requests.get("https://api.gofile.io/servers").json()
    server = servers["data"]["servers"][0]["name"]

    with open(filepath, "rb") as f:
        data = {}
        if token:
            data["token"] = token
        r = requests.post(
            f"https://{server}.gofile.io/contents/uploadfile",
            files={"file": f},
            data=data
        )
    result = r.json()
    if result["status"] == "ok":
        code = result["data"]["folderCode"]
        print(f"Uploaded: https://gofile.io/d/{code}")
        return result["data"]
    raise Exception(f"Upload failed: {result}")

# Guest upload
upload_to_gofile("/path/to/file.zip")

# Authenticated upload (token from account settings)
upload_to_gofile("/path/to/file.zip", token="YOUR_ACCOUNT_TOKEN")
```

Always fetch the upload server dynamically via `/servers` instead of hardcoding one.

### 2.3 Managing Files

File management (renaming, organizing, setting passwords, deleting) requires a Gofile account. Register free at https://gofile.io/register.

```python
import requests

TOKEN = "your_account_token"
BASE = "https://api.gofile.io"

def get_account_info(token: str) -> dict:
    r = requests.get(f"{BASE}/accounts/getid", headers={"Authorization": f"Bearer {token}"})
    return r.json()["data"]

def set_folder_password(folder_id: str, password: str, token: str) -> bool:
    r = requests.put(
        f"{BASE}/contents/{folder_id}/update",
        headers={"Authorization": f"Bearer {token}"},
        json={"attribute": "password", "attributeValue": password}
    )
    return r.json()["status"] == "ok"

def delete_content(content_id: str, token: str) -> bool:
    r = requests.delete(
        f"{BASE}/contents",
        headers={"Authorization": f"Bearer {token}"},
        json={"contentsId": content_id}
    )
    return r.json()["status"] == "ok"

def get_folder_contents(folder_id: str, token: str) -> list:
    r = requests.get(
        f"{BASE}/contents/{folder_id}",
        headers={"Authorization": f"Bearer {token}"},
        params={"token": token, "wt": "4fd6sg89d7s6"}
    )
    return r.json()["data"]["children"]
```

### 2.4 API

Full API documentation: https://gofile.io/api

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/servers` | GET | Get available upload servers |
| `/contents/uploadfile` | POST | Upload a file |
| `/contents/{id}` | GET | Get content metadata |
| `/contents/{id}/update` | PUT | Update content (name, password, etc.) |
| `/contents` | DELETE | Delete content |
| `/accounts/getid` | GET | Get account ID from token |
| `/accounts/{id}` | GET | Get account details |

Authenticated requests use a Bearer token in the `Authorization` header. Get the token from https://gofile.io/myprofile after logging in.

### 2.5 Use Cases & Limitations

**Where it fits:** distributing ISOs, VM images, datasets, and video beyond other platforms' size caps (unlimited size); zero-friction one-off anonymous sharing; temporary exchanges with the 10-day guest clock; automated pipelines via the API.

**Limitations & gotchas:**

- **Guest expiry** — uploads deleted after 10 days without activity; create a free account for permanent storage
- **No encryption** — files are stored unencrypted; encrypt sensitive data yourself first
- **Content policy** — illegal content is removed, DMCA takedowns processed
- **Link is a folder page** — the share link opens Gofile's web UI, not a direct file download; recipients click through

---

## 3. MediaFire — Persistent Public Storage

MediaFire is a free cloud file hosting and sharing service. It is widely used for distributing large files, ROM collections, software archives, and datasets — the model is storage, not transfer: links don't expire as long as the account stays active, and recipients never need an account or see a countdown timer.

- **Website:** https://www.mediafire.com
- **Founded:** 2006
- **Storage:** 10 GB free, 100 GB (Ultra) or 1 TB (Pro)
- **Max file size:** 5 GB per file on free (50 GB on Pro/Ultra)

### 3.1 Plans

| Feature | Basic (Free) | Pro | Ultra |
|---------|---------------|-----|-------|
| **Storage** | 10 GB | 1 TB | 100 GB |
| **Ad-free transfers** | ❌ | 1 TB | 50 GB (CDN) |
| **Max file size** | 5 GB | 50 GB | 50 GB |
| **Bandwidth** | Unlimited | Unlimited | Unlimited |
| **Download wait** | None (no countdown timer) | None | None |
| **Direct links** | ❌ | ✅ | ✅ |
| **No account for download** | ✅ | ✅ | ✅ |
| **Ad-free downloads** | ❌ (ads shown) | ✅ | ✅ |
| **Bulk download** | ❌ (single-file only) | ✅ | ✅ |
| **FileDrop file requests** | ❌ | ✅ | ✅ |
| **Custom subdomain** | ❌ | ✅ | ✅ |
| **Password protection** | ❌ | ✅ | ✅ |
| **One-time links** | ❌ | ✅ | ✅ |
| **Priority support** | ❌ | ✅ | ✅ |
| **Price** | $0 | $5.83/mo billed annually, or $6.99 month-to-month | $10/mo |

Business is a separate tier: 2 TB+ storage, 100 user accounts, customisable branding and a detailed security log, priced separately.

Free tier in one line: 10 GB, 5 GB per file, no expiry, no recipient login, no timer — but links are public and unprotected.

### 3.2 Uploading Files

**Web:** log in at https://www.mediafire.com → **Upload** → drag and drop → files appear in your MediaFire Drive.

**Desktop app:** Windows and macOS apps add a Dropbox-style sync folder.

**Mobile:** Android and iOS apps for uploading from your phone.

**API uploads:** see [§3.5](#35-api).

### 3.3 Sharing Links

Every file gets a shareable link:

```
https://www.mediafire.com/file/FILEID/filename.ext/file
```

| Type | Who can access | Availability |
|------|---------------|-------------|
| **Public link** | Anyone with the URL | Free |
| **Direct download link** | Bypasses MediaFire page (not reliably offered) | See CLI notes below |
| **Password-protected** | Only those with password | Pro+ |
| **Folder link** | Anyone — downloads whole folder or individual files | Free |

MediaFire does not officially offer permanent direct download links on the free tier; CLI tricks with `wget --content-disposition` or `curl -L` often trigger a direct download by following redirects.

### 3.4 Folders & Organization

Folder links share a whole collection:

```
https://www.mediafire.com/folder/FOLDERID/FolderName
```

Recipients browse in a web interface and download single files or the entire folder as a ZIP. Create via **New Folder** in your Drive, upload into it, then right-click → **Share**.

### 3.5 API

REST API with session-token authentication: https://app.mediafire.com/developers/core-api/

```python
import requests
import hashlib

def get_session_token(email: str, password: str) -> str:
    """Authenticate and get a MediaFire session token."""
    password_hash = hashlib.sha256(password.encode()).hexdigest()[:10].upper()

    url = "https://www.mediafire.com/api/1.5/user/get_session_token.php"
    params = {
        "email": email,
        "password": password_hash,
        "application_id": "YOUR_APP_ID",   # Register at mediafire.com/developers
        "signature": "YOUR_SIGNATURE",
        "response_format": "json"
    }
    r = requests.get(url, params=params)
    data = r.json()
    return data["response"]["session_token"]
```

File operations:

```python
import requests

SESSION_TOKEN = "your_session_token"
BASE = "https://www.mediafire.com/api/1.5"

def get_file_info(quickkey: str) -> dict:
    """Get metadata for a file by its quickkey (the ID in the share link)."""
    r = requests.get(f"{BASE}/file/get_info.php", params={
        "quick_key": quickkey,
        "session_token": SESSION_TOKEN,
        "response_format": "json"
    })
    return r.json()["response"]["file_info"]

def get_folder_content(folder_key: str = "myfiles") -> list:
    """List files in a folder. 'myfiles' is the root folder."""
    r = requests.get(f"{BASE}/folder/get_content.php", params={
        "folder_key": folder_key,
        "content_type": "files",
        "session_token": SESSION_TOKEN,
        "response_format": "json"
    })
    return r.json()["response"]["folder_content"]["files"]

def get_links(quickkey: str) -> dict:
    """Get all download links for a file."""
    r = requests.get(f"{BASE}/file/get_links.php", params={
        "quick_keys": quickkey,
        "session_token": SESSION_TOKEN,
        "response_format": "json"
    })
    return r.json()["response"]["links"]

def delete_file(quickkey: str) -> bool:
    """Move a file to trash."""
    r = requests.post(f"{BASE}/file/delete.php", data={
        "quick_keys": quickkey,
        "session_token": SESSION_TOKEN,
        "response_format": "json"
    })
    return r.json()["response"]["result"] == "Success"
```

Upload via API:

```python
def upload_file(filepath: str, folder_key: str = None) -> dict:
    """Upload a file to MediaFire."""
    import os
    filename = os.path.basename(filepath)

    headers = {
        "x-filehash": compute_sha256(filepath),     # SHA-256 of file content
        "x-filename": filename,
        "x-filesize": str(os.path.getsize(filepath)),
        "x-session-token": SESSION_TOKEN,
    }
    if folder_key:
        headers["x-folder-key"] = folder_key

    url = "https://www.mediafire.com/api/1.5/upload/simple.php?response_format=json"
    with open(filepath, "rb") as f:
        r = requests.post(url, headers=headers, data=f)
    return r.json()
```

### 3.6 Downloading via CLI

The download page is regular HTML with a download button; automated downloading means following the redirect chain or scraping the button href:

```bash
wget "https://www.mediafire.com/file/FILEID/filename.zip/file" \
  --content-disposition --user-agent="Mozilla/5.0"

curl -L -J -O "https://www.mediafire.com/file/FILEID/filename.zip/file" \
  -H "User-Agent: Mozilla/5.0"

aria2c "https://www.mediafire.com/file/FILEID/filename.zip/file"
```

Large files may route through a confirmation page. If direct download fails, fetch the HTML, extract the direct link, then download it:

```python
import requests
from bs4 import BeautifulSoup

def get_mediafire_direct_link(page_url: str):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    r = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find("a", id="downloadButton")
    if link:
        return link["href"]
    for a in soup.find_all("a", href=True):
        if "download" in a["href"].lower():
            return a["href"]
    return None

direct = get_mediafire_direct_link("https://www.mediafire.com/file/FILEID/file.zip/file")
if direct:
    import subprocess
    subprocess.run(["wget", "-O", "output.zip", direct])
```

### 3.7 Use Cases & Limitations

**Where it fits:** public distribution of ISOs, ROM packs, video, and archives without timers; 10 GB free backup via sync app; folder links for collections; heavily used in emulation communities for hosting ROM archives and BIOS files.

**Limitations & gotchas:**

- **No encryption at rest** — files stored unencrypted; encrypt them yourself first
- **No free password protection** — anyone with the URL can download (Pro adds passwords)
- **Terms of Service** — illegal content, infringement, malware removed; DMCA takedowns processed and widely-shared files (ROMs, movies) are frequently taken down
- **Account inactivity** — long-idle free accounts may have files deleted; log in every few months
- **Link permanence cuts both ways** — public, non-expiring links get indexed, shared, and cached beyond your control; don't use for files you may want to revoke

---

## 4. Mega.nz — End-to-End Encrypted Storage

Mega.nz is a cloud storage platform built around client-side encryption: files are encrypted with AES-128 on your device before upload, and the key is derived from your password — Mega holds ciphertext only and cannot read your files, filenames, or folder contents. It pairs this with one of the more generous free storage tiers available.

- **Website:** https://mega.nz
- **Founded:** 2013 by Kim Dotcom (operated by Mega Limited, New Zealand)
- **Free storage:** 20 GB (signup bonus storage is temporary)
- **Encryption:** AES-128 end-to-end, client-side; client crypto is open source

### 4.1 Plans

| Feature | Free | Pro I | Pro II | Pro III |
|---------|------|-------|--------|---------|
| **Storage** | 20 GB | 2 TB | 8 TB | 16 TB |
| **Transfer quota** | Limited | 2 TB/mo | 8 TB/mo | 16 TB/mo |
| **Max upload size** | Unlimited | Unlimited | Unlimited | Unlimited |
| **End-to-end encryption** | ✅ | ✅ | ✅ | ✅ |
| **Price** | Free | ~€5/mo | ~€10/mo | ~€20/mo |

**Transfer quota is the key constraint:** free accounts get a limited monthly transfer allowance. When exceeded, *recipients* of your public links temporarily can't download until the quota resets (a few hours to a day). This limits Mega's usefulness for popular public sharing, regardless of storage room.

### 4.2 Core Features

**End-to-end encryption.** Files are AES-128 encrypted before leaving the device; the key is derived from your password.

```
Your file → AES-128 encrypt (client-side) → upload encrypted blob → Mega servers
                                ↑
                    Key stored only in your browser/app
                    (Mega never sees the key)
```

If you forget your password, files are unrecoverable — Mega cannot reset your key. Export the Recovery Key from account settings and store it safely.

**File versioning** — previous versions survive overwrites and can be recovered from file properties.

**MEGAchat** — built-in end-to-end encrypted chat and video calls in web and mobile apps.

**Multi-device sync** — the desktop app syncs selected folders between computer and cloud.

### 4.3 Sharing Files & Folders

**Public links carry the key in the URL fragment:**

```
https://mega.nz/file/FILEID#ENCRYPTIONKEY
https://mega.nz/folder/FOLDERID#ENCRYPTIONKEY
```

The `#ENCRYPTIONKEY` fragment is never transmitted to Mega's servers — browsers don't send fragments in HTTP requests. Mega is only storing and serving ciphertext; decryption happens in the recipient's browser.

**Password-protected links** add another layer on top: right-click → Share → Get Link → **Set password**. This re-encrypts the link key with your password, so recipients need both.

**Expiry dates** on links are a Pro feature; free links don't expire.

**Collaboration** — share folders with specific Mega accounts read-only or read-write; changes sync in real time.

### 4.4 MEGAcmd — Command Line

MEGAcmd is the official CLI providing full account access from a terminal.

```bash
# Install MEGAcmd
# Ubuntu/Debian — .deb from https://mega.nz/cmd
sudo apt install ./megacmd-*.deb

# Arch (AUR)
yay -S megacmd

# macOS
brew install --cask megacmd
```

Authentication & navigation:

```bash
mega-login your@email.com your_password
mega-df -h                       # Storage and quota
mega-ls -l /
mega-cd /MyFolder
mega-logout
```

File operations:

```bash
# Upload / download
mega-put file.zip /MyFolder/
mega-put -r ./my-project/ /Backups/my-project/
mega-get /MyFolder/file.zip ./
mega-get -r /MyFolder ./local-folder/

# Copy / move / delete
mega-cp /Source/file.zip /Destination/
mega-mv /Source/file.zip /Destination/
mega-rm /MyFolder/file.zip               # to trash
mega-rm -f /MyFolder/file.zip            # permanent
mega-mkdir -p /Parent/Child/GrandChild
```

Sharing:

```bash
# Export as public link (prints URL with key fragment)
mega-export -a /MyFolder/file.zip
mega-export /                        # list shared links
mega-export -d /MyFolder/file.zip    # revoke link

# Share folder with a user (0 = read-only)
mega-share -a --with=their@email.com /SharedFolder
mega-share -a --with=their@email.com --level=0 /SharedFolder
```

Sync:

```bash
mega-sync /local/path /RemotePath    # create sync
mega-sync                            # list syncs
mega-sync -d /local/path             # remove sync (keeps files)
```

Automated backup example:

```bash
#!/bin/bash
# Daily backup using MEGAcmd
DATE=$(date +%Y-%m-%d)
BACKUP_NAME="backup-$DATE.tar.gz"
LOCAL_SOURCE="/home/user/important-data"
MEGA_DEST="/Backups"

tar -czf "/tmp/$BACKUP_NAME" "$LOCAL_SOURCE"
mega-put "/tmp/$BACKUP_NAME" "$MEGA_DEST/"
echo "Backup uploaded: $MEGA_DEST/$BACKUP_NAME"

# Keep only the last 7 backups
mega-ls -l "$MEGA_DEST" | awk '{print $NF}' | sort -r | tail -n +8 | while read f; do
    mega-rm "$MEGA_DEST/$f"
    echo "Deleted old backup: $f"
done

rm "/tmp/$BACKUP_NAME"
```

### 4.5 API & SDK

Official SDKs exist for C++, Python, Android, iOS, and JavaScript.

```bash
pip install mega.py
```

```python
from mega import Mega

mega = Mega()
m = mega.login("your@email.com", "your_password")

# Account info
info = m.get_user()
print(f"Email: {info['email']}")
print(f"Storage used: {info['cstor']} bytes")

# Upload and link
file = m.upload("local_file.zip")
link = m.get_upload_link(file)
print(f"Share link: {link}")

# Search and download
file = m.find("filename.zip")
m.download(file)
m.download_url("https://mega.nz/file/FILEID#KEY")

# List all files
files = m.get_files()
for fh, f in files.items():
    if f.get("t") == 0:  # type 0 = file
        print(f["a"].get("n", "unknown"))
```

### 4.6 Security Model

| Threat | Protected? | Notes |
|--------|-----------|-------|
| **Mega reading your files** | ✅ | Client-side AES-128 — they hold ciphertext only |
| **Server breach exposing content** | ✅ | Encrypted before upload |
| **Share link interception** | ✅ | Key in `#fragment` never sent to server |
| **Anyone with the link** | Partial | The full URL (with key) decrypts the file — share carefully |
| **Password-protected links** | ✅ | Extra encryption layer on the key |
| **Compromised device** | ❌ | Malware can read files before encryption |
| **Legal requests** | ❌ | Mega complies with valid court orders — can hand over metadata and account info, though not file contents |

What Mega explicitly does *not* protect: forgotten passwords (key lost forever), compromised browsers/devices, and metadata — Mega knows login times, file sizes, and folder tree structure, and is subject to New Zealand law.

### 4.7 Limitations & Gotchas

- **Transfer quota throttling** — free-tier shared files fail to download for recipients once your monthly quota resets window is exhausted
- **Password recovery impossible** — no Recovery Key export + forgotten password = permanently lost files
- **Key lives in the URL** — anywhere the full link (with `#KEY`) is posted, the file is decryptable
- **Browser extension recommended** — official MEGA extension speeds up large transfers and reduces memory usage
- **Signup bonuses expire** — temporary storage bonuses shrink back to the base 20 GB

---

## 5. Smash — Large File Transfer

Smash is a transfer-focused service from France (launched 2017 in Lyon) — the workflow model is **upload → send link → recipient downloads → link expires**. It resembles WeTransfer more than Dropbox, and its free tier is limited to **2 GB per transfer** and a **7-day** expiry window.

- **Website:** https://fromsmash.com
- **Model:** File transfer (send-focused, not storage)
- **Account required:** No (sender or recipient, on free tier)
- **Encryption:** TLS in transit, AES-256 at rest (no client-side E2E encryption)
- **Free retention:** 7 days

### 5.1 Plans

| Feature | Free | Pro | Team / Enterprise (custom) |
|---------|------|-----|--------------------------|
| **Max file size** | 2 GB | Unlimited | Unlimited |
| **Transfer expiry** | 7 days | up to 30 days | Custom |
| **Password protection** | ✅ | ✅ | ✅ |
| **Custom link** | ❌ | ✅ | ✅ |
| **Download tracking** | ❌ | ✅ | ✅ |
| **Custom domain** | ❌ | ❌ | ✅ |

The non-obvious caveats: files over ~2 GB get lower processing priority on the free tier, and free transfers carry Smash branding.

### 5.2 How It Works

Transfer-centric mental model:

```
Sender uploads → Smash generates link → Sender shares link → Recipient downloads
                                                              (link expires in 7 days)
```

Files are stored AES-256 encrypted during the transfer window and permanently deleted after expiry. Smash is explicitly not a backup or hosting target — that's what MediaFire/Gofile/Mega are for.

### 5.3 Sending Files

**Web:** visit https://fromsmash.com → drag and drop files or folders → optionally add recipient emails (Smash emails them the link directly) → **Transfer**.

```
Link format: https://fromsmash.com/TRANSFERID
```

**Email delivery** sends a clean notification with a download button — presents better than a raw link for client-facing work. **Download tracking** (Premium) shows when and how often recipients downloaded.

### 5.4 API & SDK

REST API with API-key auth (key from the account dashboard): https://api.fromsmash.com/docs

```bash
# Create a transfer, get an upload URL
curl -X POST https://api.fromsmash.com/v1/transfers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "files": [{"name": "report.pdf", "size": 1048576}],
    "availabilityDuration": 14
  }'

# Upload the file to the returned URL
curl -X PUT "UPLOAD_URL_FROM_RESPONSE" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @report.pdf
```

```python
import requests

API_KEY = "your_api_key"
BASE = "https://api.fromsmash.com/v1"

def create_transfer(filename: str, filesize: int, days: int = 14) -> dict:
    """Create a transfer and get an upload URL."""
    r = requests.post(
        f"{BASE}/transfers",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "files": [{"name": filename, "size": filesize}],
            "availabilityDuration": days
        }
    )
    return r.json()

def upload_file(filepath: str, days: int = 14) -> str:
    """Upload a file to Smash and return the shareable link."""
    import os
    transfer = create_transfer(
        os.path.basename(filepath), os.path.getsize(filepath), days
    )
    upload_url = transfer["files"][0]["uploadUrl"]
    transfer_id = transfer["id"]

    with open(filepath, "rb") as f:
        requests.put(upload_url,
                     headers={"Content-Type": "application/octet-stream"},
                     data=f)

    return f"https://fromsmash.com/{transfer_id}"

link = upload_file("/path/to/largefile.zip")
print(f"Share link: {link}")
```

Node.js SDK:

```bash
npm install @smash-sdk/uploader
```

```javascript
const { Uploader } = require("@smash-sdk/uploader");

const uploader = new Uploader({
    token: "YOUR_API_KEY",
    files: ["./large-file.zip"],
    availabilityDuration: 14
});

uploader.on("progress", (progress) => {
    console.log(`Upload progress: ${progress.percent}%`);
});

uploader.on("finish", (transfer) => {
    console.log(`Transfer link: https://fromsmash.com/${transfer.id}`);
});

await uploader.start();
```

### 5.5 Use Cases & Limitations

**Where it fits:** sending large video files to clients (renders, project files) without a size cap; professional-looking email delivery for handoffs; one-time big sends where 7 days is plenty; replacing clunky FTP handoffs with a simple link-and-email flow.

**Limitations & gotchas:**

- **7-day expiry on the free tier** — deleted after expiry; this is a parcel service, not storage
- **Password protection is available on the free tier**
- **No client-side E2E encryption** — Smash handles encryption server-side; for maximum privacy use OnionShare
- **Throttling** — free transfers may be throttled during peak times, and files above ~2 GB get lower priority
- **API needs an account** — web uploads work account-free, but the API requires a key from a free account

---

## 6. Comparison

| Service | Model | Free Storage | Max File Size | Free Retention | Download Account? | Password Links | API / CLI | Client-Side Encryption |
|---------|-------|-------------|---------------|----------------|--------------------|----------------|-----------|------------------------|
| **Gofile** | Hosting (anonymous) | No quota | Unlimited | 10 days inactive (guest) / indefinite (account) | No | Account only | REST | ❌ |
| **MediaFire** | Hosting (persistent) | 10 GB | 5 GB free / 50 GB paid | Indefinite | No | Pro only | REST | ❌ |
| **Mega.nz** | Encrypted storage | 20 GB | Unlimited | Indefinite | Yes (unless link includes key) | ✅ | MEGAcmd + SDKs | ✅ AES-128 |
| **Smash** | Transfer | — | 2 GB free / Unlimited paid | 7 days | No | ✅ (all plans) | REST + Node SDK | ❌ (server-side) |
| **WeTransfer** | Transfer | — | 3 GB | 3 days | No | Paid | — | ❌ |
| **Catbox.moe** | Hosting (retrieval-focused) | No quota | 200 MB | Indefinite | No | ❌ | — | ❌ |
| **Archive.org** | Permanent archive | No quota | Large | Indefinite | No | ❌ | ✅ (CDX/S3) | ❌ |
| **OnionShare** | Tor P2P | Your disk | Your disk | Session | No (Tor required) | — | — | ✅ (Tor) |

### Quick Decision Guide

| Need | Recommendation |
|------|---------------|
| Send a huge file once, no account | **Smash** |
| Public file that must not expire | **MediaFire** |
| Public file > 20 GB, indefinite hosting | **Gofile** (free account) |
| Private storage only you can read | **Mega.nz** |
| Encrypted one-time sharing, no third party | **OnionShare** |
| Tiny files with permanent direct links | **Catbox.moe** |
| Permanent archival of public-domain content | **Archive.org** |
| Files for a project/team with live collaboration | **Google Drive** |

---

## 7. See Also

- [Archive.org](archive-org.md) — permanent free archival storage and the Wayback Machine
- [OnionShare](../networking/onionshare.md) — anonymous sharing over Tor
- [URL Shorteners](url-shorteners.md) — wrap long download URLs into trackable short links
- [APIs & Resources](../devtools/apis-and-resources.md) — developer API reference
