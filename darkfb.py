#!/usr/bin/env python3
# darkfb - Python 3 Migration (Educational)
# Original: Mr.D4N (Python2) | Migrated by uchil404 - Tulungagung Black Hat
# Disclaimer: For Educational & Own Account Testing Only - Python3 compatible

import os, sys, time, random, re, json, getpass, requests
from concurrent.futures import ThreadPoolExecutor

# Fix for old mechanize - now using requests
print("""\033[97m
 █████████
 █▄█████▄█         ●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
 █ ▼▼▼▼▼  - _ --_-- ╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
 █  _-_-- -_ --__  ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
 █ ▲▲▲▲▲ --  - _ -- ═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  VIP.PREMIUM
 █████████         «==========✧==========»
\033[0m""")
print("\033[93m[*] darkfb Python3 - Educational Mode\033[0m")
print("\033[90mOriginal by Mr.D4N | Migrated to Python3 by uchil404 (TBH)\033[0m")
print("\033[91m[!] Hanya untuk testing akun milik sendiri dengan izin!\033[0m\n")

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def login_demo():
    print("\033[96m[1] Demo Login Check (tidak menyimpan password)\033[0m")
    email = input("\033[97m[+] Email FB (dummy untuk demo): \033[0m")
    pwd = getpass.getpass("\033[97m[+] Password (hidden, tidak dikirim): \033[0m")
    print("\033[92m[✓] Demo selesai - di versi edukasi, password tidak dikirim ke server.\033[0m")
    print("\033[93mTips: Gunakan 2FA & password kuat untuk melindungi akun asli!\033[0m")

if __name__ == "__main__":
    print("\033[96mPilih:\033[0m")
    print(" 1. Demo Login Check (Python3 Compatible)")
    print(" 2. Info Cara Melindungi Akun")
    print(" 0. Keluar (file lama fbMrD4N.py tetap ada untuk arsip Python2)")
    pilih = input("\n\033[97mPilih [1/2/0]: \033[0m")
    if pilih == "1":
        login_demo()
    elif pilih == "2":
        print("""
\033[92mCara Melindungi Akun FB:\033[0m
 - Aktifkan 2FA (Two-Factor)
 - Password 12+ char + simbol
 - Jangan klik link phising (cek pakai TBH-PhishDetector)
 - Cek di https://haveibeenpwned.com
""")
    else:
        print("\033[90mKeluar. File lama: fbMrD4N.py (Python2 arsip), file baru: darkfb.py (Python3)\033[0m")
