import shutil


def check_ffmpeg():

    if shutil.which("ffmpeg") is None:
        raise RuntimeError(
            "FFmpeg tidak ditemukan."
        )
