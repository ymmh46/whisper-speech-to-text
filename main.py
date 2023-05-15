import os
import openai
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()


# Setup openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# * Get List Model
# list_model = openai.Model.list()

# * Set file path

input_path = r"./input"
output_path = r"./output"
# audio_file = open("./tmp/audio.mp3", "rb")
# output_file = open("./tmp/subtitle.txt", "wt")

# * Loop Whisper Model

for file in os.listdir(input_path):
    input_file_path = input_path + "/" + file
    input_file = open(input_file_path, "rb")
    file_name = file.split(".")[0]

    print(f'Processing: {file_name} ...')

    transcript = openai.Audio.transcribe(
        file=input_file, model="whisper-1", response_format="text", language="zh"
    )
    input_file.close()

    output_file_path = output_path + "/" + file_name + ".txt"
    output_file = open(output_file_path, "wt")
    output_file.write(transcript)
    output_file.close()

    print(f'Successfully transcribed: {file_name} !')

# output_file.write(transcript)
# output_file.close()
# audio_file.close()
