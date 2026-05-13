[app]

# (str) Judul aplikasi kamu
title = Denjaka SOC

# (str) Nama paket
package.name = denjakasoc

# (str) Domain paket
package.domain = org.denjaka

# (str) Direktori tempat main.py berada
source.dir = .

# (list) Ekstensi file yang akan dimasukkan ke dalam APK
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (list) List library yang dibutuhkan
# Menambahkan 'plyer' untuk akses sensor/bluetooth yang lebih stabil 
# dan 'requests' jika dashboard kamu mengambil data dari internet.
requirements = python3,kivy==2.3.0,android,pyjnius,plyer

# (str) Versi aplikasi
version = 1.0.0

# (list) IZIN AKSES (DIPERBARUI)
# Android 12+ (API 31, 32, 33) butuh BLUETOOTH_SCAN dan CONNECT secara spesifik.
# INTERNET ditambahkan agar WebView/Dashboard bisa merender aset lokal dengan lancar.
android.permissions = INTERNET, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION

# (int) Target Android API (Tetap di 33 untuk standar 2026)
android.api = 33

# (int) Minimum Android API
android.minapi = 21

# (str) Orientasi layar
orientation = landscape

# (bool) Fullscreen mode
fullscreen = 1

# (list) Fitur hardware yang dikunci
android.features = android.hardware.bluetooth, android.hardware.location.gps

# (list) Arsitektur HP 
# Pastikan arm64-v8a ada di urutan pertama untuk performa HP modern.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Biarkan aplikasi tetap menyala (Penting untuk Dashboard OBD2)
android.wakelock = True

[buildozer]
# (int) Level log (Tetap 2 agar kita bisa melihat detail jika gagal lagi)
log_level = 2

# (int) Apakah akan menghapus build lama?
warn_on_root = 1
