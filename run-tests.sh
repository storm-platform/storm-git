#!/usr/bin/env bash
#
# This file is part of Git helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Git helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle storm_git examples tests setup.py && \
isort storm_git examples tests setup.py --check-only --diff && \
check-manifest --ignore ".travis.yml,.drone.yml,.readthedocs.yml" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest
