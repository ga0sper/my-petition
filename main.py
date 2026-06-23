import streamlit as st
import pandas as pd
import os

# إعداد الصفحة
st.set_page_config(page_title="عريضة الجماهير", page_icon="📝")

# ملف تخزين التوقيعات باش ما يروحوش
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

# ==========================================
# 🛑 هنا البلاصة اللي تبدل فيها الكتيبة تاعك 🛑
# ==========================================

# بدل واش كاين بين المزدوجتين
st.title("عريضة للمطالبة بـ .........") 
st.write("نحن الجماهير الممضية أسفله، نطالب بـ ......... لأن .........")

# ==========================================

# إعدادات العداد
df = load_signatures()
current_signatures = len(df)
target = 5000000 # الهدف تاع التوقيعات (تقدر تبدلو)

# عرض العداد وشريط التقدم
st.subheader(f"📊 التوقيعات: {current_signatures} / {target}")
progress = min(current_signatures / target, 1.0)
st.progress(progress)

st.markdown("---")

# فورم التوقيع
with st.form("signature_form"):
    st.write("### ✍️ شارك في العريضة")
    name = st.text_input("اكتب اسمك ولا اللقب تاعك:")
    submitted = st.form_submit_button("أنا أوقع وأدعم العريضة")

    if submitted:
        if name.strip():
            save_signature(name)
            st.success("تم تسجيل توقيعك بنجاح! بارك الله فيك.")
            st.rerun() # تحديث الصفحة باش يطلع العداد ديريكت
        else:
            st.error("أيا البوس، لازم تكتب اسمك باش يحسبك السيستام!")

# عرض آخر الموقعين (باش تبان فيها المصداقية)
if current_signatures > 0:
    st.markdown("---")
    with st.expander("👀 شوف شكون وقع مؤخراً"):
        # نعرضو غير 10 توقيعات التوالى باش ما تتعمرش الشاشة
        st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)

st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 12px;'>Developed by GASPER</p>", unsafe_allow_html=True)
