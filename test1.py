'''
pip install asyncio edge-tts

'''

import asyncio
import edge_tts
import os
## aarjav and Karan please try en-US-AnaNeural as voice here P.S. recommanded
def save_text_to_speech(text, voice="en-US-GuyNeural", filename="output.mp3", folder="audio"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    output_file = os.path.join(folder, filename)

    async def amain():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

    loop = asyncio.get_event_loop_policy().get_event_loop()
    
    loop.run_until_complete(amain())
    print(f"Audio saved to {output_file}")
 



# text = "i lelouch v britania commands you .... kill yourself!!"
# save_text_to_speech(text, voice= "en-US-GuyNeural", filename="hello_world.mp3")


# voice options:
# cute : en-US-AnaNeural
# friendly male : en-US-GuyNeural


def delete_all_audio_files(folder_path = "/workspaces/Socrates-Ai/audio"):
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.mp3'):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        print("all audio files deleted successfully")
    
    except Exception as e:
        print(f"Error: {e}")

delete_all_audio_files()