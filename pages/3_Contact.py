from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
css_file1 = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jose Sigawa| Contact"
PAGE_ICON = ":smile:"
NAME = "Joseph Sigawa"
DESCRIPTION = """
Software Engineer, (excellent web developer): assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "sigawajoseph1@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/joseph-sigawa/",
    "GitHub": "https://github.com/Jos254Kenya/",
    "Twitter": "https://twitter.com/sigawa_jose",
    "Mobile": "tel:+254741945883",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 See My Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
# --- EXPERIENCE & QUALIFICATIONS ---

contact_form = """
<form action="https://formsubmit.co/sigawajoseph1@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""


st.markdown(contact_form, unsafe_allow_html=True)


# Use Local CSS File
with open(css_file1) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
