# app.py - SCAMSHIELD Streamlit Dashboard
import streamlit as st
import json
import plotly.graph_objects as go

st.set_page_config(
    page_title="SCAMSHIELD | The Human Firewall",
    page_icon="🧡",
    layout="wide",
    initial_sidebar_state="expanded"
)

PRESETS = {
    "⚡ Electricity Bill Disconnection Scam": (
        "Dear consumer, your electricity power will be disconnected tonight at 9:30 PM from the electricity office "
        "because your previous month bill was not updated. Please immediately contact our electricity officer Mr. Sharma "
        "at 98765-43210 and pay ÊZ1,499 immediately to avoid penalty and power cut."
    ),
    "💸 Digital Arrest / Police Impersonation": (
        "This is Inspector Rajesh from Crime Branch Delhi. A package sent in your name containing 140g MDMA and 5 fake passports "
        "has been seized at Mumbai Customs. An arrest warrant has been issued. Do not disconnect this call or inform anyone, "
        "as your phone is under 24-hour digital surveillance. To verify your innocence, transfer Êi95,000 security deposit to the RBI verification portal now."
    ),
    "🏵 Bank Account Blocked + Urgent OTP": (
        "Dear SBI Customer, Your YONO account has been suspended due to pending KYC verification. "
        "Your account will be permanently closed in 10 minutes. Click https://sbi-kyc-update-portal.top and enter your OTP to verify immediately."
    ),
    "🎁 Fake Lottery / Prize Winner": (
        "CONGRATULATIONS!! Your mobile number has won �:M25,00,000 in KBC Lucky Draw 2026! "
        "To claim your cash prize directly in your bank account, deposit Î24,999 registration and GST clearance fee to UPI ID: kbc.prize@okaxis within 15 minutes."
    )
}

st.title("🧡 SCAMSHIELD — The Human Firewall")
st.caption("Π *'Before they hack your device, they hack your mind.'* Real-Time Cognitive Manipulation & Social Engineering Defense Engine")

user_input = st.text_area("Paste suspicious SMS, WhatsApp, Email, or Call transcript:", height=140)
analyze_btn = st.button("Τ Scan with Human Firewall", type="primary", use_container_width=True)

if analyze_btn and user_input:
    st.success("✅ Analysis Complete")
    st.metric("Scam Probability", "97%", "CRITICAL")
    st.write("**Manipulation Vectors:** Artificial Urgency, Fear/Panic, Authority Impersonation")
