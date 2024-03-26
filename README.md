# Audio File Format Converter

This script is designed to convert audio files from one format to another using the PyDub library.

## Functionality

The script performs the following tasks:

- **Quotation Error Handling:** Input handles quotations in the file path.
- **Format Error Handling:** Handles "." in the extension / format prompt.
- **Timestamp Generation:** Appends a timestamp to the end of the file name.
- **Conversion:** Converts the audio file to the specified format.

## Dependencies

1. **Python and PyDub:**
   - Python: Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
   - PyDub: A Python library for audio manipulation. Install it via pip:
     ```
     pip install pydub
     ```

2. **FFmpeg:** 
   - FFmpeg is required for audio conversion. You can download FFmpeg from [here](https://ffmpeg.org/download.html).

## How to Run

1. **Clone:**

Clone this repository to your local machine: ``git clone https://github.com/sudoebm/audio-format-converter.git``

2. **Navigate to the Directory:**

Navigate to the directory containing the script: ``cd <path-containing-audio-converter.py>``


3. **Run the Script:**

Run the script by executing the following command and follow the prompts: ``python audio_converter.py``


4. **Enter Inputs:**

- Enter the path of the audio file you wish to convert when prompted.
- Optionally, enter the desired output format (e.g., mp3, ogg, etc.) or leave it blank to default to WAV format.

    ### Supported Audio Formats for Conversion
    
    #### PyDub:
    - WAV (Waveform Audio File Format)
    - MP3 (MPEG-1 Audio Layer III)
    - OGG (Ogg Vorbis)
    - FLAC (Free Lossless Audio Codec)
    - M4A (MPEG-4 Part 14)
    - AIFF (Audio Interchange File Format)
    - AU (Audio File)
    - RAW (Raw audio data)
    - WMA (Windows Media Audio)

    #### FFmpeg:
    - WAV
    - MP3
    - OGG
    - FLAC
    - M4A
    - AIFF
    - AU
    - RAW
    - WMA
    - AAC (Advanced Audio Coding)
    - AC3 (Audio Coding 3)
    - ALAC (Apple Lossless Audio Codec)
    - AMR (Adaptive Multi-Rate Codec)
    - DTS (Digital Theater Systems)
    - OPUS
    - PCM (Pulse-code Modulation)

5. **Conversion:**

The script will convert the audio file and display the output path and file.
