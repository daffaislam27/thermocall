import streamlit as st
# CONFIG
st.set_page_config(
    page_title="ThermoCalcz",
    page_icon="🌌",
    layout="wide"
)
# CSS FUTURISTIK SUPER UPGRADE
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #020617, #1e1b4b, #0f172a, #581c87, #3b0764);
    background-size: 500% 500%;
    animation: gradientBG 18s ease infinite;
    color:white;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

.title {
    text-align:center;
    font-size:68px;
    font-weight:900;
    background: linear-gradient(to right,#93c5fd,#dbeafe,#60a5fa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(59,130,246,.8);
    animation: floatTitle 3s ease-in-out infinite;
}

@keyframes floatTitle {
    0% {transform:translateY(0px);}
    50% {transform:translateY(-8px);}
    100% {transform:translateY(0px);}
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:35px;
}

.intro-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 40px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
}

.result {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    color:white;
    padding:25px;
    border-radius:22px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 8px 40px rgba(0,0,0,.35);
    animation: fadeIn 0.7s ease;
    margin-top:20px;
}

@keyframes fadeIn {
    from { opacity:0; transform:translateY(20px); }
    to { opacity:1; transform:translateY(0); }
}

/* Memaksa semua jenis tombol berukuran lebar penuh yang seragam */
.stButton>button, div[data-testid="stButton"]>button {
    width: 100% !important;
    display: block !important;
    padding:15px !important;
    border-radius:18px !important;
    font-weight:700 !important;
    font-size:16px !important;
    border:none !important;
    color:white !important;
    background: linear-gradient(135deg, #7c3aed, #d946ef) !important;
    box-shadow:0 0 18px rgba(217, 70, 239, 0.5) !important;
    transition:all .3s ease !important;
}

.stButton>button:hover, div[data-testid="stButton"]>button:hover {
    transform:translateY(-6px) scale(1.02) !important;
    box-shadow:0 0 30px rgba(217, 70, 239, 0.9) !important;
}

.stNumberInput input, .stTextInput input {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #000000 !important;
    border-radius:15px !important;
    font-weight: 600 !important;
}

[data-testid="stWidgetLabel"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    text-shadow: 0 0 8px rgba(255,255,255,0.4);
}

.katex {
    color:#f5d0fe !important;
    font-size:24px !important;
}

.stAlert {
    border-radius:18px;
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(216,180,254,0.25) !important;
    backdrop-filter: blur(10px);
}

.stAlert p { color: #f5d0fe !important; font-weight: 500; }
.stAlert svg { fill: #d8b4fe !important; }
h1,h2,h3 { color:#f5d0fe; } 
/* Efek hover kartu modul */
.intro-box:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 35px rgba(147,197,253,0.25);
    transition: all 0.3s ease;
}
</style>
""", unsafe_allow_html=True)


# UTILITIES
def fmt(angka):
    try:
        return f"{angka:g}"
    except:
        return str(angka)

# SESSION STATE NAVIGATION
if "current_page" not in st.session_state:
    st.session_state.current_page = "slide1"
if "menu" not in st.session_state:
    st.session_state.menu = None

menu_list = [
    "Hukum 1 Termodinamika", "Usaha", "Kalor", "Entalpi", "Hukum Hess",
    "ΔH Reaksi", "Energi Gibbs", "Entropi", "Gas Ideal", "Gas Nyata",
    "Proses Isobarik", "Proses Isokhorik", "Proses Isotermal", "Edukasi Isotop Gas"
]
# SLIDE 1: JUDUL, SAMBUTAN & TUJUAN
if st.session_state.current_page == "slide1":

    st.snow()

    # CSS KHUSUS JUDUL
    st.markdown("""
    <style>
    .animated-title {
        font-size: 68px;
        font-weight: 900;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #60a5fa,
            #818cf8,
            #a855f7,
            #d946ef,
            #38bdf8
        );
        background-size: 400% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 6s linear infinite;
    }

    @keyframes gradientFlow {
        from {background-position:0% center;}
        to {background-position:400% center;}
    }
    </style>
    """, unsafe_allow_html=True)

    # JUDUL
    st.markdown("""
    <div style="text-align:center;">
        <span style="font-size:70px;">🧮</span>
        <span class="animated-title">ThermoCalculator</span>
        <span style="font-size:70px;">🌡️</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='subtitle'>Kalkulator & Modul Edukasi Termodinamika Universal</div>",
        unsafe_allow_html=True
    )

    st.write("")

    # BOX PENJELASAN
    with st.container(border=True):
        st.markdown("""
        ### 🎯 Selamat Datang di ThermoCalculator!
        
        **ThermoCalculator** adalah platform komputasi termodinamika interaktif yang jadi "asisten" andalan buat mahasiswa, akademisi, sampai praktisi. Alat ini dibuat khusus untuk memangkas waktu pengerjaan analisis energi, perhitungan gas, hingga reaksi kimia dengan hasil yang akurat.
        
        ---
        
        ### 🚀 Tujuan & Kegunaan Aplikasi
        
        1. **Hitung Instan & Otomatis** : Hemat waktu Anda dengan otomatisasi pencarian variabel termodinamika, tanpa perlu repot memanipulasi rumus manual yang rumit.
        2. **Validasi Hasil Studi & Lab** : Validasi data hasil praktikum Anda secara akurat, mulai dari perhitungan entalpi reaktan/produk, kalor gas, hingga Hukum Hess.
        3. **Pahami Konsep, Bukan Cuma Hasil** : Dukung proses belajar Anda lewat fitur penurunan rumus langkah demi langkah (*step-by-step*) untuk pemahaman konseptual yang lebih mendalam.
        """)

    st.write("")

    _, col_btn, _ = st.columns([1,2,1])

    with col_btn:
        if st.button(
            "🚀 Lanjut ke Pemilihan Modul",
            key="next_to_slide2"
        ):
            st.session_state.current_page = "slide2"
            st.rerun()
# SLIDE 2: PILIHAN MODUL KALKULATOR
elif st.session_state.current_page == "slide2":

    st.markdown("""
    <style>
    .menu-title {
        color: #dbeafe !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        margin-bottom: 25px;
        text-align: center;
        text-shadow: 0 0 18px rgba(147,197,253,0.7);
    }

    .st-key-card_energi {
        background: linear-gradient(135deg, rgba(59,130,246,0.28), rgba(168,85,247,0.22));
        border: 1px solid rgba(147,197,253,0.35);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 0 25px rgba(59,130,246,0.25);
    }

    .st-key-card_termo {
        background: linear-gradient(135deg, rgba(236,72,153,0.25), rgba(249,115,22,0.20));
        border: 1px solid rgba(244,114,182,0.35);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 0 25px rgba(236,72,153,0.25);
    }

    .st-key-card_gas {
        background: linear-gradient(135deg, rgba(20,184,166,0.25), rgba(56,189,248,0.20));
        border: 1px solid rgba(45,212,191,0.35);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 0 25px rgba(20,184,166,0.25);
    }

    .st-key-card_proses {
        background: linear-gradient(135deg, rgba(139,92,246,0.25), rgba(34,197,94,0.18));
        border: 1px solid rgba(167,139,250,0.35);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 0 25px rgba(139,92,246,0.25);
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("⬅️ Kembali ke Menu Pengantar", key="back_to_slide1"):
        st.session_state.current_page = "slide1"
        st.rerun()

    st.markdown("<div class='menu-title'>⚗️ Kategori Kalkulator Termodinamika  🌡️</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        with st.container(key="card_energi"):
            st.subheader("⚡ Energetika Dasar")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔸 Hukum 1 Termo", key="btn_h1"):
                    st.session_state.menu = "Hukum 1 Termodinamika"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 Kalor", key="btn_kalor"):
                    st.session_state.menu = "Kalor"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

            with c2:
                if st.button("🔸 Usaha", key="btn_usaha"):
                    st.session_state.menu = "Usaha"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 Entropi", key="btn_entropi"):
                    st.session_state.menu = "Entropi"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

        st.write("")

        with st.container(key="card_gas"):
            st.subheader("🧬 Fisika Gas")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔸 Gas Ideal", key="btn_ideal"):
                    st.session_state.menu = "Gas Ideal"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

            with c2:
                if st.button("🔸 Gas Nyata", key="btn_nyata"):
                    st.session_state.menu = "Gas Nyata"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

    with col2:
        with st.container(key="card_termo"):
            st.subheader("🧪 Termokimia")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔸 Entalpi", key="btn_entalpi"):
                    st.session_state.menu = "Entalpi"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 ΔH Reaksi", key="btn_dh_reaksi"):
                    st.session_state.menu = "ΔH Reaksi"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

            with c2:
                if st.button("🔸 Hukum Hess", key="btn_hess"):
                    st.session_state.menu = "Hukum Hess"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 Energi Gibbs", key="btn_gibbs"):
                    st.session_state.menu = "Energi Gibbs"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

        st.write("")

        with st.container(key="card_proses"):
            st.subheader("⚙️ Proses Termodinamika")

            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔸 Proses Isobarik", key="btn_isobarik"):
                    st.session_state.menu = "Proses Isobarik"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 Proses Isotermal", key="btn_isotermal"):
                    st.session_state.menu = "Proses Isotermal"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

            with c2:
                if st.button("🔸 Proses Isokhorik", key="btn_isokhorik"):
                    st.session_state.menu = "Proses Isokhorik"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

                if st.button("🔸 Isotop Gas", key="btn_isotop"):
                    st.session_state.menu = "Edukasi Isotop Gas"
                    st.session_state.current_page = "calc_page"
                    st.rerun()

# PAGES: HALAMAN PERHITUNGAN AKTIF
elif st.session_state.current_page == "calc_page":
    menu = st.session_state.menu

    if st.button("⬅️ Kembali ke Pemilihan Modul"):
        st.session_state.current_page = "slide2"
        st.session_state.menu = None
        st.rerun()

    st.header(f"⚗️ {menu}")
    st.divider()

    # 1. HUKUM 1 TERMODINAMIKA
    if menu == "Hukum 1 Termodinamika":
        st.latex(r"\Delta U = Q - W")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["ΔU (Perubahan Energi Dalam)", "Q (Kalor)", "W (Usaha)"])

        # Tambahan Pengertian Dinamis
        if "ΔU" in target:
            st.info("💡 **Perubahan Energi Dalam (ΔU):** Jumlah total energi kinetik dan potensial yang dimiliki oleh partikel-partikel di dalam sistem. Dipengaruhi oleh kalor yang diserap/dilepas dan usaha yang dilakukan/diterima.")
        elif "Q" in target:
            st.info("💡 **Kalor (Q):** Energi panas yang berpindah antara sistem dan lingkungan karena adanya perbedaan suhu. Nilai (+) jika sistem menyerap kalor, (-) jika sistem melepas kalor.")
        else:
            st.info("💡 **Usaha (W):** Energi yang dipindahkan melalui gaya mekanis ketika sistem mengalami perubahan volume. Nilai (+) jika sistem melakukan usaha (ekspansi), (-) jika sistem menerima usaha (kompresi).")

        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        W = st.number_input("W (kJ)", value=0.0) if target != "W (Usaha)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Perubahan Energi Dalam)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔU" in target:
                hasil = Q - W
                langkah = f"ΔU = Q - W <br> ΔU = {fmt(Q)} - {fmt(W)} <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Q" in target:
                hasil = dU + W
                langkah = f"Q = ΔU + W <br> Q = {fmt(dU)} + {fmt(W)} <br> Q = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q - dU
                langkah = f"W = Q - ΔU <br> W = {fmt(Q)} - {fmt(dU)} <br> W = <b>{fmt(hasil)} kJ</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 2. USAHA
    elif menu == "Usaha":
        st.latex(r"W = P \cdot \Delta V")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["W (Usaha)", "P (Tekanan)", "ΔV (Perubahan Volume)"])

        # Tambahan Pengertian Dinamis
        if "W" in target:
            st.info("💡 **Usaha Mekanis (W):** Kerja yang dilakukan oleh gas saat memuai (ekspansi) atau dilakukan pada gas saat menyusut (kompresi) di bawah tekanan tertentu.")
        elif "P" in target:
            st.info("💡 **Tekanan (P):** Gaya tegak lurus yang diberikan oleh molekul gas per satuan luas dinding wadah sistem.")
        else:
            st.info("💡 **Perubahan Volume (ΔV):** Selisih antara volume akhir ($V_2$) dan volume awal ($V_1$) sistem gas ($\\Delta V = V_2 - V_1$).")

        W = st.number_input("W (J)", value=0.0) if target != "W (Usaha)" else 0.0
        P = st.number_input("P (Pa)", value=0.0) if target != "P (Tekanan)" else 0.0
        dV = st.number_input("ΔV (m³)", value=0.0) if target != "ΔV (Perubahan Volume)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "W" in target:
                hasil = P * dV
                langkah = f"W = P × ΔV <br> W = {fmt(P)} × {fmt(dV)} <br> W = <b>{fmt(hasil)} J</b>"
            elif "P" in target:
                hasil = W / dV if dV != 0 else 0
                langkah = f"P = W / ΔV <br> P = {fmt(W)} / {fmt(dV)} <br> P = <b>{fmt(hasil)} Pa</b>"
            else:
                hasil = W / P if P != 0 else 0
                langkah = f"ΔV = W / P <br> ΔV = {fmt(W)} / {fmt(P)} <br> ΔV = <b>{fmt(hasil)} m³</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 3. KALOR
    elif menu == "Kalor":
        st.latex(r"Q = m \cdot c \cdot \Delta T")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["Q (Kalor)", "m (Massa)", "c (Kalor Jenis)", "ΔT (Perubahan Suhu)"])

        # Tambahan Pengertian Dinamis
        if "Q" in target:
            st.info("💡 **Kalor (Q):** Energi panas total yang diserap atau dilepaskan oleh suatu benda bermassa untuk mengubah suhunya.")
        elif "m" in target:
            st.info("💡 **Massa (m):** Kuantitas materi dalam zat atau objek yang sedang dipanaskan atau didinginkan.")
        elif "c" in target:
            st.info("💡 **Kalor Jenis (c):** Banyaknya kalor yang diperlukan oleh 1 gram zat untuk menaikkan suhunya sebesar 1°C atau 1 K. Ini menunjukkan karakteristik termal zat tersebut.")
        else:
            st.info("💡 **Perubahan Suhu (ΔT):** Selisih antara suhu akhir ($T_{akhir}$) dan suhu awal ($T_{awal}$) dari zat.")

        Q = st.number_input("Q (J)", value=0.0) if target != "Q (Kalor)" else 0.0
        m = st.number_input("m (g)", value=0.0) if target != "m (Massa)" else 0.0
        c = st.number_input("c (J/g°C)", value=0.0) if target != "c (Kalor Jenis)" else 0.0
        dT = st.number_input("ΔT (K atau °C)", value=0.0) if target != "ΔT (Perubahan Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "Q" in target:
                hasil = m * c * dT
                langkah = f"Q = m × c × ΔT <br> Q = {fmt(m)} × {fmt(c)} × {fmt(dT)} <br> Q = <b>{fmt(hasil)} J</b>"
            elif "m" in target:
                hasil = Q / (c * dT) if (c * dT) != 0 else 0
                langkah = f"m = Q / (c × ΔT) <br> m = {fmt(Q)} / ({fmt(c)} × {fmt(dT)}) <br> m = <b>{fmt(hasil)} g</b>"
            elif "c" in target:
                hasil = Q / (m * dT) if (m * dT) != 0 else 0
                langkah = f"c = Q / (m × ΔT) <br> c = {fmt(Q)} / ({fmt(m)} × {fmt(dT)}) <br> c = <b>{fmt(hasil)} J/g°C</b>"
            else:
                hasil = Q / (m * c) if (m * c) != 0 else 0
                langkah = f"ΔT = Q / (m × c) <br> ΔT = {fmt(Q)} / ({fmt(m)} × {fmt(c)}) <br> ΔT = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 4. ENTALPI
    elif menu == "Entalpi":
        st.latex(r"\Delta H = \Delta U + \Delta n \cdot R \cdot T")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["ΔH (Entalpi)", "ΔU (Energi Dalam)", "Δn (Perubahan Mol)", "T (Suhu)"])
        R = 0.008314

        # Tambahan Pengertian Dinamis
        if "ΔH" in target:
            st.info("💡 **Perubahan Entalpi (ΔH):** Jumlah energi atau kalor total yang dilepas atau diserap sistem pada kondisi tekanan konstan.")
        elif "ΔU" in target:
            st.info("💡 **Perubahan Energi Dalam (ΔU):** Komponen energi internal sistem (energi kinetik + potensial partikel) di luar kerja ekspansi volume.")
        elif "Δn" in target:
            st.info("💡 **Perubahan Jumlah Mol Gas (Δn):** Selisih jumlah mol produk berwujud gas dengan jumlah mol reaktan berwujud gas ($\\Delta n = n_{produk} - n_{reaktan}$).")
        else:
            st.info("💡 **Suhu Mutlak (T):** Suhu operasi sistem termodinamika yang wajib dinyatakan dalam satuan Kelvin (K).")

        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        dU = st.number_input("ΔU (kJ)", value=0.0) if target != "ΔU (Energi Dalam)" else 0.0
        dn = st.number_input("Δn (mol)", value=0.0) if target != "Δn (Perubahan Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔH" in target:
                hasil = dU + (dn * R * T)
                langkah = f"ΔH = ΔU + (Δn × R × T) <br> ΔH = {fmt(dU)} + ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔH = <b>{fmt(hasil)} kJ</b>"
            elif "ΔU" in target:
                hasil = dH - (dn * R * T)
                langkah = f"ΔU = ΔH - (Δn × R × T) <br> ΔU = {fmt(dH)} - ({fmt(dn)} × {R} × {fmt(T)}) <br> ΔU = <b>{fmt(hasil)} kJ</b>"
            elif "Δn" in target:
                hasil = (dH - dU) / (R * T) if T != 0 else 0
                langkah = f"Δn = (ΔH - ΔU) / (R × T) <br> Δn = ({fmt(dH)} - {fmt(dU)}) / ({R} × {fmt(T)}) <br> Δn = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (dH - dU) / (dn * R) if dn != 0 else 0
                langkah = f"T = (ΔH - ΔU) / (Δn × R) <br> T = ({fmt(dH)} - {fmt(dU)}) / ({fmt(dn)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 5. HUKUM HESS
    elif menu == "Hukum Hess":
        st.latex(r"\Delta H_{total} = \Delta H_1 + \Delta H_2 + ... + \Delta H_n")
        target = st.selectbox("Pilih operasi:", ["Hitung ΔH Total dari list", "Cari satu ΔH yang hilang"])

        # Tambahan Pengertian Dinamis
        if "Total" in target:
            st.info("💡 **Hukum Hess:** Menyatakan bahwa perubahan entalpi total dari suatu reaksi kimia bernilai sama, baik reaksi itu berlangsung dalam satu tahap maupun beberapa tahap (tidak bergantung pada jalannya reaksi, hanya kondisi awal dan akhir).")
        else:
            st.info("💡 **Mencari Komponen ΔH:** Jika total entalpi rute langsung diketahui, kita bisa mencari nilai entalpi salah satu sub-reaksi yang hilang dengan prinsip hukum penjumlahan.")

        if target == "Hitung ΔH Total dari list":
            data = st.text_input("Masukkan semua nilai ΔH (pisahkan dengan koma)", "10,-20,30")
            if st.button("Hitung"):
                arr = [float(x) for x in data.split(",") if x.strip() != ""]
                st.balloons()
                st.markdown(f"<div class='result'><h3>Hasil</h3>ΣΔH = <b>{fmt(sum(arr))} kJ</b></div>",
                            unsafe_allow_html=True)
        else:
            total_h = st.number_input("Masukkan ΔH Total", value=0.0)
            data_parsial = st.text_input("Masukkan ΔH komponen lain yang diketahui (pisahkan dengan koma)", "10,-20")
            if st.button("Hitung"):
                arr = [float(x) for x in data_parsial.split(",") if x.strip() != ""]
                hasil = total_h - sum(arr)
                st.balloons()
                st.markdown(
                    f"<div class='result'><h3>Hasil</h3>ΔH_x = {fmt(total_h)} - {fmt(sum(arr))} <br> ΔH_x = <b>{fmt(hasil)} kJ</b></div>",
                    unsafe_allow_html=True)

    # 6. ΔH REAKSI
    elif menu == "ΔH Reaksi":
        st.latex(r"\Delta H = \sum Hf_{produk} - \sum Hf_{reaktan}")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔH Reaksi", "ΣHf Produk", "ΣHf Reaktan"])

        # Tambahan Pengertian Dinamis
        if "ΔH Reaksi" in target:
            st.info("💡 **ΔH Reaksi:** Kalor netto reaksi yang dihitung dari total entalpi pembentukan standar ($H_f^\\circ$) zat-zat produk dikurangi zat-zat reaktan.")
        elif "Produk" in target:
            st.info("💡 **ΣHf Produk:** Total energi entalpi pembentukan standar milik seluruh senyawa baru hasil akhir reaksi (sisi kanan panah).")
        else:
            st.info("💡 **ΣHf Reaktan:** Total energi entalpi pembentukan standar milik seluruh senyawa awal / pereaksi (sisi kiri panah).")

        dH = st.number_input("ΔH Reaksi (kJ)", value=0.0) if target != "ΔH Reaksi" else 0.0
        prod = st.text_input("Masukkan nilai Produk (pisah koma)", "0") if target != "ΣHf Produk" else "0"
        reak = st.text_input("Masukkan nilai Reaktan (pisah koma)", "0") if target != "ΣHf Reaktan" else "0"

        if st.button("Hitung"):
            st.balloons()
            p_sum = sum([float(x) for x in prod.split(",") if x.strip() != ""])
            r_sum = sum([float(x) for x in reak.split(",") if x.strip() != ""])

            if target == "ΔH Reaksi":
                hasil = p_sum - r_sum
                langkah = f"ΔH = {fmt(p_sum)} - {fmt(r_sum)} = <b>{fmt(hasil)} kJ/mol</b>"
            elif target == "ΣHf Produk":
                hasil = dH + r_sum
                langkah = f"ΣHf_produk = {fmt(dH)} + {fmt(r_sum)} = <b>{fmt(hasil)} kJ/mol</b>"
            else:
                hasil = p_sum - dH
                langkah = f"ΣHf_reaktan = {fmt(p_sum)} - {fmt(dH)} = <b>{fmt(hasil)} kJ/mol</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 7. ENERGI GIBBS
    elif menu == "Energi Gibbs":
        st.latex(r"\Delta G = \Delta H - T \cdot \Delta S")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["ΔG (Energi Gibbs)", "ΔH (Entalpi)", "T (Suhu dalam K)", "ΔS (Entropi dalam kJ/K)"])

        # Tambahan Pengertian Dinamis
        if "ΔG" in target:
            st.info("💡 **Energi Bebas Gibbs (ΔG):** Parameter potensial termodinamika untuk memprediksi kespontanan reaksi. Reaksi berjalan spontan jika $\\Delta G < 0$, tidak spontan jika $\\Delta G > 0$, dan setimbang jika $\\Delta G = 0$.")
        elif "ΔH" in target:
            st.info("💡 **Entalpi (ΔH):** Kuantitas energi panas internal total pada sistem.")
        elif "T" in target:
            st.info("💡 **Suhu (T):** Faktor pengali termal derajat ketidakteraturan (Kelvin).")
        else:
            st.info("💡 **Perubahan Entropi (ΔS):** Ukuran derajat ketidakteraturan atau keacakan partikel dalam sistem.")

        dG = st.number_input("ΔG (kJ)", value=0.0) if target != "ΔG (Energi Gibbs)" else 0.0
        dH = st.number_input("ΔH (kJ)", value=0.0) if target != "ΔH (Entalpi)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu dalam K)" else 0.0
        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi dalam kJ/K)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔG" in target:
                hasil = dH - (T * dS)
                langkah = f"ΔG = {fmt(dH)} - ({fmt(T)} × {fmt(dS)}) = <b>{fmt(hasil)} kJ</b>"
            elif "ΔH" in target:
                hasil = dG + (T * dS)
                langkah = f"ΔH = {fmt(dG)} + ({fmt(T)} × {fmt(dS)}) = <b>{fmt(hasil)} kJ</b>"
            elif "T" in target:
                hasil = (dH - dG) / dS if dS != 0 else 0
                langkah = f"T = ({fmt(dH)} - {fmt(dG)}) / {fmt(dS)} = <b>{fmt(hasil)} K</b>"
            else:
                hasil = (dH - dG) / T if T != 0 else 0
                langkah = f"ΔS = ({fmt(dH)} - {fmt(dG)}) / {fmt(T)} = <b>{fmt(hasil)} kJ/K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 8. ENTROPI
    elif menu == "Entropi":
        st.latex(r"\Delta S = \frac{Q}{T}")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["ΔS (Entropi)", "Q (Kalor)", "T (Suhu)"])

        # Tambahan Pengertian Dinamis
        if "ΔS" in target:
            st.info("💡 **Perubahan Entropi (ΔS):** Rasio perpindahan kalor reversibel sistem terhadap suhu mutlaknya, mendefinisikan tingkat penyebaran energi atau ketidakteraturan molekul.")
        elif "Q" in target:
            st.info("💡 **Kalor Reversibel (Q):** Energi termal yang ditransfer masuk/keluar sistem secara perlahan sehingga sistem selalu berada pada kesetimbangan konstan.")
        else:
            st.info("💡 **Suhu Mutlak (T):** Titik temperatur konstan (Kelvin) lingkungan tempat pertukaran energi entropi berlangsung.")

        dS = st.number_input("ΔS (kJ/K)", value=0.0) if target != "ΔS (Entropi)" else 0.0
        Q = st.number_input("Q (kJ)", value=0.0) if target != "Q (Kalor)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "ΔS" in target:
                hasil = Q / T if T != 0 else 0
                langkah = f"ΔS = {fmt(Q)} / {fmt(T)} = <b>{fmt(hasil)} kJ/K</b>"
            elif "Q" in target:
                hasil = dS * T
                langkah = f"Q = {fmt(dS)} × {fmt(T)} = <b>{fmt(hasil)} kJ</b>"
            else:
                hasil = Q / dS if dS != 0 else 0
                langkah = f"T = {fmt(Q)} / {fmt(dS)} = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 9. GAS IDEAL
    elif menu == "Gas Ideal":
        st.latex(r"P \cdot V = n \cdot R \cdot T")
        target = st.selectbox("Pilih variabel yang ingin dicari:",
                              ["P (Tekanan)", "V (Volume)", "n (Jumlah Mol)", "T (Suhu)"])
        R = 0.0821

        # Tambahan Pengertian Dinamis
        if "P" in target:
            st.info("💡 **Tekanan Gas Ideal (P):** Gaya makroskopis tumbukan partikel gas teoritis pada dinding wadah yang kerapatan volumenya diabaikan dan interaksi antarpartikelnya nol.")
        elif "V" in target:
            st.info("💡 **Volume Gas (V):** Ruang geometris wadah penampung gas ideal (satuan liter).")
        elif "n" in target:
            st.info("💡 **Jumlah Mol (n):** Ukuran kuantitas zat yang menyatakan jumlah partikel gas dalam satuan mol.")
        else:
            st.info("💡 **Suhu Mutlak (T):** Derajat panas kinetik partikel dalam derajat Kelvin ($K = ^\\circ C + 273$).")

        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        V = st.number_input("V (L)", value=0.0) if target != "V (Volume)" else 0.0
        n = st.number_input("n (mol)", value=0.0) if target != "n (Jumlah Mol)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "P" in target:
                hasil = (n * R * T) / V if V != 0 else 0
                langkah = f"P = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(V)} = <b>{fmt(hasil)} atm</b>"
            elif "V" in target:
                hasil = (n * R * T) / P if P != 0 else 0
                langkah = f"V = ({fmt(n)} × {R} × {fmt(T)}) / {fmt(P)} = <b>{fmt(hasil)} L</b>"
            elif "n" in target:
                hasil = (P * V) / (R * T) if T != 0 else 0
                langkah = f"n = ({fmt(P)} × {fmt(V)}) / ({R} × {fmt(T)}) = <b>{fmt(hasil)} mol</b>"
            else:
                hasil = (P * V) / (n * R) if n != 0 else 0
                langkah = f"T = ({fmt(P)} × {fmt(V)}) / ({fmt(n)} × {R}) = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 10. GAS NYATA
    elif menu == "Gas Nyata":
        st.latex(r"\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT")
        target = st.selectbox("Pilih variabel yang ingin dicari:", ["P (Tekanan)", "T (Suhu)"])
        R = 0.0821

        # Tambahan Pengertian Dinamis
        if "P" in target:
            st.info("💡 **Tekanan Gas Nyata (Persamaan Van der Waals):** Menghitung koreksi tekanan akibat adanya gaya tarik-menarik antar-molekul gas ($a$) dan volume eksklusi efektif partikel gas nyata itu sendiri ($b$).")
        else:
            st.info("💡 **Suhu Gas Nyata:** Suhu sistem non-ideal yang dipengaruhi oleh koreksi kerapatan internal dan volume aktual molekuler.")

        n = st.number_input("n (mol)", value=0.0)
        V = st.number_input("V (L)", value=0.0)
        a = st.number_input("a (atm.L²/mol²)", value=0.0)
        b = st.number_input("b (L/mol)", value=0.0)

        P = st.number_input("P (atm)", value=0.0) if target != "P (Tekanan)" else 0.0
        T = st.number_input("T (K)", value=0.0) if target != "T (Suhu)" else 0.0

        if st.button("Hitung"):
            st.balloons()
            if "P" in target:
                hasil = ((n * R * T) / (V - n * b)) - ((a * (n ** 2)) / (V ** 2)) if (V - n * b) != 0 and V != 0 else 0
                langkah = f"P = [({fmt(n)} × {R} × {fmt(T)}) / ({fmt(V)} - ({fmt(n)} × {b}))] - [({a} × {fmt(n)}²) / {fmt(V)}²] <br> P = <b>{fmt(hasil)} atm</b>"
            else:
                p_term = P + ((a * (n ** 2)) / (V ** 2)) if V != 0 else 0
                v_term = V - (n * b)
                hasil = (p_term * v_term) / (n * R) if (n * R) != 0 else 0
                langkah = f"T = [({fmt(P)} + {a}×{fmt(n)}²/{fmt(V)}²) × ({fmt(V)} - {fmt(n)}×{b})] / ({fmt(n)} × {R}) <br> T = <b>{fmt(hasil)} K</b>"
            st.markdown(f"<div class='result'><h3>Langkah Penyelesaian</h3>{langkah}</div>", unsafe_allow_html=True)

    # 11. PROSES ISOBARIK
    elif menu == "Proses Isobarik":
        st.latex(r"W = P \cdot (V_2 - V_1), \quad Q = n \cdot C_p \cdot \Delta T")
        
        target_isobarik = st.selectbox("Pilih komponen yang ingin dipelajari/dihitung:", 
                                       ["Usaha Mekanis (W)", "Kalor Isobarik (Q)"])
        
        if "Usaha" in target_isobarik:
            st.info("💡 **Usaha Isobarik (W):** Kerja mekanis yang dilakukan oleh gas atau pada gas ketika sistem memuai/menyusut pada tekanan konstan (tetap).")
        else:
            st.info("💡 **Kalor Isobarik (Q):** Energi panas yang diserap atau dilepas sistem pada tekanan konstan, di mana nilai kapasitas kalornya menggunakan $C_p$.")

        P = st.number_input("P (Pa atau atm)", value=0.0)
        V1 = st.number_input("V1 (m³ atau L)", value=0.0)
        V2 = st.number_input("V2 (m³ atau L)", value=0.0)
        if st.button("Hitung Usaha Isobarik"):
            hasil = P * (V2 - V1)
            st.markdown(
                f"<div class='result'>W = {fmt(P)} × ({fmt(V2)} - {fmt(V1)}) = <b>{fmt(hasil)} Joule/Liter-atm</b></div>",
                unsafe_allow_html=True)

    # 12. PROSES ISOKHORIK
    elif menu == "Proses Isokhorik":
        st.latex(r"W = 0, \quad \Delta U = Q = n \cdot C_v \cdot \Delta T")
        
        st.info("💡 **Proses Isokhorik (Volume Konstan):** Karena wadah sistem kaku dan tidak mengalami perubahan volume ($\Delta V = 0$), maka sistem **tidak melakukan atau menerima usaha mekanis luar** ($W = 0$). Semua kalor yang masuk langsung diubah menjadi energi dalam ($Q = \Delta U$).")
        
        n = st.number_input("n (mol)", value=0.0)
        Cv = st.number_input("Cv (J/mol.K)", value=0.0)
        dT = st.number_input("ΔT (K)", value=0.0)
        if st.button("Hitung Kalor/Energi Dalam"):
            hasil = n * Cv * dT
            st.markdown(
                f"<div class='result'>W = 0 <br> Q = ΔU = {fmt(n)} × {fmt(Cv)} × {fmt(dT)} = <b>{fmt(hasil)} Joule</b></div>",
                unsafe_allow_html=True)

    # 13. PROSES ISOTERMAL
    elif menu == "Proses Isotermal":
        st.latex(r"W = Q = n \cdot R \cdot T \cdot \ln\left(\frac{V_2}{V_1}\right)")
        
        st.info("💡 **Proses Isotermal (Suhu Konstan):** Proses termodinamika yang menjaga suhu sistem agar selalu tetap ($\Delta T = 0$). Karena suhu konstan, perubahan energi dalamnya nol ($\Delta U = 0$), sehingga seluruh kalor yang diserap sistem diubah seutuhnya menjadi usaha mekanis ($Q = W$).")
        
        R = 8.314
        n = st.number_input("n (mol)", value=0.0)
        T = st.number_input("T (K)", value=0.0)
        V1 = st.number_input("V1 (L atau m³)", value=1.0)
        V2 = st.number_input("V2 (L atau m³)", value=1.0)
        if st.button("Hitung Kerja Isotermal"):
            import math

            if V1 != 0 and V2 / V1 > 0:
                hasil = n * R * T * math.log(V2 / V1)
                st.markdown(
                    f"<div class='result'>W = {fmt(n)} × {R} × {fmt(T)} × ln({fmt(V2)}/{fmt(V1)}) = <b>{fmt(hasil)} Joule</b></div>",
                    unsafe_allow_html=True)
            else:
                st.error("Volume tidak valid untuk rasio logaritma alami.")

    # 14. EDUKASI ISOTOP GAS
    elif menu == "Edukasi Isotop Gas":
        st.markdown("""
        ### 🧪 Efek Isotop pada Sifat Termodinamika Gas
        Penggantian unsur dengan isotopnya yang lebih berat (misal $H_2 \\rightarrow D_2$) akan mengubah sifat fisis makro zat tanpa mengganggu struktur konfigurasi elektron luarnya.

        #### Poin Teoretis Utama:
        1. **Kecepatan Efektif ($v_{rms}$):** Berbanding terbalik dengan akar massa molar ($M$). Partikel isotop berat bergerak lebih lambat pada kesetimbangan termal yang sama.
        """)

        st.latex(r"v_{rms} = \sqrt{\frac{3RT}{M}}")

        st.markdown("""
        2. **Pergeseran Kapasitas Kalor:** Perubahan massa merubah momen inersia molekul serta tingkat energi vibrasi kuantumnya.
        """)

        st.write("")
        st.subheader("📊 Komputasi Nilai Efektif ($v_{rms}$) antar Isotop")
        
        pilihan_gas = st.selectbox(
            "Pilih Kelompok Gas / Isotop:",
            ["Hidrogen (H₂ vs D₂)", "Uranium Heksafluorida (²³⁵UF₆ vs ²³⁸UF₆)", "Uap Air (H₂O vs D₂O)"]
        )
        
        if "Hidrogen" in pilihan_gas:
            st.info("💡 **Isotop Hidrogen:** Mengganti Hidrogen ($H_2$) menjadi Deuterium ($D_2$) melipatgandakan massa molar zat, yang secara drastis menurunkan kecepatan rata-rata kinetik molekul gas pada suhu kamar.")
        elif "Uranium" in pilihan_gas:
            st.info("💡 **Isotop Uranium:** Perbedaan massa antara $^{235}UF_6$ dan $^{238}UF_6$ sangat kecil. Fraksionasi kinetik yang tipis inilah yang mendasari metode pemisahan membran/sentrifugasi gas pada pengayaan uranium nuklir.")
        else:
            st.info("💡 **Isotop Uap Air:** Uap air berat ($D_2O$) memiliki interaksi energi ikatan antar-molekul yang sedikit berbeda dari uap air biasa ($H_2O$), memengaruhi tekanan uap jenuh dan entalpi penguapannya.")

        T_isotop = st.number_input("Suhu Sistem (K)", value=300.0, min_value=0.1)

        if pilihan_gas == "Hidrogen (H₂ vs D₂)":
            label_1, M1 = "Hidrogen Biasa ($H_2$)", 0.002016
            label_2, M2 = "Deuterium ($D_2$)", 0.004028
        elif pilihan_gas == "Uranium Heksafluorida (²³⁵UF₆ vs ²³⁸UF₆)":
            label_1, M1 = "²³⁵UF₆ Gas", 0.34903
            label_2, M2 = "²³⁸UF₆ Gas", 0.35204
        else:
            label_1, M1 = "Uap Air Biasa ($H_2O$)", 0.018015
            label_2, M2 = "Uap Air Berat ($D_2O$)", 0.020027

        if st.button("Hitung Rasio Kecepatan"):
            import math

            R = 8.314
            v1 = math.sqrt((3 * R * T_isotop) / M1)
            v2 = math.sqrt((3 * R * T_isotop) / M2)
            rasio = v1 / v2

            st.markdown(f"### 📊 Hasil Simulasi Presentasi ({fmt(T_isotop)} K):")

            with st.container(border=True):
                st.markdown(f"""
                * **{label_1}** ($M$ = {fmt(M1 * 1000)} g/mol) $\\rightarrow$ $v_{{rms}}$ = **{fmt(v1)} m/s**
                * **{label_2}** ($M$ = {fmt(M2 * 1000)} g/mol) $\\rightarrow$ $v_{{rms}}$ = **{fmt(v2)} m/s**

                ---

                📌 **Kesimpulan Analisis:** Senyawa gas ringan ({label_1}) berdifusi **{fmt(rasio)} kali lebih cepat** dibanding isotop beratnya. Perbedaan properti kinetik gas akibat fraksionasi isotop termodinamika ini diaplikasikan langsung pada teknologi pemisahan membran nuklir.
                """)
