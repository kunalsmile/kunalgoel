import streamlit as st
from streamlit_timeline import timeline
import json
from datetime import datetime, date
from dateutil.relativedelta import relativedelta



st.set_page_config(
    page_title="Kunal Goel",
    page_icon="https://raw.githubusercontent.com/kunalsmile/kunalgoel/0b29e507525a196591f275232c54a7113043993b/resume_image.png",
    layout="wide",
    initial_sidebar_state=st.session_state.get('sidebar_state', 'expanded'),
)

@st.cache_data(ttl=86400)  # Cache expires every 24 hours
def get_data():
    return None

get_data()
today = datetime.today()

def closeSidebar(status):
    st.session_state.sidebar_state = status

st.header("About me")
st.write("Engineering Manager with enriched experience in developing enterprise applications and motivating individuals. Experience in frontend and backend technologies -AWS Services, Core Java, .NET, Postgres, MSSQL AWS Services, NodeJS. Core strength in improving customer satisfaction through high quality software. Always looking to expand skill set and searching for new learning opportunities. Built different metrics to look for opportunities to improve.")

expander = st.expander("Key Highlights")
with open('./data/highlights.html', "r") as f:
    data = f.read()
    expander.markdown(data, unsafe_allow_html=True)
st.divider()

def professional_timeline():
    st.header("Professional Timeline")
    with open('./data/professional_timeline.json', "r") as f:
        data = f.read()
        pro = json.loads(data)
        for i in range(len(pro["events"])):
            if pro["events"][i]["end_date"]["year"] == "0":
                pro["events"][i]["end_date"]["year"] = today.year
                pro["events"][i]["end_date"]["month"] = today.month             
                
    timeline(pro)
    st.divider()


def educational_timeline():
    st.header("Educational Timeline 📖")
    with open('./data/educational_timeline.json', "r") as f:
        data = f.read()
    timeline(data)
    st.divider()




def createSidebar():
    startDate =  date(2007, 2, 1)
    difference = relativedelta(today, startDate)
    # st.sidebar.button("Close sidebar",on_click=closeSidebar('collapsed'))
    if difference.months >= 10:
        difference.years += 1
    st.sidebar.image("https://raw.githubusercontent.com/kunalsmile/kunalgoel/0b29e507525a196591f275232c54a7113043993b/resume_image.png")
    st.sidebar.header("Kunal Goel")
    # st.sidebar.write("Engineering manager with " + str(difference.years) + " years of experience in high quality enterprise application development and management.")
    st.sidebar.write("A seasoned Software Development Manager with over " + str(difference.years) + " years of experience in the realm of high-quality enterprise application development and management. Specialized in ecommerce platforms technologies, I have a proven track record of leading and mentoring high-performing teams. My leadership is deﬁned by a steadfast commitment to delivering exceptional results, making me an invaluable asset to any team seeking to elevate their engineering projects to new heights of success.")
    st.sidebar.write(":email: kunalsmile@gmail.com")
    st.sidebar.write(":iphone: +919986010491")
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/goelkunal/)")
    st.sidebar.write("[Github](https://github.com/kunalsmile)")
    with open("KunalGoelResume.docx", "rb") as file:
        btn = st.sidebar.download_button(
            label="Download resume",
            data=file,
            file_name="KunalGoel.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
          )

def create_skill():
    st.header("Skills ⚒️")
    languageColumn, toolsColumn = st.columns(2)
    languageColumn.info("Languages & Platforms")
    toolsColumn.info("Tools")
    
    with open('./data/skills.json', "r") as f:
        data = f.read()
    skills = json.loads(data)
    for skill in skills["languages"]:
        languageColumn.image(skill["imageUrl"], width=100, caption=skill["skill"])
    for tool in skills["tools"]:
        toolsColumn.image(tool["imageUrl"], width=100, caption=tool["skill"])
        
    methods = ""
    for method in skills["methodologies"]:
        methods += "<ul><div style='box-shadow: 2px 2px 20px 23px #7fecad;border-radius: 4px;padding: 10px;background-color: #2ecc71; width: 50%'>" + method["skill"] + "</div></ul>"

    st.header("Other Skills")    
    st.markdown(methods, unsafe_allow_html=True)
    st.divider()

create_skill()
professional_timeline()
educational_timeline()
createSidebar()
