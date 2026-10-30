import streamlit as st
import datetime
import swisseph as swe
from weasyprint import HTML
import base64

# ==========================================================
# PAGE CONFIG & BRAND THEME (THE AMOGH ASTRO)
# ==========================================================
st.set_page_config(
    page_title="The Amogh Astro • Vedic Muhurta Audit Engine",
    page_icon="🏛️",
    layout="wide"
)

# Custom CSS for Royal Navy Blue & Gold Theme
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        background: linear-gradient(135deg, #0b1d3a, #1a365d);
        color: #ffd700;
        font-weight: bold;
        border: 1.5px solid #c5a059;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1a365d, #0b1d3a);
        color: #ffffff;
        border-color: #ffd700;
        box-shadow: 0 4px 12px rgba(197, 160, 89, 0.4);
    }
    .header-box {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #0b1d3a, #17325c);
        border: 2px solid #c5a059;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .header-box h1 { color: #ffd700; margin: 0; font-size: 2.2rem; font-weight: 800; }
    .header-box p { color: #e2e8f0; margin-top: 5px; font-size: 1rem; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# MULTI-LINGUAL DATABASE & TRANSLATIONS
# ==========================================================
I18N = {
    "GU": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "ડેટા-ડ્રિવન ૧૦૦ ગુણ પારદર્શક વૈદિક મુહૂર્ત ઓડિટ રિપોર્ટ",
        "client": "જાતક",
        "gender": "જાતિ",
        "male": "પુરુષ",
        "female": "સ્ત્રી",
        "rashi": "ચંદ્ર રાશિ",
        "nak": "જન્મ નક્ષત્ર",
        "cat": "શ્રેણી",
        "event": "વિધાન",
        "range": "ગાળો",
        "summary_title": "📊 શ્રેષ્ઠ મુહૂર્તોનું સંક્ષિપ્ત ટેબલ (TOP 10 Ranked Windows)",
        "rank": "ક્રમ",
        "date": "તારીખ",
        "day": "વાર",
        "tithi": "તિથિ",
        "score": "સ્કોર",
        "verdict": "પરિણામ",
        "card_sub": "વૈદિક મુહૂર્ત સંપૂર્ણ ઓડિટ કાર્ડ",
        "panchang_title": "🪐 પંચાંગ તત્વો અને સમય નિર્ધારણ",
        "yoga": "નિત્યયોગ",
        "karan": "કરણ",
        "rahu_alert": "<b>⛔ અશુભ રાહુકાળ વિન્ડો:</b> {rahu} (આ સમય દરમિયાન કાર્ય વર્જ્ય રાખવું)",
        "audit_title": "⚖️ ૧૦૦ ગુણનું શાસ્ત્રોક્ત ઓડિટ ગણિત (Detailed 8 Parameters)",
        "guide_title": "💡 એક્ઝિક્યુટિવ નિર્ણય અને પરા
