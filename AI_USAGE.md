# AI Usage & Prompt Engineering Notes

As part of the Assignment 2: AI Content Generation Studio, this document outlines the prompt strategies and AI integration techniques used.

## Prompt Improvement Iterations

In order to ensure that outputs are highly organized and editable, we iterated our system prompts significantly. This evolution can be viewed and tested live in the **Prompt Lab** section of the application.

### Version 1: The Basic Instruction
**Prompt:** `Write a [template_type] about [topic].`
- **Result**: Output is generic, lacks formatting, and often misses the target audience's tone completely.

### Version 2: Structural Constraints
**Prompt:** `Write a [template_type] about: [topic]. Make sure to format it as [format_control].`
- **Result**: The output is better structured (e.g., using Markdown) but still reads very blandly. It doesn't adapt to different industries or audiences.

### Version 3: Persona and Audience Focus
**Prompt:** `You are a helpful content writer. Write a [template_type] about: [topic]. Target Audience: [audience]. Tone of voice: [tone].`
- **Result**: Significant improvement in relevance. The language changes based on the audience, and the tone controls work nicely. However, the model sometimes hallucinates placeholders (like `[Insert Company Name Here]`) and misses structural goals.

### Version 4: The Production System Prompt (Final)
The final engineered prompt combines persona, strict formatting rules, length controls, and negative constraints (to prevent placeholders).

**Prompt Structure:**
```text
You are an elite, results-driven AI content architect specializing in copywriting.
Your task is to write a high-converting, professional-grade [template_type] about the topic specified below.

--- AUDIENCE & VOICE CONTROL ---
- Target Audience: [audience] (Write specifically using terminology and themes that resonate with this group).
- Tone: [tone] (Strictly adopt this writing style).
- Length: [length_desc]

--- FORMATTING RULES ---
- Output Format: [format_control]
- Do NOT use generic placeholder text (like '[Your Name]', '[Insert Link]', or '[Company]'). Provide realistic context instead.
- Keep the output clean, starting directly with the title/headline and ending with a final call to action or summary.

--- TOPIC ---
Topic / Subject details:
[topic]

--- ADDITIONAL USER CONSTRAINTS ---
[extra_info]
```

- **Result**: Highly accurate, fully formatted, editable, and strictly adhering to length and audience parameters. It requires zero cleanup and is ready for publishing.

## Tools and APIs Used
- **Google Gemini API (`google-generativeai`)**: Used for the primary generation endpoint (`gemini-1.5-flash`). It offers incredible speed and handles structural constraints very well.
- **OpenAI API (`openai`)**: Fallback integration (`gpt-4o-mini`) using standard chat completion structures.
- **Mock Fallback System**: We engineered a custom simulated fallback generator using Python that constructs rich text based on the parameters if an API key isn't present, allowing for immediate testing.
