import os
import requests
from app.openai_integration import summarize_video_openai


def get_video_summary(video_url):
    url = "https://video-to-text-video-transcription-and-summarization.p.rapidapi.com/transcribe"
    payload = {"url": video_url}
    headers = {
        "x-rapidapi-key": "7c1c41e8dfmshbcdff8a9c47c3dcp115a6cjsn736c42e0d50a",
        "x-rapidapi-host": "video-to-text-video-transcription-and-summarization.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    video_content = response.json()
    # Use OpenAI to generate a concise summary
    summary = summarize_video_openai(video_content)
    return summary