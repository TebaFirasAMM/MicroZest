import streamlit as st

# إعداد الصفحة وتكوين العرض
st.set_page_config(
    page_title="Biobell - المطهر الطبيعي",
    page_icon="🌿",
    layout="wide"
)

# حقن أكواد الـ CSS والتصميم الداخلي مع التأكد من تغليفها بشكل صحيح
st.markdown("""
    <style>
        :root {
            --primary-color: #2e5d32;
            --accent-color: #81c784;
            --bg-color: #f4f7f2;
            --card-bg: #ffffff;
            --text-color: #333333;
        }
        
        .main {
            background-color: var(--bg-color);
        }

        /* تنسيق الهيدر العلوي */
        .header-box {
            background: var(--card-bg);
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border-radius: 10px;
            margin-bottom: 25px;
        }
        
        .logo-area {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: bold;
            font-size: 1.3rem;
            color: var(--primary-color);
        }

        /* بطاقات الخطوات */
        .step-card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            border-top: 5px solid var(--primary-color);
            margin-bottom: 20px;
        }
        
        .step-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--primary-color);
        }

        /* حالة التخمير */
        .status-item {
            background: #f9fbf9;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
            border-right: 4px solid var(--accent-color);
            font-size: 0.95rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .status-badge {
            background: #c8e6c9;
            color: #1b5e20;
            padding: 3px 10px;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: bold;
        }

        /* أزرار التفاعل الذكي */
        .action-footer {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 15px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# العنوان العلوي والشعار
st.markdown("""
    <div class="header-box">
        <div class="logo-area">
            <span>🌿 Biobell</span>
        </div>
        <div style="color: #666; font-size: 0.95rem;">
            منصة التخمر الحيوي المنزلي
        </div>
    </div>
""", unsafe_allow_html=True)

# واجهة الترحيب الرئيسية
st.markdown("""
    <div style="background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1543168257-4ba7af1c3e54?auto=format&fit=crop&w=1200&q=80') center/cover; padding: 40px 20px; color: white; border-radius: 15px; margin-bottom: 30px; text-align: center;">
        <h1 style="font-size: 2.2rem; margin-bottom: 10px;">حولي قشور الفواكه إلى مطهرات طبيعية</h1>
        <p style="font-size: 1.1rem; opacity: 0.9;">مبادرة منزلية بسيطة.. لبيئة أنظف وصحة أفضل</p>
    </div>
""", unsafe_allow_html=True)

# تقسيم الصفحة إلى 3 أعمدة للخطوات الأساسية
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="step-card">
            <div class="step-title">1. اختر نوع القشور</div>
        </div>
    """, unsafe_allow_html=True)
    selected_peel = st.selectbox("حدد نوع قشور الفواكه:", ["برتقال", "ليمون", "تفاح", "موز", "رمان", "أخرى"])
with col2:  
    st.markdown("""
        <div class="step-card">
            <div class="step-title">2. تحديد تاريخ البدء</div>
        </div>
    """, unsafe_allow_html=True)
    start_date = st.date_input("تاريخ بداية التخمير:")
    st.caption("سيقوم النظام بحساب فترة التخمير تلقائياً.")

with col3:
    st.markdown("""
        <div class="step-card">
            <div class="step-title">3. متابعة التخمير الواقعية</div>
            <div class="status-item">
                <span>حالة الحموضة:</span>
                <span class="status-badge">حموضة لطيفة وآمنة</span>
            </div>
            <div class="status-item">
                <span>مظهر السائل:</span>
                <span class="status-badge">معكر طبيعي مع فقاعات</span>
            </div>
            <div class="status-item">
                <span>الرائحة:</span>
                <span class="status-badge">زكية وعطرية (ناجح)</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# شريط التقدم للتخمير
st.markdown("### مستوى التخمير الحالي")
st.progress(50)
st.caption("المنتصف - جارِ استكمال دورة التخمير الطبيعية")

# شريط التفاعل الصوتي والصوري السفلي
st.markdown("""
    <div class="action-footer">
        <div style="text-align: center; cursor: pointer;">
            <div style="font-size: 1.5rem;">📷</div>
            <div style="font-weight: bold; color: #2e5d32; font-size: 0.9rem;">التقاط صورة للمظهر</div>
        </div>
        <div style="text-align: center; cursor: pointer;">
            <div style="font-size: 1.5rem;">🔊</div>
            <div style="font-weight: bold; color: #2e5d32; font-size: 0.9rem;">استمع إلى رد التطبيق</div>
        </div>
        <div style="text-align: center; cursor: pointer;">
            <div style="font-size: 1.5rem;">🎙️</div>
            <div style="font-weight: bold; color: #2e5d32; font-size: 0.9rem;">تحدث الآن للمساعد</div>
        </div>
    </div>
""", unsafe_allow_html=True)
