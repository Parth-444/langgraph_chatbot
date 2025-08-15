# LangGraph Chatbot (Dockerized)

This is a **LangGraph-based AI chatbot** containerized with Docker for easy deployment and portability.  
The chatbot uses the **Google Generative AI API** for responses.

---

## 🚀 Features
- Built with **Python** and **LangGraph**
- Fully containerized with **Docker**
- No local setup required — just run the image with your API key
- Available on **Docker Hub**

---

## 📦 Docker Hub Image
This chatbot is available on Docker Hub:  
👉 [(http://hub.docker.com/r/p4rth444/chatbot)]

---

## 🔧 How to Run

### 1️⃣ Pull the Docker Image
```bash
docker pull p4rth444/chatbot:latest
```

### 2️⃣ Run with Your API Key

### Replace GOOGLE_API_KEY with your own key:
```bash
docker run -e GOOGLE_API_KEY_PRO="sk-xxxxx" p4rth444/chatbot
```

### 🛠 Local Development (Optional)
```bash
# Clone repository
git clone https://github.com/Parth-444/langgraph_chatbot.git
cd langgraph_chatbot

# Build Docker image
docker build -t langgraph_chatbot .

# Run container with env variable
docker run -e GOOGLE_API_KEY="sk-xxxxx" langgraph_chatbot
```

### Cloud hosted link
https://chatbot-pi2y.onrender.com
