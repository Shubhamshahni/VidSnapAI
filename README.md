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