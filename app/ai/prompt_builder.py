def build_prompt(reference: str, verse: str) -> str:

    return f"""
Anda adalah sutradara video Kristen profesional.

Berdasarkan ayat berikut:

{reference}

"{verse}"

Buat jawaban JSON valid tanpa markdown dengan format:

{{
  "title": "...",
  "hook": "...",
  "narration": "...",
  "keywords":[
    "...",
    "...",
    "...",
    "...",
    "..."
  ]
}}

Rules:

- narration maksimal 90 kata
- hook maksimal 15 kata
- keywords harus dalam Bahasa Inggris
- keywords berupa visual yang bisa dicari di Pexels
- jangan gunakan kata bible
- jangan gunakan kata jesus
- jangan gunakan kata christian
"""
