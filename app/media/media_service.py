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
    ):

        videos = self.client.search(
            query=keyword,
            per_page=limit,
        )

        downloaded = []

        for video in videos:

            best = self.client.get_best_quality(video)

            if not best:
                continue

            filename = f"{video['id']}.mp4"

            path = self.downloader.download(
                best["link"],
                filename,
            )

            downloaded.append(path)

        return downloaded
