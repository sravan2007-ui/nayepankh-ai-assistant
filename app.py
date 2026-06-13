import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="NayePankh AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize GenAI Client
@st.cache_resource
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("API Key is missing. Please set GEMINI_API_KEY in your .env file.")
        st.stop()
    return genai.Client(api_key=api_key)

client = get_client()

# System Instruction
SYSTEM_INSTRUCTION = """
You are the official NayePankh Foundation AI Assistant.
Your tone should be warm, compassionate, helpful, and inspiring, reflecting the NGO's mission of helping volunteers, donors, and students.
NayePankh Foundation is a non-governmental organization (NGO) in India dedicated to the upliftment of the underprivileged, providing education, meals, and social support.

Help users with:
1. Volunteering: How to join, responsibilities, benefits, and registration.
2. Donations: How donations are used (food, education, shelter), how to contribute, and the impact.
3. Internships: Student internship opportunities, projects, certificates, and learning outcomes.
4. NGO Activities: Teaching drives, food distribution, blood donation camps, and social awareness campaigns.

Keep your answers concise, clear, and action-oriented. Provide positive encouragement for volunteers and donors.
"""

# Custom Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}

/* Header style */
.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(90deg, #FF9933 0%, #138808 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
    text-align: center;
}

.sub-title {
    font-size: 1.1rem;
    color: #555555;
    text-align: center;
    margin-bottom: 25px;
    font-weight: 400;
}

/* Milestone Box Styling */
.stat-box {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 10px;
    border-left: 4px solid #FF9933;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.stat-title {
    font-size: 0.9rem;
    color: #6c757d;
    text-transform: uppercase;
    font-weight: 600;
}

.stat-value {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1c1c1c;
}
</style>
""", unsafe_allow_html=True)

# Dialog Definitions
@st.dialog("Become a Volunteer")
def volunteer_form():
    st.write("Thank you for your interest in volunteering with NayePankh Foundation! Please fill out this short form and our team will get in touch.")
    name = st.text_input("Full Name", placeholder="John Doe")
    email = st.text_input("Email Address", placeholder="john@example.com")
    phone = st.text_input("Phone Number", placeholder="+91 XXXXX XXXXX")
    interest = st.selectbox(
        "Area of Interest",
        [
            "Teaching & Education Support",
            "Food & Meals Distribution",
            "Social Media & Content Creation",
            "Event Planning & Management",
            "Fundraising & Partnership"
        ]
    )
    message = st.text_area("Why do you want to join NayePankh?", placeholder="Tell us a bit about yourself...")
    
    if st.button("Submit Registration", width="stretch"):
        if not name or not email or not phone:
            st.warning("Please fill in all required fields (Name, Email, Phone).")
        else:
            st.success(f"Thank you, {name}! Your registration has been received. Our volunteer coordination team will contact you at {email} within 48 hours.")

@st.dialog("Make a Donation")
def donation_dialog():
    st.write("Your generosity enables us to provide meals, education, and shelter to children in need.")
    
    amount = st.number_input("Donation Amount (INR)", min_value=100, value=1000, step=100)
    purpose = st.selectbox(
        "Direct My Donation To",
        [
            "Daily Meals Distribution (₹50 feeds a child for a day)",
            "Underprivileged Children Education (Books, Uniforms, Fees)",
            "Health & Sanitation Drives",
            "General NGO Development Fund"
        ]
    )
    
    donor_name = st.text_input("Donor Name", placeholder="Anonymous")
    donor_email = st.text_input("Donor Email Address", placeholder="donor@example.com")
    
    st.markdown("### Mock Payment Portal")
    st.info("This is a demo assistant. In a live system, this would redirect you to a secure payment gateway (Razorpay/Paytm).")
    
    if st.button("Proceed to Donate (Mock)", width="stretch"):
        name_to_use = donor_name if donor_name else "Generous Donor"
        st.success(f"Thank you, {name_to_use}! We have recorded a mock donation of ₹{amount} for '{purpose}'. A receipt has been generated.")

@st.dialog("Available Internships")
def internship_dialog():
    st.write("Join our student internship program to gain experience while driving social change. We offer flexible work-from-home and hybrid options.")
    
    st.markdown("""
    ### 📂 Active Internships:
    
    1. **Social Work & Field Coordinator** (Duration: 2-6 months)
       - **Role**: Plan local educational drives and food distribution camps.
       - **Benefits**: Performance certificate, flexible workspace, leadership training.
       
    2. **Creative Content Writer** (Duration: 1-3 months)
       - **Role**: Write blog posts, newsletters, and social media copy to raise awareness.
       - **Benefits**: Internship certificate, portfolio-building support.
       
    3. **Human Resources & Admin Coordinator** (Duration: 2 months)
       - **Role**: Assist in screening, interviewing, and onboarding new volunteers.
       - **Benefits**: HR training certificate, LOR based on performance.
    """)
    
    st.markdown("---")
    st.write("To apply, write a message in the chat assistant saying: **'I want to apply for the [Internship Name] internship'** or contact our HR team via email.")

# Sidebar setup
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>NayePankh Foundation</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Empowering lives, spreading wings of hope.</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Key NGO Milestones")
    
    st.markdown("""
    <div class="stat-box">
        <div class="stat-title">Volunteers Mobilized</div>
        <div class="stat-value">5,000+</div>
    </div>
    <div class="stat-box">
        <div class="stat-title">Meals Distributed</div>
        <div class="stat-value">50,000+</div>
    </div>
    <div class="stat-box">
        <div class="stat-title">Interns Supported</div>
        <div class="stat-value">1,200+</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Quick Operations")
    
    if st.button("🌱 Become a Volunteer", width="stretch"):
        volunteer_form()
        
    if st.button("💝 Support with Donation", width="stretch"):
        donation_dialog()
        
    if st.button("🎓 Active Internships", width="stretch"):
        internship_dialog()

