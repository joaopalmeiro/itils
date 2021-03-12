from pathlib import Path

import plac
from wand.image import Image

from . import __description__, __version__
from .constants import INPUT_HELP, RESIZE_HELP


# Based on: https://plac.readthedocs.io/en/latest/#implementing-subcommands
class ItilsInterface(object):
    commands = ["resize4gslides", "quit"]

    def __init__(self):
        self.__doc__ = f"{__description__}\n"

    @plac.pos("input_img", help=INPUT_HELP, type=Path)
    @plac.pos("resize", help=RESIZE_HELP, type=int)
    def resize4gslides(self, input_img, resize):
        """Resize an image to be smaller than 25 megapixels for Google Slides."""
        with Image(filename=input_img) as img:
            print("Original size:", img.size)

            # -resize X% (70%, for example)

            # Option #1:
            # scaler = 0.7
            # img.resize(int(img.width * scaler), int(img.height * scaler))

            # Option #2:
            img.transform(resize=f"{resize}%")
            print("New size:", img.size)

            img.save(filename=f"{input_img.stem}_output.png")

    def quit(self):
        raise plac.Interpreter.Exit


# @plac.pos("input_img", help="The path to the image to be transformed", type=Path)
# def main(input_img):
#     pass


# The following entry point definition is for the console_scripts
# keyword option (setuptools) or [tool.poetry.scripts] (Poetry).
# The entry point for console_scripts has to be a function that
# takes zero arguments.
# Source:
# - https://github.com/ialbert/plac/issues/31#issuecomment-572239360
# - https://github.com/caltechlibrary/handprint
def console_scripts_main():
    # version: https://github.com/ialbert/plac/blob/master/plac_core.py#L411
    # plac.call(main, version=__version__)
    plac.Interpreter.call(
        ItilsInterface,
        prompt="itils> ",
    )
