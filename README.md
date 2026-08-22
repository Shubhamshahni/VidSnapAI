
# 🎬 VidSnap AI

> **Turn your images and text into short-form videos with AI-generated voiceovers.**

VidSnap AI is an AI-powered short-video generator built with Python and Flask. Upload multiple images, provide a text description, and VidSnap AI combines them with an AI-generated voiceover to create a short-form video.

The project also includes private cloud storage for uploaded media and generated reels, along with a gallery for viewing generated videos.

## ✨ Features

- 🖼️ Upload multiple images
- ☁️ Direct browser-to-Vercel Blob uploads
- 🔒 Private media storage
- 🎙️ AI-generated voiceovers from text
- 🎬 Automatic video generation using FFmpeg
- 🖥️ Responsive web interface
- 🖼️ Generated reel gallery
- ▶️ Private reel streaming
- ⚡ Serverless deployment with Vercel
- 🐍 Flask-based backend

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Vercel Python Runtime

### AI & Media Processing
- AI Text-to-Speech
- FFmpeg

### Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Storage & Deployment
- Vercel Blob
- Vercel
- GitHub

## 🏗️ Architecture

VidSnap AI uses a hybrid architecture to avoid sending large image files through the serverless Flask function.

```text
                    ┌──────────────────┐
                    │     Browser      │
                    │                  │
                    │ Select Images    │
                    └────────┬─────────┘
                             │
                             │ Direct Upload
                             ▼
                    ┌──────────────────┐
                    │   Vercel Blob    │
                    │  Private Storage │
                    └────────┬─────────┘
                             │
                             │ Blob Pathnames
                             ▼
                    ┌──────────────────┐
                    │   Flask /create  │
                    │                  │
                    │ Download Images  │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    ▼                  ▼
             ┌──────────────┐   ┌──────────────┐
             │ AI Voiceover │   │    FFmpeg    │
             └──────┬───────┘   └──────┬───────┘
                    │                  │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │ Generated Reel   │
                    │                  │
                    │ Vercel Blob      │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │     Gallery      │
                    └──────────────────┘

                    
```
# 📸 Screenshots
## HOME PAGE
<img width="1895" height="905" alt="home" src="https://github.com/user-attachments/assets/f0d87f1b-ac55-42c2-a13c-cc942944138d" />

## CREATE PAGE
<img width="1900" height="902" alt="create" src="https://github.com/user-attachments/assets/fe6157b9-d97c-4332-97eb-73b59283a3da" />

## GALLERY PAGE
<img width="1919" height="508" alt="gallery" src="https://github.com/user-attachments/assets/dd6225f8-2285-4542-951c-12f1046d7f6a" />


