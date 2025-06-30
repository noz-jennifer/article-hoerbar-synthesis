# 🗣️ Article Hörbar Synthesis App

**Version: 2.0.1**

This is a Streamlit-based web application that transforms news articles into audio-friendly summaries using OpenAI's language models.

---

## ✨ Features

- 🔐 Secure integration with an internal Exporter API (Basic Auth)
- 📄 Automatic parsing of article `title` and `text`
- 🤖 Summarization and optimization using OpenAI models
- 📤 Optional local JSONL logging
- 📢 Optimized for text-to-speech playback
- 🛠️ Error handling, loading animations, and evaluation toggles

---

## 🚀 Usage

1. **Clone the repository**

```bash
git clone https://github.com/your-username/article-hoerbar-synthesis.git
cd article-hoerbar-synthesis
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add secrets to `.streamlit/secrets.toml`**

```toml
[api_tokens]
exporter_auth_token = "your_exporter_token"
exporter_api_base_url = "https://your-exporter-api-url/"
tts_api_url = "https://your-tts-api-url.com"
tts_api_key = "your_tts_api_key"
```

4. **Run the app locally**

```bash
streamlit run app.py
```

---

## 🧠 How it works

- User enters an `articleId` from the internal CMS.
- The app fetches the article via the Exporter API using the ID.
- It extracts `title` and `text` from the Exporter response.
- These are sent to the Article Optimization Service (defined via `tts_api_url` and `tts_api_key` in `secrets.toml`).
- The returned `content` from the TTS API is rendered in the app using markdown formatting.

---

## 🛡 Security

- Secrets like tokens and URLs are stored securely in `.streamlit/secrets.toml`
- This file is excluded from version control via `.gitignore`
- No user-submitted data is shared unless Evals is explicitly enabled

---

## 🖥 Deployment

To deploy on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this repo to GitHub
2. Create a new Streamlit app
3. Paste your secrets into the *App Settings → Secrets* section of the Cloud UI