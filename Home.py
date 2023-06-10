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
    "Projects": "Project",
    "Hire Me": "Hire",
    "Contact Me": "Contact",
    "Call (Mobile)": "tel:+254741945883",
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
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("About Myself")
st.write(
    """
- Back in 2017, when I was joining the University, I had no idea what or how to use a computer felt like.
I had no interest either in knowing it, or coming across to use one. All I trusted was my mobile phone (android 4.4.1)
That was really cool from my perspective in life. 
And, then, boom, there was a first unit in my course that sounded like 'Introduction to IT' whaat! that really got me unaware.
But, still, at least i could tell myself, "i will use those things in the labs". But things got more serious than that!
Until one day I found myself requesting for a laptop ...
....
I have progressed from that point, and came to fall in real Love with IT, I immediately decided to follow youtube channels for windows form applications development in C#
ALL THE WAY up to when I joined ALX, i have done a tremendeous progress and achieved several milestones....
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Challenges")
st.write(
    """
- 👩‍💻 Programming may have sounded easy or ('A nightmare'). When I joined ALX, I only had an ambition of gaining a title, a title which I tought I did not have to strain or go 
an extra mile in earning it. But things turned out to be really "Hard things." 
I anticipated to find PHP,(plenty of it) but that has not been the case. 
iI foound myselft struggling to understand Python, after realizing that I had to make this page (Portfolio) in python!
I strambled here and there, serving more than one master, (side hustle job, casual jobs and ALX). 
This has been the biggest challenges I have had so far. and so I might not have mastered all the techs but ALX has offered me MORE THAN I COULD IMAGINE
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Collaboration")
st.write("""
I must say that truelly, i might have been busy but I gave in all I had for my team always, working on all projects as a team, 
and having to stay up on time with other outside activities for life sustainability. It might have looked very tough on me.. but yeah, it was.

         """)

# --- JOB 1
st.write('\n')
st.subheader("Project Updates")
st.write(
    """
- ► There is going to be tramendeous and robust adjustments to this project.
- Just like the vision I had while joining ALX, I am goin to make my best out of this too.
- With the current progress, there will be other changes, from suggestions and bugs (if there may be)

I would say, I give myself a 9/10 for this progress.
Because, It has been toughm starting from scratch but still had to make it count, given the limited time I had.
By the end of the timeline (deadline on MVP), this project would have reached a tramendeous stage, and would be out for the would to see.
"""
)
