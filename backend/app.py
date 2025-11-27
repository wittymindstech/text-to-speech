from flask import Flask, request, send_file, jsonify
from tts_engine import generate_audio
import uuid
import os

app = Flask(__name__)

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text")
    language = data.get("language", "english")
    voice_id = data.get("voice_id")

    filename = f"output_{uuid.uuid4().hex}.wav"
    output_path = f"./output/{filename}"

    os.makedirs("output", exist_ok=True)

    try:
        generate_audio(text, language, voice_id, output_path)
        return jsonify({"download_url": f"/download/{filename}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download/<filename>")
def download(filename):
    return send_file(f"./output/{filename}", as_attachment=True)

if __name__ == "__main__":
    app.run()
