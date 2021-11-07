#
# This file is part of Git helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Git helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Repository operator."""

import sys
from typing import List, Union

import dulwich.porcelain as dulwich


def _decode_byte_string(byte_string: bytes):
    """Decode string by O.S encoding system."""
    return byte_string.decode(sys.getfilesystemencoding())


def _stage_files(repository_path: str, files_to_stage: List[Union[str, bytes]]):
    """Stage files."""

    # preparing file paths to stage (bytes to str)
    files_to_stage = [
        _decode_byte_string(f) if type(f) == bytes else f for f in files_to_stage
    ]

    # staging
    if files_to_stage:
        dulwich.add(repository_path, paths=files_to_stage)


class RepositoryOperator:

    @staticmethod
    def commit(repository_path: str, message: str, **kwargs):
        pass


class AllStagedOperator(RepositoryOperator):

    @staticmethod
    def commit(repository_path: str, message: str, **kwargs):
        # commiting the files (added, deleted and modified)
        return _decode_byte_string(dulwich.commit(repository_path, message, **kwargs))


class AllFilesOperator(RepositoryOperator):

    @staticmethod
    def commit(repository_path: str, message: str, **kwargs):
        # getting the staged files (added, deleted and modified)
        repository_status = dulwich.status(repository_path)

        # adding unstaged and untracked files to stage
        _stage_files(repository_path, repository_status.unstaged + repository_status.untracked)

        # commiting the files
        return _decode_byte_string(dulwich.commit(repository_path, message, **kwargs))


class AllRepositoryOperator(RepositoryOperator):

    @staticmethod
    def commit(repository_path: str, message: str, **kwargs):
        # getting the staged files (added, deleted and modified)
        repository_status = dulwich.status(repository_path)

        # adding unstaged files to stage
        _stage_files(repository_path, repository_status.unstaged)

        # commiting the files
        return _decode_byte_string(dulwich.commit(repository_path, message, **kwargs))


__all__ = (
    "AllStagedOperator",
    "AllFilesOperator",
    "AllRepositoryOperator"
)
