 TalentScout - Hiring Assistant Chatbot

📋 Project Overview

**TalentScout** is an AI-powered Hiring Assistant Chatbot developed using Streamlit and OpenAI's GPT models. This intelligent chatbot streamlines the initial candidate screening process by collecting candidate information and asking relevant technical questions based on their tech stack.

Key Features

- 🤖 **AI-Powered**: Uses OpenAI GPT-3.5 for intelligent question generation
- 📝 **Sequential Data Collection**: Collects candidate information in a structured flow
- 💻 **Technical Assessment**: Generates relevant technical questions based on candidate's tech stack
- 💬 **Conversational Interface**: Natural language interaction with context maintenance
- 📊 **Real-time Progress Tracking**: Visual progress indicator for collection steps


🏗️ Project Architecture

### Technology Stack
| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| AI/ML | OpenAI GPT-3.5 Turbo |
| Backend | Python |
| Environment | python-dotenv |


File Structure

AIML/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── SPEC.md            # Project specification
├── README.md          # Project documentation
├── .env               # Environment variables (API keys)
└── candidate_info.json # Stored candidate data


Dependencies

streamlit>=1.28.0
openai>=1.3.0
python-dotenv>=1.0.0


🚀 How to Run

1. Install Dependencies
bash
pip install -r requirements.txt

2. Configure Environment Variables
Create a `.env` file in the project root:

env
OPENAI_API_KEY=your_openai_api_key_here

3. Run the Application

bash
streamlit run app.py

The application will open in your default web browser at `http://localhost:8501`.


💡 Functionality Overview

1. Information Collection Flow
The chatbot collects candidate information in the following sequence:
1. **Full Name** - Validates alphabetic input
2. **Email Address** - Validates email format
3. **Phone Number** - Validates 10+ digits
4. **Years of Experience** - Validates 0-30 range
5. **Desired Position** - Non-empty string
6. **Current Location** - Non-empty string
7. **Tech Stack** - Comma-separated technologies (e.g., "Python, Django, React")

2. Technical Question Generation
- Uses OpenAI GPT-3.5 to generate 3-5 relevant technical questions per technology
- Falls back to predefined question bank if API is unavailable
- Questions are intermediate level and role-appropriate

3. Conversation Management
- **Exit Keywords**: "exit", "quit", "bye", "thank you", "that's all", "done", "goodbye"
- **Restart**: Users can restart the conversation at any time
- **Fallback Handling**: Graceful handling of irrelevant inputs

4. Data Persistence
- Candidate information is saved to `candidate_info.json`
- Maintains conversation history in session state


🎨 UI/UX Design

Color Scheme
| Element | Color |
|---------|-------|
| Primary | #1E3A5F (Deep Navy Blue) |
| Secondary | #2E7D32 (Forest Green) |
| Background | #F5F7FA (Light Gray-Blue) |
| Bot Message | #E3F2FD (Light Blue) |
| User Message | #FFF3E0 (Light Orange) |

Components
- **Welcome Banner**: Company branding with gradient header
- **Chat Messages**: Differentiated user/bot message bubbles
- **Progress Indicator**: Visual step tracker
- **Sidebar**: Real-time candidate profile summary
- **Question Cards**: Formatted technical questions

### Visual Effects
- Smooth fade-in animations for messages
- Gradient backgrounds
- Rounded corners (12px)
- Subtle shadows


🔧 Key Implementation Details

Session State Management
The application uses Streamlit's session_state to maintain:
- `conversation_history`: All chat messages
- `candidate_info`: Collected candidate data
- `current_step`: Current collection step index
- `generated_questions`: AI-generated technical questions
- `questions_per_tech`: Questions organized by technology
- `current_tech_index`: Current technology being assessed
- `conversation_started`: Boolean flag for conversation state

Validation Functions
- `validate_email()`: Regex-based email validation
- `validate_phone()`: Phone digit extraction and count
- `validate_experience()`: Numeric range validation (0-30)
- `parse_tech_stack()`: Comma-separated parsing with trimming

LLM Integration
- Primary: OpenAI GPT-3.5 Turbo API
- Fallback: Predefined question bank for common technologies
- Technologies covered in fallback: Python, Django, React, JavaScript, MySQL, SQL, HTML, CSS, Java, Node.js, TypeScript

📝 Sample Conversation Flow

TalentScout: 👋 Welcome to TalentScout! I'm your AI-powered hiring assistant...
TalentScout: What's your full name?
User: John Doe
TalentScout: What's your email address?
User: john@example.com
TalentScout: What's your phone number?
User: 1234567890

TalentScout: Please enter your tech stack (e.g., Python, Django, React, MySQL)
User: Python, Django, React
TalentScout: Great! Your tech stack includes: Python, Django, React. Now let's check your technical knowledge.
TalentScout: Python Questions:
1. Explain the difference between list and tuple in Python.
2. What are Python decorators and how do you use them?

✅ Acceptance Criteria Met

- [x] Welcome message displays on app start
- [x] All 7 fields collected in sequence with validation
- [x] Tech stack properly parsed and stored
- [x] Questions generated for each technology (3-5 per tech)
- [x] Candidate name remembered throughout conversation
- [x] Graceful handling of irrelevant messages
- [x] Professional closing message with candidate name
- [x] Responsive chat interface with professional styling

📄 License

This project is for demonstration and educational purposes.


👨‍💻 Author

TalentScout - AI Hiring Assistant


## 🆘 Troubleshooting

1. **API Key Issues**: Ensure `OPENAI_API_KEY` is set in `.env` file
2. **Port Already in Use**: Use `streamlit run app.py --server.port 8502`
3. **Session State Issues**: Refresh the browser to reset the conversation


Happy hiring 
