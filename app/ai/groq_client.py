import json

import httpx

from app.core.config import settings


class GroqClient:

    BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

    MODEL = "llama-3.3-70b-versatile"

    def generate(self, prompt: str) -> dict:

        response = httpx.post(

            self.BASE_URL,

            headers={

                "Authorization": f"Bearer {settings.GROQ_API_KEY}",

                "Content-Type": "application/json",

            },

            json={

                "model": self.MODEL,

                "messages": [

                    {

                        "role": "user",

                        "content": prompt

                    }

                ],

                "temperature": 0.8,

            },

            timeout=120,

        )

        response.raise_for_status()

        text = response.json()["choices"][0]["message"]["content"]

        return json.loads(text)