# Main page banner
if os.path.exists("banner.png"):
    st.image("banner.png", width="stretch")

st.markdown("<h1 class='main-title'>🤖 NayePankh AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your gateway to volunteering, donation inquiries, student internships, and NGO activities.</p>", unsafe_allow_html=True)

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Quick Starter Buttons (Only show when there are no messages)
if len(st.session_state.messages) == 0:
    st.markdown("### How can we help you today? 👋")
    st.write("Select one of the topics below to get started immediately, or type your question in the chat bar.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌱 Tell me how I can volunteer for teaching children", width="stretch"):
            st.session_state.messages.append({"role": "user", "content": "How can I volunteer for teaching children?"})
            st.rerun()
        if st.button("🎓 What internships are available for college students?", width="stretch"):
            st.session_state.messages.append({"role": "user", "content": "What internships are available for college students?"})
            st.rerun()
    with col2:
        if st.button("💝 Where and how do donations get utilized?", width="stretch"):
            st.session_state.messages.append({"role": "user", "content": "Where and how do donations get utilized?"})
            st.rerun()
        if st.button("📢 What campaigns is NayePankh running currently?", width="stretch"):
            st.session_state.messages.append({"role": "user", "content": "What campaigns is NayePankh running currently?"})
            st.rerun()

# Chat Input
prompt = st.chat_input("Ask about volunteering, donations, internships...")

if prompt:
    # Append user prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Rerun to show user message instantly in history loop
    st.rerun()

# Check if the last message is from user (which means assistant needs to reply)
if len(st.session_state.messages) > 0 and st.session_state.messages[-1]["role"] == "user":
    with st.spinner("Generating response..."):
        try:
            # Format history for Gemini API
            contents = []
            for msg in st.session_state.messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
            
            # Request response from model (we use gemini-2.5-flash which is widely supported and active)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION
                )
            )
            
            answer = response.text
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()
        except Exception as e:
            st.error(f"Error calling Gemini API: {str(e)}")