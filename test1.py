import asyncio
import edge_tts
import os

def save_text_to_speech(text, voice="en-US-GuyNeural", filename="output.mp3", folder="audio"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    output_file = os.path.join(folder, filename)

    async def amain():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

    # Create a new event loop if one doesn't exist
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as e:
        if str(e) == 'There is no current event loop in thread':
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    
    loop.run_until_complete(amain())
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

delete_all_audio_files()
