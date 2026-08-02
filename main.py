from app.media.pexels_client import PexelsClient


def main():

    client = PexelsClient()

    print("=" * 50)
    print("JIG Studio")
    print("=" * 50)

    keyword = "cross"

    print(f"Mencari video: {keyword}")

    videos = client.search(keyword)

    print(f"Ditemukan {len(videos)} video\n")

    for index, video in enumerate(videos, start=1):

        best = client.get_best_quality(video)

        if not best:
            continue

        print(f"[{index}]")
        print(f"ID        : {video['id']}")
        print(f"Duration  : {video['duration']} detik")
        print(f"Resolution: {best['width']}x{best['height']}")
        print(f"URL       : {best['link']}")
        print("-" * 50)

    client.close()


if __name__ == "__main__":
    main()from app.media.pexels_client import PexelsClient


def main():

    client = PexelsClient()

    print("=" * 50)
    print("JIG Studio")
    print("=" * 50)

    keyword = "cross"

    print(f"Mencari video: {keyword}")

    videos = client.search(keyword)

    print(f"Ditemukan {len(videos)} video\n")

    for index, video in enumerate(videos, start=1):

        best = client.get_best_quality(video)

        if not best:
            continue

        print(f"[{index}]")
        print(f"ID        : {video['id']}")
        print(f"Duration  : {video['duration']} detik")
        print(f"Resolution: {best['width']}x{best['height']}")
        print(f"URL       : {best['link']}")
        print("-" * 50)

    client.close()


if __name__ == "__main__":
    main()
