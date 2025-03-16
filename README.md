# QuickPitch AI 🔮 ✨

## Introduction
QuickPitch AI is an intelligent job application assistant that leverages machine learning to extract job details from career pages, match relevant skills to your portfolio, and generate a cold email to a potential employer. This project integrates Langchain, Groq, and ChromaDB to help you automatically generate tailored internship or job application emails by analyzing job descriptions.

The app provides a streamlined process to enhance your job application experience by analyzing job postings, matching them with your portfolio, and crafting personalized emails.

## What the Project is About
QuickPitch AI performs the following tasks:

- **Job Description Extraction**: Given a URL of a job listing, the app scrapes and extracts details such as the role, required experience, skills, and job description.
- **Portfolio Matching**: Matches the extracted skills from the job listing to a predefined portfolio, providing links to relevant projects and tech stacks.
- **Cold Email Generation**: Based on the job description and portfolio links, the app generates a personalized cold email that can be sent to potential employers, expressing interest in an internship or job role.

## How to Install the Requirements and Run the Code

### Step 1: Clone the Repository
```bash
git clone https://github.com/ArulKevin2004/QuickPitch-AI
cd QuickPitch-AI
```
### Step 2: Set Up Virtual Environment

It's recommended to use a virtual environment to manage the dependencies for this project.

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```
### Step 3: Install Dependencies

Install all the required packages using pip:

```bash
pip install -r requirements.txt
```
  
  You'll need to create an account on GroqCloud and obtain your API key. Follow these steps:
  
  1. Go to [GroqCloud](https://groq.com).
  
  2. Sign up or log in to your account.
  
  3. Once logged in, navigate to the **API** section (usually under your profile settings).
  
  4. Generate a new API key and copy it.

  ### Step 3.1: Create a .env File
  
  In the project root directory, create a file named `.env`.
  
  ```plaintext
  GROQ_API_KEY=your_api_key_here
  ```
  
  ### Step 3.2: Paste Your API Key
  
  Paste the API key you copied from GroqCloud into the `.env` file. The code will automatically load the key when run.

### **Note**
The `portfolio.csv` file contains links to your portfolio projects, tech stack, and other details. You can modify this CSV file to include your own projects.

1. Open the `my_portfolio.csv` file.

2. The file should have at least two columns:
   - **Techstack**: A description of your skills or tech stack.
   - **Links**: A URL to the project or portfolio page.

3. Add or remove rows based on the projects or skills you want to showcase.

  

## Step 4: Run the Streamlit App

Once the dependencies are installed, you can run the app:

```bash
streamlit run app.py
```

## Conclusion

QuickPitch AI is a powerful and intuitive app designed to assist job seekers with automated job application processes. With Groq's language model for extraction, portfolio matching via ChromaDB, and personalized email generation, this app simplifies applying to jobs, especially for internships.

By customizing the prompts and portfolio CSV file, you can adapt QuickPitch AI to your specific needs, whether you're focusing on web development, machine learning, or any other field.

Feel free to modify the code and adapt it further as per your requirements.
