# 🎬 VidSnap AI

> **Turn your images and text into short-form videos with AI-generated voiceovers.**

VidSnap AI is a web application that transforms a collection of images and a text description into a vertical short-form video.

The application uses **ElevenLabs** for AI-powered text-to-speech and **FFmpeg** for automated video generation. Generated videos are stored using **Vercel Blob** and displayed through a dedicated gallery.

🔗 **Live Demo:** https://vid-snap-ai-one.vercel.app?_vercel_share=YZaThAR7IFUgIif4MBaPuBYaPmFximea

---

## ✨ Features

- 📸 Upload multiple images
- 📝 Provide custom text for the video narration
- 🗣️ Generate AI voiceovers using ElevenLabs
- 🎞️ Automatically combine images and audio into a video
- 📱 Generate videos in vertical **1080×1920** format
- ⚡ Process videos using FFmpeg
- ☁️ Store generated videos using Vercel Blob
- 🖼️ Browse generated videos through a gallery
- ▶️ Play generated videos directly in the browser
- 🌐 Deployable as a serverless Flask application on Vercel

---
# HOME
<img width="1809" height="890" alt="Screenshot 2026-08-13 021334" src="https://github.com/user-attachments/assets/3234139a-0bc5-47a3-bb16-985f2636045a" />

# Create Page
<img width="1560" height="892" alt="Screenshot 2026-08-13 021348" src="https://github.com/user-attachments/assets/451dbcc6-d347-4d9f-aa49-9c0b3f9f425a" />

# Gallery Page
<img width="1753" height="885" alt="Screenshot 2026-08-13 021402" src="https://github.com/user-attachments/assets/725cbf1a-2c49-45e6-8035-1b6808e2160d" />





## 🎥 How It Works

The application follows this pipeline:

```text
        User
         │
         ▼
 ┌─────────────────┐
 │ Upload Images   │
 │ + Enter Text    │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │   Flask App     │
 │  Request /create│
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │  Temporary      │
 │  File Storage    │
 │     /tmp        │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │   ElevenLabs    │
 │  Text-to-Speech │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │     FFmpeg      │
 │ Images + Audio  │
 │   → MP4 Video   │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │  Vercel Blob    │
 │ Cloud Storage   │
 └────────┬────────┘
          │
          ▼
 ┌─────────────────┐
 │     Gallery     │
 │  Play Generated │
 │      Videos     │
 └─────────────────┘


