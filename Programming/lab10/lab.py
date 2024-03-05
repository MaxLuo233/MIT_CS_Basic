import sys
import doctest
from http009 import http_response

sys.setrecursionlimit(10000)

# NO ADDITIONAL IMPORTS!

CHUNK_SIZE = 8192


def download_file(loc, cache=None):
    """
    Yield the raw data from the given URL, in segments of CHUNK_SIZE bytes.

    If the request results in a redirect, yield bytes from the endpoint of the
    redirect.

    If the given URL represents a manifest, yield bytes from the parts
    represented therein, in the order they are specified.

    Raises a RuntimeError if the URL can't be reached, or in the case of a 500
    status code.  Raises a FileNotFoundError in the case of a 404 status code.
    """

    # Try implementing cache as dictionary mapping "url" -> file data

    # Hint: consider making another function to handle manifests
    # Hint: b''.decode("utf-8") decodes a bytestring to a python string
    #       use this when deciding what URLs in the manifest to download again
    raise NotImplementedError

def files_from_sequence(stream):
    """
    Yield the files from the sequence in the order they are specified.

    stream: the return value (a generator) of a download_file
                        call that represents a file sequence
    """

    # Use next(stream) to yield the more data.
    raise NotImplementedError


if __name__ == '__main__':
    """
    Remember you can use python3 gui.py URL_NAME to test your images!
    """
    pass
