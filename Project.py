from datetime import date
import os
import glob as glob
import streamlit as st
import pathlib
import re


PROFILE_IMAGE="https://omdena.com/wp-content/uploads/2023/02/Munich-Germany-Chapter.png"


BACKGROUND_IMAGE="https://omdena.com/wp-content/uploads/2023/02/Deepfakes-detection-480x400.png"

PAGE_TITLE="Detecting Deepfakes in Germany through Images"

FOOTER_TEXT=f"Project by Omdena Münich, Germany Chapter - {date.today().year}"

def get_page_title_id():
  s = re.sub(r"[^\w\s]", '', PAGE_TITLE)
  s = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', s)
  s = re.sub(r"\s+", '-', s)
  return s.lower()
    
def page_header(): 
    HEADER_STYLE=f"""<style>
	    [data-testid="stToolbar"]{{
	    visibility: hidden;
	    top: -50px;
	    }}
            #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div > div > div > div > div
            {{
            height: 300px;
            width: 300px;
            }}
            #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div > div > div > div > div > img
            {{
            height: 300px;
            width: 300px;
            padding-top: 40%;
            padding-bottom: 10%;
            padding-left: 15%;
            padding-right: 10%;
            }}
            #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div{{
            background-image: url({BACKGROUND_IMAGE});
            background-size: cover; 
            background-position: center;
            }}
            #{get_page_title_id()}{{
            height: 250px;
            }}
            #{get_page_title_id()} > div {{
            bottom: 1%;
            position: absolute;
            color: white;
            }}
            footer {{
            visibility: hidden;
            position: relative;
            }}
            footer:before {{
            visibility: visible;
            position: relative;
	    content: {FOOTER_TEXT}
            }}
            button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {{
            font-size: 24px;
            padding: 0px 20px;
            background-color: rgb(240, 242, 246);
            }}
        </style>
    """
    
    st.markdown(HEADER_STYLE, unsafe_allow_html=True)
    with st.container():
        left_side, right_side = st.columns([1,2], gap="small")
        with left_side:
            st.image(PROFILE_IMAGE, width=300)
        with right_side:
            st.title(PAGE_TITLE)
    st.markdown("")


def about_project():
    HOMEPAGE_CONTENT='''
#####  This project is initiated by the Münich, Germany Chapter to solve Real World Problems.
### The Problem
Deepfake generators have been able to produce imitations almost undetectable through human inspection. Per se, Deepfake detection is one of the notable challenges of digital forensics and media security. They can be used for:
+ Spreading false information and manipulating public opinion.
+ Defaming, harassing, or blackmailing individuals.
+ Damaging the credibility of media information and undermining trust.
+ Spreading fake news, making political propaganda, and manipulating elections.
An artificial intelligence (AI) solution can help identify Deepfake images with accuracy and precision.
### The Goals
The goal of this project is to develop a deep learning model for detecting forgeries in images. 
+ Develop an accurate and reliable deep learning model that can detect deepfake images with **high precision** and **recall**. 
''' 
    with st.container():
        st.markdown(HOMEPAGE_CONTENT)
        
def active_contributors():
    HOMEPAGE_CHAPTERLEAD='''
| Chapter Name | Lead Name |
|--|--|
| Münich, Germany Chapter Leads | Imane El Maakoul |
'''

    HOMEPAGE_ACTIVE_MEMBERS='''
| Task Name | Active Members |
|--|--|
| Data Collection | Parnika Damle, Mussie Berhane, Akash Kundu, Kevin Medri, Vinod Cherian, Mussie Berhane, Abdelrahman Youssry, Qutaiba Ahmed Ansari, Melih yazgan, Saurabh Zinjad  |
| Data-Preprocessing and Cleaning | Rishabh Sabharwal, Imane El Maakoul, Akash Kundu, Saurav Suman, Abdul Rahman, Abdelrahman Youssry, Abdelrahman Rabah |
| Feature Extraction | Vishu Kalier, Imane El Maakoul, Mussie Berhane, Abdelrahman Youssry, Reem Abdel-Salam, Parnika Damle, Qutaiba Ahmed Ansari, Akash Kundu, Abdul Rahman, Rishabh Sabharwal |
| Model Training | Vishu Kalier, Imane El Maakoul, Mussie Berhane, Abdelrahman Youssry, Reem Abdel-Salam, Parnika Damle, Qutaiba Ahmed Ansari, Akash Kundu, Abdul Rahman, Rishabh Sabharwal |
| Model Testing and Validation | Akash Kundu, Reem Abdel-Salam, Parnika Damle, Abdelrahman Youssry, Qutaiba Ahmed Ansari |
| Model Deployment | Vinod, Akash Kundu, Abdelrahman Youssry |
'''

    with st.container():
        st.markdown(HOMEPAGE_CHAPTERLEAD)
        st.markdown("")
        st.markdown(HOMEPAGE_ACTIVE_MEMBERS)
    

def data_source_information():
    DATA_SOURCE_CONTENT='''
### Data Sources / References

The model is trained with datasets produced from the following original data sources:
+ Guarnera, Luca, et al. "The Face Deepfake Detection Challenge." Journal of Imaging 8.10 (2022): 263.
+ Guarnera, Luca, Oliver Giudice, and Sebastiano Battiato. "Fighting deepfake by exposing the convolutional traces on images." IEEE Access 8 (2020): 165085-165098.
+ Giudice, Oliver, Luca Guarnera, and Sebastiano Battiato. "Fighting deepfakes by detecting gan dct anomalies." Journal of Imaging 7.8 (2021): 128.
''' 
    with st.container():
        st.markdown(DATA_SOURCE_CONTENT)

def set_page_settings():
        st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded", 
)

def main():
    page_header()
    set_page_settings()
    project_tab, team_tab, data_source = st.tabs(["  **About Project** ", "  **Active Team Contributors**  ","  **Data Sources** "])
    st.markdown()
    with project_tab:
        about_project()
    
    with team_tab:
        active_contributors()
        
    with data_source:
        data_source_information()

if __name__ == "__main__":
  main()  
    
    

