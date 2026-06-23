import streamlit as st
import pandas as pd
import os

# إعداد الصفحة
st.set_page_config(page_title="عريضة الجماهير", page_icon="🚨", layout="centered")

# ==========================================
# 🎨 كود التصميم (CSS) باش يولي عصري
# ==========================================
st.markdown("""
<style>
    .big-title {
        text-align: center;
        color: #ff4b4b; /* لون أحمر */
        font-size: 45px;
        font-weight: 900;
        margin-bottom: 5px;
    }
    .sub-text {
        text-align: center;
        color: #cfd4df;
        font-size: 20px;
        margin-bottom: 25px;
    }
    .image-box {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .image-box img {
        border-radius: 15px; /* حواف دائرية */
        box-shadow: 0px 4px 20px rgba(255, 75, 75, 0.4); /* ظل أحمر للتصويرة */
        max-width: 100%;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🛑 هنا حط الرابط تاع التصويرة اللي تحبها 🛑
# ==========================================
# روح لجوجل، حوس على تصويرة، دير كليك دروا ومبعد Copy Image Address
# وحط الرابط داخل المزدوجتين هنا:
IMAGE_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCHq7vixadUget9DyVwDug2dBPMlqiNTh7tSBICyA218bvoDofvcn_6Krk&s=10"

if IMAGE_URL:
    st.markdown(f'<div class="image-box"><img src="{IMAGE_URL}" width="500"></div>', unsafe_allow_html=True)

# ==========================================
# 🛑 هنا بدل الكتيبة تاعك 🛑
# ==========================================
st.markdown('<div class="big-title">عريضة للمطالبة بنفي رامز زروقي ـ .........</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">نحن الجماهير الممضية أسفله، نطالب بـ نفي زروقي من الجزائر  .........</div>', unsafe_allow_html=True)
st.markdown("---")

# ملف تخزين التوقيعات
DATA_FILE = "signatures.csv"

def load_signatures():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["الاسم"])

def save_signature(name):
    df = load_signatures()
    new_row = pd.DataFrame({"الاسم": [name]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# إعدادات العداد
df = load_signatures()
current_signatures = len(df)
target = 5000000 

# عرض العداد
st.markdown(f"<h3 style='text-align: center;'>🔥 التوقيعات الحالية: {current_signatures} من {target}</h3>", unsafe_allow_html=True)
progress = min(current_signatures / target, 1.0)
st.progress(progress)

# فورم التوقيع
with st.form("signature_form"):
    st.write("### ✍️ انضم للحملة ووقع الآن")
    name = st.text_input("الاسم واللقب:")
    submitted = st.form_submit_button("أنا أوقع وأدعم العريضة ✊", type="primary")

    if submitted:
        if name.strip():
            save_signature(name)
            st.success("تم تسجيل التوقيع! بارطاجي العريضة.")
            st.rerun()
        else:
            st.error("لازم تكتب اسمك باش يحسبك السيستام!")

# عرض آخر الموقعين
if current_signatures > 0:
    st.markdown("---")
    with st.expander("👀 شوف آخر من وقعوا"):
        st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)

st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 12px;'>Developed by GASPER</p>", unsafe_allow_html=True)
