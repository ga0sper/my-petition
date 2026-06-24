import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="بورصة الدخان", page_icon="💸", layout="centered")

# تصميم السيت (CSS) باش يبان غالي
st.markdown("""
<style>
    .luxury-title {
        text-align: center;
        color: #d4af37; /* لون ذهبي */
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .price-tag {
        color: #ff4b4b;
        font-size: 24px;
        font-weight: bold;
    }
    .fake-alert {
        text-align: center;
        color: gray;
        font-size: 14px;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown('<div class="luxury-title">🚬 البورصة الوطنية للتبغ</div>', unsafe_allow_html=True)
st.write("### أول منصة جزائرية لبيع الدخان بالتقسيط المريح وبدون فوائد (ربوية) 📉")
st.markdown("---")

# عرض "المنتجات" الفاخرة
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥇 مارلبورو (Marlboro)")
    st.write("حبة وحدة، مستعملة جبدة برك، نقية ومافيهاش ريحة الشياط.")
    st.markdown('<p class="price-tag">السعر: 15,000 دج (أو غرام ذهب)</p>', unsafe_allow_html=True)
    buy_marlboro = st.button("🛒 تقديم طلب قرض لشرائها")
    if buy_marlboro:
        st.error("❌ تم رفض الطلب: الراتب تاعك ما يكفيش باش تشري حبة مارلبورو. روح اشري الخبز لداركم خير!")

with col2:
    st.markdown("### 🥉 ريم (Rym)")
    st.write("نص ڨارو، مخبي في باكي تاع ماكاو باش ما يفيقوش بيه.")
    st.markdown('<p class="price-tag">السعر: 5,000 دج (بالتقسيط على 3 أشهر)</p>', unsafe_allow_html=True)
    buy_rym = st.button("🛒 اشتري الآن (بالتقسيط)")
    if buy_rym:
        st.warning("⚠️ لازم تجيب كفيل (ضامن) وشهادة عمل باش نبيعولك نص ڨارو ريم.")

st.markdown("---")

# قسم الاستثمار
st.subheader("📈 استثمر في 'الڨارو-كوين'")
st.write("الأسعار راهي طالعة كثر من البيتكوين! اشري كارطوشة اليوم، وبيعها العام الجاي تشري بيها سكنة عدل.")
st.progress(85)
st.caption("مؤشر ارتفاع أسعار الدخان في السوق السوداء")

# التوثيق
st.markdown('<div class="fake-alert">⚠️ هذي المنصة مجرد مزحة (Troll) بمناسبة الزيادة في الأسعار. التدخين مضر بالصحة والجيب! <br> Developed by GASPER</div>', unsafe_allow_html=True)
