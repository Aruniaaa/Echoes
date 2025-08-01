import streamlit as st
import urllib.parse
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

template = """
You are a professional letter-writing assistant helping users express love, gratitude, or memories to their parents. 
Your tone should be emotionally warm, sincere, and a little poetic—but still easy to understand.

Step 1: Gently guide the user with a meaningful prompt they can respond to. 
Make it about childhood memories, moments of appreciation, or things they’ve always wanted to say. 
Keep the prompt simple, like a journaling starter.


Examples:

Prompt: “What’s one moment from your childhood with your parents that always makes you smile? Describe it like you’re reliving it.”

Prompt: “Is there something your parents did for you that you’ve never properly thanked them for? Now’s the time.”

Make sure your ouput is a simple one-liner that always starts with the word 'Prompt:', nothing else, no clutter

Now, generate a new prompt in that style, the user is writing a letter to their {person}
"""

model = Ollama(model="gemma2:2b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model



def get_prompt(person):

    result = chain.invoke({"person": person})

    return result

    



st.set_page_config(
        page_title="Letters for Life",
        page_icon="💗",
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
    

st.title("Letters for Life 💌")

msg = st.text_area(label="Write your message", height=300, placeholder="Type your heartfelt letter here...")
number = st.text_input("Recipient's number, please ensure that there is no space between the number and country code!!!", value="+91")

if st.button("Generate WhatsApp Link", type="primary"):
    if msg.strip() == "" or number.strip() == "":
        st.warning("Please enter both a message and a number.")
    else:
        encoded_msg = urllib.parse.quote(msg)
        url = f"https://wa.me/{number}?text={encoded_msg}"
        st.markdown(f"[Click here to send the letter on WhatsApp 📤]({url})", unsafe_allow_html=True)

st.markdown("---")

name = st.text_input("Who are you writing to?", placeholder="e.g. Mom, Dad, Papa, Amma")
if st.button("Generate a prompt!", type="primary"):
    with st.spinner("Writing a perfect prompt just for you..."):
        res = get_prompt(name)
        title_line = "Here's your prompt 💌"

        try:
            lines = [line.strip() for line in res.strip().split("\n") if line.strip()]
            prompt_line = ""

            for line in lines:
                if line.startswith("Prompt:"):
                    prompt_line = line.replace("Prompt:", "").strip()    
        except:
            prompt_line = res

        print(res)


        st.markdown(f"""
    <div class='chat-container'>
        <h2 style='text-align: center; color: black;'>{title_line}</h2>
        <p style='font-size: 1.1em; text-align: center; color: black;'>{prompt_line}</p>
    </div>
    """, unsafe_allow_html=True)

