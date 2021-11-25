#
# This file is part of Git helper library for Storm platform.
# Copyright (C) 2021 INPE.
#
# Git helper library for Storm platform is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Git helper library for Storm platform."""

import os

import dulwich.porcelain as dulwich
import dulwich.errors as dulwich_errors

from .operator import AllStagedOperator, AllFilesOperator, AllRepositoryOperator

SUPPORTED_OPERATION_MODE = {
    "files": AllFilesOperator,
    "staged": AllStagedOperator,
    "unstaged": AllRepositoryOperator,
}


class StormGit:
    def __init__(self, repository_path: str, operation_mode):
        repository_operator = SUPPORTED_OPERATION_MODE.get(operation_mode)
        if not repository_operator:
            raise NotImplementedError(
                f"Repository Operation mode `{operation_mode}` is not implemented."
            )

        self._repository_path = repository_path
        self._repository_operator = repository_operator

    def commit(self, message: str, **kwargs):
        return self._repository_operator.commit(
            self._repository_path, message, **kwargs
        )

    @classmethod
    def init(cls, repository_path: str, operation_mode: str = "files", **kwargs):

        if not os.path.exists(repository_path):
            raise NotADirectoryError("Invalid directory")

        # creating the repository
        git_file_reference = os.path.join(repository_path, ".git")

        if not os.path.exists(git_file_reference):
            dulwich.init(repository_path, **kwargs)

        # building self-object for the new repository
        return cls(repository_path, operation_mode)

    @staticmethod
    def is_repository(repository_path: str):

        try:
            repository_status = dulwich.status(repository_path)
        except dulwich_errors.NotGitRepository:
            repository_status = None

        return repository_status is not None

    def __repr__(self):
        return f"[StormGit] {self._repository_path}"


__all__ = "StormGit"
