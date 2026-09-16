<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title id="page-title">من قشور الفواكه - المطهر الطبيعي</title>
    <style>
        :root {
            --primary-color: #2e5d32;
            --accent-color: #81c784;
            --bg-color: #f4f7f2;
            --card-bg: #ffffff;
            --text-color: #333333;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; }
        
        /* شريط التنقل العلوي */
        header { background: var(--card-bg); padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
       
        .logo-area { display: flex; align-items: center; gap: 10px; font-weight: bold; font-size: 1.2rem; color: var(--primary-color); }
        .nav-links { display: flex; gap: 20px; align-items: center; }
        .nav-item { cursor: pointer; color: #666; text-decoration: none; font-size: 0.95rem; display: flex; align-items: center; gap: 5px; }
        .lang-switch { background: #e8f5e9; border: 1px solid var(--accent-color); padding: 5px 12px; border-radius: 20px; cursor: pointer; font-weight: bold; color: var(--primary-color); font-size: 1rem; }

        /* الهيدر الرئيسي */
        .hero { background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1543168257-4ba7af1c3e54?auto=format&fit=crop&w=1200&q=80') center/cover; padding: 40px 20px; color: white; display: flex; justify-content: space-between; align-items: center; border-radius: 0 0 20px 20px; margin-bottom: 30px; }
        .hero-text h1 { font-size: 2.2rem; margin-bottom: 10px; }
        .hero-text p { font-size: 1.1rem; opacity: 0.9; }

        /* الحاويات الثلاث للخطوات */
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .step-card { background: var(--card-bg); border-radius: 15px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); position: relative; border-top: 5px solid var(--primary-color); }
        .step-number { position: absolute; top: -15px; right: 20px; background: var(--primary-color); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; }
        .step-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 15px; color: var(--primary-color); }

        /* الخطوة 1: اختيار القشور */
        .peels-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
        .peel-option { border: 2px solid #ddd; border-radius: 10px; padding: 10px; text-align: center; cursor: pointer; transition: 0.2s; }
        .peel-option.active { border-color: var(--primary-color); background: #e8f5e9; }

        /* الخطوة 2: التاريخ والوقت المبسط */
        .datetime-box { display: flex; flex-direction: column; gap: 15px; margin-top: 20px; }
        .datetime-box input { padding: 12px; border: 1px solid #ddd; border-radius: 8px; font-size: 1rem; width: 100%; }

        /* الخطوة 3: التقييم الواقعي */
        .status-item { background: #f9fbf9; padding: 12px; border-radius: 8px; margin-bottom: 10px; border-right: 4px solid var(--accent-color); font-size: 0.95rem; }
        .status-badge { float: left; background: #c8e6c9; color: #1b5e20; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; font-weight: bold; }

        /* شريط التخمير السفلي */
        .progress-section { background: var(--card-bg); padding: 20px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }
[9/16/2026 8:34 PM] طيبة فراس: .progress-bar-container { display: flex; align-items: center; justify-content: space-between; margin: 20px 0; position: relative; }
        .progress-line { position: absolute; height: 4px; background: var(--accent-color); width: 70%; right: 15%; z-index: 1; }
        .progress-node { width: 20px; height: 20px; border-radius: 50%; background: var(--primary-color); z-index: 2; position: relative; }
        
        /* شريط التفاعل الصوتي والصوري السفلي */
        .action-footer { background: var(--card-bg); padding: 20px; border-radius: 15px; display: flex; justify-content: space-around; align-items: center; margin-bottom: 40px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); flex-wrap: wrap; gap: 15px; }
        .action-btn { display: flex; align-items: center; gap: 10px; cursor: pointer; font-weight: bold; color: var(--primary-color); }
        .action-icon { width: 45px; height: 45px; background: #e8f5e9; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; }
    </style>
</head>
<body>

    <!-- الشريط العلوي مع زر اللغة المخصص ع / EN -->
    <header>
        <div class="logo-area">
            <span>🌿</span>
            <span id="logo-text">من قشور الفواكه</span>
        </div>
        <div class="nav-links">
            <button class="lang-switch" onclick="toggleLanguage()" id="lang-btn">EN</button>
            <a href="#" class="nav-item">⚙️ <span id="nav-settings">الإعدادات</span></a>
            <a href="#" class="nav-item">❓ <span id="nav-help">مساعدة</span></a>
            <a href="#" class="nav-item">👤 <span id="nav-account">حسابي</span></a>
        </div>
    </header>

    <div class="container">
        <!-- الهيدر الرئيسي -->
        <div class="hero">
            <div class="hero-text">
                <h1 id="hero-title">حولي قشور الفواكه إلى مطهرات طبيعية</h1>
                <p id="hero-subtitle">مبادرة منزلية بسيطة.. لبيئة أنظف وصحة أفضل</p>
            </div>
        </div>

        <!-- الخطوات الثلاث -->
        <div class="steps-grid">
            <!-- الخطوة 1 -->
            <div class="step-card">
                <div class="step-number">1</div>
                <div class="step-title" id="step1-title">اختر نوع القشور</div>
                <div class="peels-grid">
                    <div class="peel-option active" id="peel-1">🍊 <br><small>برتقال</small></div>
                    <div class="peel-option" id="peel-2">🍋 <br><small>ليمون</small></div>
                    <div class="peel-option" id="peel-3">🍌 <br><small>موز</small></div>
                    <div class="peel-option" id="peel-4">🍎 <br><small>تفاح</small></div>
                    <div class="peel-option" id="peel-5">🍅 <br><small>رمان</small></div>
                    <div class="peel-option" id="peel-6">📦 <br><small>أخرى</small></div>
                </div>
            </div>

            <!-- الخطوة 2: التاريخ والوقت المبسط -->
            <div class="step-card">
                <div class="step-number">2</div>
                <div class="step-title" id="step2-title">حدد تاريخ ووقت البدء</div>
                <div class="datetime-box">
                    <input type="date" id="start-date" value="2026-09-16">
                    <input type="time" id="start-time" value="10:00">
                    <small style="color: #666;" id="step2-hint">سيقوم النظام بحساب فترة التخمير تلقائياً.</small>
                </div>
            </div>

            <!-- الخطوة 3: التقييم الواقعي (الرائحة بحالتين: زكية للنجاح أو سيئة للفشل) -->
            <div class="step-card">
                <div class="step-number">3</div>
                <div class="step-title" id="step3-title">متابعة التخمير الواقعية</div>
                
                <div class="status-item">
                    <span id="status-acid-label">حالة الحموضة:</span>
                <span class="status-badge" id="status-acid-val">حموضة لطيفة وآمنة</span>
                </div>
                <div class="status-item">
                    <span id="status-look-label">مظهر السائل:</span>
                    <span class="status-badge" id="status-look-val">معكر طبيعي مع فقاعات</span>
                </div>
                <div class="status-item">
                    <span id="status-smell-label">الرائحة:</span>
                    <span class="status-badge" id="status-smell-val">رائحة زكية وعطرية (ناجح)</span>
                </div>
            </div>
        </div>

        <!-- شريط التقدم -->
        <div class="progress-section">
            <h3 style="color: var(--primary-color); margin-bottom: 10px;" id="progress-heading">مستوى التخمير الحالي</h3>
            <div class="progress-bar-container">
                <div class="progress-node"></div>
                <div class="progress-line"></div>
                <div class="progress-node" style="background: var(--accent-color);"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.9rem; color: #666;">
                <span id="prog-start">البداية</span>
                <span id="prog-mid">منتصف التخمير</span>
                <span id="prog-end">الانتهاء المتوقع (بعد شهر)</span>
            </div>
        </div>

        <!-- شريط التفاعل الصوتي والصوري (الذكاء الاصطناعي للمنزل) -->
        <div class="action-footer">
            <div class="action-btn">
                <div class="action-icon">📷</div>
                <span id="action-photo">التقاط صورة للمظهر</span>
            </div>
            <div class="action-btn">
                <div class="action-icon">🔊</div>
                <span id="action-listen">استمع إلى رد التطبيق</span>
            </div>
            <div class="action-btn">
                <div class="action-icon">🎙️</div>
                <span id="action-voice">تحدث الآن للمساعد</span>
            </div>
        </div>
    </div>

    <!-- كود الجافاسكريبت المدمج لتبديل اللغات وتفاعل الأزرار -->
    <script>
        let currentLang = 'ar';

        const translations = {
            ar: {
                pageTitle: "من قشور الفواكه - المطهر الطبيعي",
                logoText: "من قشور الفواكه",
                navSettings: "الإعدادات",
                navHelp: "مساعدة",
                navAccount: "حسابي",
                heroTitle: "حولي قشور الفواكه إلى مطهرات طبيعية",
                heroSubtitle: "مبادرة منزلية بسيطة.. لبيئة أنظف وصحة أفضل",
                step1Title: "اختر نوع القشور",
                step2Title: "حدد تاريخ ووقت البدء",
                step2Hint: "سيقوم النظام بحساب فترة التخمير تلقائياً.",
                step3Title: "متابعة التخمير الواقعية",
                statusAcidLabel: "حالة الحموضة:",
                statusAcidVal: "حموضة لطيفة وآمنة",
                statusLookLabel: "مظهر السائل:",
                statusLookVal: "معكر طبيعي مع فقاعات",
                statusSmellLabel: "الرائحة:",
                statusSmellVal: "رائحة زكية وعطرية (ناجح)",
                progressHeading: "مستوى التخمير الحالي",
                progStart: "البداية",
                progMid: "منتصف التخمير",
                progEnd: "الانتهاء المتوقع (بعد شهر)",
                actionPhoto: "التقاط صورة للمظهر",
                actionListen: "استمع إلى رد التطبيق",
                actionVoice: "تحدث الآن للمساعد",
                peel1: "برتقال",
                peel2: "ليمون",
                peel3: "موز",
                peel4: "تفاح",
                peel5: "رمان",
                peel6: "أخرى"
            },
            en: {
                pageTitle: "From Fruit Peels - Natural Disinfectant",
                logoText: "Fruit Peels",
                navSettings: "Settings",
navHelp: "Help",
                navAccount: "My Account",
                heroTitle: "Turn Fruit Peels Into Natural Disinfectants",
                heroSubtitle: "A simple home initiative.. for a cleaner environment and better health",
                step1Title: "Select Peel Type",
                step2Title: "Select Start Date & Time",
                step2Hint: "The system will automatically calculate fermentation time.",
                step3Title: "Realistic Fermentation Tracking",
                statusAcidLabel: "Acidity Status:",
                statusAcidVal: "Mild & Safe Acidity",
                statusLookLabel: "Liquid Appearance:",
                statusLookVal: "Natural turbid with bubbles",
                statusSmellLabel: "Aroma:",
                statusSmellVal: "Fragrant & Aromatic (Success)",
                progressHeading: "Current Fermentation Level",
                progStart: "Start",
                progMid: "Mid-Fermentation",
                progEnd: "Expected End (After 1 Month)",
                actionPhoto: "Capture Appearance Photo",
                actionListen: "Listen to App Response",
                actionVoice: "Speak to Assistant Now",
                peel1: "Orange",
                peel2: "Lemon",
                peel3: "Banana",
                peel4: "Apple",
                peel5: "Pomegranate",
                peel6: "Other"
            }
        };

        function toggleLanguage() {
            currentLang = currentLang === 'ar' ? 'en' : 'ar';
            document.documentElement.lang = currentLang;
            document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
            document.getElementById('lang-btn').innerText = currentLang === 'ar' ? 'EN' : 'ع';

            const t = translations[currentLang];
            document.getElementById('page-title').innerText = t.pageTitle;
            document.getElementById('logo-text').innerText = t.logoText;
            document.getElementById('nav-settings').innerText = t.navSettings;
            document.getElementById('nav-help').innerText = t.navHelp;
            document.getElementById('nav-account').innerText = t.navAccount;
            document.getElementById('hero-title').innerText = t.heroTitle;
            document.getElementById('hero-subtitle').innerText = t.heroSubtitle;
            document.getElementById('step1-title').innerText = t.step1Title;
            document.getElementById('step2-title').innerText = t.step2Title;
            document.getElementById('step2-hint').innerText = t.step2Hint;
            document.getElementById('step3-title').innerText = t.step3Title;
            document.getElementById('status-acid-label').innerText = t.statusAcidLabel;
            document.getElementById('status-acid-val').innerText = t.statusAcidVal;
            document.getElementById('status-look-label').innerText = t.statusLookLabel;
            document.getElementById('status-look-val').innerText = t.statusLookVal;
            document.getElementById('status-smell-label').innerText = t.statusSmellLabel;
            document.getElementById('status-smell-val').innerText = t.statusSmellVal;
            document.getElementById('progress-heading').innerText = t.progressHeading;
            document.getElementById('prog-start').innerText = t.progStart;
            document.getElementById('prog-mid').innerText = t.progMid;
            document.getElementById('prog-end').innerText = t.progEnd;
            document.getElementById('action-photo').innerText = t.actionPhoto;
            document.getElementById('action-listen').innerText = t.actionListen;
            document.getElementById('action-voice').innerText = t.actionVoice;

            // تحديث أسماء الفواكه
            document.getElementById('peel-1').innerHTML = 🍊 <br><small>${t.peel1}</small>;
[9/16/2026 8:34 PM] طيبة فراس: document.getElementById('peel-2').innerHTML = 🍋 <br><small>${t.peel2}</small>;
            document.getElementById('peel-3').innerHTML = 🍌 <br><small>${t.peel3}</small>;
            document.getElementById('peel-4').innerHTML = 🍎 <br><small>${t.peel4}</small>;
            document.getElementById('peel-5').innerHTML = 🍅 <br><small>${t.peel5}</small>;
            document.getElementById('peel-6').innerHTML = 📦 <br><small>${t.peel6}</small>;
        }

        // تفاعل اختيار القشور (تفعيل العنصر المختار)
        document.querySelectorAll('.peel-option').forEach(item => {
            item.addEventListener('click', () => {
                document.querySelectorAll('.peel-option').forEach(opt => opt.classList.remove('active'));
                item.classList.add('active');
            });
        });
    </script>
</body>
</html>
