import streamlit as st
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import re

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

/* Background */
body {
    background: linear-gradient(135deg, #141E30, #243B55);
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f2027, #203a43, #2c5364);
}

/* Card */
.sidebar-card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
}

/* Profile */
.profile {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    margin-bottom: 10px;
}

/* Name */
.sidebar-name {
    font-size: 20px;
    font-weight: bold;
    color: white;
}

/* Role */
.sidebar-role {
    font-size: 14px;
    color: #00c6ff;
    margin-bottom: 10px;
}

/* Contact */
.sidebar-contact {
    font-size: 13px;
    color: #ddd;
    margin-bottom: 15px;
}

/* Social icons */
.sidebar-social {
    display: flex;
    justify-content: center;
    gap: 15px;
}

.sidebar-social img {
    width: 25px;
    transition: 0.3s;
}

.sidebar-social img:hover {
    transform: scale(1.2);
}

/* Resume button */
.resume-btn {
    display: block;
    margin-top: 15px;
    padding: 10px;
    border-radius: 10px;
    background: linear-gradient(135deg,#ff6a00,#ee0979);
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.resume-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(255,106,0,0.8);
}

/* Navigation styling */
section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-weight: 500;
}
         
/* Card */
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Input fields */
input, textarea {
    border-radius: 10px !important;
    border: 2px solid #ccc !important;
}

input:focus, textarea:focus {
    border: 2px solid #00c6ff !important;
    box-shadow: 0 0 10px rgba(0,198,255,0.7) !important;
    outline: none !important;
}

/* Button Style */
/* 🎯 Target BOTH normal + form buttons */
div.stButton > button:first-child,
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* Hover */
div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    transform: scale(1.08);
    box-shadow: 0 0 20px rgba(255, 106, 0, 0.8);
}

/* Click */
div.stButton > button:active,
div[data-testid="stFormSubmitButton"] > button:active {
    transform: scale(0.95);
}
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

import base64

def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_image("profile.jpeg")

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
    <a href="https://github.com/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
    </a>
</div>

<a href="#" class="resume-btn">📥 Download Resume</a>

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

        st.header("🎯 Career Objective")
        st.write("Aspiring Data Analyst seeking to leverage analytical skills and tools like Python, SQL, and Power BI to solve real-world business problems and drive data-driven decisions.")

        st.header("💡 Why Hire Me?")
        st.write("""
        ✔ Strong analytical skills  
        ✔ Real-world project experience  
        ✔ Dashboard creation  
        ✔ Quick learner  
        """)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st_lottie(lottie_home, height=300)

    # Chart
    st.header("📊 Skills Overview")

    data = {
        "Skills": ["Python", "SQL", "Power BI", "Excel", "Visualization"],
        "Level": [90, 85, 80, 88, 87]
    }

    fig = px.bar(data, x="Skills", y="Level", text="Level", color="Skills")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)"),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)")
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# PROJECTS
# -----------------------------------
elif menu == "Projects":

    st.title("📂 Projects")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🚖 OLA Ride Analytics")
    st.write("""
        ✔ Analyzed ride demand, revenue, cancellations  
        ✔ Built interactive dashboard using Streamlit  
        ✔ Tools: Python, SQL  
        """)

    st.success("📈 Impact: Improved demand insights")

    st.subheader("🐦 Bird Vision Analytics")
    st.write("""
        ✔ Analyzed bird species and habitat trends  
        ✔ Built interactive analytics platform  
        ✔ Tools: Python, SQL, Streamlit  
        """)
    st.success("📈 Impact: Conservation insights")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# EXPERIENCE
# -----------------------------------
elif menu == "Experience":

    st.title("💼 Experience")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Data Analyst Intern — Labmentix")
    st.write("""
        ✔ Worked on real datasets  
        ✔ Performed EDA and data cleaning  
        ✔ Generated business insights  
        """)

    st.subheader("Web Dev Intern — LetsGrowMore")
    st.write("""
        ✔ Built responsive web applications  
        ✔ Improved debugging and UI skills  
        """)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------
# EDUCATION
# -----------------------------------
elif menu == "Education":

    st.title("🎓 Education")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
    🎓 B.Sc. — Himalayan Garhwal University  
    🏫 12th — Govt. School  
    🏫 10th — Holy Child School  
    """)

    st.header("📜 Certifications")
    st.write("""
        ✔ Data Science — Udemy  
        ✔ Python — Great Learning  
        ✔ Full Stack Development — AttainU  
        ✔ AI Tools — Be10x  
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