# DarkFB - Facebook Security Testing Tool (Educational)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x%2B%20%7C%202.7-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Purpose-Educational%20Only-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Migrated-Python3%20Ready-green?style=for-the-badge">
</p>

> **⚠️ EDUCATIONAL ONLY** - Untuk pembelajaran keamanan akun sendiri. Jangan untuk meretas akun orang lain.

Original: **Mr.D4N** | Migrated Python3 by **uchil404 (TBH)**

---

### 📦 Files
- `fbMrD4N.py` - **Arsip Python2** (original, butuh `python2` + `mechanize`)
- `darkfb.py` - **Baru Python3** (tanpa mechanize, pakai `requests`, jalan di Termux baru)

### ✨ Migrasi Python3
File lama `fbMrD4N.py` error di Python3 (`print` tanpa `()` dan `mechanize`). File baru `darkfb.py` sudah:
- ✅ `print()` Python3
- ✅ `input()` bukan `raw_input`
- ✅ `requests` bukan `mechanize`
- ✅ Tidak menyimpan password (demo edukasi)

### 📦 Installation

**Termux Baru (Python3 - Recommended):**
```bash
pkg update && pkg install python git
pip install requests
git clone https://github.com/TulungagungBlackHat/darkfb
cd darkfb
python3 darkfb.py
```

**Termux Lama (Python2 - Arsip):**
```bash
pkg install python2
pip2 install requests mechanize
python2 fbMrD4N.py
```

### 🚀 Usage
```bash
python3 darkfb.py
# Pilih 1 untuk demo, 2 untuk tips proteksi
```

### 🛡️ Lindungi Akun
- 2FA, password kuat, cek phising pakai [TBH-PhishDetector](https://github.com/TulungagungBlackHat/TBH-PhishDetector)

### 👥 Credits
- Original: Mr.D4N
- Python3: uchil404 - [Tulungagung Black Hat](https://github.com/TulungagungBlackHat)

<p align="center"><b>Always Smile :)</b></p>
