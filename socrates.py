"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import test1

import google.generativeai as genai

genai.configure(api_key="AIzaSyAuoRViqVlrynAfAOLu725z4MuO45apDos")

def socrates(text : str):
# Create the model
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
      ''' ,
  )

  chat_session = model.start_chat(
    history=[
    ]
  )

  response = chat_session.send_message(text)
  return(response.text)


text = "" 

while text != "got it":
  text = input("user : ")
  if text == "got it":
    print("Socrates : ", socrates(text= "i have understood thanks for helping"))
    test1.delete_all_audio_files()
    
    break
  resp = socrates(text)
  test1.save_text_to_speech(resp)
  print(f"Socrates : {resp}")
