from gtts import gTTS

class AudioAgent:
    def generate_audio(self, text, output_file):
        tts = gTTS(text)
        tts.save(output_file)