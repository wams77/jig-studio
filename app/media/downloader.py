from pathlib import Path

import httpx


class Downloader:

    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def download(self, url: str, filename: str) -> Path:

        destination = self.download_dir / filename

        with httpx.stream("GET", url, timeout=120) as response:
            response.raise_for_status()

            with open(destination, "wb") as file:
                for chunk in response.iter_bytes():
                    file.write(chunk)

        return destinationfrom pathlib import Path

import httpx


class Downloader:

    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def download(self, url: str, filename: str) -> Path:

        destination = self.download_dir / filename

        with httpx.stream("GET", url, timeout=120) as response:
            response.raise_for_status()

            with open(destination, "wb") as file:
                for chunk in response.iter_bytes():
                    file.write(chunk)

        return destination
