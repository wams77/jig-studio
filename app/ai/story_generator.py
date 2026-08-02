from app.ai.groq_client import GroqClient
from app.ai.prompt_builder import build_prompt


class StoryGenerator:

    def __init__(self):

        self.client = GroqClient()

    def generate(self, verse):

        prompt = build_prompt(

            verse.reference,

            verse.text,

        )

        return self.client.generate(prompt)
