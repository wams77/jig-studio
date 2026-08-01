from pathlib import Path

# Root project
ROOT_DIR = Path(__file__).resolve().parents[2]

APP_DIR = ROOT_DIR / "app"

ASSETS_DIR = ROOT_DIR / "assets"

DATABASE_DIR = ROOT_DIR / "database"

LOGS_DIR = ROOT_DIR / "logs"

OUTPUT_DIR = ROOT_DIR / "output"

DOWNLOAD_DIR = ROOT_DIR / "downloads"

CACHE_DIR = ROOT_DIR / "cache"

TEMP_DIR = ROOT_DIR / "temp"

DOCS_DIR = ROOT_DIR / "docs"

TESTS_DIR = ROOT_DIR / "tests"

# Assets

FONT_DIR = ASSETS_DIR / "fonts"

MUSIC_DIR = ASSETS_DIR / "music"

LOGO_DIR = ASSETS_DIR / "logos"

THUMBNAIL_DIR = ASSETS_DIR / "thumbnails"

# Database

DATABASE_FILE = DATABASE_DIR / "jig.db"
