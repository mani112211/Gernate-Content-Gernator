import os
import google.generativeai as genai
from openai import OpenAI

# System prompts showing prompt engineering iterations (v1 - v4)

def get_prompt_v1(template_type: str, topic: str) -> str:
    return f"Write a {template_type} about {topic}."

def get_prompt_v2(template_type: str, topic: str, format_control: str) -> str:
    return (
        f"Write a {template_type} about: {topic}.\n"
        f"Make sure to format it as {format_control}."
    )

def get_prompt_v3(template_type: str, topic: str, tone: str, audience: str, format_control: str) -> str:
    return (
        f"You are a helpful content writer. Write a {template_type} about: {topic}.\n"
        f"Target Audience: {audience}\n"
        f"Tone of voice: {tone}\n"
        f"Output Format: {format_control}"
    )

def get_prompt_v4(template_type: str, topic: str, tone: str, audience: str, format_control: str, length: str, extra_info: str) -> str:
    length_desc = {
        "short": "Short (around 100-150 words, concise, high impact)",
        "medium": "Medium (around 300-500 words, balanced details)",
        "long": "Long (around 800-1000 words, deep-dive article layout, detailed points)"
    }.get(length.lower(), "Medium length")

    return (
        f"You are an elite, results-driven AI content architect specializing in copywriting.\n"
        f"Your task is to write a high-converting, professional-grade {template_type} about the topic specified below.\n\n"
        f"--- AUDIENCE & VOICE CONTROL ---\n"
        f"- Target Audience: {audience} (Write specifically using terminology and themes that resonate with this group).\n"
        f"- Tone: {tone} (Strictly adopt this writing style. If casual, use relatable, friendly phrasing. If professional, use industry standard verbs and structured phrasing. If persuasive, build up to a strong benefit-driven conclusion).\n"
        f"- Length: {length_desc}\n\n"
        f"--- FORMATTING RULES ---\n"
        f"- Output Format: {format_control} (If markdown, use headers, list items, bold keywords for scannability; if bullet points, start each key insight with an emoji or hyphen).\n"
        f"- Do NOT use generic placeholder text (like '[Your Name]', '[Insert Link]', or '[Company]'). Provide realistic context instead.\n"
        f"- Keep the output clean, starting directly with the title/headline and ending with a final call to action or summary.\n\n"
        f"--- TOPIC ---\n"
        f"Topic / Subject details:\n"
        f"{topic}\n\n"
        f"--- ADDITIONAL USER CONSTRAINTS ---\n"
        f"{extra_info if extra_info else 'None provided'}\n\n"
        f"Draft the {template_type} following these instructions. Present the text directly in clean Markdown format."
    )

