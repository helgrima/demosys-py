import functools
import os
from demosys.core import finders
from demosys.conf import settings
from demosys.core.exceptions import ImproperlyConfigured
from demosys.utils.module_loading import import_string

TEXTURE_DIR = 'textures'


class FileSystemFinder(finders.FileSystemFinder):
    """Find textures in ``TEXTURE_DIRS``"""
    def __init__(self):
        if not hasattr(settings, 'TEXTURE_DIRS'):
            raise ImproperlyConfigured(
                "Settings module don't define TEXTURE_DIRS."
                "This is required when using a FileSystemFinder."
            )
        super().__init__(settings.TEXTURE_DIRS)

    # TODO: Use values from settings to filter texture files
    # def find(self, path):
    #     pass


class EffectDirectoriesFinder(finders.FileSystemFinder):
    """Finds textures in the registered effects"""
    def __init__(self):
        from demosys.effects.registry import effects
        dirs = list(effects.get_dirs())
        super().__init__(dirs)

    # TODO: Use values from settings to filter texture files
    def find(self, path):
        return self._find(os.path.join(TEXTURE_DIR, path))


def get_finders():
    for finder in settings.TEXTURE_FINDERS:
        yield get_finder(finder)


@functools.lru_cache(maxsize=None)
def get_finder(import_path):
    """
    Get a finder class from an import path.
    Raises ``demosys.core.exceptions.ImproperlyConfigured`` if the finder is not found.
    This function uses an lru cache.

    :param import_path: string representing an import path
    :return: An instance of the finder
    """
    Finder = import_string(import_path)
    if not issubclass(Finder, finders.FileSystemFinder):
        raise ImproperlyConfigured('Finder {} is not a subclass of core.finders.FileSystemFinder'.format(import_path))
    return Finder()
