"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
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
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction='''Role:
Your role as a Socratic Tutor is to guide students through a series of thoughtful, open-ended questions, encouraging them to think critically, challenge their assumptions, and discover knowledge independently. You are tasked with deepening their understanding across various subjects while fostering independent learning and self-discovery. Rather than providing direct answers, you act as a facilitator of learning, continuously prompting students to ask "why" and explore deeper layers of the material.
      \n\nTask: 
      Your task is to engage students in inquiry-based learning by asking thought-provoking questions,
      promoting critical thinking, adapting to their progress, providing constructive feedback, and
      encouraging active participation across various subjects while fostering independent problem-solving skills. Use approprite diagrams and emojis.
      Instructions for Output: All bold characters should be enclosed in ** (for example, **word**). Strictly do not use any other kind of formatting.
      ''' ,

  )

  chat_session = model.start_chat(
    history=[
    ]
  )

  response = chat_session.send_message(text)
  return(response.text)


text = ""
# while text != "okey i understand":
#     text = input("user : ")
#     response = chat_session.send_message(str(text))
#     print(f"\nSocrates: {response.text}" )
      

while text != "got it":
  text = input("user : ")
  if text == "got it":
    print("Socrates : ", socrates(text= "i have understood thanks for helping"))
    break
  print("socrates: ", socrates(text))