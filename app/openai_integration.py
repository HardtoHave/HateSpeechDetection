from openai import OpenAI
from config import OPENAI_API_KEY

chat_api_key = OPENAI_API_KEY

client = OpenAI(
    api_key=chat_api_key,
    base_url="https://api.aimlapi.com",
)

def check_hate_speech_openai(comment, video_summary):
    prompt = f"""
    Video summary: {video_summary}

    Comment: "{comment}"

    Analyze the comment above in the context of the video summary. 
    Determine if it contains hate speech or promotes hateful behavior. 
    Consider the guidelines for hate speech on social media platforms.

    Respond with:
    1. Whether the comment is hate speech (Yes/No)
    2. A brief explanation of your decision
    """

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant who knows everything.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    analysis = response.choices[0].message.content.strip().split('\n')
    is_hate_speech = 'yes' in analysis[0].lower()
    explanation = ' '.join(analysis[1:])

    return {
        'is_hate_speech': is_hate_speech,
        'explanation': explanation
    }


def summarize_video_openai(video_content):
    prompt = f"""
    Summarize the following video content in a concise manner:

    {video_content}

    Provide a brief summary that captures the main points and context of the video.
    """

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant who knows everything.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content.strip()