import streamlit as st
import os
from main import video_to_summary

def main():
    st.title("Video Summarizer")
    st.write("Upload a video file, and get a summarized transcript!")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        temp_video_path = "uploaded_video.mp4"

        # Save uploaded video temporarily
        with open(temp_video_path, "wb") as f:
            f.write(uploaded_file.read())

        st.info("Transcribing and summarizing... This may take a few minutes.")

        try:
            # Run the summarization pipeline
            summary_result = video_to_summary(
                video_path=temp_video_path,
                model_size="base",
                summarizer_model_name="facebook/bart-large-cnn",
                use_chunking=True
            )

            # Display the final summary
            st.subheader("Summary")
            st.write(summary_result)

        except Exception as e:
            st.error(f"Error processing video: {e}")

        finally:
            # Clean up uploaded video file
            if os.path.exists(temp_video_path):
                os.remove(temp_video_path)

if __name__ == "__main__":
    main()
