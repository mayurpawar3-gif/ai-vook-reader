def determine_voice_style(emotion):

    voice_map = {
        "joy": {
            "voice": "en-US-JennyNeural",
            "rate": "+10%"
        },

        "sadness": {
            "voice": "en-US-AriaNeural",
            "rate": "-15%"
        },

        "anger": {
            "voice": "en-US-GuyNeural",
            "rate": "+20%"
        },

        "fear": {
            "voice": "en-US-EricNeural",
            "rate": "-10%"
        },

        "surprise": {
            "voice": "en-US-DavisNeural",
            "rate": "+15%"
        },

        "neutral": {
            "voice": "en-US-GuyNeural",
            "rate": "+0%"
        }
    }

    return voice_map.get(
        emotion,
        voice_map["neutral"]
    )


def determine_ambience(emotion, dialogue_density):

    if emotion == "fear":
        return "suspense"

    if emotion == "sadness":
        return "piano"

    if emotion == "anger":
        return "intense"

    if dialogue_density > 0.3:
        return "conversation"

    return "neutral"
    