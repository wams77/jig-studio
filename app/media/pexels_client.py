from typing import Any

import httpx

from app.core.config import settings


class PexelsClient:
    """
    Client untuk Pexels Video API.
    """

    BASE_URL = "https://api.pexels.com/videos/search"

    def __init__(self):
        if not settings.PEXELS_API_KEY:
            raise RuntimeError("PEXELS_API_KEY belum diatur.")

        self.client = httpx.Client(
            headers={
                "Authorization": settings.PEXELS_API_KEY
            },
            timeout=60,
        )

    def search(
        self,
        query: str,
        per_page: int = 10,
        orientation: str = "portrait",
    ) -> list[dict[str, Any]]:

        response = self.client.get(
            self.BASE_URL,
            params={
                "query": query,
                "per_page": per_page,
                "orientation": orientation,
            },
        )

        response.raise_for_status()

        return response.json().get("videos", [])

    @staticmethod
    def get_best_quality(video: dict) -> dict | None:

        files = video.get("video_files", [])

        if not files:
            return None

        mp4_files = [
            file for file in files
            if file.get("file_type") == "video/mp4"
        ]

        if not mp4_files:
            return None

        return max(
            mp4_files,
            key=lambda item: (
                item.get("width", 0),
                item.get("height", 0),
            ),
        )

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
