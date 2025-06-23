import whisper
import moviepy.editor as mp
import os
import glob
import torch
import tempfile

def transcribe_video(video_path, model):
    """
    Extracts audio from a video file, transcribes it using Whisper,
    and saves the transcription to a text file.
    """
    print(f"Starting transcription for {video_path}...")
    
    try:
        # Use a temporary directory for the audio file
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = os.path.join(tmpdir, "audio.wav")

            print("Extracting audio...")
            video = mp.VideoFileClip(video_path)
            # Specify a codec to avoid potential issues
            video.audio.write_audiofile(audio_path, codec='pcm_s16le')

            print("Transcribing audio...")
            # Whisper will automatically use the GPU if torch is installed with CUDA.
            result = model.transcribe(audio_path)
            
            transcription = result["text"]
            
            # Save the transcription to the 'transcriptions' directory
            output_dir = "transcriptions"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            base_name = os.path.splitext(os.path.basename(video_path))[0]
            output_path = os.path.join(output_dir, f"{base_name}.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(transcription)
                
            print(f"Transcription saved to {output_path}")

    except Exception as e:
        print(f"An error occurred with {video_path}: {e}")

def main():
    """
    Finds all video files in the 'videos' directory and transcribes them.
    """
    # Load the Whisper model.
    # With an RTX 4070ti, you can likely use "medium.en" or even "large"
    # for better accuracy. "base.en" is faster but less accurate.
    # Whisper automatically uses the GPU if available.
    try:
        print("Loading Whisper model...")
        model = whisper.load_model("base.en")
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading whisper model: {e}")
        print("Please ensure you have PyTorch installed correctly.")
        print("If you have an NVIDIA GPU, make sure you installed PyTorch with CUDA support.")
        print("You can try: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121")
        return

    videos_dir = "videos"
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)
        print(f"Created directory: {videos_dir}")
        print("Please add your video files to this directory.")
        return

    # Supported video formats by moviepy
    video_extensions = ["*.mp4", "*.mkv", "*.avi", "*.mov", "*.webm"]
    video_files = []
    for ext in video_extensions:
        video_files.extend(glob.glob(os.path.join(videos_dir, ext)))

    if not video_files:
        print(f"No video files found in the '{videos_dir}' directory.")
        print("Please add your video files to this directory.")
        return

    for video_file in video_files:
        transcribe_video(video_file, model)

if __name__ == "__main__":
    main() 