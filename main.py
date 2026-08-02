from app.media.media_service import MediaService


def main():

    print("=" * 60)
    print("JIG Studio V2")
    print("=" * 60)

    keyword = "cross"

    service = MediaService()

    files = service.download_best_videos(
        keyword=keyword,
        limit=5,
    )

    print()
    print("Download selesai\n")

    for file in files:
        print(file)


if __name__ == "__main__":
    main()
