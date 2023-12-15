import streamlit as st
from streamlit_timeline import timeline
import json
from datetime import datetime

st.set_page_config(
    page_title="Kunal Goel",
    page_icon="https://raw.githubusercontent.com/kunalsmile/kunalgoel/0b29e507525a196591f275232c54a7113043993b/resume_image.png",
    layout="wide"
)

st.header("About me")
st.write("Engineering Manager with enriched experience in developing enterprise applications and motivating individuals. Experience in frontend and backend technologies -AWS Services, Core Java, .NET, Postgres, MSSQL AWS Services, NodeJS. Core strength in improving customer satisfaction through high quality software. Always looking to expand skill set and searching for new learning opportunities. Built different metrics to look for opportunities to improve.")
st.divider()

def professional_timeline():
    st.header("Professional Timeline")
    with open('./data/professional_timeline.json', "r") as f:
        data = f.read()
        pro = json.loads(data)
        today = datetime.today()
        
        for i in range(len(pro["events"])):
            if pro["events"][i]["end_date"]["year"] == "0":
                pro["events"][i]["end_date"]["year"] = today.year
                pro["events"][i]["end_date"]["month"] = today.month             
                
    timeline(pro)


def educational_timeline():
    st.header("Educational Timeline")
    with open('./data/educational_timeline.json', "r") as f:
        data = f.read()
    timeline(data)


def createSidebar():
    st.sidebar.image("https://raw.githubusercontent.com/kunalsmile/kunalgoel/0b29e507525a196591f275232c54a7113043993b/resume_image.png")
    st.sidebar.header("Kunal Goel")
    st.sidebar.write("Engineering manager with 16+ years of experience in high quality enterprise application development and management.")
    st.sidebar.write(":email: kunalsmile@gmail.com")
    st.sidebar.write(":iphone: +919986010491")
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/goelkunal/)")
    with open("KunalGoelResume.docx", "rb") as file:
        btn = st.sidebar.download_button(
            label="Download resume",
            data=file,
            file_name="KunalGoel.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
          )

def create_skill():
    st.header("Skills")
    languageColumn, technologyColumn, toolsColumn = st.columns(3)
    languageColumn.info("Languages & Platforms")
    technologyColumn.info("Technologies")
    toolsColumn.info("Tools")
    with open('./data/skills.json', "r") as f:
        data = f.read()
    skills = json.loads(data)
    for skill in skills["languages"]:
        languageColumn.button(skill["skill"])
    for tool in skills["tools"]:
        toolsColumn.button(tool["skill"])    


create_skill()
professional_timeline()
st.divider()

st.divider()
educational_timeline()
st.divider()
createSidebar()
