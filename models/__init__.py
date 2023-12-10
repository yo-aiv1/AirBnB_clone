#!/usr/bin/python3
"""Module and packages :  models
Import modules and packages."""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
