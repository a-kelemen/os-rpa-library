#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, generators, print_function, unicode_literals
import sys
import os
from functools import wraps
from robot.api import logger
#from robot.api.deco import keyword
#import osmodule
#from . import osmodule
#file_dir = os.path.dirname(__file__)
#sys.path.append(file_dir)
from robot.api import logger

from .osmodule.keywords.definition.data import DataKeywords
from .osmodule.keywords.definition.filehandler import FileHandlerKeywords
#from keywords.definition.basic import BasicKeyWords

def msg_logger(f):
	def wrap(*args, **kwargs):
		return_value, msg = f(*args, **kwargs)
		#print("Bye")
		if msg != "":
			logger.info(msg)
		return return_value
	return wrap


# class say_bye(object):
# 	def __init__(self, func):
# 		self._locals = {}
# 		self.func = func
#
# 	def __call__(self, *args, **kwargs):
# 		def tracer(frame, event, arg):
# 			if event == 'return':
# 				self._locals = frame.f_locals.copy()
#
# 		# tracer is activated on next call, return or exception
# 		sys.setprofile(tracer)
# 		try:
# 			# trace the function call
# 			res = self.func(*args, **kwargs)
# 		finally:
# 			# disable tracer and replace with old one
# 			sys.setprofile(None)
# 		return res
#
# 	def clear_locals(self):
# 		self._locals = {}
#
# 	@property
# 	def locals(self):
# 		return self._locals


def keyword(name=None):
	#TODO ebbe az kell, hogy lefuttassa a keywordot, es ha sikres, akkor kiir valamit hogy sikeres hogy legyen
	#valami haszna
	if callable(name):
		#logger.warn(str(name))
		logger.warn("csaxsa")
		return keyword()(name)

	def _method_wrapper(func):
		func.robot_name = name
		return func
	return _method_wrapper


