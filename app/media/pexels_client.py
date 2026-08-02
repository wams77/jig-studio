from typing import Any

import httpx

from app.core.config import settings


class PexelsClient:
    BASE_URL = "https://api.pexels.com/videos/search"

    def __init__(self):
        self.headers = {
            "Authorization": settings.PEXELS_API_KEY
        }

    def search(
        self,
        query: str,
        per_page: int = 5,
        orientation: str = "portrait",
    ) -> list[dict[str, Any]]:

        params = {
            "query": query,
            "per_page": per_page,
            "orientation": orientation,
        }

        response = httpx.get(
            self.BASE_URL,
            headers=self.headers,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("videos", [])
