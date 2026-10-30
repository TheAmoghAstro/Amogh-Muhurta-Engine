import streamlit as st
import datetime
import swisseph as swe
from weasyprint import HTML
import base64

st.set_page_config(page_title="The Amogh Astro • Vedic Muhurta Audit Engine", page_icon="🏛️", layout="wide")

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
        "guide_title": "💡 એક્ઝિક્યુટિવ નિર્ણય અને પરામર્શ માર્ગદર્શન:",
        "guide_top": "આ મુહૂર્ત અત્યંત શુભ અને પ્રશસ્ત છે.",
        "guide_mod": "રાહુકાળ બાદ કરીને કાર્ય કરવું હિતાવહ છે.",
        "disclaimer_title": "⚠️ વૈધાનિક ચેતવણી અને પરામર્શ નોંધ (Statutory Disclaimer):",
        "disclaimer_text": "આ મુહૂર્ત રિપોર્ટ પ્રાચીન ભારતીય વૈદિક જ્યોતિષ સિદ્ધાંતો, સ્વિત્ઝ એફેમેરિસ (Swiss Ephemeris / Lahiri Ayanamsa) ના ખગોળીય ગણિત અને આપ દ્વારા પૂરી પાડવામાં આવેલી જન્મ વિગતો પર આધારિત છે. આ રિપોર્ટ નિર્ણય લેવામાં સહાયક ટાઈમિંગ ગાઇડન્સ માટે છે અને કોઈ વ્યવસાયિક કે નાણાકીય પરિણામોની સંપૂર્ણ બાંયધરી આપતો નથી. કોઈપણ મોટો વ્યવહારિક કે કાનૂની નિર્ણય લેતા પહેલાં સંબંધિત અધિકૃત નિષ્ણાતોની સલાહ લેવી હિતાવહ છે.",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Noto Sans Gujarati', 'DejaVu Sans', sans-serif",
        "wmap": ["સોમવાર", "મંગળવાર", "બુધવાર", "ગુરુવાર", "શુક્રવાર", "શનિવાર", "રવિવાર"],
        "shubh": "શુભ",
        "madhyam": "મધ્યમ",
        "varjya": "વર્જ્ય",
        "sud": "સુદ",
        "vad": "વદ",
        "p1_c": "૧. ચંદ્રબળ (૧૫)",
        "p2_t": "૨. તારાબળ (૧૫)",
        "p3_ti": "૩. તિથિ (૧૦)",
        "p4_n": "૪. નક્ષત્ર (૧૦)",
        "p5_y": "૫. નિત્યયોગ (૧૦)",
        "p6_k": "૬. કરણ (૧૦)",
        "p7_v": "૭. વાર (૧૦)",
        "p8_s": "૮. વિશેષ યોગ અને ઘાત ચક્ર (૨૦)",
        "ghat_err": "ઘાત ચક્ર દોષ ઉપસ્થિત",
        "pts": "ગુણ"
    },
    "HI": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "डेटा-संचालित १०० अंक पारदर्शी वैदिक मुहूर्त ऑडिट रिपोर्ट",
        "client": "जातक",
        "gender": "लिंग",
        "male": "पुरुष",
        "female": "महिला",
        "rashi": "चंद्र राशि",
        "nak": "जन्म नक्षत्र",
        "cat": "श्रेणी",
        "event": "विधान",
        "range": "अवधि",
        "summary_title": "📊 सर्वश्रेष्ठ मुहूर्तों की संक्षिप्त तालिका (TOP 10 Ranked Windows)",
        "rank": "क्रमांक",
        "date": "दिनांक",
        "day": "वार",
        "tithi": "तिथि",
        "score": "स्कोर",
        "verdict": "परिणाम",
        "card_sub": "वैदिक मुहूर्त सम्पूर्ण ऑडिट कार्ड",
        "panchang_title": "🪐 पंचांग तत्व एवं समय निर्धारण",
        "yoga": "नित्ययोग",
        "karan": "करण",
        "rahu_alert": "<b>⛔ अशुभ राहुकाल विंडो:</b> {rahu} (इस समय के दौरान कार्य वर्जित रखें)",
        "audit_title": "⚖️ १०० अंकों का शास्त्रीय ऑडिट गणित (Detailed 8 Parameters)",
        "guide_title": "💡 कार्यकारी निर्णय एवं परामर्श मार्गदर्शन:",
        "guide_top": "यह मुहूर्त अत्यंत शुभ और प्रशस्त है।",
        "guide_mod": "राहुकाल का त्याग करके कार्य करना हितकर है।",
        "disclaimer_title": "⚠️ वैधानिक चेतावनी एवं परामर्श नोट (Statutory Disclaimer):",
        "disclaimer_text": "यह मुहूर्त रिपोर्ट प्राचीन भारतीय वैदिक ज्योतिष सिद्धांतों, स्विस एफिमेरिस (Swiss Ephemeris / Lahiri Ayanamsa) के खगोलीय गणित और आपके द्वारा प्रदान किए गए जन्म विवरणों पर आधारित है। यह रिपोर्ट निर्णय लेने में समय मार्गदर्शन हेतु है और किसी व्यावसायिक या वित्तीय परिणाम की पूर्ण गारंटी नहीं देती। कोई भी बड़ा व्यावहारिक या कानूनी निर्णय लेने से पहले संबंधित अधिकृत विशेषज्ञों की सलाह लेना हितकर है।",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Noto Sans Devanagari', 'DejaVu Sans', sans-serif",
        "wmap": ["सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार", "रविवार"],
        "shubh": "शुभ",
        "madhyam": "मध्यम",
        "varjya": "वर्ज्य",
        "sud": "शुक्ल",
        "vad": "कृष्ण",
        "p1_c": "१. चंद्रबल (१५)",
        "p2_t": "२. ताराबल (१५)",
        "p3_ti": "३. तिथि (१०)",
        "p4_n": "૪. नक्षत्र (१०)",
        "p5_y": "५. नित्ययोग (१०)",
        "p6_k": "६. करण (१०)",
        "p7_v": "७. वार (१०)",
        "p8_s": "૮. विशेष योग एवं घात चक्र (२०)",
        "ghat_err": "घात चक्र दोष उपस्थित",
        "pts": "अंक"
    },
    "EN": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "DATA-DRIVEN 100-POINT TRANSPARENT MUHURTA AUDIT REPORT",
        "client": "Client",
        "gender": "Gender",
        "male": "Male",
        "female": "Female",
        "rashi": "Moon Sign",
        "nak": "Birth Nakshatra",
        "cat": "Category",
        "event": "Event",
        "range": "Period",
        "summary_title": "📊 TOP 10 RANKED MUHURTA WINDOWS",
        "rank": "Rank",
        "date": "Date",
        "day": "Day",
        "tithi": "Tithi",
        "score": "Score",
        "verdict": "Verdict",
        "card_sub": "Bespoke Vedic Muhurta Audit Card",
        "panchang_title": "🪐 Panchang Elements & Timing Windows",
        "yoga": "Yoga",
        "karan": "Karana",
        "rahu_alert": "<b>⛔ Inauspicious Rahu Kaal:</b> {rahu} (Avoid starting critical activities)",
        "audit_title": "⚖️ 100-Point Classical Vedic Audit (Detailed 8 Parameters)",
        "guide_title": "💡 Executive Guidance & Astro Verdict:",
        "guide_top": "Highly auspicious and ideal for successful initiation.",
        "guide_mod": "Recommended window after excluding Rahu Kaal.",
        "disclaimer_title": "⚠️ Statutory Disclaimer:",
        "disclaimer_text": "This audit is calculated using high-precision Swiss Ephemeris (Lahiri Ayanamsa) and classical Vedic Jyotish principles based on user-provided birth details. Provided strictly for strategic timing guidance without legal or commercial liability. Independent verification with qualified experts is advised for major commitments.",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Liberation Sans', Arial, sans-serif",
        "wmap": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "shubh": "Auspicious",
        "madhyam": "Moderate",
        "varjya": "Inauspicious",
        "sud": "Shukla",
        "vad": "Krishna",
        "p1_c": "1. Moon Strength (15)",
        "p2_t": "2. Tara Strength (15)",
        "p3_ti": "3. Tithi (10)",
        "p4_n": "4. Nakshatra (10)",
        "p5_y": "5. Nitya Yoga (10)",
        "p6_k": "6. Karana (10)",
        "p7_v": "7. Weekday (10)",
        "p8_s": "8. Special Yoga & Ghat Chakra (20)",
        "ghat_err": "Ghat Chakra Inauspicious",
        "pts": "Pts"
    }
}

