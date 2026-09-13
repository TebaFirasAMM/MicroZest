import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="AI-Marshes Microbe",
    page_icon="🦠",
    layout="centered"
)

# عنوان التطبيق الواجهة الاحترافية
st.title("🦠 AI-Marshes Microbe")
st.markdown("### نظام الدعم الذكي لتقييم الخطورة والتشخيص الميكروبي الميداني والسريري")
st.write("---")

# 1. قائمة العينات التسع (البيئية والسريرية)
st.subheader("1. إدخال بيانات العينة")
sample_types = [
    "Water (عينة ماء بيئية / مستنقعات)",
    "Urine (عينة بول)",
    "Blood (عينة دم)",
    "Stool (عينة براز / خروج)",
    "Rectal Swab (مسحة شرجية)",
    "Wound Swab / Pus (مسحة جرح أو صديد)",
    "Vaginal Swab (مسحة مهبلية)",
    "Sputum (بلغم / إفرازات تنفسية)",
    "Throat Swab (مسحة حلق)"
]

selected_sample = st.selectbox("اختر نوع العينة المخبرية أو البيئية:", sample_types)

# 2. البكتيريا الأربع الأساسية المرتبطة
st.subheader("2. البكتيريا المستهدفة (Target Pathogens)")
target_bacteria = [
    "Escherichia coli (E. coli)",
    "Pseudomonas aeruginosa",
    "Klebsiella pneumoniae",
    "Vibrio cholerae"
]

selected_bacteria = st.selectbox("اختر البكتيريا المعزولة أو المحتملة:", target_bacteria)

# 3. إدخال مؤشر أو درجة المعاملة
st.subheader("3. مؤشرات الخطر المبدئية")
severity_indicator = st.slider("حدد مستوى الشدة أو الحمل الميكروبي الظاهري:", 1, 10, 5)

# زر التحليل الذكي
if st.button("تشغيل التحليل الذكي (Run AI Assessment)"):
    st.write("---")
    st.subheader("📊 تقرير التقييم السريع والتشخيص:")
    
    # منطق بسيط لتقييم الخطورة بناءً على المدخلات
    if severity_indicator >= 8:
        risk_level = "حرج / مرتفع جداً (Critical & High Risk) 🔴"
        recommendation = "تتطلب الحالة تدخلاً علاجياً عاجلاً وفحص حساسية مضادات فورية (MDR Alert)."
    elif severity_indicator >= 4:
        risk_level = "متوسط الخطورة (Moderate Risk) 🟡"
        recommendation = "تتطلب متابعة سريرية وتأكيد الفحص بالوسائل المختبرية القياسية."
    else:
        risk_level = "منخفض الخطورة (Low Risk) 🟢"
        recommendation = "حالة اعتيادية، توجيه بإجراءات الوقاية والتعقيم القياسية."

    st.success(f"العينة المختارة: {selected_sample}")
    st.info(f"البكتيريا المرتبطة: {selected_bacteria}")
    st.markdown(f"مستوى الخطورة المقدر بواسطة الذكاء الاصطناعي: {risk_level}")
    st.markdown(f"التوجيه الإكلينيكي / البيئي المقترح: {recommendation}")
    
    st.balloons()

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>AI-Marshes Microbe - مشروع تخرج مرحلة رابعة 2027</p>", unsafe_allow_html=True)
