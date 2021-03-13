from pathlib import Path

import plac
from halo import Halo
from wand.image import Image

from . import __description__, __version__
from .constants import INPUT_HELP, RESIZE_HELP, THRESHOLD, Log


def generate_size_message(img: Image, prefix: str) -> str:
    return f"{prefix} size: {img.size} • {img.size[0] * img.size[1]:,} megapixels\n"


# Based on: https://plac.readthedocs.io/en/latest/#implementing-subcommands
class ItilsInterface(object):
    commands = ["gslide", "quit"]

    def __init__(self):
        self.__doc__ = f"{__description__} ({__version__})\n"

    @plac.pos("input_img", help=INPUT_HELP, type=Path)
    @plac.opt("resize", help=RESIZE_HELP, type=int, metavar="PCT")
    def gslide(self, input_img, resize=None):
        """
        Resize an image to be smaller than 25 megapixels for Google Slides.
        The image can be resized using an explicit percentage as well.
        """
        spinner = Halo(text=Log.READ.value, spinner="arc")

        spinner.start()
        with Image(filename=input_img) as img:
            spinner.succeed()
            print(generate_size_message(img, "Original"))

            spinner.start(Log.RESIZE.value)
            if resize is None:
                # Resize `img` to have the specified area in pixels.
                # Aspect ratio is preserved.
                img.transform(resize=f"{THRESHOLD}@")
            else:
                # -resize X% (70%, for example)

                # Option #1:
                # scaler = 0.7
                # img.resize(int(img.width * scaler), int(img.height * scaler))

                # Option #2:
                img.transform(resize=f"{resize}%")

            spinner.succeed()
            print(generate_size_message(img, "New"))

            spinner.start(Log.SAVE.value)
            img.save(filename=f"{input_img.stem}_output.png")
            spinner.succeed()
            print(f"Filename: {input_img.stem}_output.png\n")

            print("All done! ✨")

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

    # plac.Interpreter(plac.call(ItilsInterface, version=__version__)).interact()
    plac.Interpreter.call(ItilsInterface, prompt="itils> ")
