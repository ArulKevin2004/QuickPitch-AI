import streamlit as st
import uuid
import chromadb
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ API Key is missing!")

# Set up the Streamlit page
st.title("QuickPitch AI 🔮 ✨")

# Input for scraping a URL
url = st.text_input("Enter a job URL", "https://careers.nike.com/director-supply-chain-ai-ml-engineering/job/R-45852")

# Initialize Langchain-Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=api_key
)

prompt_extract = PromptTemplate.from_template("""
    #### SCRAPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTION:
    The scraped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containing the following keys: 'role', 'experience', 'skills' and 'description'.
    Only return the valid JSON.
    #### VALID JSON (NO PREAMBLE):
""")
chain_extract = prompt_extract | llm

if st.button("Extract Job Details"):
    if url:
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content
        res = chain_extract.invoke(input={"page_data": page_data})
        json_parser = JsonOutputParser()
        json_res = json_parser.parse(res.content)
        job = json_res
        st.write("Job details extracted successfully:", job)

        # Load portfolio data
        df = pd.read_csv("my_portfolio.csv")
        collection = chromadb.PersistentClient('vectorstore').get_or_create_collection(name="portfolio")

        if not collection.count():
            for _, row in df.iterrows():
                collection.add(documents=row["Techstack"],
                               metadatas={"links": row["Links"]},
                               ids=[str(uuid.uuid4())])

        links = collection.query(query_texts=job['skills'], n_results=2).get('metadatas', [])
        st.write("Relevant links from portfolio:", links)

        # Create email prompt
        prompt_email = PromptTemplate.from_template("""
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Arulkevin J, a Student from PSG College of Technology, who is particularly interested in exploring fields such as Web Development, cloud computing and machine learning.
            Your job is to write a cold email to the client asking for an internship regarding the job mentioned above describing the capability of Arulkevin in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Arulkevin's portfolio: {link_list}
            Remember you are Arulkevin J, Student at PSG College of Technology. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
        """)

        chain_mail = prompt_email | llm
        res = chain_mail.invoke({"job_description": str(job), "link_list": links})

        # Make "Generated Cold Email" a subheading and add emojis
        st.markdown("## ✉️ **Generated Cold Email**")
        st.code(res.content, language='text')
    else:
        st.error("Please provide a valid URL.")
