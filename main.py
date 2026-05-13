<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DENJAKA SMART OBD2 SOC</title>
    <style>
        :root {
            --neon-blue: #00d2ff; --neon-green: #39ff14;
            --danger: #ff3131; --warning: #ffca28;
            --bg: #0a0b10; --card: #1c1f26;
        }
        
        body { background-color: var(--bg); color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; overflow-x: hidden; }
        
        .header {
            display: flex; justify-content: space-between; align-items: center;
            background: var(--card); padding: 12px 15px;
            border-bottom: 2px solid var(--neon-blue); position: sticky; top: 0; z-index: 100;
        }
        .brand-section h1 { font-size: 0.95rem; letter-spacing: 1px; color: var(--neon-blue); margin: 0; font-weight: 800; }
        .brand-section span { font-size: 0.55rem; color: #fff; display: block; }

        .btn-group { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px; width: 45%; }
        .btn-sm { background: #1a1a1a; color: white; border: 1px solid #444; padding: 6px 2px; border-radius: 4px; font-size: 0.55rem; font-weight: bold; cursor: pointer; }
        .btn-connect { background: var(--neon-blue); color: black; border: none; padding: 8px; margin-top: 2px; font-size: 0.65rem; grid-column: span 3; border-radius: 4px; font-weight: bold; cursor: pointer; }
        /* Container Tombol: Kita buat baris atas seragam 3 kolom */
.btn-group { 
    display: grid; 
    grid-template-columns: repeat(3, 1fr); /* Membagi 3 kolom sama rata secara presisi */
    gap: 6px; 
    width: 55%; /* Sedikit diperlebar agar teks tidak berdesakan */
}

/* Tombol Kecil: Dibuat seragam tinggi dan bentuknya */
.btn-sm { 
    background: linear-gradient(145deg, #1a1a1a, #252830); /* Efek gradien agar lebih estetik */
    color: white; 
    border: 1px solid #444; 
    padding: 10px 0; /* Padding atas-bawah tetap, samping biarkan auto agar center */
    border-radius: 6px; 
    font-size: 0.7rem; 
    font-weight: 700; 
    cursor: pointer;
    user-select: none;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
}

/* Efek saat ditekan (Feedback Visual) */
.btn-sm:active {
    transform: scale(0.95);
    background: #333;
    border-color: var(--neon-blue);
}

/* Tombol Connect: Dibuat melintang penuh di bawah 3 tombol atas */
.btn-connect { 
    background: linear-gradient(90deg, var(--neon-blue), #008fb3);
    color: black; 
    border: none; 
    padding: 12px; 
    margin-top: 6px; 
    font-size: 0.8rem; 
    grid-column: span 3; /* Menghabiskan seluruh lebar baris */
    border-radius: 6px; 
    font-weight: 800; 
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 0 10px rgba(0, 210, 255, 0.3);
}


        .grid-container { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 12px; }
        .card { background: var(--card); padding: 12px; border-radius: 12px; border: 1px solid #333; display: none; transition: 0.3s; }
        .card.active { display: block; border: 1px solid var(--neon-blue); }
       /* Ganti bagian .card.problem dan @keyframes blink dengan ini */
/* CSS untuk kartu yang bermasalah saat scan */
.card.problem {
    border: 2px solid var(--danger) !important;
    box-shadow: 0 0 15px rgba(255, 49, 49, 0.6);
    animation: alert-blink 0.8s infinite alternate ease-in-out;
}

@keyframes alert-blink {
    from { opacity: 1; border-color: var(--danger); }
    to { opacity: 0.4; border-color: transparent; }
}


@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0.7; }
    100% { opacity: 1; }
}

        .label { font-size: 0.6rem; color: #aaa; text-transform: uppercase; display: block; margin-bottom: 5px; }
        .value { font-size: 1.5rem; font-weight: bold; }
        .unit { font-size: 0.7rem; color: var(--neon-blue); margin-left: 3px; }

        .bar-wrapper { display: flex; align-items: center; gap: 8px; margin-top: 10px; }
        .bar-container { flex-grow: 1; height: 6px; background: #111; border-radius: 3px; overflow: hidden; }
        .bar-fill { height: 100%; width: 0%; transition: width 0.5s ease; }
        .percent-text { font-size: 0.65rem; font-weight: bold; min-width: 30px; color: var(--neon-blue); }

        #settings-panel { position: fixed; top: 0; right: 0; width: 85%; height: 100%; background: #0f1117; z-index: 1000; padding: 20px; overflow-y: auto; transform: translateX(100%); transition: 0.4s; border-left: 2px solid var(--neon-blue); }
        #settings-panel.open { transform: translateX(0); }
        .cat-title { color: var(--neon-blue); font-size: 0.75rem; margin: 15px 0 8px; border-left: 3px solid var(--neon-blue); padding-left: 8px; background: rgba(0,210,255,0.05); padding: 5px; }
        
        .setting-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #222; }
        .switch { position: relative; display: inline-block; width: 34px; height: 20px; }
        .switch input { opacity: 0; width: 0; height: 0; }
        .slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #444; transition: .4s; border-radius: 34px; }
        .slider:before { position: absolute; content: ""; height: 14px; width: 14px; left: 3px; bottom: 3px; background-color: white; transition: .4s; border-radius: 50%; }
        input:checked + .slider { background-color: var(--neon-blue); }
        input:checked + .slider:before { transform: translateX(14px); }

        #custom-alert { position: fixed; inset: 0; background: rgba(0,0,0,0.8); display: none; align-items: center; justify-content: center; z-index: 9999; }
        .modal-box { background: #1c1f26; border: 2px solid var(--neon-blue); padding: 25px; border-radius: 15px; text-align: center; width: 80%; }
    </style>
</head>
<body>

<div class="header">
    <div class="brand-section">
        <h1>DENJAKA <span style="color:#fff;">SMART OBD2</span></h1>
        <span>SOCIETY OF CYBERNETICS (SOC)</span>
    </div>
    <div class="btn-group">
        <button class="btn-sm" style="color: var(--neon-blue); border: 1px solid var(--neon-blue);" onclick="runFullHealthScan()">🔍 SCAN 50</button>
        <button class="btn-sm" style="color: var(--danger);" onclick="sendCmd('04\r')">⚠️ DTC</button>
        <button class="btn-sm" onclick="toggleSettings()">⚙️ SAKLAR</button>
        <button class="btn-sm" style="color: var(--neon-green);" onclick="location.reload()">🔄 RESET</button>
        <button class="btn-connect" onclick="connectOBD()">CONNECT SYSTEM</button>
    </div>
</div>

<div id="log-info" style="padding: 10px 15px; font-size: 0.65rem; color: #777; background: #000; display: flex; justify-content: space-between;">
    <span id="conn-status">• Status: Standby.</span>
    <span id="car-info" style="color: var(--neon-blue); font-weight: bold;"></span>
</div>


<div id="dashboard" class="grid-container"></div>

<div id="settings-panel">
    <h2 style="color: var(--neon-blue); font-size: 1rem;">KONFIGURASI SENSOR (50)</h2>
    <button class="btn-connect" style="width: 100%; margin-bottom: 20px;" onclick="toggleSettings()">SIMPAN & KELUAR</button>
    <div id="settings-list"></div>
</div>

<div id="custom-alert">
    <div class="modal-box">
        <p id="alert-msg"></p>
        <button onclick="closeAlert()" style="background: var(--neon-blue); border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold;">OK</button>
    </div>
</div>

<script>
    let gattChar, isLooping = false;
    const enc = new TextEncoder(), dec = new TextDecoder();

        const allFeatures = [
        { cat: "DIAGNOSA UTAMA", pids: [
            { id: "volt", n: "Tegangan Aki", u: "V", cmd: "AT RV", min: 11.0, max: 14.8, active: true },
            { id: "temp", n: "Suhu Pendingin", u: "°C", cmd: "01 05", min: 40, max: 115, active: true },
            { id: "rpm", n: "Putaran Mesin", u: "RPM", cmd: "01 0C", min: 0, max: 8000, active: true },
            { id: "speed", n: "Kecepatan", u: "Km/jam", cmd: "01 0D", min: 0, max: 200, active: true },
            { id: "load", n: "Beban Mesin", u: "%", cmd: "01 04", min: 0, max: 100, active: true },
            { id: "gas", n: "Bukaan Gas", u: "%", cmd: "01 11", min: 0, max: 100, active: true },
            { id: "dtc_count", n: "Jumlah Kode Eror", u: "", cmd: "01 01", min: 0, max: 5, active: false },
            { id: "runtime", n: "Waktu Mesin Hidup", u: "dtk", cmd: "01 1F", min: 0, max: 5000, active: false },
            { id: "distance", n: "Jarak Lampu MIL", u: "Km", cmd: "01 21", min: 0, max: 1000, active: false },
            { id: "warmups", n: "Jumlah Pemanasan", u: "", cmd: "01 30", min: 0, max: 255, active: false }
        ]},
        { cat: "BAHAN BAKAR & UDARA", pids: [
            { id: "fuel_level", n: "Level Bahan Bakar", u: "%", cmd: "01 2F", min: 0, max: 100, active: false },
            { id: "fuel_press", n: "Tekanan BBM", u: "kPa", cmd: "01 0A", min: 0, max: 600, active: false },
            { id: "iat", n: "Suhu Udara Masuk", u: "°C", cmd: "01 0F", min: 10, max: 70, active: false },
            { id: "maf", n: "Aliran Udara (MAF)", u: "g/s", cmd: "01 10", min: 0, max: 200, active: false },
            { id: "map", n: "Tekanan Intake (MAP)", u: "kPa", cmd: "01 0B", min: 0, max: 255, active: false },
            { id: "baro", n: "Tekanan Barometrik", u: "kPa", cmd: "01 33", min: 0, max: 110, active: false },
            { id: "trim_s1", n: "Koreksi BBM J.Pendek", u: "%", cmd: "01 06", min: -20, max: 20, active: false },
            { id: "trim_l1", n: "Koreksi BBM J.Panjang", u: "%", cmd: "01 07", min: -20, max: 20, active: false },
            { id: "trim_s2", n: "Koreksi BBM Bank 2", u: "%", cmd: "01 08", min: -20, max: 20, active: false },
            { id: "fuel_rate", n: "Konsumsi BBM", u: "L/jam", cmd: "01 5E", min: 0, max: 40, active: false }
        ]},
        { cat: "SISTEM LISTRIK & EMISI", pids: [
            { id: "ctrl_v", n: "Voltase Kontrol", u: "V", cmd: "01 42", min: 10, max: 16, active: false },
            { id: "ambient", n: "Suhu Luar", u: "°C", cmd: "01 46", min: 0, max: 50, active: false },
            { id: "oil_temp", n: "Suhu Oli", u: "°C", cmd: "01 5C", min: 40, max: 150, active: false },
            { id: "o2_v1", n: "Sensor Oksigen", u: "V", cmd: "01 14", min: 0, max: 1.2, active: false },
            { id: "cat_t1", n: "Suhu Katalis", u: "°C", cmd: "01 3C", min: 100, max: 800, active: false },
            { id: "egr_err", n: "Eror Katup EGR", u: "%", cmd: "01 2D", min: -100, max: 100, active: false },
            { id: "evap", n: "Tekanan Evap", u: "Pa", cmd: "01 32", min: -5000, max: 5000, active: false },
            { id: "abs_load", n: "Beban Absolut", u: "%", cmd: "01 43", min: 0, max: 100, active: false },
            { id: "clear_dist", n: "Jarak Sejak Reset", u: "Km", cmd: "01 31", min: 0, max: 5000, active: false },
            { id: "bat_soc", n: "Kesehatan Baterai", u: "%", cmd: "01 5B", min: 0, max: 100, active: false }
        ]},
        { cat: "TRANSMISI & RODA", pids: [
            { id: "trans_t", n: "Suhu Transmisi", u: "°C", cmd: "21 82", min: 40, max: 130, active: false },
            { id: "gear", n: "Posisi Gigi", u: "", cmd: "21 0A", min: 0, max: 6, active: false },
            { id: "tpms_fl", n: "Ban Depan Kiri", u: "Psi", cmd: "21 01", min: 25, max: 45, active: false },
            { id: "tpms_fr", n: "Ban Depan Kanan", u: "Psi", cmd: "21 02", min: 25, max: 45, active: false },
            { id: "tpms_rl", n: "Ban Belakang Kiri", u: "Psi", cmd: "21 03", min: 25, max: 45, active: false },
            { id: "tpms_rr", n: "Ban Belakang Kanan", u: "Psi", cmd: "21 04", min: 25, max: 45, active: false },
            { id: "steer_angle", n: "Sudut Setir", u: "°", cmd: "21 05", min: -360, max: 360, active: false },
            { id: "brk_press", n: "Tekanan Rem", u: "Bar", cmd: "21 06", min: 0, max: 150, active: false },
            { id: "odo", n: "Odometer", u: "Km", cmd: "21 07", min: 0, max: 999999, active: false },
            { id: "service", n: "Jarak Servis", u: "Km", cmd: "21 08", min: 0, max: 10000, active: false }
        ]},
        { cat: "KONTROL GAS LANJUTAN", pids: [
            { id: "thr_b", n: "Katup Gas B", u: "%", cmd: "01 47", min: 0, max: 100, active: false },
            { id: "thr_c", n: "Katup Gas C", u: "%", cmd: "01 48", min: 0, max: 100, active: false },
            { id: "ped_d", n: "Pedal Gas D", u: "%", cmd: "01 49", min: 0, max: 100, active: false },
            { id: "ped_e", n: "Pedal Gas E", u: "%", cmd: "01 4A", min: 0, max: 100, active: false },
            { id: "ped_f", n: "Pedal Gas F", u: "%", cmd: "01 4B", min: 0, max: 100, active: false },
            { id: "thr_cmd", n: "Perintah Katup Gas", u: "%", cmd: "01 4C", min: 0, max: 100, active: false },
            { id: "boost", n: "Tekanan Turbo", u: "kPa", cmd: "01 70", min: 0, max: 200, active: false },
            { id: "oil_press", n: "Tekanan Oli", u: "kPa", cmd: "01 6C", min: 0, max: 1000, active: false },
            { id: "exhaust_p", n: "Tekanan Knalpot", u: "kPa", cmd: "01 73", min: 0, max: 500, active: false },
            { id: "iat_b1", n: "Suhu Udara Bank 1", u: "°C", cmd: "01 68", min: 0, max: 100, active: false }
        ]}
    ];

    const dash = document.getElementById('dashboard'), setList = document.getElementById('settings-list');
    // --- BAGIAN INISIALISASI UI (Ganti baris 158 ke bawah dengan ini) ---
let dashHTML = "";
let setHTML = "";

allFeatures.forEach(group => {
    // 1. Membangun Judul Kategori (Group Title)
    setHTML += `<div class="cat-title">${group.cat}</div>`;

    group.pids.forEach(p => {
        // 2. Membangun Kartu Dashboard (Hanya muncul jika saklar aktif)
        // Penambahan class 'active' menentukan apakah kartu terlihat di grid
        dashHTML += `
        <div id="card-${p.id}" class="card ${p.active ? 'active' : ''}" onclick="showAdvice('${p.id}')">
            <span class="label">${p.n}</span>
            <div class="value">
                <span id="val-${p.id}">--</span>
                <span class="unit">${p.u}</span>
            </div>
            <div class="bar-wrapper">
                <div class="bar-container">
                    <div id="bar-${p.id}" class="bar-fill" style="background:var(--neon-blue)"></div>
                </div>
                <span id="pct-${p.id}" class="percent-text">0%</span>
            </div>
        </div>`;

        // 3. Membangun Item Saklar (Settings Menu)
        // Menambahkan label yang jelas dan transisi yang sinkron dengan dashboard
        setHTML += `
        <div class="setting-item">
            <div class="setting-info">
                <span style="font-size: 0.8rem; font-weight: 500;">${p.n}</span>
                <small style="display: block; color: #666; font-size: 0.6rem;">CMD: ${p.cmd}</small>
            </div>
            <label class="switch">
                <input type="checkbox" ${p.active ? 'checked' : ''} 
                       onchange="toggleFeature('${p.id}')">
                <span class="slider"></span>
            </label>
        </div>`;
    });
});


dash.innerHTML = dashHTML;
setList.innerHTML = setHTML;

    function toggleSettings() { document.getElementById('settings-panel').classList.toggle('open'); }
    function toggleFeature(id) { 
    const card = document.getElementById(`card-${id}`);
    card.classList.toggle('active');
    // Sinkronkan status active ke dalam data allFeatures
    allFeatures.forEach(g => {
        let p = g.pids.find(f => f.id === id);
        if(p) p.active = card.classList.contains('active');
    });
}

    function showAlert(msg) { document.getElementById('alert-msg').innerText = msg; document.getElementById('custom-alert').style.display = 'flex'; }
    function closeAlert() { document.getElementById('custom-alert').style.display = 'none'; }

        // Fungsi Bridge untuk memanggil Python Native
async function connectOBD() {
    const statusEl = document.getElementById('conn-status');
    
    // 1. Cek apakah jembatan Python tersedia (saat sudah jadi APK)
    if (typeof python !== 'undefined' || window.python_api) {
        try {
            statusEl.innerText = "• Mencari V-LINK via Native API...";
            statusEl.style.color = "var(--neon-blue)";

            // Memanggil fungsi di main.py (Native Android)
            // Kita kirimkan UUID yang dibutuhkan Vgate iCar Pro
            const success = await python.start_native_bluetooth("0000fff0-0000-1000-8000-00805f9b34fb");
            
            if (success) {
    // Pemicu otomatis agar startLoop() langsung jalan
    updateConnStatus("Connected via Native API");
}

        } catch (e) {
            statusEl.innerText = "• Error Native: " + e.message;
        }
    } else {
        // Fallback untuk testing di browser biasa
        alert("Mode Native tidak terdeteksi. Pastikan aplikasi dijalankan sebagai APK Denjaka SOC.");
    }
}

// Fungsi baru untuk menerima data "setoran" dari Python ke dashboard
function receiveDataFromNative(raw) {
    // Fungsi parseData kamu yang sudah gahar tetap dipakai di sini
    parseData(raw);
}



async function sendCmd(c) { 
    // Kita tidak lagi cek gattChar, tapi cek apakah jembatan Python tersedia
    if (typeof python !== 'undefined') {
        try {
            // Memastikan perintah punya akhiran \r (Carriage Return)
            let formattedCmd = c.endsWith('\r') ? c : c + '\r';
            
            // Melempar perintah ke fungsi 'send_command_native' yang ada di main.py
            python.call("send_command_native", formattedCmd);
            
        } catch (e) {
            console.error("Native Write Error:", e);
        }
    } else {
        // Fallback untuk simulasi di browser laptop saat pengembangan
        console.log("Simulasi Kirim Command: " + c);
    }
}

// Kamus tahun berdasarkan digit ke-10 VIN
function getVehicleYear(code) {
    const years = { 
        'P': 2023, 'R': 2024, 'S': 2025, 'T': 2026, 
        'V': 2027, 'W': 2028, 'X': 2029, 'Y': 2030 
    };
    return years[code] || code;
}

// Logika untuk menangkap dan memproses nomor VIN
function processVIN(cleanRaw) {
    if (cleanRaw.startsWith("4902")) {
        let vin = "";
        // Konversi Hex ke teks mulai dari karakter ke-7
        for (let i = 6; i < cleanRaw.length; i += 2) {
            let hex = cleanRaw.substring(i, i + 2);
            let charCode = parseInt(hex, 16);
            if (charCode > 31 && charCode < 127) vin += String.fromCharCode(charCode);
        }
        
        if (vin.length >= 10) {
            let yearCode = vin.charAt(9);
            let year = getVehicleYear(yearCode);
            let wmi = vin.substring(0, 3); // World Manufacturer Identifier
            let brand = "Mobil";

            // Deteksi Merek (Umum di Indonesia)
            if (wmi === "MHF" || wmi === "93H") brand = "TOYOTA";
            else if (wmi === "MHR") brand = "HONDA";
            else if (wmi === "MK4") brand = "SUZUKI";
            else if (wmi === "MNA") brand = "MITSUBISHI";

            document.getElementById('car-info').innerText = `${brand} [${year}]`;
            document.getElementById('conn-status').innerText = "• Sistem Teridentifikasi";
        }
    }
}

        function parseData(raw) {
    let cleanRaw = raw.replace(/\s|>|\r|\n/g, "").toUpperCase();
    if (!cleanRaw) return;

    // Tambahkan baris ini untuk cek VIN
    if (cleanRaw.startsWith("4902")) { processVIN(cleanRaw); return; }
    // Menangani respon AT RV (Aki) yang biasanya formatnya "12.4V"
    if (cleanRaw.includes(".") || (!cleanRaw.startsWith("41") && !cleanRaw.startsWith("61"))) {
        let match = cleanRaw.match(/(\d+\.\d+)/); 
        if (match) {
            let v = parseFloat(match[1]);
            if (v > 5 && v < 18) updateValue('volt', v.toFixed(1));
        }
        return; 
    }
    const mode = cleanRaw.substring(0, 2);
    const pid = cleanRaw.substring(2, 4);
    const getByte = (start) => {
    if (cleanRaw.length < start + 2) return 0; // Pengaman jika data terpotong
    return parseInt(cleanRaw.substring(start, start + 2), 16);
};


    try {
        if (mode === "41") {
            let A = getByte(4), B = getByte(6), C = getByte(8), D = getByte(10);
            switch(pid) {
                // DIAGNOSA UTAMA
                case "05": updateValue('temp', A - 40); break;
                case "0C": updateValue('rpm', Math.round(((A * 256) + B) / 4)); break;
                case "0D": updateValue('speed', A); break;
                case "04": updateValue('load', Math.round(A * 100 / 255)); break;
                case "11": updateValue('gas', Math.round(A * 100 / 255)); break;
                case "01": updateValue('dtc_count', A & 0x7F); break;
                case "1F": updateValue('runtime', (A * 256) + B); break;
                case "21": updateValue('distance', (A * 256) + B); break;
                case "30": updateValue('warmups', A); break;
                case "31": updateValue('clear_dist', (A * 256) + B); break;

                // BAHAN BAKAR & UDARA
                case "2F": updateValue('fuel_level', Math.round(A * 100 / 255)); break;
                case "0A": updateValue('fuel_press', A * 3); break;
                case "0F": updateValue('iat', A - 40); break;
                case "10": updateValue('maf', ((A * 256) + B) / 100); break;
                case "0B": updateValue('map', A); break;
                case "33": updateValue('baro', A); break;
                case "06": updateValue('trim_s1', Math.round((A - 128) * 100 / 128)); break;
                case "07": updateValue('trim_l1', Math.round((A - 128) * 100 / 128)); break;
                case "08": updateValue('trim_s2', Math.round((A - 128) * 100 / 128)); break;
                case "5E": updateValue('fuel_rate', ((A * 256) + B) / 20); break;

                // ELEKTRIKAL & EMISI
                case "42": updateValue('ctrl_v', ((A * 256) + B) / 1000); break;
                case "46": updateValue('ambient', A - 40); break;
                case "5C": updateValue('oil_temp', A - 40); break;
                case "14": updateValue('o2_v1', (A / 200).toFixed(2)); break;
                case "3C": updateValue('cat_t1', (((A * 256) + B) / 10) - 40); break;
                case "2D": updateValue('egr_err', Math.round((A - 128) * 100 / 128)); break;
                case "32": updateValue('evap', ((A * 256) + B) / 4); break;
                case "43": updateValue('abs_load', Math.round(((A * 256) + B) * 100 / 255)); break;
                case "5B": updateValue('bat_soc', Math.round(A * 100 / 255)); break;

                // THROTTLE & OIL
                case "47": updateValue('thr_b', Math.round(A * 100 / 255)); break;
                case "48": updateValue('thr_c', Math.round(A * 100 / 255)); break;
                case "49": updateValue('ped_d', Math.round(A * 100 / 255)); break;
                case "4A": updateValue('ped_e', Math.round(A * 100 / 255)); break;
                case "4B": updateValue('ped_f', Math.round(A * 100 / 255)); break;
                case "4C": updateValue('thr_cmd', Math.round(A * 100 / 255)); break;
                case "70": updateValue('boost', (A * 256) + B); break;
                case "6C": updateValue('oil_press', A * 10); break;
                case "73": updateValue('exhaust_p', ((A * 256) + B) / 10); break;
                case "68": updateValue('iat_b1', A - 40); break;
            }
        } 
        else if (mode === "61") {
            let A = getByte(4), B = getByte(6);
            switch(pid) {
                case "82": updateValue('trans_t', A - 40); break;
                case "0A": updateValue('gear', A); break;
                case "01": updateValue('tpms_fl', Math.round(A * 0.232)); break;
                case "02": updateValue('tpms_fr', Math.round(A * 0.232)); break;
                case "03": updateValue('tpms_rl', Math.round(A * 0.232)); break;
                case "04": updateValue('tpms_rr', Math.round(A * 0.232)); break;
                case "05": updateValue('steer_angle', ((A * 256) + B) - 32768); break;
                case "06": updateValue('brk_press', A); break;
                case "07": updateValue('odo', (A * 65536) + (B * 256) + getByte(8)); break;
                case "08": updateValue('service', (A * 256) + B); break;
            }
        }
    } catch(err) { console.error("Parse Error:", err); }
}


        function updateValue(id, v) {
        const el = document.getElementById(`val-${id}`);
        if (!el) return; 
        
        el.innerText = v; // Menampilkan angka di layar
        
        let s = null; 
        allFeatures.forEach(g => { 
            let f = g.pids.find(p => p.id === id); 
            if(f) s = f; 
        });

        if (s) {
            // --- TEMPEL DI SINI ---
            let currentVal = parseFloat(v); 
            let p = Math.min(100, Math.max(0, ((currentVal - s.min) / (s.max - s.min)) * 100));
            // -----------------------
            
            document.getElementById(`bar-${id}`).style.width = p + "%";
            document.getElementById(`pct-${id}`).innerText = Math.round(p) + "%";
        }
    }

// GANTIKAN SEMUA FUNGSI startLoop LAMA DENGAN INI
async function startLoop() {
    while (isLooping) {
        try {
            let activePids = [];
            // Mengumpulkan sensor yang saklarnya posisi ON
            allFeatures.forEach(g => {
                g.pids.forEach(p => { 
                    if(p.active) activePids.push(p); 
                });
            });

            if(activePids.length === 0) {
                await new Promise(r => setTimeout(r, 1000));
                continue;
            }

            for (let target of activePids) {
                if (!isLooping || !target.active) continue;

                // Kirim perintah ke Python Native
                await sendCmd(target.cmd);
                
                // Jeda 180ms agar modul OBD2 tidak panas (Overload)
                await new Promise(r => setTimeout(r, 180)); 
            }
        } catch (err) {
            isLooping = false;
            document.getElementById('conn-status').innerText = "• Koneksi Terputus.";
            console.error("Loop Error:", err);
            break;
        }
    }
}

    

// --- PERBAIKAN FUNGSI UPDATE STATUS ---
function updateConnStatus(msg) {
    const el = document.getElementById('conn-status'); 
    
    // Validasi elemen agar tidak error jika UI belum siap
    if (!el) {
        console.error("Elemen 'conn-status' tidak ditemukan di DOM.");
        return;
    }
    
    // Update teks status sesuai kiriman dari Python
    el.innerText = "• " + msg;
    
    // Logika Deteksi Koneksi Berhasil
    // Mendukung kata kunci 'Connected' (Inggris) atau 'Terhubung' (Indonesia)
    if (msg.includes("Connected") || msg.includes("Terhubung")) {
        
        // Ubah warna teks jadi hijau neon (Normal/Aktif)
        el.style.color = "var(--neon-green)";
        
        // Jalankan Loop Data hanya jika belum berjalan
        // Ini penting agar perintah OBD tidak dikirim double
        if (!isLooping) {
            console.log("Koneksi terdeteksi, memulai siklus pengambilan data...");
            isLooping = true;
            startLoop(); 
        }
    } 
    // Logika Deteksi Putus Koneksi
    else if (msg.includes("Disconnected") || msg.includes("Terputus") || msg.includes("Error")) {
        
        // Ubah warna teks jadi merah (Bahaya/Mati)
        el.style.color = "var(--danger)";
        
        // Hentikan Loop agar tidak membebani prosesor HP
        isLooping = false;
        console.warn("Koneksi terputus, siklus data dihentikan.");
    }
}
// --- PERBAIKAN LOOP DATA ---


function showAdvice(id) {
    let s = null;
    allFeatures.forEach(g => { 
        let f = g.pids.find(p => p.id === id); 
        if(f) s = f; 
    });

    if (!s) return;

    let currentVal = document.getElementById(`val-${id}`).innerText;
    let msg = "";

    if (currentVal === "--") {
        msg = `Sensor ${s.n} belum menerima data. Pastikan mesin menyala dan OBD2 terhubung.`;
    } else {
        let v = parseFloat(currentVal);
        if (v < s.min) msg = `⚠️ ${s.n} Terlalu Rendah (${v}${s.u}). Segera periksa sistem!`;
        else if (v > s.max) msg = `🔥 BAHAYA! ${s.n} Overheat/Overlimit (${v}${s.u}).`;
        else msg = `✅ ${s.n} Normal (${v}${s.u}). Sistem bekerja dengan baik.`;
    }
    showAlert(msg);
}

async function runFullHealthScan() {
    document.getElementById('log-info').innerText = "• MEMULAI PEMINDAIAN 50 PILAR SISTEM...";
    let healthReport = [];
    let criticalIssues = 0;

    // Sisir semua kategori dan sensor
    allFeatures.forEach(group => {
        group.pids.forEach(p => {
            let valEl = document.getElementById(`val-${p.id}`);
            if (valEl && valEl.innerText !== "--") {
                let v = parseFloat(valEl.innerText);
                
                // Cek apakah nilai di luar ambang batas aman
                if (v > p.max) {
                    healthReport.push(`🔥 ${p.n} TERLALU TINGGI: ${v}${p.u}`);
                    criticalIssues++;
                    document.getElementById(`card-${p.id}`).classList.add('problem');
                } else if (v < p.min) {
                    healthReport.push(`⚠️ ${p.n} TERLALU RENDAH: ${v}${p.u}`);
                    criticalIssues++;
                    document.getElementById(`card-${p.id}`).classList.add('problem');
                } else {
                    // Jika kembali normal, hapus tanda problem
                    document.getElementById(`card-${p.id}`).classList.remove('problem');
                }
            }
        });
    });

    // Diagnosa Tambahan: Jadwal Ganti Oli (Jika Odo terbaca)
    const odoEl = document.getElementById('val-odo');
    if (odoEl && odoEl.innerText !== "--") {
        let currentOdo = parseFloat(odoEl.innerText);
        if (currentOdo % 10000 > 9500) { // Pengingat setiap kelipatan 10rb km
            healthReport.push("🛠️ PERINGATAN SERVICE: Cek kondisi Oli & Filter!");
            criticalIssues++;
        }
    }

    // Tampilkan Hasil
    if (criticalIssues > 0) {
        showAlert("HASIL PEMINDAIAN 50 PILAR:\n\n" + healthReport.join("\n"));
    } else {
        document.getElementById('log-info').innerText = "• Scan Selesai: 50 Pilar Sistem Normal.";
        showAlert("✅ SEMUA SISTEM NORMAL\n\n50 Pilar kesehatan kendaraan dalam kondisi prima.");
    }
}
// Auto-scan setiap 5 menit (300.000 ms) saat sistem terhubung
setInterval(() => {
    if (isLooping) runFullHealthScan();
}, 300000);

</script>
</body>
</html>
