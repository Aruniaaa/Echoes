import streamlit as st
import time
from typing import Generator
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama


model = Ollama(model="gemma2:2b")

template = """
You are simulating the personality of the user's parent by **deeply analyzing and internalizing** the sample message below. This is not just text — it is a full reflection of their emotional tone, cultural habits, emotional tactics (guilt-tripping, sarcasm, sweetness, passive-aggressiveness), and texting quirks (code-mixing, dramatic pauses, emotional exaggeration).

Your goal is to **embody this parent’s persona completely** — their emotional logic, reactions, and communication style — and respond just as they would, even if the topic or input message is unrelated to the sample.

Here is a real example of how this parent speaks to their child:
---------------------
{example}
---------------------

Now, respond to the user as this parent would. Use their typical sentence structure, emotional reactions, and tone (whether warm, dramatic, passive-aggressive, sarcastic, or sweet) based on the example. **Fully become them**.

Keep the message under 50 words. Channel their essence. Don't include any code blocks in your response like </div> or anything else, be conversational like a human

User’s message:
---------------------
{user}
---------------------
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def init_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'parent_example' not in st.session_state:
        st.session_state.parent_example = ""
    if 'setup_complete' not in st.session_state:
        st.session_state.setup_complete = False
    if 'is_generating' not in st.session_state:
        st.session_state.is_generating = False

def simulate_typing_delay(duration=3):
    placeholder = st.empty()
    dots = [".", "..", "...", "....", "....."]
    for _ in range(int(duration * 3.33)):
        for dot in dots:
            placeholder.markdown(f"**Typing{dot}**")
            time.sleep(0.3)
    placeholder.empty()

def clean_message(message: str) -> str:

    cleaned = message.replace("</div>", "").replace("<div>", "").strip()
    return cleaned

def get_parent_response(user_message: str, parent_example: str) -> str:

    result = chain.invoke({"example": parent_example, "user": user_message})

   
    return clean_message(str(result))

def display_chat_message(message: dict, is_user: bool = True):

    message = clean_message(str(message['content']))

    if is_user:
            st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
                <div style="
                    background: linear-gradient(135deg, #A1C4FD 0%, #C2E9FB 100%);
                    padding: 12px 20px;
                    border-radius: 20px 20px 5px 20px;
                    max-width: 80%;
                    color: #54494B;
                    font-weight: 500;
                    box-shadow: 0 2px 10px rgba(84, 73, 75, 0.1);
                ">
                    {message}
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
       
    else:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-start; margin: 10px 0;">
                <div style="
                    background: linear-gradient(135deg, #BFD6F6 0%, #F2D2AE 100%);
                    padding: 12px 20px;
                    border-radius: 20px 20px 20px 5px;
                    max-width: 80%;
                    color: #54494B;
                    font-weight: 500;
                    box-shadow: 0 2px 10px rgba(84, 73, 75, 0.1);
                ">
                    <strong>Parent:</strong> {message}
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    


def main():
    # Page configuration
    st.set_page_config(
        page_title="Parent Chat Simulator",
        page_icon="💬",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #54494B 0%, #D8E4FF 100%);
            min-height: 100vh;
        }
        
        .stApp {
            background: linear-gradient(135deg, #54494B 0%, #D8E4FF 100%);
        }
        
        .chat-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(84, 73, 75, 0.2);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .setup-container {
            background: rgba(255, 255, 255, 0.98);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(84, 73, 75, 0.15);
            text-align: center;
        }
        
        .stTextInput > div > div > input {
            border-radius: 25px;
            border: 2px solid #C4A381;
            padding: 12px 20px;
            background: rgba(255, 255, 255, 0.9);
            color: #54494B !important;
            box-shadow: 0 4px 15px rgba(196, 163, 129, 0.2);
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #94FBAB;
            box-shadow: 0 0 0 0.2rem rgba(148, 251, 171, 0.25);
            outline: none;
            transform: translateY(-1px);
        }
        
        /* Default button styling - for "Start Chatting" button */
        .stButton > button {
            background: #54494B;
            color: #D8E4FF;
            border: 2px solid #C4A381;
            border-radius: 25px;
            padding: 10px 30px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(84, 73, 75, 0.3);
            background: #C4A381;
            color: #54494B;
        }
        
        /* Send button styling - different color */
        .stButton > button[kind="primary"] {
            background: #D8E4FF;
            color: #54494B;
            border: 2px solid #54494B;
        }
        
        .stButton > button[kind="primary"]:hover {
            background: #D8E4FF;
            color: #C4A381; # change this
            box-shadow: 0 5px 15px rgba(148, 251, 171, 0.4);
        }
        
        /* New Conversation button styling - third color scheme */
        .stButton > button:nth-of-type(3) {
            background: #C4A381;
            color: #54494B;
            border: 2px solid #94FBAB;
        }
        
        .stButton > button:nth-of-type(3):hover {
            background: #94FBAB;
            color: #54494B;
            box-shadow: 0 5px 15px rgba(216, 228, 255, 0.4);
        }
        
        h1 {
            color: #54494B;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        .subtitle {
            color: #54494B;
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 30px;
            opacity: 0.8;
        }
        </style>
    """, unsafe_allow_html=True)
    

    
    # Initialize session state
    init_session_state()
    
    # Header
    st.markdown("""
        <h1>💬 Parent Chat Simulator</h1>
        <p class="subtitle">Have a conversation with your parent's digital twin</p>
    """, unsafe_allow_html=True)
    
    # Setup phase
    if not st.session_state.setup_complete:
        # st.markdown('<div class="setup-container">', unsafe_allow_html=True)
        
        st.markdown("### Let's Set Up Your Parent's Personality")
        st.markdown("Please provide an example of how your parent typically texts/texted you. This will help the AI learn their communication style and respond accordingly.")
        
        parent_example = st.text_area(
            "Example of your parent's text:",
            placeholder="e.g., 'Beta, have you eaten? I made your favorite dal today. Call me when you get this message. Love you so much!'",
            height=100,
            key="parent_example_input"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("Start Chatting?", type="primary"):
                if parent_example.strip():
                    st.session_state.parent_example = parent_example
                    st.session_state.setup_complete = True
                    st.rerun()
                else:
                    st.error("Please provide an example of your parent's texting style!")
        
        # st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat phase
    else:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for message in st.session_state.messages:
            display_chat_message(message, message['role'] == 'user')
        

        st.markdown("---")
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_area(
                "Type your message:",
                placeholder="What would you like to say to your parent?",
                key="user_input",
                label_visibility="collapsed",
                height=100
            )
        
        with col2:
            send_button = st.button("Send 📤", type="primary")
        
        
        if send_button and user_input.strip():


            st.session_state.is_generating = True
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            parent_response = get_parent_response(user_input, st.session_state.parent_example)
            
           
            st.session_state.is_generating = False
            
        
            parent_message = {"role": "parent", "content": parent_response}
            st.session_state.messages.append(parent_message)
            
            st.rerun()
        
        
       
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 New Conversation"):
                st.session_state.messages = []
                st.session_state.setup_complete = False
                st.session_state.parent_example = ""
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()