def generate_mock_content(template_type: str, topic: str, tone: str, audience: str, format_control: str, length: str, version: str) -> str:
    # Rich mock text generator to make the app fully testable without keys
    intro_version = {
        "v1": f"# Draft (Basic V1 prompt)\n\nHere is a simple generation about {topic}.\n\n",
        "v2": f"# Generated {template_type} (V2 Structured prompt)\n\n",
        "v3": f"# {template_type.title()} for {audience} (V3 Persona prompt)\n\n*Tone: {tone}* | *Audience: {audience}*\n\n",
        "v4": f"# 🚀 THE FINAL ARTICLE: {topic.upper()}\n\n"
              f"**Target Audience:** `{audience}` | **Style & Tone:** `{tone}` | **Format:** `{format_control}` | **Draft:** `v4 (Production System Prompt)`\n\n"
              f"--- \n\n"
    }.get(version, "# Generated Output\n\n")

    # Body generation based on template type
    if template_type.lower() == "blog post":
        body = (
            f"## Introduction: Why {topic} Matters\n"
            f"In today's fast-paced environment, `{topic}` has emerged as a crucial area of interest. "
            f"Whether you are looking to optimize your workflows or understand key dynamics, paying attention to details is the first step.\n\n"
            f"## Key Takeaways to Keep in Mind\n"
            f"1. **Strategic Intent**: Successful execution starts with clarity of goals.\n"
            f"2. **Audience Connection**: Always format your message for `{audience}`.\n"
            f"3. **Consistency**: Consistent tone helps in building long term retention.\n\n"
            f"## Deep Dive & Insights\n"
            f"Analyzing `{topic}` shows that using a `{tone}` approach yields the best interaction rates. "
            f"By aligning the length to `{length}`, we ensure our readers are fully engaged without being overwhelmed.\n\n"
            f"## Conclusion & Next Steps\n"
            f"Ultimately, mastering `{topic}` requires continuous iteration. If you want to explore more, feel free to start your journey today!"
        )
    elif template_type.lower() == "caption":
        body = (
            f"⚡ Let's talk about **{topic}**! ⚡\n\n"
            f"For anyone in the `{audience}` space, this is a game-changer. "
            f"We've been focusing on how to align our strategies in a `{tone}` way to drive real conversations.\n\n"
            f"What's your biggest challenge when it comes to this? Let us know below! 👇\n\n"
            f"#trends #{template_type.replace(' ', '')} #learning"
        )
    elif template_type.lower() == "ad copy":
        body = (
            f"### 🔥 Stop Scrolling! Let's talk about {topic}.\n\n"
            f"Are you tired of typical solutions that don't fit your target needs?\n\n"
            f"Introducing our latest solution designed specifically for **{audience}**! Written in a `{tone}` tone, we focus on delivering actual results.\n\n"
            f"✔ **High Performance**: Maximize your reach.\n"
            f"✔ **Saves Time**: Get ready-made configurations in seconds.\n"
            f"✔ **Designed for You**: Tailored formatting rules matching `{format_control}`.\n\n"
            f"👉 **Click the link below to get started today!** 🚀"
        )
    elif template_type.lower() == "email":
        body = (
            f"**Subject:** Quick question regarding {topic} for {audience}\n\n"
            f"Hi there,\n\n"
            f"I hope this message finds you well.\n\n"
            f"I'm reaching out because we've been helping professionals in the `{audience}` category master `{topic}`. "
            f"Given your focus, I thought you might find our approach interesting.\n\n"
            f"Here is a quick overview of what we do:\n"
            f"- Deliver messaging in a `{tone}` voice.\n"
            f"- Ensure concise formatting matching `{length}` specifications.\n"
            f"- Keep layouts organized in a `{format_control}` format.\n\n"
            f"Would you be open to a brief chat next Tuesday at 10 AM to discuss how this applies to your team?\n\n"
            f"Best regards,\n"
            f"Content Generation Lead"
        )
    elif template_type.lower() == "product description":
        body = (
            f"## The Ultimate {topic} Solution\n\n"
            f"Elevate your experience with our new product designed for `{audience}`. "
            f"Crafted with precision, this system brings a `{tone}` aesthetic to your daily workflow.\n\n"
            f"### Features & Highlights\n"
            f"- **Tailored Fit**: Optimized for high-frequency use.\n"
            f"- **Premium Styling**: Fits right into any dashboard.\n"
            f"- **Clear Architecture**: Built on clean, lightweight structures.\n\n"
            f"### Specifications\n"
            f"Ideal for anyone looking to simplify `{topic}`. Try it now and experience the difference!"
        )
    elif template_type.lower() == "linkedin post":
        body = (
            f"💡 **Why `{topic}` is shifting the paradigm for `{audience}`** 💡\n\n"
            f"I've spent the last few weeks observing trends around `{topic}`. Many leaders are trying to adapt, but many forget the importance of a `{tone}` approach.\n\n"
            f"Here are my top 3 rules for executing this effectively:\n"
            f"1️⃣ **Acknowledge the Audience**: Speak directly to their core needs.\n"
            f"2️⃣ **Choose Your Format**: Prefer a clean `{format_control}` layout for accessibility.\n"
            f"3️⃣ **Iterate Constantly**: Your first draft is just the starting point.\n\n"
            f"What are your thoughts on this? Let's discuss in the comments! 💬\n\n"
            f"#networking #professionalgrowth #leadership"
        )
    else:
        body = f"This is a generated text about **{topic}** for a `{audience}` audience with a `{tone}` tone and `{length}` length."

    # Adjusting body complexity based on prompt engineering versions to show improvement
    if version == "v1":
        # Raw plain text, no structure, very simple
        plain_body = body.replace("#", "").replace("**", "").replace("`", "").replace("✔", "-").replace("👉", "").replace("🚀", "")
        return f"Basic Draft for topic: {topic}\n\n{plain_body}\n\n(Generated using basic v1 prompt: no styling rules, plain paragraphs, simplified text)"
    
    elif version == "v2":
        # Add basic markdown headers but no tone adaptation
        return intro_version + body + "\n\n*(Note: formatted in markdown layout as requested in v2 prompt)*"
    
    elif version == "v3":
        # Persona injected
        return intro_version + body + f"\n\n*(Self-Correction/Reasoning Check: This text was written adopting a '{tone}' persona targeting '{audience}')*"
        
    else: # v4
        # Fully optimized professional draft
        return intro_version + body + (
            f"\n\n---\n"
            f"### ⚙️ Prompt Engineering Audit Log (V4 System Rules Check):\n"
            f"- [x] **Adhered to Tone:** Verified `{tone}` tone characteristics matches throughout.\n"
            f"- [x] **Length Checked:** Checked length conforms to `{length}` specifications.\n"
            f"- [x] **Audience Check:** Re-targeted terminology for `{audience}`.\n"
            f"- [x] **Format Standard:** Outputted in clean `{format_control}`."
        )

