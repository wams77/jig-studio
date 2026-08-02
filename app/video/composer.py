from pathlib import Path
import subprocess

from app.video.ffmpeg import check_ffmpeg


class VideoComposer:

    def compose(
        self,
        videos: list[Path],
        output: str = "output/final.mp4",
    ):

        check_ffmpeg()

        Path("temp").mkdir(exist_ok=True)

        concat = Path("temp/concat.txt")

        with open(concat, "w", encoding="utf-8") as f:

            for video in videos:

                f.write(f"file '{video.resolve()}'\n")

        Path("output").mkdir(exist_ok=True)

        subprocess.run(

            [

                "ffmpeg",

                "-y",

                "-f",

                "concat",

                "-safe",

                "0",

                "-i",

                str(concat),

                "-c",

                "copy",

                output,

            ],

            check=True,

        )

        return output
