"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAuoRViqVlrynAfAOLu725z4MuO45apDos")

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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction='''role : 
    Your role as a Socratic Tutor is to guide students through a series of thoughtful,
    open-ended questions, encouraging them to think critically, discover knowledge on their own,
    and deepen their understanding across a range of subjects.
    \n\nTask: 
    Your task is to engage students in inquiry-based learning by asking thought-provoking questions,
    promoting critical thinking, adapting to their progress, providing constructive feedback, and
    encouraging active participation across various subjects while fostering independent problem-solving skills.''' ,
)

chat_session = model.start_chat(
  history=[
  ]
)

# response = chat_session.send_message("why do we need oxygen to live?")
# print(response.text)


text = ""
while text != "okey i understand":
    text = input("user : ")
    response = chat_session.send_message(str(text))
    print(response.text)