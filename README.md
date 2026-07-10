# AI Content Generation Studio - InnoViast

## Overview
A modern, premium **AI Content Generation Studio** developed as part of the **InnoViast Internship Assignment Framework** (Week 2 - AI Solutions Engineering). This tool allows users to generate structured, high-quality content such as blog posts, social media captions, ad copy, emails, product descriptions, and LinkedIn posts.

## Problem Statement
Content creators and marketers often struggle to maintain consistency in tone, audience targeting, and formatting. This tool solves this by providing a highly structured template-based AI generation system where users have fine-grained control over length, tone, and audience.

## Features
- **Template Studio**: Generate highly structured content targeting specific formats (Blog, Ad Copy, etc.).
- **Fine-Grained Controls**: Control the tone (professional, casual, persuasive), audience, and length of the output.
- **Prompt Lab**: A built-in testing environment allowing users to compare four different iterations of prompt engineering (from basic to advanced system-level prompts) to understand how constraints improve quality.
- **Saved Library**: Auto-saves generated content into a local SQLite database for future editing and review.
- **Editable Outputs**: All generated content is fully editable directly in the UI before being saved or exported.
- **Mock/Offline Mode**: A rich simulated fallback mode allowing you to test the app even without API keys.

## Tech Stack
- **Frontend**: React (Vite), Custom CSS (Glassmorphism design), Lucide React (Icons).
- **Backend**: Python (FastAPI), SQLite (Database).
- **AI Integration**: Google Gemini API, OpenAI API (switchable from settings).

## Setup Steps

### 1. Backend Setup
```bash
cd backend
python -m venv .venv
# Activate the environment: 
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m uvicorn app.main:app --port 8000 --reload
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 3. API Keys (Optional)
The application works in "Mock Mode" by default. To use actual AI, go to the **Settings** tab in the app to configure your Gemini or OpenAI API keys, or set them in `backend/.env`.

## Screenshots
*(Add screenshots of your UI here to meet the assignment requirements)*
- [x] Template Studio
- [x] Prompt Lab
- [x] Saved Library

## Learning Outcomes
- Developed a full-stack AI integrated application using FastAPI and React.
- Mastered prompt engineering techniques (as demonstrated in the Prompt Lab) to control AI personas and structural outputs.
- Built a premium glassmorphism user interface without relying heavily on pre-built UI frameworks.
- Managed API integrations and error-handling fallbacks gracefully.