NAK_DICT = {
    "GU": ["અશ્વિની","ભરણી","કૃતિકા","રોહિણી","મૃગશીર્ષ","આર્દ્રા","પુનર્વસુ","પુષ્ય","આશ્લેષા","મઘા","પૂ. ફાલ્ગુની","ઉ. ફાલ્ગુની","હસ્ત","ચિત્રા","સ્વાતિ","વિશાખા","અનુરાધા","જ્યેષ્ઠા","મૂળ","પૂ. ષાઢા","ઉ. ષાઢા","શ્રવણ","ધનિષ્ઠા","શતભિષા","પૂ. ભાદ્રપદ","ઉ. ભાદ્રપદ","રેવતી"],
    "HI": ["अश्विनी","भरणी","कृत्तिका","रोहिणी","मृगशिरा","आर्द्रा","पुनर्वसु","पुष्य","आश्लेषा","मघा","पूर्वाफाल्गुनी","उत्तराफाल्गुनी","हस्त","चित्रा","स्वाति","विशाखा","अनुराधा","ज्येष्ठा","मूल","पूर्वाषाढ़ा","उत्तराषाढ़ा","श्रवण","धनिष्ठा","शतभिषा","पूर्वाभाद्रपद","उत्तराभाद्रपद","रेवती"],
    "EN": ["Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra","Punarvasu","Pushya","Ashlesha","Magha","P. Phalguni","U. Phalguni","Hasta","Chitra","Swati","Vishakha","Anuradha","Jyeshtha","Mula","P. Ashadha","U. Ashadha","Shravana","Dhanishta","Shatabhisha","P. Bhadrapada","U. Bhadrapada","Revati"]
}

