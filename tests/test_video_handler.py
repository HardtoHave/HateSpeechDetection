import unittest
from app.video_handler import get_video_summary

class TestVideoHandler(unittest.TestCase):
    def test_get_video_summary(self):
        summary = get_video_summary('static/video/Download.mp4')
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) > 0)