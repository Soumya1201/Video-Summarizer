import subprocess
import whisper
import os

# subprocess executes shell command

def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    """
    Extracts audio from a video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.
        audio_path (str): Path to save the extracted audio file.

    Returns:
        str: Path to the extracted audio file.
    """
    if os.path.exists(audio_path):
        os.remove(audio_path)

    command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        audio_path,
        "-y"
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    return audio_path

def transcribe_audio(audio_path: str, model_size: str = "base") -> str:
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    transcript = result["text"]
    return transcript

    