"""
TalentScout - Hiring Assistant Chatbot
An AI-powered chatbot that collects candidate information and asks technical questions
"""

import streamlit as st
import openai
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TalentScout - Hiring Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #F5F7FA 0%, #E4E8EC 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #1E3A5F 0%, #2E5A8A 100%);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(30, 58, 95, 0.3);
    }
    
    .header-title {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .header-subtitle {
        color: #B8C5D6;
        font-size: 16px;
    }
    
    /* Chat container */
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 20px;
        background: white;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
    }
    
    /* Message bubbles */
    .message {
        padding: 16px 20px;
        border-radius: 16px;
        margin-bottom: 12px;
        max-width: 80%;
        animation: fadeIn 0.3s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .bot-message {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        color: #1E3A5F;
        border-left: 4px solid #1E3A5F;
        margin-right: auto;
    }
    
    .user-message {
        background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%);
        color: #5D4037;
        border-right: 4px solid #FF9800;
        margin-left: auto;
        text-align: right;
    }
    
    .message-sender {
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .bot-message .message-sender {
        color: #1E3A5F;
    }
    
    .user-message .message-sender {
        color: #E65100;
    }
    
    .message-text {
        font-size: 15px;
        line-height: 1.5;
    }
    
    /* Sidebar card */
    .candidate-card {
        background: linear-gradient(135deg, #1E3A5F 0%, #2E5A8A 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        margin-bottom: 16px;
    }
    
    .candidate-card h3 {
        margin-top: 0;
        margin-bottom: 16px;
        font-size: 18px;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        padding-bottom: 12px;
    }
    
    .info-item {
        margin-bottom: 12px;
    }
    
    .info-label {
        font-size: 12px;
        color: #B8C5D6;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .info-value {
        font-size: 15px;
        font-weight: 500;
    }
    
    /* Progress indicator */
    .progress-container {
        background: white;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    .progress-step {
        display: inline-block;
        padding: 8px 16px;
        margin: 4px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
    }
    
    .progress-active {
        background: #1E3A5F;
        color: white;
    }
    
    .progress-completed {
        background: #2E7D32;
        color: white;
    }
    
    .progress-pending {
        background: #E0E0E0;
        color: #757575;
    }
    
    /* Question card */
    .question-card {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        border: 2px solid #2E7D32;
        padding: 20px;
        border-radius: 12px;
        margin: 12px 0;
    }
    
    .question-card h4 {
        color: #1B5E20;
        margin-top: 0;
        margin-bottom: 12px;
    }
    
    .question-item {
        background: white;
        padding: 12px 16px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 3px solid #4CAF50;
    }
    
    /* Input area */
    .input-container {
        display: flex;
        gap: 12px;
        background: white;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #E0E0E0;
        padding: 12px 16px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1E3A5F;
        outline: none;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1E3A5F 0%, #2E5A8A 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #2E5A8A 0%, #1E3A5F 100%);
    }
    
    /* Error message */
    .error-message {
        background: #FFEBEE;
        color: #C62828;
        padding: 12px 16px;
        border-radius: 8px;
        border-left: 4px solid #C62828;
        margin: 8px 0;
    }
    
    /* Typing indicator */
    .typing-indicator {
        display: inline-block;
    }
    
    .typing-indicator span {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #1E3A5F;
        border-radius: 50%;
        margin: 0 2px;
        animation: typing 1.4s infinite;
    }
    
    .typing-indicator span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-indicator span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-8px); }
    }
    
    /* Divider */
    .section-divider {
        margin: 20px 0;
        border: none;
        border-top: 1px solid #E0E0E0;
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'conversation_history': [],
        'candidate_info': {},
        'current_step': 0,
        'generated_questions': {},
        'questions_asked': [],
        'current_tech_index': 0,
        'questions_per_tech': {},
        'current_question_index': 0,
        'awaiting_question_response': False,
        'conversation_started': False,
        'conversation_ended': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# Collection steps
COLLECTION_STEPS = [
    ("name", "Full Name", "What's your full name?"),
    ("email", "Email Address", "What's your email address?"),
    ("phone", "Phone Number", "What's your phone number?"),
    ("experience", "Years of Experience", "How many years of experience do you have?"),
    ("position", "Desired Position", "What position are you applying for?"),
    ("location", "Current Location", "What's your current location (city)?"),
    ("tech_stack", "Tech Stack", "Please enter your tech stack (e.g., Python, Django, React, MySQL)")
]

EXIT_KEYWORDS = ["exit", "quit", "bye", "thank you", "that's all", "done", "goodbye"]


def is_exit_message(message: str) -> bool:
    """Check if the message contains exit keywords"""
    message_lower = message.lower().strip()
    return any(keyword in message_lower for keyword in EXIT_KEYWORDS)


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate phone number (at least 10 digits)"""
    digits = re.sub(r'\D', '', phone)
    return len(digits) >= 10


def validate_experience(exp: str) -> bool:
    """Validate years of experience"""
    try:
        years = float(exp)
        return 0 <= years <= 30
    except ValueError:
        return False


def parse_tech_stack(tech_stack: str) -> list:
    """Parse tech stack from comma-separated string"""
    if not tech_stack:
        return []
    technologies = [tech.strip() for tech in tech_stack.split(',')]
    # Filter out empty strings and capitalize
    return [tech.strip() for tech in technologies if tech.strip()]


def generate_questions_with_llm(technologies: list) -> dict:
    """Generate technical questions using LLM"""
    questions = {}
    
    # Try to use OpenAI API
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key:
        try:
            openai.api_key = api_key
            
            for tech in technologies:
                prompt = f"""Generate 3 intermediate-level technical interview questions for a candidate skilled in {tech}.
Return ONLY the questions, one per line, numbered 1-3. No introductions or explanations needed."""
                
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500,
                    temperature=0.7
                )
                
                response_text = response.choices[0].message.content
                tech_questions = [q.strip() for q in response_text.split('\n') if q.strip()]
                questions[tech] = tech_questions
                
        except Exception as e:
            st.error(f"Error generating questions with LLM: {e}")
            questions = generate_fallback_questions(technologies)
    else:
        questions = generate_fallback_questions(technologies)
    
    return questions


def generate_fallback_questions(technologies: list) -> dict:
    """Generate fallback questions if LLM is not available"""
    fallback_questions = {
        "python": [
            "Explain the difference between list and tuple in Python.",
            "What are Python decorators and how do you use them?",
            "How does garbage collection work in Python?",
            "What is the difference between shallow and deep copy?",
            "Explain the concept of list comprehension with an example."
        ],
        "django": [
            "Explain the Django MVT architecture.",
            "What are Django models and how do they work?",
            "How does Django middleware work?",
            "What is the purpose of Django ORM?",
            "Explain Django's URL routing mechanism."
        ],
        "react": [
            "What is the difference between class and functional components?",
            "Explain the React component lifecycle methods.",
            "What is state in React and how do you manage it?",
            "What are React hooks and name a few commonly used ones?",
            "Explain the virtual DOM in React."
        ],
        "javascript": [
            "What is the difference between let, const, and var?",
            "Explain closures in JavaScript.",
            "What is async/await and how does it work?",
            "What are the different ways to create objects in JavaScript?",
            "Explain event bubbling and capturing."
        ],
        "mysql": [
            "What is the difference between INNER JOIN and LEFT JOIN?",
            "Explain the concept of database normalization.",
            "What are indexes in MySQL and how do they improve performance?",
            "What is the difference between CHAR and VARCHAR?",
            "How do you optimize a slow SQL query?"
        ],
        "sql": [
            "What is the difference between DELETE and TRUNCATE?",
            "Explain the concept of primary key and foreign key.",
            "What are SQL aggregate functions?",
            "How do you handle NULL values in SQL?",
            "What is a subquery and how is it used?"
        ],
        "html": [
            "What is the difference between div and span?",
            "Explain semantic HTML elements.",
            "What are HTML5 semantic tags?",
            "How do you create a responsive webpage?",
            "What is the purpose of the DOCTYPE declaration?"
        ],
        "css": [
            "Explain the box model in CSS.",
            "What is the difference between flexbox and grid?",
            "How do CSS selectors work?",
            "What is the difference between position: relative and absolute?",
            "Explain responsive design and media queries."
        ],
        "java": [
            "What is the difference between abstract class and interface?",
            "Explain the Java collection framework.",
            "What is multithreading in Java?",
            "How does exception handling work in Java?",
            "What is the difference between == and .equals()?"
        ],
        "nodejs": [
            "What is Node.js and how does it work?",
            "Explain the event loop in Node.js.",
            "What are callbacks and promises?",
            "How do you handle errors in Node.js?",
            "What is Express.js and its main features?"
        ],
        "typescript": [
            "What is TypeScript and why is it used?",
            "Explain the difference between type and interface.",
            "What are generics in TypeScript?",
            "How do you define custom types in TypeScript?",
            "What is the purpose of the 'as' keyword?"
        ]
    }
    
    questions = {}
    for tech in technologies:
        tech_lower = tech.lower()
        if tech_lower in fallback_questions:
            questions[tech] = fallback_questions[tech_lower]
        else:
            # Generic questions for unknown technologies
            questions[tech] = [
                f"Explain your experience with {tech}.",
                f"What projects have you built using {tech}?",
                f"What are the best practices for {tech}?",
                f"Describe a challenging problem you solved using {tech}.",
                f"What are the latest updates or features in {tech}?"
            ]
    
    return questions


def add_message(role: str, content: str):
    """Add a message to the conversation history"""
    st.session_state.conversation_history.append({
        "role": role,
        "content": content
    })


def get_current_field_info():
    """Get current field information for collection"""
    if st.session_state.current_step < len(COLLECTION_STEPS):
        field_key, field_name, question = COLLECTION_STEPS[st.session_state.current_step]
        return field_key, field_name, question
    return None, None, None


def validate_input(field_key: str, value: str) -> tuple:
    """Validate input based on field type"""
    value = value.strip()
    
    if not value:
        return False, "This field is required. Please provide your response."
    
    if field_key == "email":
        if not validate_email(value):
            return False, "Please enter a valid email address (e.g., john@example.com)"
    
    elif field_key == "phone":
        if not validate_phone(value):
            return False, "Please enter a valid phone number (at least 10 digits)"
    
    elif field_key == "experience":
        if not validate_experience(value):
            return False, "Please enter valid years of experience (0-30)"
    
    return True, ""


def handle_user_input(user_input: str):
    """Process user input based on current conversation state"""
    
    # Check for exit keywords
    if is_exit_message(user_input):
        return handle_exit()
    
    # If conversation has ended, restart
    if st.session_state.conversation_ended:
        return handle_restart(user_input)
    
    # Get current field info
    field_key, field_name, question = get_current_field_info()
    
    # If all fields collected and in question phase
    if st.session_state.current_step >= len(COLLECTION_STEPS):
        return handle_question_phase(user_input)
    
    # Validate input
    is_valid, error_msg = validate_input(field_key, user_input)
    
    if not is_valid:
        add_message("assistant", f"❌ {error_msg}")
        return
    
    # Store the valid input
    if field_key == "tech_stack":
        # Parse tech stack
        technologies = parse_tech_stack(user_input)
        st.session_state.candidate_info["tech_stack_list"] = technologies
        st.session_state.candidate_info[field_key] = ", ".join(technologies)
        
        # Generate questions
        with st.spinner("🤔 Generating technical questions based on your tech stack..."):
            questions = generate_questions_with_llm(technologies)
            st.session_state.generated_questions = questions
            st.session_state.questions_per_tech = questions
            st.session_state.current_tech_index = 0
            st.session_state.current_question_index = 0
            
            # Initialize questions asked tracking
            st.session_state.questions_asked = []
            
            # Show questions for first technology
            tech_names = list(questions.keys())
            if tech_names:
                first_tech = tech_names[0]
                tech_questions = questions[first_tech]
                st.session_state.awaiting_question_response = True
                
                add_message("user", user_input)
                add_message("assistant", f"Great! Your tech stack includes: {', '.join(technologies)}. Now let's check your technical knowledge.\n\n**{first_tech} Questions:**\n")
                for i, q in enumerate(tech_questions, 1):
                    add_message("assistant", f"{i}. {q}")
                
                add_message("assistant", "\n💬 Please answer these questions or type 'next' to continue to the next technology, or 'skip' to skip these questions.")
    else:
        st.session_state.candidate_info[field_key] = user_input
        add_message("user", user_input)
        
        # Move to next step
        st.session_state.current_step += 1
        
        # Get next field info
        next_field_key, next_field_name, next_question = get_current_field_info()
        
        if next_field_key:
            add_message("assistant", next_question)
        else:
            # All fields collected, start questions
            start_question_phase()
    
    # Save candidate info to file (simulated storage)
    save_candidate_info()


def handle_question_phase(user_input: str):
    """Handle responses during question phase"""
    input_lower = user_input.lower().strip()
    
    # Check for navigation commands
    if input_lower in ["next", "skip", "continue"]:
        # Move to next technology
        tech_names = list(st.session_state.questions_per_tech.keys())
        st.session_state.current_tech_index += 1
        
        if st.session_state.current_tech_index >= len(tech_names):
            # All technologies covered
            add_message("user", user_input)
            add_message("assistant", "✅ You've completed all the technical questions!\n\nThank you for your time! 🎉")
            st.session_state.conversation_ended = True
        else:
            # Show next technology questions
            next_tech = tech_names[st.session_state.current_tech_index]
            tech_questions = st.session_state.questions_per_tech[next_tech]
            
            add_message("user", user_input)
            add_message("assistant", f"\n**{next_tech} Questions:**\n")
            for i, q in enumerate(tech_questions, 1):
                add_message("assistant", f"{i}. {q}")
            add_message("assistant", "\n💬 Please answer these questions or type 'next' to continue.")
        
        return
    
    # Check for exit
    if is_exit_message(user_input):
        return handle_exit()
    
    # Store the answer (in a real app, you'd save this)
    st.session_state.questions_asked.append({
        "question": user_input,
        "user_input": user_input
    })
    
    add_message("user", user_input)
    add_message("assistant", "Great answer! Type 'next' to continue to the next technology or answer more questions if you'd like.")


def start_question_phase():
    """Start the question phase after collecting all info"""
    technologies = st.session_state.candidate_info.get("tech_stack_list", [])
    
    if not technologies:
        st.session_state.conversation_ended = True
        add_message("assistant", "Thank you for providing your information! We'll be in touch soon.")
        return
    
    # Start with first technology
    first_tech = technologies[0]
    tech_questions = st.session_state.generated_questions.get(first_tech, [])
    
    if tech_questions:
        questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(tech_questions)])
        add_message("assistant", f"Perfect! Now let's verify your technical skills.\n\n**Questions for {first_tech}:**\n{questions_text}\n\n💬 Please answer these questions or type 'next' to continue.")
    else:
        # No questions available, end conversation
        add_message("assistant", "Thank you for providing your information! We'll be in touch soon.")
        st.session_state.conversation_ended = True


def handle_exit():
    """Handle conversation exit"""
    name = st.session_state.candidate_info.get("name", "Candidate")
    add_message("user", "exit")
    add_message("assistant", f"👋 Thank you for your time, {name}! Our recruitment team will contact you shortly.\n\nTo start a new conversation, type anything.")
    st.session_state.conversation_ended = True


def handle_restart(user_input: str):
    """Handle restarting the conversation"""
    if any(keyword in user_input.lower() for keyword in ["restart", "start over", "new"]):
        # Reset all session state
        st.session_state.conversation_history = []
        st.session_state.candidate_info = {}
        st.session_state.current_step = 0
        st.session_state.generated_questions = {}
        st.session_state.questions_asked = []
        st.session_state.current_tech_index = 0
        st.session_state.questions_per_tech = {}
        st.session_state.current_question_index = 0
        st.session_state.awaiting_question_response = False
        st.session_state.conversation_started = False
        st.session_state.conversation_ended = False
        
        # Start fresh conversation
        display_welcome_message()
    else:
        add_message("user", user_input)
        add_message("assistant", "The conversation has ended. To start a new conversation, type 'restart' or 'start over'.")


def save_candidate_info():
    """Save candidate info to a JSON file (simulated storage)"""
    import json
    import os
    
    try:
        filename = "candidate_info.json"
        candidates = []
        
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                candidates = json.load(f)
        
        candidates.append(st.session_state.candidate_info)
        
        with open(filename, 'w') as f:
            json.dump(candidates, f, indent=2)
    except Exception as e:
        st.error(f"Error saving candidate info: {e}")


def display_welcome_message():
    """Display the welcome message"""
    welcome_msg = """👋 **Welcome to TalentScout!**

I'm your AI-powered hiring assistant. I'm here to help you through the initial screening process.

**What I'll do:**
1. 📝 Collect your basic information
2. 💻 Ask you some technical questions based on your tech stack
3. ✅ Provide a smooth interview experience

Let's get started!"""
    
    add_message("assistant", welcome_msg)
    
    # Ask for first field
    field_key, field_name, question = get_current_field_info()
    if question:
        add_message("assistant", question)
    
    st.session_state.conversation_started = True


def render_chat_messages():
    """Render all chat messages"""
    for msg in st.session_state.conversation_history:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="message user-message">
                <div class="message-sender">You</div>
                <div class="message-text">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Convert markdown to styled HTML
            content = msg["content"].replace("\n", "<br>")
            st.markdown(f"""
            <div class="message bot-message">
                <div class="message-sender">TalentScout</div>
                <div class="message-text">{content}</div>
            </div>
            """, unsafe_allow_html=True)


def render_sidebar():
    """Render sidebar with candidate info"""
    st.sidebar.title("📋 Candidate Profile")
    
    candidate = st.session_state.candidate_info
    
    if not candidate:
        st.sidebar.info("No candidate information collected yet.")
        return
    
    st.sidebar.markdown(f"""
    <div class="candidate-card">
        <h3>👤 {candidate.get('name', 'N/A')}</h3>
        <div class="info-item">
            <div class="info-label">Email</div>
            <div class="info-value">{candidate.get('email', 'N/A')}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Phone</div>
            <div class="info-value">{candidate.get('phone', 'N/A')}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Experience</div>
            <div class="info-value">{candidate.get('experience', 'N/A')} years</div>
        </div>
        <div class="info-item">
            <div class="info-label">Position</div>
            <div class="info-value">{candidate.get('position', 'N/A')}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Location</div>
            <div class="info-value">{candidate.get('location', 'N/A')}</div>
        </div>
        <div class="info-item">
            <div class="info-label">Tech Stack</div>
            <div class="info-value">{candidate.get('tech_stack', 'N/A')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_progress():
    """Render progress indicator"""
    if st.session_state.conversation_ended:
        return
    
    steps_html = '<div class="progress-container">'
    
    for i, (key, name, _) in enumerate(COLLECTION_STEPS):
        if i < st.session_state.current_step:
            steps_html += f'<span class="progress-step progress-completed">✓ {name}</span>'
        elif i == st.session_state.current_step:
            steps_html += f'<span class="progress-step progress-active">● {name}</span>'
        else:
            steps_html += f'<span class="progress-step progress-pending">○ {name}</span>'
    
    # Add question phase indicator
    if st.session_state.current_step >= len(COLLECTION_STEPS):
        steps_html += f'<span class="progress-step progress-active">● Technical Questions</span>'
    
    steps_html += '</div>'
    st.markdown(steps_html, unsafe_allow_html=True)


def main():
    """Main application function"""
    # Initialize session state
    init_session_state()
    
    # Render sidebar
    render_sidebar()
    
    # Header
    st.markdown("""
    <div class="header-container">
        <div class="header-title">🤖 TalentScout</div>
        <div class="header-subtitle">AI-Powered Hiring Assistant Chatbot</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Show welcome message if conversation hasn't started
    if not st.session_state.conversation_started:
        display_welcome_message()
    
    # Show progress
    render_progress()
    
    # Chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    render_chat_messages()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Input area using form for proper submission handling
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Type your message:",
            key="user_input",
            placeholder="Type your response here...",
            label_visibility="collapsed"
        )
        submit_button = st.form_submit_button(label="Send")
    
    # Handle form submission
    if submit_button and user_input:
        handle_user_input(user_input)
        st.rerun()


if __name__ == "__main__":
    main()
