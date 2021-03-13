# itils

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python CLI for transforming images.

Powered by [plac](https://github.com/ialbert/plac) (CLI), [Wand](https://github.com/emcconville/wand) (images), and [halo](https://github.com/ManrajGrover/halo) (spinners).

## Usage

### Interactive mode

```text
itils -i
```

Run `quit` to close `itils`.

### `gslide` subcommand

<!-- poetry run itils gslide -h | pbcopy -->

```text
usage: itils gslide [-h] [-r PCT] input_img

Resize an image to be smaller than 25 megapixels for Google Slides.
The image can be resized using an explicit percentage as well.

positional arguments:
  input_img             The path to the image to be transformed.

optional arguments:
  -h, --help            show this help message and exit
  -r PCT, --resize PCT  The (explicit) percentage value (e.g., 70) to scale
                        both width and height. Values less than 100 reduce the
                        image size.
```

## Development

1. `poetry install`
2. `poetry shell`

## Notes

- `convert image.png -resize 70% smaller_image.png` ([documentation](http://www.imagemagick.org/script/convert.php)).
- ["Improve Windows Support"](https://github.com/manrajgrover/halo/issues/5) (open) issue (halo).
