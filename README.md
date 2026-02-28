👔 TalentScout - AI-Powered Hiring Assistant Chatbot

TalentScout is an intelligent AI-powered chatbot built using Python and Streamlit that automates the initial screening process for technical positions. It collects candidate information, dynamically analyzes tech stacks, and generates tailored technical interview questions using Large Language Models (LLMs).

📋 Project Overview

TalentScout is designed to streamline the initial hiring process by:

1. Automating candidate screening – Collects structured information without human intervention

2. Dynamically generating technical questions – Uses LLM to create 3–5 relevant questions per technology

3. Maintaining conversational context – Uses session state to preserve candidate details

4. Providing professional experience – Clean UI with structured multi-step interaction
   

⭐ Key Capabilities

1. Multi-step conversation flow (Greeting → Info Collection → Tech Stack → Dynamic Technical Questions → End)

2. Dynamic LLM-based question generation (No fixed hardcoded questions)

3. Context retention using Streamlit session_state

4. Structured and formatted technical questions

5. Fallback handling for unclear input

6. Exit handling with professional closing

7. Session-based candidate data handling


🚀 Installation Steps
Prerequisites

1. Python 3.8 or higher

2. OpenAI API key

Step-by-Step Installation
1. Clone or download the project files

    git clone <repository-url>
    cd talentscout

2. Install dependencies

    pip install -r requirements.txt

3. Set up environment variables

    Create a .env file and add:

    OPENAI_API_KEY=your_actual_api_key_here

4. Run the application

    streamlit run app.py

5. Open your browser

    The app will automatically open at:
    http://localhost:8501

Or check the terminal for the exact URL.


📖 Usage Instructions
For Candidates
1. Start the conversation

The bot greets you automatically.

2. Provide personal information (one-by-one):

. Full Name

. Email Address (validated)

. Phone Number (validated)

. Years of Experience

. Desired Position

. Current Location

3. Enter your tech stack (comma-separated format)

. Example:
Python, Django, PostgreSQL, Docker

. Example:
React, Node.js, MongoDB, AWS

4. Answer dynamically generated technical questions

. 3–5 questions per technology

. Medium-level difficulty

. No answers shown

. Professionally formatted

5. Complete the screening

After the questions, you will see:

"Thank you for your time. Our recruitment team will review your responses and contact you soon."


🛑 Exit Commands

Type any of these to end the conversation immediately:

exit, quit, bye, goodbye, stop, end


🧠 Prompt Design Explanation
Dynamic Question Generation (LLM-Based)

The system uses an OpenAI GPT model to generate tailored technical questions.

Example prompt structure:

You are a senior technical interviewer.
Based on the following tech stack: {tech_stack}
Generate 3–5 medium-level technical interview questions per technology.
Do not provide answers.
Format clearly under each technology.

Design Principles

. Role-based prompting

. Structured formatting

. Controlled difficulty

. Domain restriction to hiring context

. Prevention of irrelevant responses


🏗️ Technical Decisions
1. Streamlit for UI

Decision: Used Streamlit instead of Flask/Django

Rationale:

. Rapid development

. Built-in session state management

. Automatic UI rendering

. Ideal for chatbot-style applications

2. Session State Management

Decision: Used Streamlit's session_state instead of external database

Rationale:

. No database setup required

. Fast conversation memory

. Simplified local deployment

. Data exists only during session

3. Dynamic Questions vs Fixed Questions

Decision: Used LLM-generated dynamic questions

Rationale:

. Supports unlimited tech stacks

. More realistic interview simulation

. No need to manually maintain question sets

. Scalable architecture

4. Environment-Based API Key Management

Decision: Store API key in .env file

Rationale:

. Prevents hardcoding secrets

. Secure configuration management

. Follows best practices


🚧 Challenges Faced
1. Maintaining Conversation Context

Problem: LLM forgetting earlier candidate details
Solution: Stored conversation and user data inside session_state

2. Off-Topic Responses

Problem: Model generating unrelated responses
Solution: Strengthened system prompt and domain restrictions

3. Formatting Inconsistencies

Problem: Questions not formatted uniformly
Solution: Enforced structured formatting rules inside prompt

4. API Failure Handling

Problem: Application crashes when API fails
Solution: Added error handling and fallback messaging


🤖 Model Details

Model: GPT-3.5-turbo (or GPT-4 compatible)
Temperature: 0.6–0.7
Max Tokens: 500
Use Case: Dynamic technical question generation


🔄 Fallback Strategy

When API fails or response is unclear:

. Displays professional fallback message

. Redirects to hiring-focused conversation

. Prevents system crash


📁 Project Structure

talentscout/
├── app.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md


🔒 Security Notes

. API keys stored in .env

. .env added to .gitignore

. No permanent candidate data storage

. Session-based information handling

. No external data storage


🐛 Troubleshooting

Issue: "OpenAI API Key not configured!"
Solution: Create .env file and add your API key

Issue: "Error generating questions"
Solution: Check internet connection or API credits

Issue: Module not found errors
Solution: Run pip install -r requirements.txt

Issue: Unexpected responses
Solution: Verify prompt formatting


📝 Output Format (Session Data Example)

{
"candidate_info": {
"full_name": "John Doe",
"email": "john@example.com
",
"phone": "+91-9876543210",
"years_experience": "4",
"desired_position": "Backend Developer",
"current_location": "Bangalore, India",
"tech_stack": ["Python", "Django"]
}
}


🙏 Acknowledgments

Built with Streamlit, OpenAI API, and Python.
