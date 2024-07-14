from deepgram import Deepgram
import asyncio
import json

# Your Deepgram API Key
DEEPGRAM_API_KEY = 'f83820f4820fe850f25c3a2f0aecf5439cda8a5b'

# Name and extension of the file you downloaded (e.g., sample.wav)
PATH_TO_FILE = "Voice_sample_1.m4a"


async def main():
    # Initialize the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    # Open the audio file
    with open(PATH_TO_FILE, 'rb') as audio:
        # Replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        print(json.dumps(response, indent=4))


asyncio.run(main())