RAS_DICT = {
    "GU": ["મેષ","વૃષભ","મિથુન","કર્ક","સિંહ","કન્યા","તુલા","વૃશ્ચિક","ધન","મકર","કુંભ","મીન"],
    "HI": ["मेष","वृषभ","मिथुन","कर्क","सिंह","कन्या","तुला","वृश्चिक","धनु","मकर","कुंभ","मीन"],
    "EN": ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
}

YOG_DICT = {
    "GU": ["વિષ્કંભ","પ્રીતિ","આયુષ્માન","સૌભાગ્ય","શોભન","અતિગંડ","સુકર્મા","ધૃતિ","શૂળ","ગંડ","વૃદ્ધિ","ધ્રુવ","વ્યાઘાત","હર્ષણ","વજ્ર","સિદ્ધિ","વ્યતીપાત","વરીયાન","પરિઘ","શિવ","સિદ્ધ","સાધ્ય","શુભ","શુક્લ","બ્રહ્મ","ઇન્દ્ર","વૈધૃતિ"],
    "HI": ["विष्कुम्भ","प्रीति","आयुष्मान","सौभाग्य","शोभन","अतिगण्ड","सुकर्मा","धृति","शूल","गण्ड","वृद्धि","ध्रुव","व्याघात","हर्षण","वज्र","सिद्धि","व्यतीपात","वरीयान","परिघ","शिव","सिद्ध","साध्य","शुभ","शुक्ल","ब्रह्म","इन्द्र","वैधृति"],
    "EN": ["Vishkumbha","Priti","Ayushman","Saubhagya","Shobhana","Atiganda","Sukarma","Dhriti","Shula","Ganda","Vriddhi","Dhruva","Vyaghata","Harshana","Vajra","Siddhi","Vyatipata","Variyana","Parigha","Shiva","Siddha","Sadhya","Shubha","Shukla","Brahma","Indra","Vaidhriti"]
}

KAR_DICT = {
    "GU": ["બવ","બાલવ","કૌલવ","તૈતિલ","ગર","વણિજ","વિષ્ટિ","શકુનિ","ચતુષ્પદ","નાગ","કિસ્તુઘ્ન"],
    "HI": ["बव","बालव","कौलव","तैतिल","गर","वणिज","विष्टि","शकुनि","चतुष्पद","नाग","किस्तुघ्न"],
    "EN": ["Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Shakuni","Chatushpada","Naga","Kinstughna"]
}

TARA_DICT = {