def generate_content(
    provider: str,
    api_key: str,
    template_type: str,
    topic: str,
    tone: str,
    length: str,
    audience: str,
    output_format: str,
    extra_info: str = "",
    version: str = "v4"
) -> dict:
    
    # Establish formats
    format_control = {
        "plain text": "plain paragraphs without formatting",
        "markdown": "markdown with titles, headers, bold text and italic highlights",
        "bullet points": "a bulleted list with highlights",
        "html": "raw HTML code with paragraphs and bold tags"
    }.get(output_format.lower(), "markdown")

    # Generate full prompt strings
    prompt_strings = {
        "v1": get_prompt_v1(template_type, topic),
        "v2": get_prompt_v2(template_type, topic, format_control),
        "v3": get_prompt_v3(template_type, topic, tone, audience, format_control),
        "v4": get_prompt_v4(template_type, topic, tone, audience, format_control, length, extra_info)
    }

    selected_prompt = prompt_strings.get(version, prompt_strings["v4"])

    # Use environment variables if api_key is not provided
    if provider == "gemini" and not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
        
    if provider == "openai" and not api_key:
        api_key = os.environ.get("OPENAI_API_KEY")

    # Fallback/Mock mode logic
    if provider == "mock" or (provider in ["gemini", "openai"] and not api_key):
        generated_text = generate_mock_content(template_type, topic, tone, audience, format_control, length, version)
        return {
            "content": generated_text,
            "prompt_used": selected_prompt,
            "provider": "mock",
            "version": version
        }

    try:
        if provider == "gemini":
            genai.configure(api_key=api_key)
            # Use the recommended current gemini model
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(selected_prompt)
            return {
                "content": response.text,
                "prompt_used": selected_prompt,
                "provider": "gemini",
                "version": version
            }
        
        elif provider == "openai":
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": selected_prompt}
                ]
            )
            return {
                "content": response.choices[0].message.content,
                "prompt_used": selected_prompt,
                "provider": "openai",
                "version": version
            }
            
        else:
            raise ValueError(f"Unknown provider: {provider}")
            
    except Exception as e:
        # Fallback to mock on actual API failure, returning failure indicator
        mock_text = generate_mock_content(template_type, topic, tone, audience, format_control, length, version)
        return {
            "content": f"⚠️ **Error running {provider} API: {str(e)}**\n\nFallback generated content:\n\n{mock_text}",
            "prompt_used": selected_prompt,
            "provider": "mock_fallback",
            "version": version
        }
