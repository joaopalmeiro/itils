from pathlib import Path

import plac
from wand.image import Image

from . import __version__


@plac.pos("input_img", help="The path to the image to be transformed", type=Path)
def main(input_img):
    pass


# The following entry point definition is for the console_scripts
# keyword option (setuptools) or [tool.poetry.scripts] (Poetry).
# The entry point for console_scripts has to be a function that
# takes zero arguments.
# Source:
# - https://github.com/ialbert/plac/issues/31#issuecomment-572239360
# - https://github.com/caltechlibrary/handprint
def console_scripts_main():
    # version: https://github.com/ialbert/plac/blob/master/plac_core.py#L411
    plac.call(main, version=__version__)


# with Image(filename="test.png") as img:
#     print("Original size:", img.size)

#     # -resize X% (70%, for example)

#     # Option #1:
#     # scaler = 0.7
#     # img.resize(int(img.width * scaler), int(img.height * scaler))

#     # Option #2:
#     img.transform(resize="70%")

#     print("New size:", img.size)

#     img.save(filename="test_output.png")
