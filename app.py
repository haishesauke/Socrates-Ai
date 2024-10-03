from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import asyncio
import edge_tts
import os

app = Flask(__name__)

# Configure the Google AI SDK
genai.configure(api_key="AIzaSyAuoRViqVlrynAfAOLu725z4MuO45apDos")

# Text-to-Speech function
async def save_text_to_speech(text, voice="en-US-GuyNeural", filename="output.mp3", folder="audio"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    output_file = os.path.join(folder, filename)

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    print(f"Audio saved to {output_file}")

def delete_all_audio_files(folder_path="audio"):
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.mp3'):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        print("All audio files deleted successfully")
    
    except Exception as e:
        print(f"Error: {e}")

def socrates(text: str):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction='''role : 
          Your role as a Socratic Tutor is to guide students through a series of thoughtful,
          open-ended questions, encouraging them to think critically, discover knowledge on their own,
          and deepen their understanding across a range of subjects.
          \n\nTask: 
          Your task is to engage students in inquiry-based learning by asking thought-provoking questions,
          promoting critical thinking, adapting to their progress, providing constructive feedback, and
          encouraging active participation across various subjects while fostering independent problem-solving skills.
          Instructions for Output: All bold characters should be enclosed in ** (for example, word). Strictly do not use any other kind of formatting and emojis.
          ''',
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(text)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    print(f"User Input: {user_input}")  # Debug print

    if user_input.lower() == "got it":
        response_text = socrates("I have understood, thanks for helping.")
        delete_all_audio_files()
    else:
        response_text = socrates(user_input)
        asyncio.run(save_text_to_speech(response_text))

    print(f"Socrates Response: {response_text}")  # Debug print
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
