import streamlit as st
import datetime
import swisseph as swe
from weasyprint import HTML

st.set_page_config(page_title="The Amogh Astro • Vedic Muhurta Audit Engine", page_icon="🏛️", layout="wide")

MASTER_ACCESS_PIN = "amogh1611"

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
        "tagline": "શાસ્ત્રોક્ત ૪૨ વિધાન ૧૦૦ ગુણ વૈદિક મુહૂર્ત ઓડિટ પ્રણાલી",
        "client": "જાતક", "gender": "જાતિ", "male": "પુરુષ", "female": "સ્ત્રી",
        "bplace": "જન્મ સ્થળ", "rashi": "ચંદ્ર રાશિ", "nak": "જન્મ નક્ષત્ર", "cat": "શ્રેણી",
        "event": "વિધાન", "range": "સમયગાળો", "summary_title": "📊 શ્રેષ્ઠ મુહૂર્તોનું સંક્ષિપ્ત વિશ્લેષણ ટેબલ",
        "rank": "ક્રમ", "date": "તારીખ", "day": "વાર", "tithi": "તિથિ", "score": "સ્કોર", "verdict": "પરિણામ",
        "card_sub": "વૈદિક મુહૂર્ત સંપૂર્ણ ઓડિટ કાર્ડ", "panchang_title": "🪐 પંચાંગ તત્વો અને સમય નિર્ધારણ",
        "yoga": "નિત્યયોગ", "karan": "કરણ",
        "rahu_alert": "<b>⛔ અશુભ રાહુકાળ વિન્ડો:</b> {rahu} (આ સમય દરમિયાન કાર્ય વર્જ્ય રાખવું)",
        "audit_title": "⚖️ ૧૦૦ ગુણનું શાસ્ત્રોક્ત ઓડિટ ગણિત (Detailed Parameters)",
        "guide_title": "💡 એક્ઝિક્યુટિવ નિર્ણય અને પરામર્શ માર્ગદર્શન:",
        "guide_top": "આ મુહૂર્ત અત્યંત શુભ, દોષમુક્ત અને કાર્યસિદ્ધિ આપનાર છે.",
        "guide_mod": "રાહુકાળ અને અશુભ ચોઘડિયાં ત્યાગીને કાર્ય કરવું હિતાવહ છે.",
        "disclaimer_title": "⚠️ વૈધાનિક ચેતવણી અને પરામર્શ નોંધ (Statutory Disclaimer):",
        "disclaimer_text": "આ મુહૂર્ત રિપોર્ટ પ્રાચીન ભારતીય વૈદિક જ્યોતિષ સિદ્ધાંતો, સ્વિત્ઝ એફેમેરિસ (Swiss Ephemeris / Lahiri Ayanamsa) ના ખગોળીય ગણિત અને આપ દ્વારા પૂરી પાડવામાં આવેલી જન્મ વિગતો પર આધારિત છે. આ રિપોર્ટ નિર્ણય લેવામાં સહાયક ટાઈમિંગ ગાઇડન્સ માટે છે અને કોઈ વ્યવસાયિક કે નાણાકીય પરિણામોની સંપૂર્ણ બાંયધરી આપતો નથી. કોઈપણ મોટો વ્યવહારિક કે કાનૂની નિર્ણય લેતા પહેલાં સંબંધિત અધિકૃત નિષ્ણાતોની સલાહ લેવી હિતાવહ છે.",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Noto Sans Gujarati', 'DejaVu Sans', sans-serif",
        "wmap": ["સોમવાર", "મંગળવાર", "બુધવાર", "ગુરુવાર", "શુક્રવાર", "શનિવાર", "રવિવાર"],
        "shubh": "શુભ", "madhyam": "મધ્યમ", "varjya": "વર્જ્ય", "sud": "સુદ", "vad": "વદ",
        "p1_c": "૧. ચંદ્રબળ (૧૫)", "p2_t": "૨. તારાબળ (૧૫)", "p3_ti": "૩. તિથિ શુદ્ધિ (૧૦)",
        "p4_n": "૪. નક્ષત્ર અનુકૂળતા (૧૦)", "p5_y": "૫. નિત્યયોગ શુદ્ધિ (૧૦)", "p6_k": "૬. કરણ શુદ્ધિ (૧૦)",
        "p7_v": "૭. વાર બળ (૧૦)", "p8_s": "૮. શાસ્ત્રોક્ત યોગ અને ઘાત ચક્ર (૨૦)",
        "ghat_err": "ઘાત ચક્ર દોષ ઉપસ્થિત", "pts": "ગુણ"
    },
    "HI": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "शास्त्रीय ४२ विधान १०० अंक वैदिक मुहूर्त ऑडिट प्रणाली",
        "client": "जातक", "gender": "लिंग", "male": "पुरुष", "female": "महिला",
        "bplace": "जन्म स्थान", "rashi": "चंद्र राशि", "nak": "जन्म नक्षत्र", "cat": "श्रेणी",
        "event": "विधान", "range": "अवधि", "summary_title": "📊 सर्वश्रेष्ठ मुहूर्तों की संक्षिप्त तालिका",
        "rank": "क्रमांक", "date": "दिनांक", "day": "वार", "tithi": "तिथि", "score": "स्कोर", "verdict": "परिणाम",
        "card_sub": "वैदिक मुहूर्त सम्पूर्ण ऑडिट कार्ड", "panchang_title": "🪐 पंचांग तत्व एवं समय निर्धारण",
        "yoga": "नित्ययोग", "karan": "करण",
        "rahu_alert": "<b>⛔ अशुभ राहुकाल विंडो:</b> {rahu} (इस समय के दौरान कार्य वर्जित रखें)",
        "audit_title": "⚖️ १०० अंकों का शास्त्रीय ऑडिट गणित (Detailed Parameters)",
        "guide_title": "💡 कार्यकारी निर्णय एवं परामर्श मार्गदर्शन:",
        "guide_top": "यह मुहूर्त अत्यंत शुभ, दोषमुक्त एवं कार्यसिद्धि प्रदायक है।",
        "guide_mod": "राहुकाल का त्याग करके कार्य करना हितकर है।",
        "disclaimer_title": "⚠️ वैधानिक चेतावनी एवं परामर्श नोट (Statutory Disclaimer):",
        "disclaimer_text": "यह मुहूर्त रिपोर्ट प्राचीन भारतीय वैदिक ज्योतिष सिद्धांतों, स्विस एफिमेरिस (Swiss Ephemeris / Lahiri Ayanamsa) के खगोलीय गणित और आपके द्वारा प्रदान किए गए जन्म विवरणों पर आधारित है। यह रिपोर्ट निर्णय लेने में समय मार्गदर्शन हेतु है और किसी व्यावसायिक या वित्तीय परिणाम की पूर्ण गारंटी नहीं देती। कोई भी बड़ा व्यावहारिक या कानूनी निर्णय लेने से पहले संबंधित अधिकृत विशेषज्ञों की सलाह लेना हितकर है।",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Noto Sans Devanagari', 'DejaVu Sans', sans-serif",
        "wmap": ["सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार", "रविवार"],
        "shubh": "शुभ", "madhyam": "मध्यम", "varjya": "वर्ज्य", "sud": "शुक्ल", "vad": "कृष्ण",
        "p1_c": "१. चंद्रबल (१५)", "p2_t": "२. ताराबल (१५)", "p3_ti": "३. तिथि शुद्धि (१०)",
        "p4_n": "४. नक्षत्र अनुकूलता (१०)", "p5_y": "५. नित्ययोग शुद्धि (१०)", "p6_k": "६. करण शुद्धि (१०)",
        "p7_v": "७. वार बल (१०)", "p8_s": "૮. शास्त्रीय योग एवं घात चक्र (२०)",
        "ghat_err": "घात चक्र दोष उपस्थित", "pts": "अंक"
    },
    "EN": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "CLASSICAL 42-EVENT 100-POINT VEDIC MUHURTA AUDIT SYSTEM",
        "client": "Client", "gender": "Gender", "male": "Male", "female": "Female",
        "bplace": "Birth Place", "rashi": "Moon Sign", "nak": "Birth Nakshatra", "cat": "Category",
        "event": "Event", "range": "Period", "summary_title": "📊 TOP RANKED MUHURTA WINDOWS",
        "rank": "Rank", "date": "Date", "day": "Day", "tithi": "Tithi", "score": "Score", "verdict": "Verdict",
        "card_sub": "Bespoke Vedic Muhurta Audit Card", "panchang_title": "🪐 Panchang Elements & Timing Windows",
        "yoga": "Yoga", "karan": "Karana",
        "rahu_alert": "<b>⛔ Inauspicious Rahu Kaal:</b> {rahu} (Avoid starting critical activities)",
        "audit_title": "⚖️ 100-Point Classical Vedic Audit (Detailed Parameters)",
        "guide_title": "💡 Executive Guidance & Astro Verdict:",
        "guide_top": "Highly auspicious, defect-free window ideal for prosperous results.",
        "guide_mod": "Recommended window after excluding Rahu Kaal.",
        "disclaimer_title": "⚠️ Statutory Disclaimer:",
        "disclaimer_text": "This audit is calculated using high-precision Swiss Ephemeris (Lahiri Ayanamsa) and classical Vedic Jyotish principles based on user-provided birth details. Provided strictly for strategic timing guidance without legal or commercial liability. Independent verification with qualified experts is advised for major commitments.",
        "footer_conf": "Strictly Confidential",
        "font_family": "'Liberation Sans', Arial, sans-serif",
        "wmap": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "shubh": "Auspicious", "madhyam": "Moderate", "varjya": "Inauspicious", "sud": "Shukla", "vad": "Krishna",
        "p1_c": "1. Moon Strength (15)", "p2_t": "2. Tara Strength (15)", "p3_ti": "3. Tithi Purity (10)",
        "p4_n": "4. Nakshatra Power (10)", "p5_y": "5. Nitya Yoga (10)", "p6_k": "6. Karana Purity (10)",
        "p7_v": "7. Day Strength (10)", "p8_s": "8. Special Yoga & Ghat Chakra (20)",
        "ghat_err": "Ghat Chakra Defect", "pts": "Pts"
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
    "GU": ["જન્મ","સંપત","વિપત","ક્ષેમ","પ્રત્યરી","સાધક","વધ","મિત્ર","અતિ-મિત્ર"],
    "HI": ["जन्म","सम्पत","विपत","क्षेम","प्रत्यरी","साधक","वध","मित्र","अति-मित्र"],
    "EN": ["Janma","Sampat","Vipat","Kshema","Pratyari","Sadhaka","Vadha","Mitra","Ati-Mitra"]
}

