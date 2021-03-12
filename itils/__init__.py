import sys

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
__description__ = importlib_metadata.metadata(__name__)["Summary"]
