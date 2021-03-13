from enum import Enum

INPUT_HELP: str = "The path to the image to be transformed."
RESIZE_HELP: str = (
    "The (explicit) percentage value (e.g., 70) to scale both width and height. "
    "Values less than 100 reduce the image size."
)

# 25 megapixels
THRESHOLD: int = 25_000_000


class Log(Enum):
    READ = "Reading"
    RESIZE = "Resizing"
    SAVE = "Saving"
