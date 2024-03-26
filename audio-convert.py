from pydub import AudioSegment
import os
from datetime import datetime

def handle_quotation_error(file_path):
    """Handle quotation errors in the file path."""
    return file_path.strip("\"'")

def handle_format_error(output_format):
    """Handle errors in the output format."""
    return output_format.lstrip('.').lower() if output_format else "wav"

def generate_timestamp():
    """Generate a timestamp for unique naming."""
    return datetime.now().strftime("%Y%m%d%H%M%S")

def load_audio_file(input_file_path):
    """Load the audio file."""
    return AudioSegment.from_file(input_file_path)

def save_audio_file(audio, output_file_path, output_format):
    """Convert and save the audio file."""
    audio.export(output_file_path, format=output_format)
    print(f"Conversion completed. File saved as {output_file_path}")

def convert_audio_file(input_file_path, output_format='wav'):
    """Convert audio file to the specified format."""
    print("Starting the conversion process...")
    input_file_path = handle_quotation_error(input_file_path)
    output_format = handle_format_error(output_format)
    timestamp = generate_timestamp()
    output_file_path = os.path.splitext(input_file_path)[0] + '_' + timestamp + '.' + output_format
    audio = load_audio_file(input_file_path)
    save_audio_file(audio, output_file_path, output_format)

def prompt_for_input():
    """Prompt for input path and desired output format."""
    while True:
        input_file_path = input("Enter the path of the audio file you wish to convert: ")
        if os.path.isfile(handle_quotation_error(input_file_path)):
            break
        else:
            print("Invalid file path. Please enter a valid path.")

    while True:
        output_format = input("Enter the desired output format or [.wav]: ").strip()
        if output_format.lower() in ['wav', 'mp3', 'ogg', 'flac', 'm4a', 'aiff', 'au', 'raw', 'wma']:
            break
        else:
            print("Invalid output format. Please enter a valid format or leave it blank for WAV.")

    return input_file_path, output_format

if __name__ == "__main__":
    input_file_path, output_format = prompt_for_input()
    convert_audio_file(input_file_path, output_format)
    input("Press Enter to exit...")
