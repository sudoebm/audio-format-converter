from pydub import AudioSegment
import os
from datetime import datetime

# Quotation error handle
    # "." format error handle
    # Generate a timestamp for unique naming
    # path + timestamp + format
    # Load the audio file
    # Convert and save
def convert_audio_file(input_file_path, output_format='wav'):
    print("Starting the conversion process...")
    input_file_path = input_file_path.strip("\"'")
    output_format = output_format.lstrip('.').lower() if output_format else "wav"
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_path = os.path.splitext(input_file_path)[0] + '_' + timestamp + '.' + output_format
    audio = AudioSegment.from_file(input_file_path)
    audio.export(output_file_path, format=output_format)
    print(f"Conversion completed. File saved as {output_file_path}")

# Prompt for input path
    # Prompt for the desired output format (Default .wav)
    # Convert
    # Keep alive
if __name__ == "__main__":
    input_file_path = input("Enter the path of the audio file you wish to convert: ")
    output_format = input("Enter the desired output format or [.wav]: ").strip()
    convert_audio_file(input_file_path, output_format)
    input("Press Enter to exit...")