WINT = ["Som", "Mangal", "Budh", "Guru", "Shukra", "Shani", "Ravi"]

# શાસ્ત્રોક્ત સંપૂર્ણ ઘાત ચક્ર (કોષ્ટક મુજબ)
GHAT_DATA = {
    0: {"var": "Ravi", "tith": [1, 6, 11], "nak": 9, "c_m": 1, "c_f": 1},
    1: {"var": "Shani", "tith": [1, 10, 15], "nak": 12, "c_m": 5, "c_f": 8},
    2: {"var": "Som", "tith": [2, 7, 12], "nak": 14, "c_m": 9, "c_f": 7},
    3: {"var": "Budh", "tith": [2, 7, 12], "nak": 16, "c_m": 2, "c_f": 9},
    4: {"var": "Shani", "tith": [3, 8, 13], "nak": 18, "c_m": 6, "c_f": 4},
    5: {"var": "Shani", "tith": [5, 10, 15], "nak": 21, "c_m": 10, "c_f": 3},
    6: {"var": "Guru", "tith": [4, 9, 14], "nak": 23, "c_m": 3, "c_f": 6},
    7: {"var": "Shukra", "tith": [1, 6, 11], "nak": 26, "c_m": 7, "c_f": 2},
    8: {"var": "Shukra", "tith": [3, 8, 13], "nak": 1, "c_m": 4, "c_f": 10},
    9: {"var": "Mangal", "tith": [4, 9, 14], "nak": 3, "c_m": 8, "c_f": 11},
    10: {"var": "Guru", "tith": [3, 8, 11], "nak": 5, "c_m": 11, "c_f": 5},
    11: {"var": "Shukra", "tith": [5, 10, 15], "nak": 8, "c_m": 12, "c_f": 12}
}

