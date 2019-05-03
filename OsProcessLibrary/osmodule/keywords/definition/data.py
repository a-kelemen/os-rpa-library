#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals
import os
from ..base import Base
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from ..exception import *
import math


class DataKeywords(Base):

	def file_should_exist(self, file_name):

		file_source = self._get_source(file_name)
		#print("file_name:")
		#print(file_name)
		#print("file_source: ")
		#print(file_source)
		exist = os.path.isfile(os.path.normpath(file_source))
		#print("file exist: " + str(exist))
		if not exist:
			raise FileNotFoundException(str("File does not exist: ") + os.path.normpath(file_source))
			#raise AssertionError("File does not exist: ")

	def file_should_not_exist(self, file_name):
		file_source = self._get_source(file_name)
		exist = os.path.isfile(os.path.normpath(file_source))
		if exist:
			raise FileExistException(str("File does exist: ") + os.path.normpath(file_source))

	def folder_should_exist(self, folder_name):
		folder_source = self._get_source(folder_name)
		#print("folder_source: ")
		#print(folder_source)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if not exist:
			raise DirectoryNotFoundException(str("Folder does not exist: ") + os.path.normpath(folder_source))
		pass

	def folder_should_not_exist(self, folder_name):
		folder_source = self._get_source(folder_name)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if exist:
			raise DirectoryExistException(str("Folder does exist: ") + os.path.normpath(folder_source))

	def list_all_files(self, folder_name="default_"):
		folder_source = self._get_source(folder_name)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if exist:
			all_files = os.listdir(folder_source)
			files = [_ for _ in all_files if os.path.isfile(os.path.join(folder_source, _))]
			return files
		else:
			raise DirectoryNotFoundException(str("Folder does not exist: ") + os.path.normpath(folder_source))

	def get_file_size(self, file_name):
		file_source = self._get_source(file_name)
		exist = os.path.isfile(os.path.normpath(file_source))
		if exist:
			file_size = float(os.path.getsize(file_source))
			size_kb = math.ceil(file_size / 1024.0)
			return int(size_kb)
		else:
			raise FileNotFoundException(str("File does not exist: ") + os.path.normpath(file_source))
			#raise AssertionError("File does not exist: ")

	def list_folders(self, folder_name="default_"):
		folder_source = self._get_source(folder_name)
		exist = os.path.isdir(os.path.normpath(folder_source))
		if exist:
			all_files = os.listdir(folder_source)
			folders = [_ for _ in all_files if os.path.isdir(os.path.join(folder_source, _))]
			return folders
		else:
			raise DirectoryNotFoundException(str("Folder does not exist: ") + os.path.normpath(folder_source))
			#raise DirectoryNotFoundException("Folder does not exist: " )
