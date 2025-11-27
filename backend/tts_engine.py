import pyttsx3
from main_code import filter_voices_by_language, parse_emotion, emotion_settings

def generate_audio(text, language, voice_id, output_path):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    language_voices = filter_voices_by_language(voices, language)
    selected_voice = voices[0].id if not voice_id else voice_id

    emotion, cleaned_text = parse_emotion(text)
    settings = emotion_settings(emotion)

    engine.setProperty("voice", selected_voice)
    engine.setProperty("rate", 170 + settings["rate_delta"])
    engine.setProperty("volume", settings["volume"])

    engine.save_to_file(cleaned_text, output_path)
    engine.runAndWait()
