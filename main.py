from pathlib import Path
import os

NOTE = (
    "I counted the cheese. Six slices yesterday, four today. "
    "I am not angry \u2014 just disappointed. And cold."
)


def run():
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(NOTE + "\n", encoding="utf-8")


run()
