import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@st.cache_resource
def get_data():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("GK Questions").sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# App UI
st.set_page_config(page_title="CA/GK", layout="centered")
st.title("Current Affairs and General Knowledge")

df = get_data()

for i, row in df.iterrows():
    with st.expander(f"Q{i+1}: {row['Question']}"):
        st.write(f"A) {row['Option A']}")
        st.write(f"B) {row['Option B']}")
        st.write(f"C) {row['Option C']}")
        st.write(f"D) {row['Option D']}")
        with st.expander("Show Answer"):
            st.success(f"✅ Correct Answer: {row['CorrectAnswer']}")
