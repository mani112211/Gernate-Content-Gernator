import os
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load env variables
load_dotenv()

from .database import init_db, get_all_articles, create_article, update_article, delete_article
from .models import GenerateRequest, SaveRequest, UpdateRequest
from .generator import generate_content

app = FastAPI(title="AI Content Generation Studio API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this. For local development, allow all.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Content Generation Studio API"}

@app.post("/api/generate")
def handle_generate(req: GenerateRequest):
    result = generate_content(
        provider=req.provider,
        api_key=req.api_key,
        template_type=req.template_type,
        topic=req.topic,
        tone=req.tone,
        length=req.length,
        audience=req.audience,
        output_format=req.output_format,
        extra_info=req.extra_info,
        version=req.version
    )
    return result

@app.get("/api/library")
def handle_get_library():
    try:
        articles = get_all_articles()
        return articles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/library")
def handle_save_to_library(req: SaveRequest):
    try:
        saved_article = create_article(
            title=req.title,
            content=req.content,
            template_type=req.template_type,
            tone=req.tone,
            length=req.length,
            audience=req.audience,
            prompt_used=req.prompt_used
        )
        return saved_article
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/library/{article_id}")
def handle_update_library(article_id: int, req: UpdateRequest):
    try:
        updated = update_article(article_id, req.title, req.content)
        if not updated:
            raise HTTPException(status_code=404, detail="Article not found")
        return updated
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/library/{article_id}")
def handle_delete_library(article_id: int):
    try:
        success = delete_article(article_id)
        return {"success": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/test-keys")
def handle_test_keys(req: dict):
    provider = req.get("provider", "mock")
    api_key = req.get("api_key", "")
    
    if provider == "mock":
        return {"valid": True, "message": "Mock mode active. No API key needed."}
        
    if not api_key:
        return {"valid": False, "message": "API key is required."}
        
    try:
        if provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")
            # Minimal check
            response = model.generate_content("Say OK")
            if response.text:
                return {"valid": True, "message": "Gemini API key is valid."}
            else:
                return {"valid": False, "message": "No response returned from Gemini API."}
                
        elif provider == "openai":
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Say OK"}],
                max_tokens=5
            )
            if response.choices[0].message.content:
                return {"valid": True, "message": "OpenAI API key is valid."}
            else:
                return {"valid": False, "message": "No response returned from OpenAI API."}
        else:
            return {"valid": False, "message": "Unsupported provider."}
            
    except Exception as e:
        return {"valid": False, "message": f"Validation failed: {str(e)}"}
