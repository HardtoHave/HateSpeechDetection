import unittest
from unittest.mock import patch
from app.openai_integration import check_hate_speech_openai, summarize_video_openai


class TestOpenAIIntegration(unittest.TestCase):
    @patch('openai.Completion.create')
    def test_check_hate_speech_openai(self, mock_create):
        mock_create.return_value.choices = [type('obj', (object,), {'text': 'No\nThis comment is not hate speech.'})()]

        result = check_hate_speech_openai("Test comment", "Video summary")

        self.assertFalse(result['is_hate_speech'])
        self.assertTrue('explanation' in result)

    @patch('openai.Completion.create')
    def test_summarize_video_openai(self, mock_create):
        mock_create.return_value.choices = [type('obj', (object,), {'text': 'This is a summary of the video.'})()]

        result = summarize_video_openai("Video content")

        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)