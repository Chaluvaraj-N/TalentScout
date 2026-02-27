👔 TalentScout – AI-Powered Hiring Assistant Chatbot

TalentScout is an intelligent AI-powered chatbot built using Python, Streamlit, and Large Language Models (LLMs) that automates the initial candidate screening process for technical roles.

Unlike traditional fixed-question systems, TalentScout dynamically generates 3–5 tailored technical interview questions per technology based on the candidate’s declared tech stack.

📋 Project Overview

TalentScout is designed to streamline and modernize the initial hiring workflow by:

🤖 Automating candidate screening

🧠 Dynamically generating tech-specific interview questions

📊 Maintaining context-aware conversations

🔐 Handling candidate data securely within session

💼 Delivering a professional recruiter-like experience

⭐ Key Capabilities
🔄 Multi-Step Intelligent Conversation Flow

Greeting → Information Collection → Tech Stack Analysis → Dynamic Technical Questions → Graceful Exit

🧾 Structured Candidate Data Collection

Full Name

Email Address (validated)

Phone Number

Years of Experience

Desired Position

Current Location

Tech Stack

🧠 Dynamic Technical Question Generation

3–5 questions per technology

Medium-level difficulty

Technology-specific

No generic or irrelevant questions

💬 Context Retention

Uses Streamlit session_state

Maintains full conversation history

Handles follow-ups smoothly

🛑 Smart Exit Handling

Recognizes:

exit, quit, bye, thank you, stop, end

Ends conversation professionally.

🚀 Installation Steps
🔹 Prerequisites

Python 3.8 or higher

OpenAI API Key

🔹 Step-by-Step Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/talentscout-chatbot.git
cd talentscout-chatbot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Environment Variables

Create .env file:

OPENAI_API_KEY=your_actual_api_key_here
4️⃣ Run the Application
streamlit run app.py

The app runs at:

http://localhost:8501
📖 Usage Instructions
👤 For Candidates

1️⃣ The chatbot greets you automatically

2️⃣ Provide information step-by-step:

Full Name

Email

Phone

Experience

Desired Role

Location

3️⃣ Enter your Tech Stack (comma-separated):

Example:

Python, Django, PostgreSQL, Docker

4️⃣ The AI generates technical questions for EACH technology

5️⃣ Answer the questions

6️⃣ The chatbot ends with:

"Thank you for your time. Our team will review your responses and contact you soon."

🧠 Prompt Design Explanation

This project heavily focuses on Prompt Engineering, which is 30% of the evaluation criteria.

🔹 Information Gathering Prompt

Designed to:

Ask only one question at a time

Maintain context

Avoid deviation from hiring purpose

Handle unclear responses

🔹 Technical Question Generation Prompt

Example structure:

TECH_PROMPT = """
You are a senior technical interviewer.

Based on the tech stack: {tech_stack}

Generate 3-5 medium-level technical interview questions per technology.
Do not provide answers.
Format clearly under each technology.
"""
🎯 Why This Works:

Role-based prompting

Clear formatting instructions

Difficulty control

Structured output enforcement

🔹 Fallback Prompt Strategy

If input is unclear:

Politely redirect conversation

Stay within hiring context

Avoid unrelated answers

🏗️ Technical Decisions
1️⃣ Streamlit for UI

✔ Rapid development
✔ Built-in session management
✔ Ideal for chat-based apps

2️⃣ LLM for Dynamic Question Generation

✔ Handles diverse tech stacks
✔ No hardcoded questions
✔ Scalable for unlimited technologies
✔ More realistic interview simulation

3️⃣ Session-Based Storage

✔ No external database
✔ Data persists during session only
✔ GDPR-conscious design
✔ No permanent sensitive storage

4️⃣ Modular Prompt Design

Separated prompts for:

Info collection

Technical generation

Fallback handling

Improves maintainability and clarity.

🚧 Challenges Faced
1. Maintaining Context

Problem: LLM forgetting earlier details
Solution: Stored conversation in session_state

2. Off-Topic Responses

Problem: Model drifting from hiring process
Solution: Strong role-based system prompts

3. Diverse Tech Stacks

Problem: Handling unlimited technologies
Solution: Dynamic prompt template with tech substitution

4. Exit Handling

Problem: Abrupt conversation termination
Solution: Implemented keyword-based graceful closing

🤖 Model Details

Model Used: GPT-based LLM
Temperature: 0.6–0.7 (balanced creativity & structure)
Max Tokens: 500

Prompt Format:
messages = [
    {"role": "system", "content": "You are an AI Hiring Assistant for TalentScout."},
    {"role": "user", "content": user_input}
]
📁 Project Structure
talentscout-chatbot/
├── app.py
├── prompts.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
🔒 Security Notes

API key stored in .env

.env added to .gitignore

No permanent candidate data storage

Session-based information handling

📝 Sample Data Output (Session Simulation)
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "phone": "+91-9876543210",
  "years_experience": "4",
  "desired_position": "Backend Developer",
  "tech_stack": ["Python", "Django"]
}
🏆 Why This Project Stands Out

Demonstrates practical LLM application

Strong prompt engineering focus

Clean UI and user experience

Context-aware conversational AI

Recruiter-ready simulation


happy hiring😊 
