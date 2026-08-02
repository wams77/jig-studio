from app.ai import StoryGenerator
from app.bible import BibleService
from app.media.media_service import MediaService


def main():

    print("=" * 60)
    print("JIG Studio V2")
    print("=" * 60)

    verse = BibleService().random()

    print()
    print(verse.reference)
    print()

    print(verse.text)
    print()

    story = StoryGenerator().generate(verse)

    print("TITLE")
    print(story["title"])
    print()

    print("HOOK")
    print(story["hook"])
    print()

    print("KEYWORDS")

    for keyword in story["keywords"]:
        print("-", keyword)

    print()

    media = MediaService()

    downloaded = []

    for keyword in story["keywords"]:

        downloaded.extend(

            media.download_best_videos(

                keyword,

                limit=1,

            )

        )

    print()

    print("DOWNLOAD")

    for file in downloaded:

        print(file)


if __name__ == "__main__":
    main()
