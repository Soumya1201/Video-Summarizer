import os
from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunk_text, chunked_summarize

def video_to_summary(
    video_path: str,
    model_size: str = "base",
    summarizer_model_name: str = "facebook/bart-large-cnn",
    use_chunking: bool = False,
) -> str:
    
    #1 Extract audio from video
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)

    #2 Transcribe audio to text
    transcript = transcribe_audio(audio_path, model_size=model_size)

    #3 Summarize the transcribed text
    if use_chunking:
        # summarize in chunks for long transcripts
        final_summary = chunked_summarize(
            text = transcript,
            summarize_func = lambda txt : summarize_text(
                txt, model_name = summarizer_model_name
            ),
            max_chunk_size = 2000
        )
    else:
        # summarize in one go
        final_summary = summarize_text(
            transcript,
            model_name = summarizer_model_name
        )

    # Clean up temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return final_summary

    
if __name__ == "__main__":
    video_file = "sample_video3.mp4"  # Replace with your video file path
    summary_output = video_to_summary(
        video_path=video_file,
        model_size="base",
        summarizer_model_name="facebook/bart-large-cnn",
        use_chunking=True
    )
    print("=== Final Summary ===")
    print(summary_output)