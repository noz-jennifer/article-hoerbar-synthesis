import streamlit as st
import requests
import json
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

# Titel der App
st.title('Hörbar Article Synthesis')
st.caption('Version 2.0.1')

# Eingabefeld für die Artikel-ID
article_id = st.text_input('Enter Article ID')

# Button zum Auslösen der Verarbeitung
if st.button('Fetch and Process'):
    with st.spinner('Processing article …'):

        # First API call (Exporter API)
        exporter_api_url = f"{st.secrets['api_tokens']['exporter_api_base_url']}{article_id}/"
        
        exporter_auth_token = st.secrets["api_tokens"]["exporter_auth_token"]
        headers_exporter = {
            "Authorization": f"Basic {exporter_auth_token}",
            "Content-Type": "application/json"
        }

        exporter_response = requests.get(exporter_api_url, headers=headers_exporter)

        if exporter_response.status_code != 200:
            # Error handling for exporter API
            st.error("Error retrieving article from Exporter API.")
        else:
            # Parse response from exporter API
            exporter_json = exporter_response.json()
            try:
                title = exporter_json.get('title', '')
                text = exporter_json.get('text', '')
            except json.JSONDecodeError:
                st.error("Failed to decode JSON from Exporter API.")
                st.stop()
            
            if not title or not text:
                st.warning("Exporter API returned empty title or text.")
                st.stop()
            
            # Custom TTS Service Call
            tts_api_url = st.secrets["api_tokens"]["tts_api_url"]
            tts_api_key = st.secrets["api_tokens"]["tts_api_key"]

            headers_tts = {
                "x-api-key": tts_api_key,
                "Content-Type": "application/json"
            }

            payload_tts = {
                "id": article_id,
                "headline": title,
                "content": text
            }

            tts_response = requests.post(tts_api_url, headers=headers_tts, json=payload_tts)

            if tts_response.status_code != 200:
                st.error("Fehler beim Abrufen der Hörfassung vom TTS-Service.")
            else:
                tts_json = tts_response.json()
                formatted_content = tts_json.get("content", "").replace("\n\n", "\n\n")
                st.success("Hörbar Article Version:")
                st.markdown(formatted_content)