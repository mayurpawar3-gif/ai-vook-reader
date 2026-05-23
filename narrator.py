import edge_tts

from audio_director import determine_voice_style


async def generate_voice(
    text,
    emotion,
    output_file
):

    style = determine_voice_style(
        emotion
    )

    voice = style["voice"]

    rate = style["rate"]

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate
    )

    await communicate.save(output_file)
    