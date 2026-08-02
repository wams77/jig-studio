from app.bible import BibleService
from app.media.media_service import MediaService


def main():

    print("=" * 60)
    print("JIG Studio V2")
    print("=" * 60)

    bible = BibleService()

    verse = bible.random()

    print()
    print("AYAT HARI INI")
    print("--------------------------")
    print(verse.reference)
    print()
    print(verse.text)
    print()

    service = MediaService()

    files = service.download_best_videos(
        keyword="cross",
        limit=5,
    )

    print()
    print("VIDEO BERHASIL DIDOWNLOAD")
    print("--------------------------")

    for file in files:
        print(file)


if __name__ == "__main__":
    main()
