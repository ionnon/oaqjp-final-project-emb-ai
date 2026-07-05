"""
Unit tests for the EmotionDetection package.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for validating dominant emotion detection.
    """

    def test_joy(self):
        """
        Test that a joyful statement returns joy as dominant emotion.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """
        Test that an angry statement returns anger as dominant emotion.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """
        Test that a disgusted statement returns disgust as dominant emotion.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """
        Test that a sad statement returns sadness as dominant emotion.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """
        Test that a fearful statement returns fear as dominant emotion.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
