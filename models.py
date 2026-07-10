from pydantic import BaseModel, Field
from typing import Optional

class GenerateRequest(BaseModel):
    template_type: str = Field(..., description="E.g., blog post, caption, ad copy, email, product description, LinkedIn post")
    topic: str = Field(..., description="The main subject or core guidelines for content creation")
    tone: str = Field(..., description="E.g., professional, casual, humorous, persuasive")
    length: str = Field(..., description="E.g., short, medium, long")
    audience: str = Field(..., description="E.g., general, professionals, tech-savvy, youth")
    output_format: str = Field(..., description="E.g., plain text, markdown, bullet points, html")
    extra_info: Optional[str] = Field("", description="Additional user specifications or parameters")
    provider: str = Field("mock", description="AI API Provider: gemini, openai, or mock")
    api_key: Optional[str] = Field(None, description="User's API Key (if using gemini or openai)")
    version: str = Field("v4", description="Prompt template version: v1, v2, v3, or v4")

class SaveRequest(BaseModel):
    title: str
    content: str
    template_type: str
    tone: str
    length: str
    audience: str
    prompt_used: str

class UpdateRequest(BaseModel):
    title: str
    content: str
