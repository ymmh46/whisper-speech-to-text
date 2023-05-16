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

# * Set Log Variables
success_list = []
failed_list = []

# * Loop Whisper Model

for file in os.listdir(input_path):

    # Setting input file
    input_file_path = input_path + "/" + file
    input_file = open(input_file_path, "rb")
    file_name = file.split(".")[0]
    print(f'Processing: {file}')

    # OpenAI Whisper Model Processing with error handling
    try:
        transcript = openai.Audio.transcribe(
            file=input_file, model="whisper-1", response_format="text", language="zh"
        )
        input_file.close()

        # Output file if success
        output_file_path = output_path + "/" + file_name + ".txt"
        output_file = open(output_file_path, "wt")
        output_file.write(transcript)
        output_file.close()

        print(f'Successfully transcribed: {file_name}\n')
        success_list.append(file)

    except openai.error.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}\n")
        failed_list.append(file)
        pass

    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}\n")
        failed_list.append(file)
        pass

    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}\n")
        failed_list.append(file)
        pass
    except:
        file_type = "." + file.split(".")[1]
        print(f"Error: Unexcepted Error\n")
        failed_list.append(file)

# * Export Log

success_list.sort()
failed_list.sort()

with open("./output/log.txt", "wt") as log:
    log.write("----Success List:----\n")
    for item in success_list:
        log.write(item + "\n")
    log.write("\n----Failed List----\n")
    for item in failed_list:
        log.write(item + "\n")