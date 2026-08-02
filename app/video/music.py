from pathlib import Path


class MusicSelector:

    def random(self):

        folder = Path("assets/music")

        music = list(folder.glob("*.mp3"))

        if not music:

            return None

        return music[0]
