# 🎥 universal-video-transcriber - Turn video links into text fast

[![Download](https://img.shields.io/badge/Download%20Here-2F80ED?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ultraconservative-abneylevel672/universal-video-transcriber)

## 🖥️ What this app does

Universal Video Transcriber turns a video URL into a transcript file in JSON format.

Use it when you want to:

- copy spoken words from a video
- keep a time-based record of audio
- process links from many sites in one tool
- get text from videos without doing it by hand

It follows this flow:

- video URL in
- media download with `yt-dlp`
- audio cleanup with `ffmpeg`
- speech to text with `faster-whisper`
- timestamped JSON out

## 📥 Download and set up on Windows

1. Visit the download page here:  
   [https://github.com/ultraconservative-abneylevel672/universal-video-transcriber](https://github.com/ultraconservative-abneylevel672/universal-video-transcriber)

2. On the page, look for the latest release or the main project files.

3. Download the Windows version if one is provided, or download the source package if that is the only option.

4. Save the file to your computer, then open the folder where it downloaded.

5. If you get a ZIP file, right-click it and choose Extract All.

6. Open the extracted folder and look for the app file or setup file.

7. If the app opens in a terminal window, that is normal for this tool.

8. Keep the folder in a place you can find again, such as Downloads or Desktop.

## ⚙️ What you need

For a smooth run on Windows, install these tools first:

- Python 3.10 or newer
- `ffmpeg`
- `yt-dlp`

You also need enough free disk space for temporary video files. A larger video will use more space.

If you plan to process long videos, use a machine with at least 8 GB of memory.

## 🚀 First-time setup

If you downloaded the source version, do this on Windows:

1. Install Python from the official Python website.
2. Make sure Python is added to PATH during install.
3. Open Command Prompt in the project folder.
4. Create a virtual environment:

```bash
python -m venv .venv
```

5. Activate it:

```bash
.venv\Scripts\activate
```

6. Install the app requirements:

```bash
pip install -r requirements.txt
```

7. Install `ffmpeg` and `yt-dlp` if they are not already on your system.

## ▶️ Run the transcriber

Use the command below to check that your setup works:

```bash
python skill/video-url-transcriber/scripts/transcribe_url.py --doctor
```

Then run a transcription with a video link:

```bash
python skill/video-url-transcriber/scripts/transcribe_url.py "https://www.youtube.com/watch?v=..." --model-size small
```

If you want faster results, keep `--model-size small`.

If you want better accuracy on harder audio, use a larger model size.

## 🌐 Run the local API

If you want to send requests from another app, start the API server:

```bash
python skill/video-url-transcriber/scripts/run_api.py
```

The server runs on:

```bash
http://127.0.0.1:8099
```

Use this endpoint to transcribe a video:

```bash
curl -s http://127.0.0.1:8099/transcribe \
  -H 'content-type: application/json' \
  -d '{
    "url": "https://www.youtube.com/watch?v=...",
    "language": null,
    "model_size": "small",
    "word_timestamps": true,
    "persist_media": false
  }'
```

## 📄 Output format

The app returns JSON with details about the source video and the transcript.

Example shape:

```json
{
  "source_url": "https://x.com/.../video/1",
  "platform": "x",
  "title": "Example Video Title",
  "language": "en",
  "model_size": "small",
  "transcript": [
    {
      "start": 0.0,
      "end": 3.2,
      "text": "Hello and welcome."
    }
  ]
}
```

Common fields include:

- `source_url` — the original link you gave the app
- `platform` — the site name detected by the tool
- `title` — the video title when available
- `language` — the spoken language, when the tool can detect it
- `model_size` — the speech model used
- `transcript` — the timed text split into parts

## 🧭 How to use it well

Use short, clear video links when possible.

If a site blocks downloads, try a different link from the same platform.

If audio is noisy, the transcript may have more errors.

If the video has more than one speaker, the output still keeps time stamps, so you can follow who said what by looking at the context.

For best results:

- use good audio
- choose the right language if you know it
- pick a larger model for harder audio
- keep `word_timestamps` on if you need fine timing

## 🧪 Common tasks

### Transcribe a single video

```bash
python skill/video-url-transcriber/scripts/transcribe_url.py "VIDEO_URL"
```

### Check your setup

```bash
python skill/video-url-transcriber/scripts/transcribe_url.py --doctor
```

### Start the API server

```bash
python skill/video-url-transcriber/scripts/run_api.py
```

### Send a test request

```bash
curl -s http://127.0.0.1:8099/transcribe \
  -H 'content-type: application/json' \
  -d '{
    "url": "VIDEO_URL",
    "language": null,
    "model_size": "small",
    "word_timestamps": true,
    "persist_media": false
  }'
```

## 🗂️ Files you may see

After a run, the tool may create:

- a JSON transcript file
- temporary media files
- audio files used during processing

If `persist_media` is set to `false`, the app cleans up temporary files after it finishes.

If you keep media, use a folder with enough space.

## 🔧 Troubleshooting

If the app does not start, check these items:

- Python is installed
- `ffmpeg` is installed
- `yt-dlp` is installed
- you are in the correct folder
- the virtual environment is active

If a video link fails, try another supported site or a different video URL.

If transcription takes a long time, use a shorter video or a smaller model.

If you see missing audio errors, the source video may not contain clear sound.

## 📌 Best results on Windows

For smoother use:

- keep the app folder simple, such as `C:\transcriber`
- avoid paths with special characters
- close other heavy apps while processing large videos
- use wired power on a laptop during long jobs

## 🧩 Supported sources

The tool works with any site that `yt-dlp` can read.

That usually includes:

- YouTube
- X
- Vimeo
- many public video pages
- other direct media pages supported by `yt-dlp`

## 📝 Typical workflow

1. Copy a video URL.
2. Run the transcriber.
3. Wait for the audio to download and process.
4. Open the JSON output.
5. Use the timestamps to find the part you need

## 📎 Example use cases

- save a class lecture as text
- turn a meeting recording into notes
- review a talk without replaying the full video
- search spoken content more easily
- keep a time-based transcript for later work