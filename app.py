import streamlit as st
import datetime
import swisseph as swe
from weasyprint import HTML

st.set_page_config(page_title="The Amogh Astro • Vedic Muhurta Engine", page_icon="🏛️", layout="wide")

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
    .header-box h1 { color: #ffd700; margin: 0; font-size: 2.2rem; }
    .header-box p { color: #e2e8f0; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

I18N = {
    "GU": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "ડેટા-ડ્રિવન ૧૦૦ ગુણ પારદર્શક વૈદિક મુહૂર્ત ઓડિટ રિપોર્ટ",
        "client": "જાતક", "gender": "જાતિ", "male": "પુરુષ", "female": "સ્ત્રી",
        "rashi": "ચંદ્ર રાશિ", "nak": "જન્મ નક્ષત્ર", "cat": "શ્રેણી", "event": "વિધાન", "range": "ગાળો",
        "summary_title": "📊 શ્રેષ્ઠ મુહૂર્તોનું સંક્ષિપ્ત ટેબલ (TOP 10 Ranked Windows)",
        "rank": "ક્રમ", "date": "તારીખ", "day": "વાર", "tithi": "તિથિ", "score": "સ્કોર", "verdict": "પરિણામ",
        "card_sub": "વૈદિક મુહૂર્ત સંપૂર્ણ ઓડિટ કાર્ડ",
        "panchang_title": "🪐 પંચાંગ તત્વો અને સમય નિર્ધારણ",
        "yoga": "નિત્યયોગ", "karan": "કરણ",
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
        "shubh": "શુભ", "madhyam": "મધ્યમ", "varjya": "વર્જ્ય", "sud": "સુદ", "vad": "વદ",
        "p1_c": "૧. ચંદ્રબળ (૧૫)", "p2_t": "૨. તારાબળ (૧૫)", "p3_ti": "૩. તિથિ (૧૦)",
        "p4_n": "૪. નક્ષત્ર (૧૦)", "p5_y": "૫. નિત્યયોગ (૧૦)", "p6_k": "૬. કરણ (૧૦)",
        "p7_v": "૭. વાર (૧૦)", "p8_s": "૮. વિશેષ યોગ અને ઘાત ચક્ર (૨૦)",
        "ghat_err": "ઘાત ચક્ર દોષ ઉપસ્થિત", "pts": "ગુણ"
    },
    "HI": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "डेटा-संचालित १०० अंक पारदर्शी वैदिक मुहूर्त ऑडिट रिपोर्ट",
        "client": "जातक", "gender": "लिंग", "male": "पुरुष", "female": "महिला",
        "rashi": "चंद्र राशि", "nak": "जन्म नक्षत्र", "cat": "श्रेणी", "event": "विधान", "range": "अवधि",
        "summary_title": "📊 सर्वश्रेष्ठ मुहूर्तों की संक्षिप्त तालिका (TOP 10 Ranked Windows)",
        "rank": "क्रमांक", "date": "दिनांक", "day": "वार", "tithi": "तिथि", "score": "स्कोर", "verdict": "परिणाम",
        "card_sub": "वैदिक मुहूर्त सम्पूर्ण ऑडिट कार्ड",
        "panchang_title": "🪐 पंचांग तत्व एवं समय निर्धारण",
        "yoga": "नित्ययोग", "karan": "करण",
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
        "shubh": "शुभ", "madhyam": "मध्यम", "varjya": "वर्ज्य", "sud": "शुक्ल", "vad": "कृष्ण",
        "p1_c": "१. चंद्रबल (१५)", "p2_t": "२. ताराबल (१५)", "p3_ti": "३. तिथि (१०)",
        "p4_n": "૪. नक्षत्र (१०)", "p5_y": "५. नित्ययोग (१०)", "p6_k": "૬. करण (१०)",
        "p7_v": "७. वार (१०)", "p8_s": "૮. विशेष योग एवं घात चक्र (२०)",
        "ghat_err": "घात चक्र दोष उपस्थित", "pts": "अंक"
    },
    "EN": {
        "brand_sub": "THE AMOGH ASTRO • VEDIC CONSULTANCY",
        "tagline": "DATA-DRIVEN 100-POINT TRANSPARENT MUHURTA AUDIT REPORT",
        "client": "Client", "gender": "Gender", "male": "Male", "female": "Female",
        "rashi": "Moon Sign", "nak": "Birth Nakshatra", "cat": "Category", "event": "Event", "range": "Period",
        "summary_title": "📊 TOP 10 RANKED MUHURTA WINDOWS",
        "rank": "Rank", "date": "Date", "day": "Day", "tithi": "Tithi", "score": "Score", "verdict": "Verdict",
        "card_sub": "Bespoke Vedic Muhurta Audit Card",
        "panchang_title": "🪐 Panchang Elements & Timing Windows",
        "yoga": "Yoga", "karan": "Karana",
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
        "shubh": "Auspicious", "madhyam": "Moderate", "varjya": "Inauspicious", "sud": "Shukla", "vad": "Krishna",
        "p1_c": "1. Moon Strength (15)", "p2_t": "2. Tara Strength (15)", "p3_ti": "3. Tithi (10)",
        "p4_n": "4. Nakshatra (10)", "p5_y": "5. Nitya Yoga (10)", "p6_k": "6. Karana (10)",
        "p7_v": "7. Weekday (10)", "p8_s": "8. Special Yoga & Ghat Chakra (20)",
        "ghat_err": "Ghat Chakra Inauspicious", "pts": "Pts"
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

GHAT_MALE = {
    0: ("Ravi", [1, 6, 11], 9), 1: ("Shani", [1, 10, 15], 12), 2: ("Som", [2, 7, 12], 14),
    3: ("Budh", [2, 7, 12], 16), 4: ("Shani", [3, 8, 13], 18), 5: ("Shani", [5, 10, 15], 21),
    6: ("Guru", [4, 9, 14], 23), 7: ("Shukra", [1, 6, 11], 26), 8: ("Shukra", [3, 8, 13], 1),
    9: ("Mangal", [4, 9, 14], 3), 10: ("Guru", [3, 8, 11], 5), 11: ("Shukra", [5, 10, 15], 8)
}

GHAT_FEMALE = {
    0: ("Budh", [3, 8, 13], 2), 1: ("Shani", [2, 7, 12], 4), 2: ("Mangal", [1, 6, 11], 6),
    3: ("Shani", [4, 9, 14], 8), 4: ("Som", [5, 10, 15], 10), 5: ("Guru", [3, 8, 13], 12),
    6: ("Ravi", [2, 7, 12], 15), 7: ("Budh", [1, 6, 11], 17), 8: ("Shukra", [5, 10, 15], 19),
    9: ("Mangal", [4, 9, 14], 22), 10: ("Guru", [2, 7, 12], 24), 11: ("Som", [3, 8, 13], 26)
}

MASTER_EVENTS = {
    "SAN_UPN": {
        "category": {"GU": "૧૬ વૈદિક સંસ્કાર મુહૂર્ત", "HI": "१६ वैदिक संस्कार मुहूर्त", "EN": "16 Classical Vedic Sanskars"},
        "name": {"GU": "૧૦. ઉપનયન / યજ્ઞોપવીત (જનોઈ) સંસ્કાર", "HI": "१०. उपनयन / जनेऊ (यज्ञोपवीत) संस्कार", "EN": "10. Upanayana / Sacred Thread Ceremony"},
        "sh_nak": [3, 7, 12, 13, 14, 16, 21, 22, 23, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Ravi", "Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "ગુરુ બળ / ઉત્તરાયણ વિશેષ યોગ", "HI": "गुरु बल / उत्तरायण विशेष योग", "EN": "Jupiter Alignment / Uttarayana Special"}
    },
    "SAN_VEV": {
        "category": {"GU": "૧૬ વૈદિક સંસ્કાર મુહૂર્ત", "HI": "१६ वैदिक संस्कार मुहूर्त", "EN": "16 Classical Vedic Sanskars"},
        "name": {"GU": "૧૩. વાગ્દાન / વેવિશાળ (સગાઈ) સંસ્કાર", "HI": "१३. वाग्दान / सगाई (वेविशाल) संस्कार", "EN": "13. Vagdan / Formal Engagement Ceremony"},
        "sh_nak": [3, 4, 6, 7, 12, 13, 16, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "ચંદ્રબળ / સૌભાગ્ય વાગ્દાન યોગ", "HI": "चंद्रबल / सौभाग्य वाग्दान योग", "EN": "Chandra Bala / Auspicious Alliance Yoga"}
    },
    "SAN_VIV": {
        "category": {"GU": "૧૬ વૈદિક સંસ્કાર મુહૂર્ત", "HI": "१६ वैदिक संस्कार मुहूर्त", "EN": "16 Classical Vedic Sanskars"},
        "name": {"GU": "૧૪. પાણિગ્રહણ / વિવાહ (લગ્ન) સંસ્કાર", "HI": "१४. पाणिग्रहण / विवाह (लग्न) संस्कार", "EN": "14. Vivaha / Sacred Nuptial Ceremony"},
        "sh_nak": [3, 4, 9, 11, 12, 14, 16, 18, 20, 25, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Ravi", "Mangal", "Shani"],
        "bonus": {"GU": "ત્રિબળ શુદ્ધિ (સૂર્ય-ચંદ્ર-ગુરુ અનુકૂળતા)", "HI": "त्रिबल शुद्धि (सूर्य-चंद्र-गुरु अनुकूलता)", "EN": "Tribala Shuddhi Alignment"}
    },
    "SAN_SIM": {
        "category": {"GU": "૧૬ વૈદિક સંસ્કાર મુહૂર્ત", "HI": "१६ वैदिक संस्कार मुहूर्त", "EN": "16 Classical Vedic Sanskars"},
        "name": {"GU": "૦૮. સીમંતોન્નયન (ખોળો ભરવો) સંસ્કાર", "HI": "०८. सीमन्तोन्नयन (गोद भराई) संस्कार", "EN": "08. Simantonnayana / Baby Shower Blessing"},
        "sh_nak": [3, 7, 12, 14, 16, 21, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "માતૃ-બાળ રક્ષા આયુષ્ય યોગ", "HI": "मातृ-शिशु रक्षा आयुष्य योग", "EN": "Maternal & Child Longevity Yoga"}
    },
    "SAN_NAM": {
        "category": {"GU": "૧૬ વૈદિક સંસ્કાર મુહૂર્ત", "HI": "१६ वैदिक संस्कार मुहूर्त", "EN": "16 Classical Vedic Sanskars"},
        "name": {"GU": "૦૫. નામકરણ (બાળકનું નામ પાડવું) સંસ્કાર", "HI": "०५. नामकरण संस्कार", "EN": "05. Namakarana / Baby Naming Ceremony"},
        "sh_nak": [0, 3, 4, 6, 7, 11, 12, 14, 16, 20, 21, 25, 26], "sh_tith": [1, 2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "સ્થિર-ચર સૌમ્ય નક્ષત્ર બળ", "HI": "સ્થિર-ચર સૌમ્ય નક્ષત્ર બળ", "EN": "Benefic Sthira-Chara Nakshatra Power"}
    },
    "COM_GLD": {
        "category": {"GU": "વેપાર, વાણિજ્ય અને નાણાકીય મુહૂર્ત", "HI": "व्यापार, वाणिज्य एवं वित्तीय मुहूर्त", "EN": "Commerce, Trade & Financial Muhurta"},
        "name": {"GU": "સુવર્ણ - રજત (સોનું-ચાંદી) ખરીદી મુહૂર્ત", "HI": "स्वर्ण - रजत (सोना-चाँदी) क्रय मुहूर्त", "EN": "Gold & Precious Metals Acquisition"},
        "sh_nak": [3, 7, 12, 14, 16, 21, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13, 15],
        "sh_var": ["Guru", "Shukra", "Ravi", "Som"], "v_var": ["Shani"],
        "bonus": {"GU": "અમૃત સિદ્ધિ / રવિ પુષ્ય સમૃદ્ધિ યોગ", "HI": "अमृत सिद्धि / रवि पुष्य समृद्धि योग", "EN": "Amrit Siddhi / Ravi Pushya Prosperity"}
    },
    "COM_SHP": {
        "category": {"GU": "વેપાર, વાણિજ્ય અને નાણાકીય મુહૂર્ત", "HI": "व्यापार, वाणिज्य एवं वित्तीय मुहूर्त", "EN": "Commerce, Trade & Financial Muhurta"},
        "name": {"GU": "નવા વેપાર / પેઢી / શોપિંગ મોલ ઉદ્ઘાટન", "HI": "नूतन व्यापार / दुकान / प्रतिष्ठान उद्घाटन", "EN": "New Business / Commercial Venture Inauguration"},
        "sh_nak": [0, 3, 7, 12, 13, 14, 16, 21, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "વેપાર લક્ષ્મી વૃદ્ધિ યોગ", "HI": "व्यापार लक्ष्मी वृद्धि योग", "EN": "Vyapar Lakshmi Wealth Acceleration"}
    },
    "AST_VAH": {
        "category": {"GU": "સ્થાવર - જંગમ મિલકત મુહૂર્ત", "HI": "स्थावर - जंगम संपत्ति मुहूर्त", "EN": "Real Estate & Asset Acquisition"},
        "name": {"GU": "નૂતન વાહન ખરીદી / શુભ ડિલિવરી મુહૂર્ત", "HI": "नवीन वाहन क्रय / शुभ डिलीवरी मुहूर्त", "EN": "New Automobile / Vehicle Delivery"},
        "sh_nak": [0, 3, 6, 7, 12, 13, 14, 21, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 13, 15],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Shani"],
        "bonus": {"GU": "ચર નક્ષત્ર વાહન સિદ્ધિ યોગ", "HI": "ચર નક્ષત્ર વાહન સિદ્ધિ યોગ", "EN": "Chara Nakshatra Safe Mobility Blessing"}
    },
    "AST_GRP": {
        "category": {"GU": "સ્થાવર - જંગમ મિલકત મુહૂર્ત", "HI": "स्थावर - जंगम संपत्ति मुहूर्त", "EN": "Real Estate & Asset Acquisition"},
        "name": {"GU": "નૂતન ગૃહ પ્રવેશ / વાસ્તુ શાંતિ પૂજન", "HI": "नूतन गृह प्रवेश / वास्तु शांति पूजन", "EN": "Griha Pravesh / Sacred Housewarming"},
        "sh_nak": [3, 11, 12, 13, 16, 20, 25, 26], "sh_tith": [2, 3, 5, 7, 10, 11, 12, 13],
        "sh_var": ["Som", "Budh", "Guru", "Shukra"], "v_var": ["Mangal", "Ravi"],
        "bonus": {"GU": "વાસ્તુ પુરુષ આશીર્વાદ / સ્થિર યોગ", "HI": "વાસ્તુ પુરુષ આશીર્વાદ / સ્થિર યોગ", "EN": "Vastu Purusha Enduring Stability Yoga"}
    }
}

st.markdown("""
<div class="header-box">
    <h1>🏛️ ધ અમોઘ એસ્ટ્રો • THE AMOGH ASTRO</h1>
    <p>ADVANCED 100-POINT DATA-DRIVEN VEDIC MUHURTA AUDIT ENGINE</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/color/96/om.png", width=70)
    st.subheader("⚙️ પ્રણાલી સેટિંગ્સ / Settings")
    lang_choice = st.selectbox("🌐 Report Language / ભાષા પસંદ કરો:", ["GU", "HI", "EN"], index=0,
                               format_func=lambda x: "ગુજરાતી (Gujarati)" if x=="GU" else ("हिन्दी (Hindi)" if x=="HI" else "English"))
    L = I18N[lang_choice]
    st.markdown("---")
    st.markdown("### 📞 Contact Consultancy")
    st.caption("**The Amogh Astro Consultancy**\\nAhmedabad, Gujarat\\ntheamoghastro@gmail.com")

st.subheader(L['client'] + " " + L['event'] + " નોંધણી ફોર્મ")

col1, col2, col3 = st.columns(3)
with col1:
    client_name = st.text_input("👤 " + L['client'] + " Name:", value="NIRAJ SHUKLA")
    gender = st.selectbox("⚧ " + L['gender'] + ":", ["MALE", "FEMALE"], index=0,
                          format_func=lambda x: L["male"] if x=="MALE" else L["female"])

with col2:
    birth_date = st.date_input("🎂 Birth Date:", value=datetime.date(1990, 5, 15))
    birth_time = st.time_input("⏰ Birth Time:", value=datetime.time(12, 50))

with col3:
    start_date = st.date_input("📅 Muhurta Search From:", value=datetime.date(2026, 11, 1))
    end_date = st.date_input("📅 Muhurta Search To:", value=datetime.date(2026, 11, 30))

st.markdown("---")
event_keys = list(MASTER_EVENTS.keys())
selected_key = st.selectbox(
    "🎯 " + L['cat'] + " & " + L['event'] + " પસંદ કરો:",
    event_keys,
    index=0,
    format_func=lambda k: "[" + MASTER_EVENTS[k]['category'][lang_choice] + "]  ➔  " + MASTER_EVENTS[k]['name'][lang_choice]
)

active_rule = MASTER_EVENTS[selected_key]
active_cat = active_rule["category"][lang_choice]
active_name = active_rule["name"][lang_choice]
active_bonus = active_rule["bonus"][lang_choice]

def get_rahu_str(w, lang):
    o = [1, 6, 4, 5, 3, 2, 7][w]
    s, e = 6.5 + o * 1.4375, 6.5 + (o + 1) * 1.4375
    sep = " થી " if lang == "GU" else (" से " if lang == "HI" else " to ")
    return f"{int(s):02d}:{int(round((s%1)*60)):02d}" + sep + f"{int(e):02d}:{int(round((e%1)*60)):02d}"

if st.button("🚀 Run 100-Point Audit & Generate Luxury 11-Page PDF"):
    with st.spinner("⏳ Swiss Ephemeris ખગોળીય ગણતરી અને ૧૧-પેજ લક્ઝરી પીડીએફ રેન્ડર થઈ રહી છે..."):
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        b_dec_hour = birth_time.hour + birth_time.minute / 60.0 + birth_time.second / 3600.0
        b_jd = swe.julday(birth_date.year, birth_date.month, birth_date.day, b_dec_hour)
        b_moon, _ = swe.calc_ut(b_jd, swe.MOON, swe.FLG_SIDEREAL)
        b_nak = int((b_moon[0] % 360) / (360 / 27))
        b_ras = int((b_moon[0] % 360) / 30)

        ACTIVE_GHAT = GHAT_FEMALE if gender == "FEMALE" else GHAT_MALE

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

            # 1. Chandrabalam (15)
            r_diff = ((int(mp[0] / 30) - b_ras) % 12) + 1
            if r_diff not in [4, 8, 12]:
                tot += 15
                mb.append(("pass", L['p1_c'] + ": +15 " + L['pts'] + f" ({r_diff} " + L['shubh'] + ")", "+15"))
            else:
                mb.append(("fail", L['p1_c'] + ": +00 " + L['pts'] + f" ({r_diff} " + L['varjya'] + ")", "+00"))

            # 2. Tarabalam (15)
            t_type = ((n_idx - b_nak) % 27) % 9
            if t_type not in [2, 4, 6]:
                tot += 15
                mb.append(("pass", L['p2_t'] + ": +15 " + L['pts'] + f" ({TARA_DICT[lang_choice][t_type]} " + L['shubh'] + ")", "+15"))
            else:
                mb.append(("fail", L['p2_t'] + ": +00 " + L['pts'] + f" ({TARA_DICT[lang_choice][t_type]} " + L['varjya'] + ")", "+00"))

            # 3. Tithi (10)
            if t_num in [4, 9, 14] or t_tot == 30:
                mb.append(("fail", L['p3_ti'] + ": +00 " + L['pts'] + f" ({t_lbl} " + L['varjya'] + ")", "+00"))
            elif t_num in active_rule["sh_tith"]:
                tot += 10
                mb.append(("pass", L['p3_ti'] + ": +10 " + L['pts'] + f" ({t_lbl} " + L['shubh'] + ")", "+10"))
            else:
                tot += 5
                mb.append(("warn", L['p3_ti'] + ": +05 " + L['pts'] + f" ({t_lbl} " + L['madhyam'] + ")", "+05"))

            # 4. Nakshatra (10)
            if n_idx in active_rule["sh_nak"]:
                tot += 10
                mb.append(("pass", L['p4_n'] + ": +10 " + L['pts'] + f" ({NAK_DICT[lang_choice][n_idx]} " + L['shubh'] + ")", "+10"))
            else:
                tot += 5
                mb.append(("warn", L['p4_n'] + ": +05 " + L['pts'] + f" ({NAK_DICT[lang_choice][n_idx]} " + L['madhyam'] + ")", "+05"))

            # 5. Nitya Yoga (10)
            if y_idx in [0, 5, 8, 9, 12, 14, 16, 18, 26]:
                mb.append(("fail", L['p5_y'] + ": +00 " + L['pts'] + f" ({YOG_DICT[lang_choice][y_idx]} " + L['varjya'] + ")", "+00"))
            else:
                tot += 10
                mb.append(("pass", L['p5_y'] + ": +10 " + L['pts'] + f" ({YOG_DICT[lang_choice][y_idx]} " + L['shubh'] + ")", "+10"))

            # 6. Karana (10)
            if k_idx == 6:
                mb.append(("fail", L['p6_k'] + ": +00 " + L['pts'] + " (Vishti Bhadra " + L['varjya'] + ")", "+00"))
            else:
                tot += 10
                mb.append(("pass", L['p6_k'] + ": +10 " + L['pts'] + f" ({KAR_DICT[lang_choice][k_idx]} " + L['shubh'] + ")", "+10"))

            # 7. Weekday (10)
            if i_var in active_rule["v_var"]:
                mb.append(("fail", L['p7_v'] + ": +00 " + L['pts'] + f" ({d_var} " + L['varjya'] + ")", "+00"))
            elif i_var in active_rule["sh_var"]:
                tot += 10
                mb.append(("pass", L['p7_v'] + ": +10 " + L['pts'] + f" ({d_var} " + L['shubh'] + ")", "+10"))
            else:
                tot += 5
                mb.append(("warn", L['p7_v'] + ": +05 " + L['pts'] + f" ({d_var} " + L['madhyam'] + ")", "+05"))

            # 8. Special Yoga & Ghat Chakra (20)
            has_ravi = ((n_idx - int(sp[0] / (360 / 27))) % 27 + 1) in [4, 6, 9, 10, 13, 20]
            gv, gt, gn = ACTIVE_GHAT.get(b_ras, ("", [], -1))
            is_ghat = (i_var == gv or t_num in gt or n_idx == gn)

            ghat_gender_lbl = L['male'] if gender == 'MALE' else L['female']
            if is_ghat:
                mb.append(("fail", L['p8_s'] + ": +00 " + L['pts'] + f" ({L['ghat_err']} - {ghat_gender_lbl})", "+00"))
            elif has_ravi:
                tot += 20
                mb.append(("bonus", L['p8_s'] + ": +20 " + L['pts'] + f" ({active_bonus})", "+20"))
            else:
                tot += 10
                mb.append(("warn", L['p8_s'] + ": +10 " + L['pts'] + f" ({L['shubh']})", "+10"))

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

        top = sorted(all_res, key=lambda x: x["score"], reverse=True)[:10]

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
                        <td><b>🪐 {L['rashi']}:</b> {RAS_DICT[lang_choice][b_ras]}</td>
                        <td><b>⭐ {L['nak']}:</b> {NAK_DICT[lang_choice][b_nak]}</td>
                    </tr>
                    <tr>
                        <td><b>🎯 {L['cat']}:</b> {active_cat}</td>
                        <td colspan="2"><b>🏛️ {L['event']}:</b> {active_name}</td>
                    </tr>
                    <tr>
                        <td colspan="3"><b>📅 {L['range']}:</b> {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}</td>
                    </tr>
                </table>
            </div>

            <div>
                <div style="color:#0b1d3a;font-size:12px;font-weight:bold;border-left:4px solid #c5a059;padding-left:6px;margin-bottom:5px;">{L['summary_title']}</div>
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
                <span>© 2026 The Amogh Astro • {L['footer_conf']}</span><span>Page 1 of 11</span>
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
                        <div style="color:#c5a059;font-weight:bold;font-size:10.5px;">RANK #{i} OF 10</div>
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
                    <span>© 2026 The Amogh Astro • {L['footer_conf']}</span><span>Page {i+1} of 11</span>
                </div>
            </div></div>
            """

        full_html = "<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + css + "</style></head><body>" + p1 + cards + "</body></html>"
        pdf_bytes = HTML(string=full_html).write_pdf()
        
        st.success("🎉 ૧૧-પેજ લક્ઝરી વૈદિક મુહૂર્ત રિપોર્ટ સફળતાપૂર્વક તૈયાર થઈ ગયો છે!")
        file_name = f"The_Amogh_Astro_{selected_key}_{lang_choice}.pdf"
        st.download_button(
            label=f"📥 ડાઉનલોડ કરો: {file_name}",
            data=pdf_bytes,
            file_name=file_name,
            mime="application/pdf"
        )
