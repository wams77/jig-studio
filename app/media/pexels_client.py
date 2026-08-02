from typing import Any

import httpx

from app.core.config import settings


class PexelsClient:
    """
    Client untuk berkomunikasi dengan Pexels Video API.
    """

    BASE_URL = "https://api.pexels.com/videos/search"

    def __init__(self):
        if not settings.PEXELS_API_KEY:
            raise ValueError("PEXELS_API_KEY belum diatur.")

        self.client = httpx.Client(
            headers={
                "Authorization": settings.PEXELS_API_KEY
            },
            timeout=30,
        )

    def search(
        self,
        query: str,
        per_page: int = 10,
        orientation: str = "portrait",
    ) -> list[dict[str, Any]]:
        """
        Mencari video berdasarkan keyword.
        """

        response = self.client.get(
            self.BASE_URL,
            params={
                "query": query,
                "per_page": per_page,
                "orientation": orientation,
            },
        )

        response.raise_for_status()

        data = response.json()

        return data.get("videos", [])

    @staticmethod
    def get_best_quality(video: dict) -> dict | None:
        """
        Memilih video dengan resolusi terbesar.
        """

        files = video.get("video_files", [])

        if not files:
            return None

        return max(
            files,
            key=lambda f: (
                f.get("width", 0),
                f.get("height", 0),
            ),
        )

    def close(self):
        self.client.close()
