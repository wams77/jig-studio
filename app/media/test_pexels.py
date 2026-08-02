from app.media.pexels_client import PexelsClient

client = PexelsClient()

videos = client.search("cross")

print(f"Ditemukan {len(videos)} video")

for video in videos:
    print(video["id"])
