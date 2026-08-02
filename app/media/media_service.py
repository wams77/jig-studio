from pathlib import Path

from app.media.downloader import Downloader
from app.media.pexels_client import PexelsClient


class MediaService:

    def __init__(self):

        self.client = PexelsClient()

        self.downloader = Downloader()

    def download_best_videos(
        self,
        keyword: str,
        limit: int = 5,
    ) -> list[Path]:

        downloaded: list[Path] = []

        videos = self.client.search(
            query=keyword,
            per_page=limit,
        )

        for video in videos:

            best = self.client.get_best_quality(video)

            if best is None:
                continue

            url = best["link"]

            filename = f"{video['id']}.mp4"

            path = self.downloader.download(
                url=url,
                filename=filename,
            )

            downloaded.append(path)

        self.client.close()

        return downloaded