# ૪૨ વિધાનોનું સંપૂર્ણ શાસ્ત્રોક્ત માસ્ટર લિસ્ટ
MASTER_EVENTS = {
    # ૧૬ સંસ્કાર
    "EV_01": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૧. ગર્ભાધાન સંસ્કાર", "nak": [11, 20, 25, 4, 12, 16, 3, 14, 21, 22, 23, 13, 6, 7, 0], "tith": [1, 2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani", "Ravi"]},
    "EV_02": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૨. પુંસવન સંસ્કાર", "nak": [0, 4, 6, 7, 12, 14, 16, 18, 19, 20, 21, 24, 25], "tith": [5, 7, 10, 11, 13], "sh_var": ["Ravi", "Mangal", "Guru"], "v_var": ["Shani"]},
    "EV_03": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૩. અનવલોભન સંસ્કાર", "nak": [0, 4, 6, 7, 12, 14, 16, 18, 19, 20, 21, 24, 25], "tith": [5, 7, 10, 11, 13], "sh_var": ["Ravi", "Mangal", "Guru"], "v_var": ["Shani"]},
    "EV_04": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૪. સીમંતોન્નયન (ખોળો ભરવો)", "nak": [4, 6, 7, 11, 12, 18, 20, 21, 25, 26], "tith": [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13], "sh_var": ["Ravi", "Mangal", "Guru"], "v_var": ["Shani"]},
    "EV_05": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૫. જાતકર્મ સંસ્કાર", "nak": [11, 20, 25, 3, 12, 0, 7, 16, 26, 4, 13, 21, 22, 23, 14, 6], "tith": [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_06": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૬. નામકરણ સંસ્કાર", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_07": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૭. કર્ણવેધ (કાન વિંધવા)", "nak": [0, 4, 6, 7, 11, 20, 25, 12, 13, 21, 22, 26], "tith": [2, 3, 5, 6, 7, 10, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_08": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૮. નિષ્ક્રમણ સંસ્કાર", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 21, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_09": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૦૯. અન્નપ્રાશન સંસ્કાર", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 13, 15], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_10": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૧૦. ચૌલકર્મ (મુંડન સંસ્કાર)", "nak": [0, 4, 6, 7, 12, 13, 14, 17, 21, 22, 23, 26, 3, 11, 20, 25], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_11": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૧૧. ઉપનયન (જનોઈ સંસ્કાર)", "nak": [0, 3, 4, 7, 11, 20, 25, 6, 12, 13, 14, 16, 21, 22, 23, 26], "tith": [2, 3, 5, 6, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_12": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૧૨. વિદ્યારંભ સંસ્કાર", "nak": [0, 4, 5, 6, 7, 8, 10, 19, 24, 21, 12, 13, 14, 22, 23], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Ravi", "Guru", "Shukra", "Budh"], "v_var": ["Mangal", "Shani"]},
    "EV_13": {"cat": "૧૬ વૈદિક સંસ્કાર", "name": "૧૩. વિવાહ (લગ્ન) સંસ્કાર", "nak": [3, 4, 9, 11, 12, 14, 16, 18, 20, 25, 26], "tith": [2, 3, 5, 7, 10, 13], "sh_var": ["Som", "Guru", "Shukra"], "v_var": ["Ravi", "Mangal", "Shani"]},
    
    # બાલ્ય સંસ્કાર અને અન્ય દૈનિક
    "EV_14": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૧૪. બાળકને પ્રથમવાર ઘર બહાર લઈ જવું", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 21, 25, 26], "tith": [1, 2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_15": {"cat": "શિક્ષણ & પ્રારંભ", "name": "૧૫. શાળા / વિદ્યાલયમાં પ્રવેશ મુહૂર્ત", "nak": [0, 4, 5, 6, 7, 8, 10, 19, 24, 12, 13, 14, 18, 16, 21, 22, 23, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_16": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૧૬. બાળકને પારણે ઝુલાવવાનું મુહૂર્ત", "nak": [0, 4, 6, 12, 13, 14, 16, 17, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_17": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૧૭. ગર્ભવતી સ્ત્રીને પ્રસૂતિ મોકલવી", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 20, 22, 23, 25, 26], "tith": [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_18": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૧૮. પ્રસૂતાને બાળ સાથે ઘરે લાવવું", "nak": [0, 3, 4, 11, 12, 13, 14, 16, 20, 21, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_19": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૧૯. સુવાવડી સ્ત્રીને શુદ્ધિ સ્નાન મુહૂર્ત", "nak": [0, 3, 4, 11, 12, 14, 16, 20, 25, 26], "tith": [1, 2, 3, 5, 7, 10, 11, 15], "sh_var": ["Ravi", "Mangal", "Guru"], "v_var": ["Shani"]},
    "EV_20": {"cat": "બાળ સંસ્કાર & પરિવાર", "name": "૨૦. સૂર્ય - ચંદ્ર દર્શન પૂજન મુહૂર્ત", "nak": [0, 3, 4, 6, 7, 11, 12, 14, 16, 21, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    
    # વાસ્તુ અને સ્થાવર મિલકત
    "EV_21": {"cat": "વાસ્તુ & સ્થાવર મિલકત", "name": "૨૧. નૂતન ગૃહ પ્રવેશ / વાસ્તુ શાંતિ", "nak": [3, 4, 7, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Ravi"]},
    "EV_22": {"cat": "વાસ્તુ & સ્થાવર મિલકત", "name": "૨૨. કુંભ મુકવાનું મુહૂર્ત", "nak": [3, 4, 6, 7, 9, 11, 12, 16, 19, 20, 22, 23, 25], "tith": [1, 3, 5, 6, 8, 10, 11, 13, 15], "sh_var": ["Som", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_23": {"cat": "વાસ્તુ & સ્થાવર મિલકત", "name": "૨૩. ખાત મુહૂર્ત (પાયો ખોદવો)", "nak": [1, 2, 8, 9, 10, 15, 18, 19, 24, 0, 3, 4, 7, 11, 12, 16, 20, 21, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Ravi"]},
    "EV_24": {"cat": "વાણિજ્ય & વ્યવહાર", "name": "૨૪. નાણાકીય લેવડ-દેવડ / રોકાણ મુહૂર્ત", "nak": [0, 4, 6, 7, 13, 14, 15, 16, 21, 22, 23, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Ravi", "Shani"]},
    "EV_25": {"cat": "વેપાર & મુસાફરી", "name": "૨૫. દરિયાઈ સફર / નૌકા નિર્માણ મુહૂર્ત", "nak": [0, 4, 6, 7, 10, 12, 13, 16, 19, 21, 22, 24, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Ravi", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_26": {"cat": "ઉદ્યોગ & ટેકનોલોજી", "name": "૨૬. મશીનરી / પ્લાન્ટ શરૂ કરવાનું મુહૂર્ત", "nak": [0, 6, 7, 12, 13, 16, 17, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_27": {"cat": "ધાર્મિક & સંન્યાસ", "name": "૨૭. દીક્ષા / ગુરુમંત્ર સ્વીકાર મુહૂર્ત", "nak": [0, 3, 6, 7, 11, 20, 25, 12, 14, 16, 18, 21, 23, 24, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Ravi", "Budh", "Guru", "Shani"], "v_var": ["Mangal"]},
    "EV_28": {"cat": "વાણિજ્ય & કાનૂની", "name": "૨૮. કરાર / એગ્રીમેન્ટ સાઇન મુહૂર્ત", "nak": [0, 3, 4, 7, 11, 12, 13, 16, 20, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_29": {"cat": "વેપાર & પ્રતિષ્ઠાન", "name": "૨૯. નવી દુકાન / શૉરૂમ ઉદ્ઘાટન મુહૂર્ત", "nak": [3, 4, 7, 12, 13, 14, 16, 11], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_30": {"cat": "વેપાર & પ્રતિષ્ઠાન", "name": "૩૦. નવો વેપાર / કંપની શુભારંભ મુહૂર્ત", "nak": [0, 3, 4, 6, 7, 11, 12, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_31": {"cat": "વેપાર & સંગ્રહ", "name": "૩૧. માલની મોટી ખરીદી કરવાનું મુહૂર્ત", "nak": [0, 13, 14, 21, 23, 26], "tith": [2, 3, 5, 7, 10, 11, 13, 15], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_32": {"cat": "વેપાર & સંગ્રહ", "name": "૩૨. માલ વેચાણ / સ્ટોક રિલીઝ મુહૂર્ત", "nak": [1, 2, 8, 15], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_33": {"cat": "કારકિર્દી & નોકરી", "name": "૩૩. નવી નોકરી / જોબ જોઈનિંગ મુહૂર્ત", "nak": [3, 11, 20, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 12, 13], "sh_var": ["Ravi", "Budh", "Guru", "Shukra"], "v_var": ["Shani", "Mangal"]},
    "EV_34": {"cat": "કૃષિ & બાગાયત", "name": "૩૪. બીજ વાવવાનું શુભ મુહૂર્ત", "nak": [0, 3, 4, 6, 7, 9, 11, 12, 13, 14, 16, 18, 22, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_35": {"cat": "કૃષિ & બાગાયત", "name": "૩૫. અનાજ કાપણી (હાર્વેસ્ટિંગ) મુહૂર્ત", "nak": [1, 2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25], "tith": [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_36": {"cat": "કૃષિ & બાગાયત", "name": "૩૬. અનાજના કણ છૂટા પાડવાનું મુહૂર્ત", "nak": [3, 9, 10, 11, 16, 17, 18, 21, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_37": {"cat": "કૃષિ & બાગાયત", "name": "૩૭. અનાજ ઘેર લાવવાનું મુહૂર્ત", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_38": {"cat": "વાસ્તુ & સ્થાવર મિલકત", "name": "૩૮. ઘર, ખેતર કે જમીન લે-વેચ મુહૂર્ત", "nak": [4, 6, 8, 9, 10, 15, 16, 18, 19, 25], "tith": [1, 5, 6, 10, 11, 15], "sh_var": ["Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_39": {"cat": "કૃષિ & સંગ્રહ", "name": "૩૯. કોઠારમાં ધાન્ય ભરવાનું મુહૂર્ત", "nak": [0, 3, 4, 6, 7, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Ravi", "Som", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_40": {"cat": "કૃષિ & વેચાણ", "name": "૪૦. અનાજ વેચવાનું શુભ મુહૂર્ત", "nak": [3, 22, 23], "tith": [2, 3, 5, 7, 10, 11, 13], "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Shani"]},
    "EV_41": {"cat": "વાસ્તુ & સ્થાવર મિલકત", "name": "૪૧. જમીન કે પ્લોટ ખરીદવાનું મુહૂર્ત", "nak": [4, 6, 8, 9, 10, 15, 16, 18, 19, 25], "tith": [1, 5, 6, 10, 11, 15], "sh_var": ["Guru", "Shukra"], "v_var": ["Mangal", "Shani"]},
    "EV_42": {"cat": "આરોગ્ય & ચિકિત્સા", "name": "૪૨. ઓપરેશન / શસ્ત્રક્રિયા મુહૂર્ત", "nak": [4, 7, 18, 21, 6, 12, 11, 20, 25, 26], "tith": [2, 3, 5, 6, 7, 8, 10, 11, 12, 13], "sh_var": ["Ravi", "Mangal", "Guru"], "v_var": ["Shani"]}
}

with st.sidebar:
    st.image("https://img.icons8.com/color/96/om.png", width=70)
    st.subheader("🔐 Security & Settings")
    entered_pin = st.text_input("Enter Access PIN to Unlock:", type="password", placeholder="Enter PIN")
    st.markdown("---")
    lang_choice = st.selectbox("🌐 Report Language / ભાષા પસંદ કરો:", ["GU", "HI", "EN"], index=0,
                               format_func=lambda x: "ગુજરાતી (Gujarati)" if x=="GU" else ("हिन्दी (Hindi)" if x=="HI" else "English"))
    L = I18N[lang_choice]
    st.markdown("---")
    top_n_choice = st.radio("📑 કેટલા શ્રેષ્ઠ મુહૂર્તો રિપોર્ટમાં જોઈએ?", [10, 5], index=0,
                            format_func=lambda x: f"Top {x} Windows ({'11 Pages' if x==10 else '6 Pages'} Luxury PDF)")
    st.markdown("---")
    st.caption("**The Amogh Astro Consultancy**\nAhmedabad, Gujarat\ntheamoghastro@gmail.com")

st.markdown("""
<div class="header-box">
    <h1>🏛️ ધ અમોઘ એસ્ટ્રો • THE AMOGH ASTRO</h1>
    <p>CLASSICAL 42-EVENT 100-POINT DATA-DRIVEN VEDIC MUHURTA AUDIT ENGINE</p>
</div>
""", unsafe_allow_html=True)

if entered_pin != MASTER_ACCESS_PIN:
    st.info("🔒 **આ એપ્લિકેશન સુરક્ષિત (Password Protected) છે.**")
    st.warning("કૃપા કરીને ડાબી બાજુ સાઇડબારમાં સાચો **Access PIN** દાખલ કરો.")
    st.stop()

st.success("🔓 એક્સેસ મંજૂર થયો! વેલકમ ટુ ધ અમોઘ એસ્ટ્રો ઓડિટ પોર્ટલ.")
st.subheader(f"📋 {L['client']} નોંધણી ફોર્મ")

c1, c2, c3, c4 = st.columns(4)
with c1:
    client_name = st.text_input(f"👤 {L['client']} Name:", value="NIRAJ SHUKLA")
    gender = st.selectbox(f"⚧ {L['gender']}:", ["MALE", "FEMALE"], index=0,
                          format_func=lambda x: L["male"] if x=="MALE" else L["female"])
with c2:
    birth_place = st.text_input(f"📍 {L['bplace']} (City/State):", value="Ahmedabad, Gujarat")
    birth_time = st.time_input("⏰ Birth Time:", value=datetime.time(12, 50))
    with c3:
    st.write("🎂 **Birth Date (DOB):**")
    d_c1, d_c2, d_c3 = st.columns(3)
    with d_c1:
        b_day = st.selectbox("Day", list(range(1, 32)), index=14)
    with d_c2:
        b_mon = st.selectbox("Month", list(range(1, 13)), index=4)
    with d_c3:
        b_yr = st.selectbox("Year", list(range(2030, 1939, -1)), index=40)
    birth_date = datetime.date(b_yr, b_mon, b_day)
    with c4:
    start_date = st.date_input("📅 Search From:", value=datetime.date(2026, 11, 1))
    end_date = st.date_input("📅 Search To:", value=datetime.date(2026, 11, 30))

st.markdown("---")
event_keys = list(MASTER_EVENTS.keys())
selected_key = st.selectbox(
    f"🎯 {L['cat']} & {L['event']} પસંદ કરો (કુલ ૪૨ શાસ્ત્રોક્ત વિધાનો):",
    event_keys,
    index=12,
    format_func=lambda k: f"[{MASTER_EVENTS[k]['cat']}]  ➔  {MASTER_EVENTS[k]['name']}"
)

active_rule = MASTER_EVENTS[selected_key]

def get_rahu_str(w, lang):
    o = [1, 6, 4, 5, 3, 2, 7][w]
    s, e = 6.5 + o * 1.4375, 6.5 + (o + 1) * 1.4375
    sep = " થી " if lang == "GU" else (" से " if lang == "HI" else " to ")
    return f"{int(s):02d}:{int(round((s%1)*60)):02d}" + sep + f"{int(e):02d}:{int(round((e%1)*60)):02d}"

if st.button(f"🚀 Run 100-Point Audit & Generate Luxury {top_n_choice + 1}-Page PDF"):
    with st.spinner("⏳ Swiss Ephemeris ખગોળીય ગણતરી અને લક્ઝરી પીડીએફ રેન્ડર થઈ રહી છે..."):
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        b_dec_hour = birth_time.hour + birth_time.minute / 60.0 + birth_time.second / 3600.0
        b_jd = swe.julday(birth_date.year, birth_date.month, birth_date.day, b_dec_hour)
        b_moon, _ = swe.calc_ut(b_jd, swe.MOON, swe.FLG_SIDEREAL)
        b_nak = int((b_moon[0] % 360) / (360 / 27))
        b_ras = int((b_moon[0] % 360) / 30)

        cur = datetime.datetime.combine(start_date, datetime.time(10, 0))
        end = datetime.datetime.combine(end_date, datetime.time(10, 0))

        all_res = []
        while cur <= end:
            jd = swe.julday(cur.year, cur.month, cur.day, 10.0)
            sp, _ = swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)
            mp, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
            diff = (mp[0] % 360 - sp[0] % 360) % 360
            
            t_tot = int(diff / 12) + 1
            t_num = ((t_tot - 1) % 15) + 1
            paksh = L["sud"] if t_tot <= 15 else L["vad"]
            t_lbl = f"{paksh} {t_num}"
            n_idx = int((mp[0] % 360) / (360 / 27))
            y_idx = int(((sp[0] % 360 + mp[0] % 360) % 360) / (360 / 27)) % 27
            k_num = int(diff / 6)
            k_idx = (k_num - 1) % 7 if 1 <= k_num <= 56 else (6 if k_num == 56 else 10)
            w_idx = cur.weekday()
            d_var, i_var = L["wmap"][w_idx], WINT[w_idx]

            mb, tot = [], 0

            # ૧. ચંદ્રબળ (૧૫)
            r_diff = ((int(mp[0] / 30) - b_ras) % 12) + 1
            if r_diff not in [4, 8, 12]:
                tot += 15
                mb.append(("pass", f"{L['p1_c']}: +15 {L['pts']} ({r_diff} {L['shubh']})", "+15"))
            else:
                mb.append(("fail", f"{L['p1_c']}: +00 {L['pts']} ({r_diff} {L['varjya']})", "+00"))

            # ૨. તારાબળ (૧૫)
            t_type = ((n_idx - b_nak) % 27) % 9
            if t_type not in [2, 4, 6]:
                tot += 15
                mb.append(("pass", f"{L['p2_t']}: +15 {L['pts']} ({TARA_DICT[lang_choice][t_type]} {L['shubh']})", "+15"))
            else:
                mb.append(("fail", f"{L['p2_t']}: +00 {L['pts']} ({TARA_DICT[lang_choice][t_type]} {L['varjya']})", "+00"))

            # ૩. તિથિ શુદ્ધિ (૧૦)
            if t_num in [4, 9, 14] or t_tot == 30:
                mb.append(("fail", f"{L['p3_ti']}: +00 {L['pts']} ({t_lbl} {L['varjya']})", "+00"))
            elif t_num in active_rule["tith"]:
                tot += 10
                mb.append(("pass", f"{L['p3_ti']}: +10 {L['pts']} ({t_lbl} {L['shubh']})", "+10"))
            else:
                tot += 5
                mb.append(("warn", f"{L['p3_ti']}: +05 {L['pts']} ({t_lbl} {L['madhyam']})", "+05"))

            # ૪. નક્ષત્ર અનુકૂળતા (૧૦)
            if n_idx in active_rule["nak"]:
                tot += 10
                mb.append(("pass", f"{L['p4_n']}: +10 {L['pts']} ({NAK_DICT[lang_choice][n_idx]} {L['shubh']})", "+10"))
            else:
                tot += 4
                mb.append(("warn", f"{L['p4_n']}: +04 {L['pts']} ({NAK_DICT[lang_choice][n_idx]} {L['madhyam']})", "+04"))

            # ૫. નિત્યયોગ શુદ્ધિ (૧૦)
            if y_idx in [0, 5, 8, 9, 12, 14, 16, 18, 26]:
                mb.append(("fail", f"{L['p5_y']}: +00 {L['pts']} ({YOG_DICT[lang_choice][y_idx]} {L['varjya']})", "+00"))
            else:
                tot += 10
                mb.append(("pass", f"{L['p5_y']}: +10 {L['pts']} ({YOG_DICT[lang_choice][y_idx]} {L['shubh']})", "+10"))

            # ૬. કરણ શુદ્ધિ (૧૦)
            if k_idx == 6:
                mb.append(("fail", f"{L['p6_k']}: +00 {L['pts']} (Vishti Bhadra {L['varjya']})", "+00"))
            else:
                tot += 10
                mb.append(("pass", f"{L['p6_k']}: +10 {L['pts']} ({KAR_DICT[lang_choice][k_idx]} {L['shubh']})", "+10"))

            # ૭. વાર બળ (૧૦)
            if i_var in active_rule.get("v_var", []):
                mb.append(("fail", f"{L['p7_v']}: +00 {L['pts']} ({d_var} {L['varjya']})", "+00"))
            elif i_var in active_rule.get("sh_var", []):
                tot += 10
                mb.append(("pass", f"{L['p7_v']}: +10 {L['pts']} ({d_var} {L['shubh']})", "+10"))
            else:
                tot += 5
                mb.append(("warn", f"{L['p7_v']}: +05 {L['pts']} ({d_var} {L['madhyam']})", "+05"))

            # ૮. શાસ્ત્રોક્ત વિશેષ યોગો અને ઘાત ચક્ર (૨૦)
            s_nak_idx = int((sp[0] % 360) / (360 / 27))
            s_diff = ((n_idx - s_nak_idx) % 27) + 1
            is_ravi_yog = s_diff in [4, 6, 9, 10, 13, 20]
            
            # અમૃત સિદ્ધિ યોગ
            amrut_pairs = {6: 12, 0: 4, 1: 0, 2: 16, 3: 7, 4: 26, 5: 3}
            is_amrut = (amrut_pairs.get(w_idx) == n_idx)

            # મૃત્યુ યોગ (અશુભ)
            mrutyu_pairs = {6: 16, 0: 20, 1: 23, 2: 0, 3: 4, 4: 8, 5: 12}
            is_mrutyu = (mrutyu_pairs.get(w_idx) == n_idx)

            # જ્વાલામુખી યોગ (અશુભ)
            is_jwala = (t_num == 1 and n_idx == 18) or (t_num == 5 and n_idx == 1) or (t_num == 8 and n_idx == 2) or (t_num == 9 and n_idx == 3) or (t_num == 10 and n_idx == 8)

            # ઘાત ચક્ર
            g_rec = GHAT_DATA.get(b_ras, {})
            is_ghat_var = (i_var == g_rec.get("var"))
            is_ghat_tith = (t_num in g_rec.get("tith", []))
            is_ghat_nak = (n_idx == g_rec.get("nak"))
            g_chandra_rashi = g_rec.get("c_f" if gender == "FEMALE" else "c_m")
            is_ghat_chandra = (((int(mp[0] / 30) - b_ras) % 12) + 1 == g_chandra_rashi)

            if is_mrutyu or is_jwala:
                mb.append(("fail", f"{L['p8_s']}: +00 {L['pts']} ({'મૃત્યુ યોગ' if is_mrutyu else 'જ્વાલામુખી યોગ'} દોષ)", "+00"))
            elif is_ghat_var or is_ghat_tith or is_ghat_nak or is_ghat_chandra:
                g_reason = "ઘાત વાર" if is_ghat_var else ("ઘાત તિથિ" if is_ghat_tith else ("ઘાત નક્ષત્ર" if is_ghat_nak else "ઘાત ચંદ્ર"))
                mb.append(("fail", f"{L['p8_s']}: +00 {L['pts']} ({L['ghat_err']} - {g_reason})", "+00"))
            elif is_ravi_yog or is_amrut:
                tot += 20
                y_lbl = "રવિ યોગ સર્વદોષહર" if is_ravi_yog else "અમૃત સિદ્ધિ યોગ"
                mb.append(("bonus", f"{L['p8_s']}: +20 {L['pts']} ({y_lbl})", "+20"))
            else:
                tot += 10
                mb.append(("warn", f"{L['p8_s']}: +10 {L['pts']} ({L['shubh']} વિધાન યોગ)", "+10"))

            sc = min(100, max(0, tot))
            all_res.append({
                "date": cur.strftime("%d-%m-%Y"),
                "tithi": t_lbl,
                "nak": NAK_DICT[lang_choice][n_idx],
                "yog": YOG_DICT[lang_choice][y_idx],
                "karan": KAR_DICT[lang_choice][k_idx],
                "var": d_var,
                "rahu": get_rahu_str(w_idx, lang_choice),
                "score": sc,
                "verdict": f"🌟 {L['shubh']}" if sc >= 75 else (f"⚠️ {L['madhyam']}" if sc >= 50 else f"❌ {L['varjya']}"),
                "breakdown": mb,
                "guide": L["guide_top"] if sc >= 75 else L["guide_mod"]
            })
            cur += datetime.timedelta(days=1)

        top = sorted(all_res, key=lambda x: x["score"], reverse=True)[:top_n_choice]
        total_report_pages = len(top) + 1

        css = f"""
        @page {{ size: A4 portrait; margin: 0; }}
        * {{ box-sizing: border-box; }}
        body {{ font-family: {L['font_family']}; margin: 0; padding: 0; background: #fff; }}
        .page {{ width: 210mm; height: 297mm; padding: 8mm; page-break-after: always; }}
        .box {{ border: 2px solid #0b1d3a; outline: 1.5px solid #c5a059; outline-offset: -5px; height: 100%; padding: 12px 14px; display: flex; flex-direction: column; justify-content: space-between; }}
        """

        t_rows = ""
        for i, r in enumerate(top, 1):
            bg = "#fcfaf6" if i % 2 == 1 else "#fff"
            t_rows += f"<tr style='background:{bg};'><td style='padding:5px;border:1px solid #c5a059;'><b>#{i}</b></td><td style='padding:5px;border:1px solid #c5a059;'><b>{r['date']}</b></td><td style='padding:5px;border:1px solid #c5a059;'>{r['var']}</td><td style='padding:5px;border:1px solid #c5a059;'>{r['tithi']}</td><td style='padding:5px;border:1px solid #c5a059;'>{r['nak']}</td><td style='padding:5px;border:1px solid #c5a059;'><b>{r['score']}/100</b></td><td style='padding:5px;border:1px solid #c5a059;'><b>{r['verdict']}</b></td></tr>"

        p1 = f"""
        <div class="page"><div class="box">
            <div style="text-align:center;">
                <div style="color:#c5a059;font-size:12px;">✦ 🏛️ ✦</div>
                <h2 style="color:#0b1d3a;margin:2px 0;font-size:22px;font-weight:800;">THE AMOGH ASTRO</h2>
                <div style="color:#c5a059;font-weight:bold;font-size:11px;letter-spacing:1.5px;">{L['brand_sub']}</div>
                <div style="height:2px;background:#c5a059;margin:4px auto;width:70%;"></div>
                <div style="color:#4a5568;font-size:11px;">{L['tagline']}</div>
            </div>
            
            <div style="background:#0b1d3a;color:#fff;border:1.5px solid #c5a059;border-radius:6px;padding:8px 12px;font-size:11px;">
                <table style="width:100%;color:#fff;border:none;">
                    <tr>
                        <td><b>👤 {L['client']}:</b> {client_name} ({L['male'] if gender=='MALE' else L['female']})</td>
                        <td><b>📍 {L['bplace']}:</b> {birth_place}</td>
                        <td><b>🪐 {L['rashi']}:</b> {RAS_DICT[lang_choice][b_ras]}</td>
                    </tr>
                    <tr>
                        <td><b>⭐ {L['nak']}:</b> {NAK_DICT[lang_choice][b_nak]}</td>
                        <td colspan="2"><b>🏛️ {L['event']}:</b> [{active_rule['cat']}] {active_rule['name']}</td>
                    </tr>
                    <tr>
                        <td colspan="3"><b>📅 {L['range']}:</b> {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')} (Top {top_n_choice} Windows)</td>
                    </tr>
                </table>
            </div>

            <div>
                <div style="color:#0b1d3a;font-size:12px;font-weight:bold;border-left:4px solid #c5a059;padding-left:6px;margin-bottom:5px;">{L['summary_title']} (TOP {top_n_choice})</div>
                <table style="width:100%;border-collapse:collapse;font-size:11px;text-align:center;">
                    <thead><tr style="background:#0b1d3a;color:#ffd700;">
                        <th style="padding:5px;border:1px solid #c5a059;">{L['rank']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['date']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['day']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['tithi']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['nak']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['score']}</th>
                        <th style="padding:5px;border:1px solid #c5a059;">{L['verdict']}</th>
                    </tr></thead>
                    <tbody>{t_rows}</tbody>
                </table>
            </div>

            <div style="background:#fffdf9;border:1px solid #e2cb9b;border-left:4px solid #c5a059;padding:6px 9px;border-radius:5px;font-size:9.5px;line-height:1.4;color:#6b4e16;">
                <b>{L['disclaimer_title']}</b><br>{L['disclaimer_text']}
            </div>

            <div style="border-top:1px solid #e0cda7;padding-top:4px;display:flex;justify-content:space-between;font-size:9.5px;color:#718096;">
                <span>© 2026 The Amogh Astro • {L['footer_conf']}</span><span>Page 1 of {total_report_pages}</span>
            </div>
        </div></div>
        """

        cards = ""
        for i, r in enumerate(top, 1):
            b_html = ""
            for st_val, txt, pts in r["breakdown"]:
                pill = "#22543d;background:#c6f6d5;" if st_val == "pass" else ("#744210;background:#fefcbf;" if st_val == "bonus" else ("#7b341e;background:#feebc8;" if st_val == "warn" else "#742a2a;background:#fed7d7;"))
                bdr = "#38a169" if st_val == "pass" else ("#d69e2e" if st_val == "bonus" else ("#ed8936" if st_val == "warn" else "#e53e3e"))
                b_html += f"<div style='display:flex;justify-content:space-between;align-items:center;padding:3.5px 8px;margin-bottom:3px;border-left:3px solid {bdr};background:#f7fafc;font-size:10px;'><span>{txt}</span><span style='padding:1px 6px;border-radius:5px;font-weight:bold;color:{pill}'>{pts}</span></div>"

            rahu_html = L['rahu_alert'].replace("{rahu}", r['rahu'])
            cards += f"""
            <div class="page"><div class="box">
                <div style="text-align:center;">
                    <div style="color:#c5a059;font-size:11px;">✦ 🏛️ ✦</div>
                    <h2 style="color:#0b1d3a;margin:2px 0;font-size:20px;font-weight:800;">THE AMOGH ASTRO</h2>
                    <div style="color:#c5a059;font-weight:bold;font-size:10.5px;letter-spacing:1px;">{L['brand_sub']}</div>
                    <div style="height:2px;background:#c5a059;margin:3px auto;width:70%;"></div>
                    <div style="color:#4a5568;font-size:10px;">{L['card_sub']} | #{i}</div>
                </div>

                <div style="background:#0b1d3a;border:2px solid #c5a059;border-radius:6px;padding:8px 12px;color:#fff;display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <div style="color:#c5a059;font-weight:bold;font-size:10.5px;">RANK #{i} OF {top_n_choice}</div>
                        <div style="font-size:15px;font-weight:bold;margin:2px 0;">📅 {r['date']} • {r['var']}</div>
                        <div style="color:#ffd700;font-weight:bold;font-size:12px;">{r['verdict']}</div>
                    </div>
                    <div style="background:rgba(197,160,89,0.3);border:2px solid #c5a059;border-radius:50%;width:50px;height:50px;display:flex;flex-direction:column;align-items:center;justify-content:center;">
                        <div style="font-size:18px;font-weight:bold;color:#fff;line-height:1;">{r['score']}</div>
                        <div style="font-size:9px;color:#ffd700;">/ 100</div>
                    </div>
                </div>

                <div style="border:1px solid #e2e8f0;border-radius:5px;padding:5px 8px;">
                    <div style="color:#0b1d3a;font-weight:bold;font-size:10.5px;border-bottom:1px dashed #cbd5e0;padding-bottom:2px;margin-bottom:4px;">{L['panchang_title']}</div>
                    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:5px;text-align:center;margin-bottom:4px;">
                        <div style="background:#f7fafc;border:1px solid #e2e8f0;border-radius:4px;padding:3px;"><div style="font-size:9px;color:#718096;">{L['tithi']}</div><div style="font-size:11.5px;font-weight:bold;color:#0b1d3a;">{r['tithi']}</div></div>
                        <div style="background:#f7fafc;border:1px solid #e2e8f0;border-radius:4px;padding:3px;"><div style="font-size:9px;color:#718096;">{L['nak']}</div><div style="font-size:11.5px;font-weight:bold;color:#0b1d3a;">{r['nak']}</div></div>
                        <div style="background:#f7fafc;border:1px solid #e2e8f0;border-radius:4px;padding:3px;"><div style="font-size:9px;color:#718096;">{L['yoga']}</div><div style="font-size:11.5px;font-weight:bold;color:#0b1d3a;">{r['yog']}</div></div>
                        <div style="background:#f7fafc;border:1px solid #e2e8f0;border-radius:4px;padding:3px;"><div style="font-size:9px;color:#718096;">{L['karan']}</div><div style="font-size:11.5px;font-weight:bold;color:#0b1d3a;">{r['karan']}</div></div>
                    </div>
                    <div style="background:#fff5f5;border:1px solid #feb2b2;border-radius:4px;padding:3px 7px;font-size:9.5px;color:#9b2c2c;">
                        {rahu_html}
                    </div>
                </div>

                <div style="border:1px solid #e2e8f0;border-radius:5px;padding:5px 8px;">
                    <div style="color:#0b1d3a;font-weight:bold;font-size:10.5px;border-bottom:1px dashed #cbd5e0;padding-bottom:2px;margin-bottom:4px;">{L['audit_title']}</div>
                    {b_html}
                </div>

                <div style="background:#ebf8ff;border-left:4px solid #3182ce;border-radius:5px;padding:5px 8px;">
                    <div style="font-size:10px;font-weight:bold;color:#2b6cb0;">{L['guide_title']}</div>
                    <div style="font-size:10px;font-weight:600;color:#1a365d;margin-top:2px;">{r['guide']}</div>
                </div>

                <div style="border-top:1px solid #e0cda7;padding-top:3px;display:flex;justify-content:space-between;font-size:9.5px;color:#718096;">
                    <span>© 2026 The Amogh Astro • {L['footer_conf']}</span><span>Page {i+1} of {total_report_pages}</span>
                </div>
            </div></div>
            """

        full_html = "<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + css + "</style></head><body>" + p1 + cards + "</body></html>"
        pdf_bytes = HTML(string=full_html).write_pdf()
        
        st.success(f"🎉 લક્ઝરી વૈદિક મુહૂર્ત રિપોર્ટ ({total_report_pages} પેજ) સફળતાપૂર્વક તૈયાર થઈ ગયો છે!")
        file_name = f"The_Amogh_Astro_{selected_key}_{lang_choice}.pdf"
        st.download_button(
            label=f"📥 ડાઉનલોડ કરો: {file_name}",
            data=pdf_bytes,
            file_name=file_name,
            mime="application/pdf"
        )
