import requests
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return output

    formatted_response = formatted_response = json.loads(response.text)

    output = {
        'anger': formatted_response["emotionPredictions"][0]["emotion"]["anger"],
        'disgust': formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
        'fear': formatted_response["emotionPredictions"][0]["emotion"]["fear"],
        'joy': formatted_response["emotionPredictions"][0]["emotion"]["joy"],
        'sadness': formatted_response["emotionPredictions"][0]["emotion"]["sadness"],
        'dominant_emotion': None
    }
    max_value = 0
    for key in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        if output[key] > max_value:
            max_value = output[key]
            highest_emotion = key
    output['dominant_emotion'] = highest_emotion
    return output