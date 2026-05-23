import streamlit as st

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="ThermoVerse",
    page_icon="🌌",
    layout="wide"
)

# =====================================
# CSS FUTURISTIK FULL FIX
# =====================================
st.markdown("""
<style>

/* IMPORT FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

/* GLOBAL */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: white !important;
}

/* BACKGROUND */
.stApp {
    background: linear-gradient(-45deg,#020617,#071330,#0f172a,#1e3a8a,#172554);
    background-size: 500% 500%;
    animation: gradientBG 18s ease infinite;
    color:white;
}

/* ANIMASI BG */
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* GLOBAL TEXT */
p, label, div, span, h1, h2, h3, h4, h5, h6 {
    color:white !important;
}

/* TITLE */
.title {
    text-align:center;
    font-size:72px;
    font-weight:900;
    background: linear-gradient(to right,#93c5fd,#dbeafe,#60a5fa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(59,130,246,.8);
    animation: floatTitle 3s ease-in-out infinite;
}

/* FLOAT TITLE */
@keyframes floatTitle {
    0% {transform:translateY(0px);}
    50% {transform:translateY(-8px);}
    100% {transform:translateY(0px);}
}

/* SUBTITLE */
.subtitle {
    text-align:center;
    color:#e2e8f0 !important;
    font-size:20px;
    margin-bottom:35px;
}

/* RESULT CARD */
.result {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(20px);
    color:white;
    padding:30px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 8px 40px rgba(0,0,0,.35);
    animation: fadeIn 0.7s ease;
    margin-top:20px;
}

/* FADE ANIMATION */
@keyframes fadeIn {
    from {
        opacity:0;
        transform:translateY(20px);
    }
    to {
        opacity:1;
        transform:translateY(0);
    }
}

/* BUTTON */
.stButton>button {
    width:100%;
    padding:15px;
    border-radius:18px;
    font-weight:700;
    font-size:16px;
    border:none;
    color:white !important;
    background: linear-gradient(135deg,#2563eb,#38bdf8);
    box-shadow:0 0 18px rgba(56,189,248,.5);
    transition:all .3s ease;
}

.stButton>button:hover {
    transform:translateY(-6px) scale(1.02);
    box-shadow:0 0 30px rgba(56,189,248,.9);
}

/* INPUT NUMBER */
.stNumberInput input {
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
    border-radius:15px !important;
    border:1px solid rgba(255,255,255,0.2) !important;
    padding:10px !important;
}

/* TEXT INPUT */
.stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
    border-radius:15px !important;
    border:1px solid rgba(255,255,255,0.2) !important;
    padding:10px !important;
}

/* PLACEHOLDER */
input::placeholder {
    color:#cbd5e1 !important;
    opacity:1 !important;
}

/* LATEX */
.katex {
    color:#dbeafe !important;
    font-size:24px !important;
}

/* INFO BOX */
.stAlert {
    border-radius:18px !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
}

/* METRIC */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border-radius:18px;
    padding:15px;
}

/* SCROLLBAR */
::-webkit-scrollbar {
    width:10px;
}

::-webkit-scrollbar-track {
    background:#0f172a;
}

::-webkit-scrollbar-thumb {
    background:#3b82f6;
    border-radius:10px;
}

/* DIVIDER */
hr {
    border:1px solid rgba(255,255,255,0.15);
}

/* DATAFRAME */
[data-testid="stTable"] {
    background: rgba(255,255,255,0.05);
    border-radius:18px;
}

/* SELECTBOX */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
}

/* RADIO */
.stRadio label {
    color:white !important;
}

/* CHECKBOX */
.stCheckbox label {
    color:white !important;
}

/* SLIDER */
.stSlider label {
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SESSION
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = None

menu_list = [
    "Hukum 1 Termodinamika",
    "Usaha",
    "Kalor",
    "Entalpi",
    "Hukum Hess",
    "ΔH Reaksi",
    "Energi Gibbs",
    "Entropi",
    "Gas Ideal",
    "Gas Nyata"
]

# =====================================
# HOME
# =====================================
if st.session_state.menu is None:

    st.snow()

    st.markdown(
        "<div class='title'>🌌 ThermoVerse ⚗️</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Kalkulator Termodinamika Futuristik + Langkah Penyelesaian Interaktif</div>",
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for i, m in enumerate(menu_list):
        with cols[i % 2]:
            if st.button(f"⚡ {m}"):
                st.session_state.menu = m
                st.rerun()

# =====================================
# CALCULATOR PAGE
# =====================================
else:

    menu = st.session_state.menu

    if st.button("⬅️ Kembali"):
        st.session_state.menu = None
        st.rerun()

    st.header(f"⚗️ {menu}")
    st.divider()

    # =====================================
    # HUKUM 1 TERMODINAMIKA
    # =====================================
    if menu == "Hukum 1 Termodinamika":

        st.info("""
        Hukum 1 Termodinamika menyatakan bahwa energi tidak dapat diciptakan maupun dimusnahkan.
        """)

        st.latex(r"\Delta U = Q - W")

        Q = st.number_input("Q (kJ)", value=0.0)
        W = st.number_input("W (kJ)", value=0.0)

        if st.button("Hitung"):

            hasil = Q - W

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h2>✨ Langkah Penyelesaian</h2>

            <b>Rumus:</b><br>
            ΔU = Q − W<br><br>

            <b>Diketahui:</b><br>
            Q = {Q} kJ<br>
            W = {W} kJ<br><br>

            <b>Substitusi:</b><br>
            ΔU = {Q} − {W}<br><br>

            <b>Hasil:</b><br>
            ΔU = <b>{hasil:.3f} kJ</b>

            </div>
            """, unsafe_allow_html=True)