class OsProcessLibrary(object):
	__version__ = '0.1.0'
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = __version__

	def __init__(self):
		self.data = DataKeywords()
		self.handler = FileHandlerKeywords()

	def testos(self):
		print("OsProcessLibraryTest")

	@keyword(name="Create Folder")
	def create_folder(self, folder):
		"""
		Creates the given ``folder`` or folder structure.
		:param folder: the path of the folder. Could be a folder name, a relative path or an absolute path.

		Keyword fails if the given folder already exists.

		Examples:
		| `Create Folder` | C://sample   | # Creates a folder named _sample_ to "C:/"         |
		| `Create Folder` | sample//a//b | # Creates a folder structure to the current folder |
		"""
		self.handler.create_folder(folder)

	@keyword(name="Delete Folder")
	def delete_folder(self, folder):
		"""
		Removes the given ``folder`` or folder structure.
		:param folder: the path of the folder. Could be a folder name, a relative path or an absolute path.

		Deletes the complete folder with the files.

		Fails if the given folder doesn't exist.

		Examples:
		| `Delete Folder` | C://sample   | # Removes the folder named _sample_ from "C:/"              |
		| `Delete Folder` | sample//a//b | # Removes the folder named _b_                              |
		| `Delete Folder` | sample       | # Removes the folder named _sample_ from the current folder |
		"""
		self.handler.delete_folder(folder)

	@keyword(name="Create New File")
	def create_new_file(self, file_name):
		"""
		Creates a new file.
		:param file_name: the source of the file. Could be a file name, a relative path or an absolute path.

		File path must be an existing path. This keyword does not create folders.

		Fails if the given file already exists.

		Examples:
		| `Create New File` | C://sample.txt | # Creates a file named _sample.txt_ to "C:/"              |
		| `Create New File` | sample.txt     | # Creates a file named _sample.txt_ to the current folder |
		"""
		self.handler.create_new_file(file_name)

	@keyword(name="Delete File")
	def delete_file(self, file_name):
		"""
		Removes a file.
		:param file_name: the source of the file. Could be a file name, a relative path or an absolute path.

		File path must be an existing path. This keyword does not remove folders.

		Fails if the given file doesn't exist.

		Examples:
		| `Delete File` | C://sample.txt | # Removes a file named _sample.txt_ from "C:/"              |
		| `Delete File` | sample.txt     | # Removes a file named _sample.txt_ from the current folder |
		"""
		self.handler.delete_file(file_name)

	@keyword(name="File Should Exist")
	def file_should_exist(self, file_name):
		"""
		Checks if the given file exists.
		:param file_name: the source of the file. Could be a filename, a relative path or an absolute path.

		Fails if the given file doesn't exist.

		Examples:
		| `File Should Exist` | ${CURDIR}//sample.xlsx         | # _sample.xlsx_ should exist in the test's folder |
		| `File Should Exist` | sample.xlsx                    | # _sample.xlsx_ should exist in the test's folder |
		| `File Should Exist` | C://Program Files//sample.xlsx | # _sample.xlsx_ should exist in the given folder  |
		| `File Should Exist` | ..//test//sample.xlsx          | # _sample.xlsx_ should exist in the given folder  |

		"""
		self.data.file_should_exist(file_name)

	@keyword(name="File Should Not Exist")
	def file_should_not_exist(self, file_name):
		"""
		Checks if the given file does not exist.
		:param file_name: the source of the file. Could be a filename, a relative path or an absolute path.

		Fails if the given file exist.

		Examples:
		| `File Should Not Exist` | ${CURDIR}//sample.xlsx         | # _sample.xlsx_ should not exist in the test's folder |
		| `File Should Not Exist` | sample.xlsx                    | # _sample.xlsx_ should not exist in the test's folder |
		| `File Should Not Exist` | C://Program Files//sample.xlsx | # _sample.xlsx_ should not exist in the given folder  |
		| `File Should Not Exist` | ..//test//sample.xlsx          | # _sample.xlsx_ should not exist in the given folder  |

		"""
		self.data.file_should_not_exist(file_name)

	@keyword(name="Folder Should Exist")
	def folder_should_exist(self, folder_name):
		"""
		Checks if the given folder exists.
		:param folder_name: the path of the folder. Could be a folder name, a relative path or an absolute path.

		Fails if the given folder doesn't exist.

		Examples:
		| `Folder Should Exist` | ${CURDIR}         | # Passes                                              |
		| `Folder Should Exist` | sample.xlsx       | # Fails, not a folder                                 |
		| `Folder Should Exist` | C://Program Files | # Passes if "C://Program Files" is an existing folder |
		| `Folder Should Exist` | test_folder       | # Passes if _test_folder_ is an existing folder       |
		"""
		self.data.folder_should_exist(folder_name)

	@keyword(name="Folder Should Not Exist")
	def folder_should_not_exist(self, folder_name):
		"""
		Checks if the given folder does not exist.
		:param folder_name: the path of the folder. Could be a folder name, a relative path or an absolute path.

		Fails if the given folder exists.

		Examples:
		| `Folder Should Not Exist` | ${CURDIR}         | # Fails                                              |
		| `Folder Should Not Exist` | sample.xlsx       | # Passes, not a folder                               |
		| `Folder Should Not Exist` | C://Program Files | # Fails if "C://Program Files" is an existing folder |
		| `Folder Should Not Exist` | test_folder       | # Passes if _test_folder_ is not existing folder     |

		"""
		self.data.folder_should_not_exist(folder_name)

	@keyword(name="List All Files")
	def list_all_files(self, folder_name="default_"):
		"""
		Returns a list with the files of the given folder.
		:param folder_name: the path of the folder. Could be a filename, a relative path or an absolute path.
		:param without parameter: default folder is the folder of the current test.

		Fails if the given folder doesn't exist.

		Examples:
		| ${file_list} | `List All Files` | ${CURDIR} | # _${file_list}_ will contain a list with filenames |
		"""
		return self.data.list_all_files(folder_name)

	@keyword(name="Get File Size")
	def get_file_size(self, file_name):
		"""
		Returns the size of the given file in kilobytes.
		:param file_name: the source of the file. Could be a filename, a relative path or an absolute path.

		Fails if the given file doesn't exist.

		Examples:
		| ${file_size} | `Get File Size` | file.txt | # returns the size of _file.txt_ |
		"""
		return self.data.get_file_size(file_name)

	@keyword(name="List Folders")
	def list_folders(self, folder_name="default_"):
		"""
		Returns a list with the folders of the given folder.
		:param folder_name: the path of the folder. Could be a folder name, a relative path or an absolute path.
		:param without parameter: default folder is the folder of the current test.

		Fails if the given folder doesn't exist.

		Examples:
		| ${folder_list} | `List Folders` | ${CURDIR} | # _${file_list}_ will contain a list of subfolders |
		"""
		return self.data.list_folders(folder_name)
