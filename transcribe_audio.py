from deepgram import Deepgram
import asyncio
import json

# Your Deepgram API Key
apiKey = "f83820f4820fe850f25c3a2f0aecf5439cda8a5b"

# Name and extension of the file you downloaded (e.g., sample.wav)
PATH_TO_FILE = 'Voice_sample_1.m4a'


async def transcribe_audio(audio_file):
    # Initialize the deepgram SDK
    dg_client = Deepgram(apiKey)
    # Open the audio file
    with open(audio_file, 'rb') as audio:
        # Replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/mp4'}
        response = await dg_client.transcription.prerecorded(source, options={"punctuate": True})
        print(json.dumps(response, indent=4))
        return json.dumps(response, indent=4)


transcribedData = asyncio.run(transcribe_audio(PATH_TO_FILE))
with open("trancribedData.json", 'w') as jsonfile:
    jsonfile.write(transcribedData)
print("Transcribed data ready!")
jsonFile = open("trancribedData.json")
fileData = json.load(jsonFile)
print(fileData["results"]["channels"][0]["alternatives"][0]["transcript"])
filedata1 = fileData["results"]["channels"]
print(filedata1[0]["alternatives"][0]["transcript"])
