from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jose Sigawa| Portfolio"
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
}
PROJECTS = {
    "🏆 TreelifeCleaners Ltd - A cleaning company, with online service booking, client management and admin dashboard - designed with PHP, MySQL": "https://treelifecleaners.transforceholdings.co.ke",
    "🏆 Transforce Holdings ltd - Web app for logistics company with admin dashboard, using PHP, Ajax, MySQL database": "https://transforceholdings.co.ke",
    "🏆 SpecialcareHealthcare - A pharmacy management system (content) with POS and Clinic, in PHP, MySQL with user settings & menubar and admin dashbaord": "https://facebook.com/sigawaPHPpoint/",
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
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years in website development and Windows applications
- ✔️ Strong hands on experience and knowledge in PHP, Python, MsAccess, Excel ...
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA, PHP (Laravel,codeignitor)
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Project Manager | Karibuwebdev**")
st.write("February 2020 - current ")
st.write(
    """
- ► Project team lead
- ► Accomplished most recent projects under my supervision
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Computer Expert and Repair Technician | Fakhri Bits & Byrtes**")
st.write("January 2021 - February 2022")
st.write(
    """
- ► Read and interpret data to participate in data quality review and troubleshooting activities 
- ► Software installation and development
- ► Basic knowledge API guidelines for instrumentation
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Full Stack Web Developer | karibuwebdev**")
st.write("April 2017 – to date")
st.write(
    """
- ► Developed and achieved several milestones along the web development
Industry

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
