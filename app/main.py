from flask import Flask, render_template, request, jsonify
from app.video_handler import get_video_summary
from app.comment_analyzer import analyze_comment
from app.openai_integration import check_hate_speech_openai

app = Flask(__name__)

VIDEO_SUMMARY = ""


@app.route('/')
def index():
    global VIDEO_SUMMARY
    if not VIDEO_SUMMARY:
        VIDEO_SUMMARY = get_video_summary()
    return render_template('index.html')


@app.route('/analyze_comment', methods=['POST'])
def analyze_comment_route():
    comment = request.json['comment']

    # First, check against our basic dataset
    basic_result = analyze_comment(comment)

    if basic_result['is_hate_speech']:
        return jsonify({'is_hate_speech': True, 'message': 'Comment blocked due to potential hate speech.'})

    # If it passes the basic check, use OpenAI for a more nuanced analysis
    openai_result = check_hate_speech_openai(comment, VIDEO_SUMMARY)

    return jsonify(openai_result)


if __name__ == '__main__':
    app.run(debug=True)