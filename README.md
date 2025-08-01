# Echoes

*Echoes* is a deeply personal AI-driven web app that helps users reconnect with voices they can no longer reach. Whether you've lost someone close, are separated by distance or circumstance, or simply crave the comfort of their familiar words, Echoes lets you recreate the warmth of those conversations. The prompt generator also lets you generate custom prompts for a specific person (Dad, Mom, Friend, Sibling, Partner, etc.), so that you can write them a heartful letter, even without a direction to start from.

---

##  What It Does

* **Chat Like Them**: Upload or type a few messages from someone important to you — like a parent — and Echoes uses that style to simulate an ongoing, realistic chat conversation. It feels like texting them again.
* **Prompt-Generated Letter Writing**: If you’re struggling to find the words, Echoes provides thoughtful prompts (e.g., "Dad, what’s something you taught me that still shapes me today?") to guide your writing.
* **Send Letters via WhatsApp**: Once you write a letter, you can send it directly to a phone number through WhatsApp — great for when the person is still with you but out of reach.
* **Memory Lane Mode**: Combine old messages and letter drafts for a full nostalgic experience.

---

##  Who It’s For

* People grieving the loss of parents or loved ones
* Those in long-distance or strained relationships
* Anyone seeking emotional closure, comfort, or a way to express unspoken feelings

---

##  Tech Stack

* **Python**
* **Streamlit** – UI and web interface
* **Langchain** – Prompt templates and LLM interface
* **Ollama** – Local LLM server runner
* **Gemma 2B (2.2b)** – Lightweight yet powerful LLM used locally

> Note: Ollama is required to run Gemma 2B locally.

---

##  Features

* AI chatbot that mimics texting style from short samples
* Prompt generator for inspiration when writing letters
* Letter editor with WhatsApp integration (enter number to send!)
* Nostalgia-based UX and gentle emotional design
* Support for both remembrance and live connection

---

##  Installation & Usage

> You must have [Ollama](https://ollama.com/) installed and running with the Gemma 2B model downloaded locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Aruniaaa/echoes.git
cd echoes
```

### 2. Create a Virtual Environment & Install Requirements

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Start the App

```bash
streamlit run app.py
```

---


This app was born from the quiet ache of missing someone. Whether it’s a parent you lost, a friend you’re distant from, or just the need to hear their voice one more time — Echoes lets you reach into the past for comfort, closure, or conversation.


---

*"Some words never fade. Echoes brings them back."*
