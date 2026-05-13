[app]

# (str) Judul aplikasi kamu
title = Denjaka SOC

# (str) Nama paket (harus unik, jangan pakai spasi)
package.name = denjakasoc.obd2

# (str) Domain paket
package.domain = org.denjaka

# (str) Direktori tempat main.py berada
source.dir = .

# (list) Ekstensi file yang akan dimasukkan ke dalam APK
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (list) List library yang dibutuhkan (Kivy dan Pyjnius wajib ada)
requirements = python3,kivy,android,pyjnius

# (str) Versi aplikasi
version = 1.0.0

# (list) IZIN AKSES (Paling Penting!)
# Menambahkan izin Bluetooth dan Lokasi agar Vgate iCar Pro bisa terbaca
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, ACCESS_FINE_LOCATION

# (int) Target Android API (Gunakan 33 untuk standar HP terbaru 2026)
android.api = 33

# (int) Minimum Android API
android.minapi = 21

# (str) Orientasi layar (Landscape cocok untuk dashboard mobil)
orientation = landscape

# (bool) Fullscreen mode
fullscreen = 1

# (list) Fitur yang dibutuhkan hardware
android.features = android.hardware.bluetooth, android.hardware.location.gps

# (str) Ikon aplikasi (jika kamu punya file icon.png)
# icon.filename = %(source.dir)s/icon.png

# (list) Arsitektur HP (arm64-v8a untuk HP modern sekarang)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Level log (2 untuk melihat error detail saat build)
log_level = 2

# (int) Apakah akan menghapus build lama?
warn_on_root = 1
