#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals
from ..base import Base
from ..exception import *
import shutil

from openpyxl import load_workbook
import os
import sys


class FileHandlerKeywords(Base):

	def create_folder(self, folder_name):
		folder_source = self._get_source(folder_name)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if exist:
			raise DirectoryExistException(str("Directory ") + os.path.normpath(folder_source) + str(" already exist!"))
		else:
			try:
				os.makedirs(folder_source)
			except Exception:
				raise AssertionError(str("Creating directory ") + os.path.normpath(folder_source) + str(" failed!"))

	def delete_folder(self, folder_name):
		folder_source = self._get_source(folder_name)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if not exist:
			raise DirectoryNotFoundException(str("Directory ") + os.path.normpath(folder_source) + str(" doesn't exist!"))
		else:
			try:
				shutil.rmtree(str(os.path.normpath(folder_source)), ignore_errors=True)
			except Exception:
				raise AssertionError(str("Deleting directory ") + os.path.normpath(folder_source) + str(" failed!"))

	def create_new_file(self, file_name):
		file_source = self._get_source(file_name)
		file_exist = os.path.isfile(os.path.normpath(file_source))
		dir_exist = os.path.isdir(os.path.normpath(os.path.dirname(file_source)))
		if file_exist:
			raise FileExistException(str("File ") + os.path.normpath(file_source) + str(" already exist!"))
		elif not dir_exist:
			raise DirectoryNotFoundException(str("Directory ") + os.path.normpath(os.path.dirname(file_source)) + str(" doesn't exist!"))
		else:
			try:
				file_new = open(str(os.path.normpath(file_source)), str('w'))
				file_new.close()
			except Exception:
				raise AssertionError(str("Creating file ") + os.path.normpath(file_source) + str(" failed!"))

	def delete_file(self, file_name):
		file_source = self._get_source(file_name)
		file_exist = os.path.isfile(os.path.normpath(file_source))
		if not file_exist:
			raise FileNotFoundException(str("File ") + os.path.normpath(file_source) + str(" doesn't exist!"))
		else:
			try:
				os.remove(file_source)
			except Exception as e:
				#print(e)
				raise AssertionError(str("Deleting file ") + os.path.normpath(file_source) + str(" failed!"))
