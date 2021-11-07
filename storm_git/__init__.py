#
# This file is part of Git helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Git helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Git helper library for Storm platform."""

from .git import StormGit

from .version import __version__

__all__ = (
    "StormGit",

    "__version__",
)
