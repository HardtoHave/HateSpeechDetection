import unittest
from app.comment_analyzer import analyze_comment

class TestCommentAnalyzer(unittest.TestCase):
    def test_analyze_comment_with_hate_speech(self):
        comment = "This fuck video is full of fcuk hate and racism"
        result = analyze_comment(comment)
        self.assertTrue(result['is_hate_speech'])
        self.assertIn('fuck', result['hate_words'])
        self.assertIn('fcuk', result['hate_words'])

    def test_analyze_comment_without_hate_speech(self):
        comment = "This video is really informative and helpful"
        result = analyze_comment(comment)
        self.assertFalse(result['is_hate_speech'])
        self.assertEqual(len(result['hate_words']), 0)