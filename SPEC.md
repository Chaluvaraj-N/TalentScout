# TalentScout - Hiring Assistant Chatbot

## 1. Project Overview
- **Project Name**: TalentScout
- **Type**: AI-powered Hiring Assistant Chatbot
- **Core Functionality**: An intelligent chatbot that collects candidate information, asks relevant technical questions based on their tech stack, and maintains conversation context throughout the hiring process
- **Target Users**: Job candidates seeking employment, HR/recruitment teams

## 2. UI/UX Specification

### Layout Structure
- **Single Page Application**: Streamlit-based chat interface
- **Chat Container**: Full-width message display area with scroll
- **Input Area**: Fixed bottom input field with send button
- **Sidebar**: Candidate information summary panel

### Visual Design
- **Color Palette**:
  - Primary: `#1E3A5F` (Deep Navy Blue)
  - Secondary: `#2E7D32` (Forest Green - for success/accent)
  - Background: `#F5F7FA` (Light Gray-Blue)
  - Bot Message: `#E3F2FD` (Light Blue)
  - User Message: `#FFF3E0` (Light Orange)
  - Error: `#D32F2F` (Red)
  - Text Primary: `#212121` (Dark Gray)
  - Text Secondary: `#757575` (Medium Gray)

- **Typography**:
  - Font Family: 'Inter', 'Segoe UI', sans-serif
  - Headings: 24px bold
  - Body: 16px regular
  - Small: 14px

- **Spacing**:
  - Container padding: 20px
  - Message gap: 12px
  - Card padding: 16px

- **Visual Effects**:
  - Message bubbles with rounded corners (12px)
  - Subtle shadow on messages
  - Smooth fade-in animation for new messages
  - Typing indicator animation

### Components
1. **Welcome Banner**: Company branding with logo placeholder
2. **Chat Messages**: Differentiated user/bot messages
3. **Input Field**: Text input with placeholder
4. **Status Indicators**: Collection progress tracker
5. **Candidate Card**: Sidebar with collected info
6. **Question Display**: Technical questions in formatted cards
7. **Exit Confirmation**: Professional closing message

## 3. Functionality Specification

### Core Features

#### 3.1 Greeting System
- Display welcome message on start
- Explain chatbot purpose (collect info, ask technical questions)
- Exit on keywords: "exit", "quit", "bye", "thank you", "that's all"

#### 3.2 Information Collection (Sequential Flow)
Collect in order:
1. **Full Name** - Validate non-empty, alphabetic
2. **Email** - Validate email format
3. **Phone Number** - Validate format (10+ digits)
4. **Years of Experience** - Validate numeric (0-30)
5. **Desired Position** - Validate non-empty
6. **Current Location** - Validate non-empty
7. **Tech Stack** - Comma-separated input (e.g., "Python, Django, React")

#### 3.3 Tech Stack Parsing
- Split by comma
- Trim whitespace
- Capitalize properly
- Store as list

#### 3.4 Technical Question Generation
- Use LLM to generate 3-5 questions per technology
- Questions should be intermediate level
- Store generated questions per tech
- Display one tech's questions at a time

#### 3.5 Context Maintenance
- Store in Streamlit session_state:
  - `candidate_info` (dict)
  - `conversation_history` (list)
  - `current_step` (int)
  - `generated_questions` (dict)
  - `questions_asked` (list)
  - `current_tech_index` (int)

#### 3.6 Fallback Mechanism
- Detect irrelevant messages
- Redirect to current collection step
- Sample responses:
  - "I didn't quite get that. Could you please provide your [field name]?"
  - "I'm here to assist with the hiring process. Could you please answer the question?"

#### 3.7 Conversation End
- Thank message with candidate name
- Offer to restart
- Display summary of collected info

### User Interactions
1. User reads welcome message
2. Bot asks for each piece of info sequentially
3. User provides input
4. Bot validates and moves to next step OR shows error
5. After tech stack, bot generates questions
6. Bot asks questions one at a time or by tech
7. User can exit anytime with keywords

### Error Handling
- Invalid email format → "Please enter a valid email address"
- Invalid phone → "Please enter a valid phone number (10+ digits)"
- Invalid experience → "Please enter years of experience (0-30)"
- Empty field → "This field is required. Please provide your [field]"
- Irrelevant input → Fallback message

## 4. Technical Implementation

### Files Structure
```
AIML/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # API keys (not committed)
└── SPEC.md            # This specification
```

### Dependencies
- streamlit>=1.28.0
- openai>=1.3.0
- python-dotenv>=1.0.0

### LLM Integration
- Use OpenAI GPT-3.5/4 API
- Fallback to simulated questions if API unavailable
- Prompt template for question generation

## 5. Acceptance Criteria

### Greeting
- [ ] Welcome message displays on app start
- [ ] Purpose is clearly explained
- [ ] App exits gracefully on exit keywords

### Information Collection
- [ ] All 7 fields collected in sequence
- [ ] Validation works for each field type
- [ ] Error messages are clear and helpful

### Tech Stack
- [ ] User can enter comma-separated technologies
- [ ] Technologies are properly parsed and stored

### Question Generation
- [ ] Questions generated for each technology
- [ ] Questions are relevant to the technology
- [ ] 3-5 questions per technology

### Context
- [ ] Candidate name remembered throughout
- [ ] Tech stack remembered
- [ ] No repeat questions

### Fallback
- [ ] Irrelevant messages handled gracefully
- [ ] User redirected to correct step

### End Conversation
- [ ] Professional closing message
- [ ] Candidate name included in goodbye

### UI
- [ ] Responsive chat interface
- [ ] Clear message differentiation
- [ ] Professional color scheme
- [ ] Smooth interactions
