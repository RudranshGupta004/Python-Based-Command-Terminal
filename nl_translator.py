from config import client

def nl_to_command(nl_query: str) -> str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a command translator. "
                        "Convert natural language into a **single raw Windows CMD command only**. "
                        "Do not include explanations, Markdown, code fences, or PowerShell alternatives. "
                        "Output just the command that should be executed."
                    ),
                },
                {"role": "user", "content": nl_query},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[nl] error: {str(e)}"
