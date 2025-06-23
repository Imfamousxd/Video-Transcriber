# Local Video Transcriber using OpenAI Whisper

This project allows you to easily transcribe video files locally using OpenAI's Whisper model. It's designed to be run on a machine with a powerful GPU (like an NVIDIA RTX series) for fast and accurate transcription.

## Features

- **Local & Free:** Runs entirely on your own machine. No API keys or fees required.
- **GPU Accelerated:** Automatically uses your NVIDIA GPU for significantly faster transcription if PyTorch with CUDA is installed.
- **Simple Workflow:** Just drop your videos in a folder and run one command.
- **Batch Processing:** Transcribes all videos found in the `videos` directory.

---

## Prerequisites

- **Python 3.8+:** Make sure you have Python installed. You can get it from [python.org](https://www.python.org/downloads/).
- **Git:** For cloning the repository.
- **NVIDIA GPU (Recommended):** For fast transcriptions. You'll need to have the NVIDIA CUDA drivers installed.

---

## Setup Instructions

Follow these steps to get the project running.

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone <your-github-repo-url>
cd <repository-folder-name>
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to keep the project's dependencies isolated.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows:**
  ```powershell
  .\\venv\\Scripts\\Activate.ps1
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```
Your terminal prompt should now be prefixed with `(venv)`.

### 4. Install Dependencies

Install all the necessary Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**Special Note for NVIDIA Users:** The `requirements.txt` file includes `torch` which should install a version with CUDA support by default if you have a compatible setup. If you encounter any issues with the GPU not being used, you may need to install a specific version of PyTorch that matches your system's CUDA toolkit version. You can find the correct command on the [PyTorch website](https://pytorch.org/get-started/locally/).

---

## How to Use

### 1. Add Your Videos

- The script will automatically create a `videos` directory if it doesn't exist.
- Place all the video files you want to transcribe (`.mp4`, `.mov`, `.mkv`, etc.) inside this `videos` folder.

### 2. Run the Transcriber

Make sure your virtual environment is still active and run the main script:

```bash
python transcriber.py
```

### 3. Find Your Transcripts

- The script will create a `transcriptions` directory.
- For each video, a corresponding `.txt` file with the transcription will be saved in this folder.
- The process can take a while depending on the size of the files and the power of your hardware. You will see progress updates in the terminal.

---

## Improving Accuracy

For higher-quality transcriptions, you can use a larger Whisper model. The default is `"base.en"`, which is fast but less accurate.

- Open the `transcriber.py` file.
- Find this line: `model = whisper.load_model("base.en")`
- You can change it to one of the following:
  - `"tiny.en"`
  - `"base.en"` (default)
  - `"small.en"`
  - `"medium.en"` (recommended for good balance)
  - `"large-v2"` (most accurate, but requires more VRAM and is slower)

Save the file and run the script again to use the new model. 