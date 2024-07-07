import json


def load_hate_speech_dataset():
    with open('../data/hate_speech_dataset.json', 'r') as f:
        return set(json.load(f))


hate_speech_words = load_hate_speech_dataset()


def analyze_comment(comment):
    words = set(comment.lower().split())
    hate_words = words.intersection(hate_speech_words)

    is_hate_speech = len(hate_words) > 0

    return {
        'is_hate_speech': is_hate_speech,
        'hate_words': list(hate_words)
    }
