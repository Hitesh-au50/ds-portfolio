import streamlit as st
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import re
import base64

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Hitesh | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# LOAD LOTTIE
# -----------------------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_home = load_lottie("https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json")
lottie_contact = load_lottie("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")

# -----------------------------------
# EMAIL FUNCTION
# -----------------------------------
def send_email(name, email, message):
    sender_email = "hiteshverma3666@gmail.com"
    sender_password = "oflk ecjf hsoy rwtw"

    receiver_email = "hiteshverma3666@gmail.com"

    msg = MIMEText(f"""
    Name: {name}
    Email: {email}
    Message: {message}
    """)

    msg["Subject"] = "New Message From Portfolio"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

# -----------------------------------
# CSS (ULTRA PREMIUM UI)
# -----------------------------------

st.markdown("""
<style>

/* ===============================
   🌌 GLOBAL BACKGROUND (ANIMATED)
=============================== */
html, body, [class*="css"]  {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #141E30);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Smooth Animation */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===============================
   📌 SIDEBAR (PREMIUM LOOK)
=============================== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f2027, #203a43, #2c5364);
    padding: 10px;
}

/* Sidebar Card */
.sidebar-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 25px;
    text-align: center;

    backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.15);

    box-shadow: 0 0 30px rgba(0,198,255,0.25);
}

/* Profile Image (Glow Ring) */
.profile {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 3px solid #00c6ff;
    padding: 3px;

    box-shadow: 0 0 25px #00c6ff;
    margin-bottom: 10px;
}

/* Sidebar Text */
.sidebar-name {
    font-size: 22px;
    font-weight: bold;
    color: white;
}

.sidebar-role {
    font-size: 14px;
    color: #00c6ff;
    margin-bottom: 10px;
}

.sidebar-contact {
    font-size: 13px;
    color: #ddd;
    margin-bottom: 15px;
}

/* Social Icons */
.sidebar-social {
    display: flex;
    justify-content: center;
    gap: 15px;
}

.sidebar-social img {
    width: 26px;
    transition: 0.3s ease;
}

.sidebar-social img:hover {
    transform: scale(1.3) rotate(5deg);
}

/* ===============================
   💎 CARDS (GLASS UI)
=============================== */
.card {
    background: rgba(255, 255, 255, 0.06);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 25px;

    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);

    transition: all 0.4s ease;
}

/* Hover Glow */
.card:hover {
    transform: translateY(-10px) scale(1.01);
    box-shadow: 0 15px 40px rgba(0, 198, 255, 0.4);
}

/* ===============================
   🚀 SKILLS SECTION
=============================== */
.skill-category {
    font-size: 20px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #00c6ff;
}

/* Skill Card */
.skill-card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 12px;

    border: 1px solid rgba(255,255,255,0.08);

    transition: all 0.3s ease;
}

.skill-card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0 10px 30px rgba(0,198,255,0.4);
}

/* Skill Name */
.skill-name {
    font-weight: 500;
    margin-bottom: 8px;
}

/* Percentage */
.skill-percent {
    float: right;
    font-size: 12px;
    color: #ccc;
}

/* Progress Bar */
.progress-container {
    width: 100%;
    height: 10px;
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(270deg, #00c6ff, #0072ff, #00c6ff);
    background-size: 400% 400%;
    animation: progressAnim 4s ease infinite;
}

/* Animation */
@keyframes progressAnim {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ===============================
   ✏️ INPUT FIELDS
=============================== */
input, textarea {
    border-radius: 12px !important;
    border: 2px solid #ccc !important;
    transition: 0.3s;
}

input:focus, textarea:focus {
    border: 2px solid #00c6ff !important;
    box-shadow: 0 0 12px rgba(0,198,255,0.7) !important;
    outline: none !important;
}

/* ===============================
   🎯 BUTTONS (GLOBAL)
=============================== */
div.stButton > button:first-child,
div[data-testid="stFormSubmitButton"] > button {

    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;

    border: none;
    padding: 12px 28px;
    border-radius: 12px;

    font-weight: 600;
    transition: all 0.3s ease;
}

/* Hover */
div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background: linear-gradient(135deg, #ff6a00, #ee0979);
    transform: scale(1.08);

    box-shadow: 0 0 25px rgba(255, 106, 0, 0.8);
}

/* Click */
div.stButton > button:active,
div[data-testid="stFormSubmitButton"] > button:active {
    transform: scale(0.95);
}

/* ===============================
   📊 SCROLLBAR (BONUS PREMIUM)
=============================== */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #1c1c1c;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#00c6ff, #0072ff);
    border-radius: 10px;
}

/* ===============================
   📌 NAVIGATION TEXT
=============================== */
section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-weight: 500;
}
            


/* 🔥 FORCE APPLY BUTTON STYLE */
.resume-wrapper {
    margin-top: 20px;
}

/* Strong selector to override Streamlit */
section[data-testid="stSidebar"] .resume-wrapper a.resume-btn {
    display: block !important;
    width: 100% !important;
    text-align: center !important;

    padding: 8px !important;
    border-radius: 14px !important;

    background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
    color: white !important;

    font-weight: bold !important;
    text-decoration: none !important;

    transition: all 0.3s ease !important;
}

/* Hover */
section[data-testid="stSidebar"] .resume-wrapper a.resume-btn:hover {
    background: linear-gradient(135deg, #ff6a00, #ee0979) !important;
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(255, 106, 0, 0.9);
}

/* Click */
section[data-testid="stSidebar"] .resume-wrapper a.resume-btn:active {
    transform: scale(0.95);
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# SIDEBAR
# -----------------------------------


def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_image("profile.jpeg")

def get_base64_file(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

resume_base64 = get_base64_file("resume.pdf")

st.sidebar.markdown(f"""
<div class="sidebar-card">

<img src="data:image/jpeg;base64,{img_base64}" class="profile">

<div class="sidebar-name">Hitesh</div>
<div class="sidebar-role">Data Analyst</div>

<div class="sidebar-contact">
📞 +91 9350408017 <br>
📧 hiteshverma3666@gmail.com
</div>

<div class="sidebar-social">
    <a href="https://www.linkedin.com/in/hitesh-8b9759251/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
    </a>
    <a href="https://github.com/Hitesh-au50" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
    </a>
</div>

<!-- 🔥 FIXED BUTTON -->
<div class="resume-wrapper">
    <a href="data:application/pdf;base64,{resume_base64}" 
       download="Hitesh_Data_Analyst_Resume.pdf"
       class="resume-btn">
       📥 Download Resume
    </a>
</div>

</div>
""", unsafe_allow_html=True)

# Divider
st.sidebar.markdown("---")

# Navigation (clean + professional)
menu = st.sidebar.radio(
    "📌 Navigation",
    ["Home", "Projects", "Experience", "Education", "Contact"]
)

# -----------------------------------
# HOME
# -----------------------------------
if menu == "Home":

    col1, col2 = st.columns([2,1])

    with col1:
        st.title("📊 Data Analyst Portfolio")
        st.write("### Transforming Data into Business Insights")

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("🎯 Professional Summary")
        st.write("""
        Results-driven Data Analyst with hands-on experience in Python, SQL, and Power BI. 
        Skilled in data cleaning, exploratory data analysis (EDA), and dashboard development. 
        Proven ability to transform raw data into actionable insights, improving decision-making 
        and business performance.
        """)

        st.header("💡 Why Hire Me?")
        st.write("""
        ✔ Strong analytical skills  
        ✔ Real-world project experience  
        ✔ Dashboard creation  
        ✔ Quick learner  
        """)

        st.markdown('</div>', unsafe_allow_html=True)

        st.header("💪 Strengths")
        st.write("""
        ✔ Strong analytical thinking  
        ✔ Attention to detail  
        ✔ Effective communication  
        ✔ Fast learner & adaptable  
        """)

    with col2:
        st_lottie(lottie_home, height=300)

    # Chart
    st.header("🚀 Skills & Expertise")

    # -------------------------
    # SKILLS DATA (CATEGORIZED)
    # -------------------------
    skills = {
        "💻 Programming": {
            "Python (Pandas, NumPy)": 90,
        },
        "📊 Data Visualization": {
            "Power BI": 80,
            "Matplotlib": 75,
            "Seaborn": 75,
        },
        "🗄 Databases": {
            "SQL": 85,
            "MongoDB": 70,
        },
        "🛠 Tools & Platforms": {
            "Excel": 88,
            "Git & GitHub": 80,
            "Streamlit": 85,
            "Jupyter Notebook": 90
        }
    }

# -------------------------
# DISPLAY UI
# -------------------------
    for category, items in skills.items():

            st.markdown(f'<div class="skill-category">{category}</div>', unsafe_allow_html=True)

            for skill, level in items.items():
                st.markdown(f"""
                <div class="skill-card">
                    <div class="skill-name">
                        {skill}
                        <span class="skill-percent">{level}%</span>
                    </div>
                    <div class="progress-container">
                        <div class="progress-bar" style="width:{level}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# -----------------------------------
# PROJECTS
# -----------------------------------
elif menu == "Projects":

    st.title("📂 Projects")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🚖 OLA Ride Analytics Dashboard")
    st.write("""
    ✔ Analyzed 10K+ ride records using Python & SQL  
    ✔ Identified peak demand hours and reduced cancellations by ~15%  
    ✔ Built interactive dashboards for KPI tracking  
    """)

    st.subheader("🐦 Bird Vision Analytics")
    st.write("""
    ✔ Analyzed large bird dataset for habitat trends  
    ✔ Built Streamlit app for data accessibility  
    ✔ Generated insights supporting conservation decisions  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# EXPERIENCE
# -----------------------------------
elif menu == "Experience":

    st.title("💼 Experience")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Data Analyst Intern — Labmentix (Mar 2026 – Aug 2026)")
    st.write("""
    ✔ Cleaned and processed datasets, improving data quality by ~25%  
    ✔ Conducted EDA, reducing manual analysis time by 30%  
    ✔ Built Power BI dashboards, improving reporting efficiency by 40%  
    ✔ Delivered data-driven insights for business decisions  
    """)

    st.subheader("💻 Web Development Intern — LetsGrowMore (Aug 2023)")
    st.write("""
    ✔ Developed responsive web apps, improving performance by ~20%  
    ✔ Optimized code and reduced load time  
    ✔ Collaborated in team-based project delivery  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# EDUCATION
# -----------------------------------
elif menu == "Education":

    st.title("🎓 Education")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
    🎓 **Bachelor of Science (B.Sc.)**  
    Himalayan Garhwal University (2021–2024)  

    🏫 Intermediate — Govt. Sec. Sr. School, Kaunt (2021)  
    🏫 Matriculation — Holy Child High School (2019)  
    """)

    st.header("📜 Certifications")
    st.write("""
    ✔ Data Science — Udemy  
    ✔ Python — Great Learning  
    ✔ Full Stack Development — AttainU  
    ✔ AI Tools & ChatGPT — Be10x  
    ✔ Open Weaver & TORC Badges  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# CONTACT
# -----------------------------------

elif menu == "Contact":

    st.title("📬 Contact Me")

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown("### ✉️ Send me a message")

        # FORM (INSIDE COLUMN + CARD)
        with st.form("contact_form", clear_on_submit=True):

            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            submit = st.form_submit_button("🚀 Send Message")

        st.markdown('</div>', unsafe_allow_html=True)

        # Email validation function
        import re
        def is_valid_email(email):
            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            return re.match(pattern, email)

        # AFTER FORM SUBMIT (outside form)
        if submit:

            if not name or not email or not message:
                st.warning("⚠️ Please fill all fields")

            elif not is_valid_email(email):
                st.error("❌ Please enter a valid email address")

            else:
                with st.spinner("Sending message..."):
                    success = send_email(name, email, message)

                if success:
                    st.success("✅ Message sent successfully!")
                    st.toast("Message sent 🎉")
                else:
                    st.error("❌ Failed to send message")

    # RIGHT SIDE (OPTIONAL ANIMATION / INFO)
    with col2:
        st_lottie(lottie_contact, height=300)

        st.info("💡 I usually respond within 24 hours.")

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.write("📧 Or email directly: hiteshverma3666@gmail.com")

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
current_year = datetime.now().year
st.write(f"© {current_year} Hitesh | Data Analyst Portfolio")

