"""
Emotion detection module using the Watson NLP Emotion Predict service.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion expressed in the provided text.

    Args:
        text_to_analyze (str): Text to be analyzed.

    Returns:
        str: Raw text response received from the Watson NLP service.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers, timeout=30)
    return response.text
