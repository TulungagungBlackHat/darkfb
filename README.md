# DarkFB - Facebook Security Testing Tool (Educational)

<p align="center">
  <img src="https://img.shields.io/badge/Python-2.7-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Purpose-Educational%20Only-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-For%20Learning-orange?style=for-the-badge">
</p>

> **⚠️ DISCLAIMER - EDUCATIONAL PURPOSE ONLY**
> Tool ini untuk **pembelajaran keamanan akun Facebook milik sendiri** dan memahami teknik Brute Force agar bisa melakukan mitigasi. **Dilarang keras** digunakan untuk meretas akun orang lain. Segala penyalahgunaan di luar tanggung jawab developer. Gunakan hanya untuk **Penetration Testing dengan izin**.

> **Note:** Facebook telah menerapkan proteksi 2FA & rate-limit. Tool ini mungkin tidak bekerja pada akun dengan keamanan modern - justru itu tujuan edukasinya: pahami pentingnya 2FA.

Original Author: **Mr.D4N** | Maintained by **Tulungagung Black Hat**

---

### ✨ Features
- 🔐 Brute Force simulation untuk edukasi
- 👥 Support crack via friendlist / group / ID list
- ⚡ Multi-threading (ThreadPool)
- 🛡️ Checkpoint & Vuln detection
- 📱 User-Agent Opera Mini (mobile emulation)

### 📦 Installation

**Termux:**
```bash
pkg update && pkg upgrade
pkg install python2 git
pip2 install requests mechanize
git clone https://github.com/TulungagungBlackHat/darkfb
cd darkfb
python2 fbMrD4N.py
```

**Kali Linux:**
```bash
apt update && apt install python2 git
pip2 install requests mechanize
git clone https://github.com/TulungagungBlackHat/darkfb
cd darkfb
python2 fbMrD4N.py
```

### 🚀 Usage
1. Jalankan `python2 fbMrD4N.py`
2. Login menggunakan akun FB dummy milik sendiri (untuk testing)
3. Pilih metode: Crack via friendlist / ID / file
4. Pelajari bagaimana password lemah mudah ditebak & pentingnya password kuat + 2FA

### 🛡️ Cara Melindungi Akun FB Kamu
- Gunakan password kuat & unik (12+ karakter)
- Aktifkan **Two-Factor Authentication (2FA)**
- Jangan gunakan password yang sama di banyak platform
- Waspada phising & jangan login di link mencurigakan

### ⚖️ Legal
Hanya gunakan pada akun **milik sendiri** atau dengan **izin tertulis**. Mengakses akun orang lain tanpa izin melanggar UU ITE di Indonesia dan melanggar ToS Facebook/GitHub.

### 👥 Credits
- Author: Mr.D4N
- Team: [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) - Tulungagung, Jawa Timur

<p align="center"><b>Always Smile :)</b></p>
