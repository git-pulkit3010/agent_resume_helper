# utils.py

import textwrap

MAX_TOKENS = 3000  # Approximate safe max token count for DeepSeek

def clean_text(text: str) -> str:
    # Remove excessive newlines and trim
    lines = [line.strip() for line in text.splitlines()]
    return '\n'.join([line for line in lines if line])

def truncate_text(text: str, max_chars: int = 10000) -> str:
    """
    Truncate text safely to avoid sending huge payloads to DeepSeek.
    You can adjust this based on max token limits.
    """
    return textwrap.shorten(text, width=max_chars, placeholder="\n...[truncated]")

def chunk_text(text: str, max_chunk_size: int = 3000) -> list[str]:
    """
    Optional future usage: split resume into logical chunks (by paragraphs).
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk_size:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
