#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals

import unittest
import os
import shutil
from OsProcessLibrary import OsProcessLibrary
from OsProcessLibrary.osmodule.keywords.exception import *


class TestDataKeywords(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestDataKeywords, self).__init__(*args, **kwargs)
		self.osLib = OsProcessLibrary()

	@classmethod
	def setUpClass(cls):
		test_dir = os.path.dirname(__file__)
		test_file = os.path.join(test_dir, 'test_files', 'file.txt')
		new_file = os.path.join(test_dir, 'file1.txt')
		shutil.copyfile(test_file, new_file)

	def test_file_should_exist_existing_filename(self):
		"""File Should Exist"""
		self.osLib.file_should_exist("file1.txt")

	def test_file_should_exist_existing_filename_2(self):
		"""File Should Exist"""
		self.osLib.file_should_exist("\\file1.txt")

	def test_file_should_exist_existing_filename_backslash(self):
		"""File Should Exist"""
		self.osLib.file_should_exist("\\test_files\\file.txt")

	def test_file_should_exist_existing_filename_slash(self):
		"""File Should Exist"""
		self.osLib.file_should_exist("/test_files/file.txt")

	def test_file_should_exist_non_existing(self):
		"""File Should Exist"""
		with self.assertRaises(FileNotFoundException):
			self.osLib.file_should_exist("test_files/no_file.txt")

	def test_file_should_exist_existing_fullpath(self):
		"""File Should Exist"""
		this_path = os.path.abspath(__file__)
		self.osLib.file_should_exist(this_path)

	def test_file_should_exist_existing_relative(self):
		"""File Should Exist"""
		self.osLib.file_should_exist("../tests/test_files/file.txt")

	def test_file_should_exist_non_existing_relative(self):
		"""File Should Exist"""
		with self.assertRaises(FileNotFoundException):
			self.osLib.file_should_exist("../test/test_files/non_existing_file.txt")

	def test_file_should_exist_dir_not_exist(self):
		"""File Should Exist"""
		with self.assertRaises(FileNotFoundException):
			self.osLib.file_should_exist("../tests/non_existing_folder/file.txt")

	def test_file_should_not_exist_existing_filename(self):
		"""File Should Not Exist"""
		with self.assertRaises(FileExistException):
			self.osLib.file_should_not_exist("file1.txt")

	def test_file_should_not_exist_non_existing(self):
		"""File Should Not Exist"""
		self.osLib.file_should_not_exist("non_existing.xlsx")

	def test_file_should_not_exist_existing_absolute(self):
		"""File Should Not Exist"""
		with self.assertRaises(FileExistException):
			this_path = os.path.abspath(__file__)
			self.osLib.file_should_not_exist(this_path)

	def test_file_should_not_exist_existing_relative(self):
		"""File Should Not Exist"""
		with self.assertRaises(FileExistException):
			self.osLib.file_should_not_exist("../tests/test_files/file.txt")

	def test_file_should_not_exist_non_existing_relative(self):
		"""File Should Not Exist"""
		self.osLib.file_should_not_exist("../tests/non_existing_file")

	def test_file_should_not_exist_dir_not_exist(self):
		"""File Should Not Exist"""
		self.osLib.file_should_not_exist("../tests/non_existing_dir/file.txt")

	def test_folder_should_exist_existing_name(self):
		"""Folder Should Exist"""
		self.osLib.folder_should_exist("\\test_files")

	def test_folder_should_exist_existing_name_2(self):
		"""Folder Should Exist"""
		self.osLib.folder_should_exist("test_files")

	def test_folder_should_exist_existing_relative(self):
		"""Folder Should Exist"""
		self.osLib.folder_should_exist("../tests/test_files")

	def test_folder_should_exist_existing_absolute(self):
		"""Folder Should Exist"""
		this_dir = os.path.dirname(os.path.abspath(__file__))
		self.osLib.folder_should_exist(this_dir)

	def test_folder_should_exist_file(self):
		"""Folder Should Exist"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.folder_should_exist("test_files/file.txt")

	def test_folder_should_exist_non_existing_name(self):
		"""Folder Should Exist"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.folder_should_exist("non_existing_folder")

	def test_folder_should_exist_non_existing_relative(self):
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.folder_should_exist("../tests/non_existing_folder")

	def test_folder_should_exist_non_existing_absolute(self):
		"""Folder Should Exist"""
		with self.assertRaises(DirectoryNotFoundException):
			this_dir = os.path.dirname(os.path.abspath(__file__))
			self.osLib.folder_should_exist(os.path.join(this_dir, str("non_existing_folder")))

	def test_folder_should_not_exist_existing_name(self):
		"""Folder Should Not Exist"""
		with self.assertRaises(DirectoryExistException):
			self.osLib.folder_should_not_exist("test_files")

	def test_folder_should_not_exist_existing_relative(self):
		"""Folder Should Not Exist"""
		with self.assertRaises(DirectoryExistException):
			self.osLib.folder_should_not_exist("../tests/test_files")

	def test_folder_should_not_exist_existing_absolute(self):
		"""Folder Should Not Exist"""
		with self.assertRaises(DirectoryExistException):
			this_dir = os.path.dirname(os.path.abspath(__file__))
			self.osLib.folder_should_not_exist(this_dir)

	def test_folder_should_not_exist_file(self):
		"""Folder Should Not Exist"""
		self.osLib.folder_should_not_exist("test_files/file.txt")

	def test_folder_should_not_exist_non_existing_name(self):
		"""Folder Should Not Exist"""
		self.osLib.folder_should_not_exist("non_existing_folder")

	def test_folder_should_not_exist_non_existing_relative(self):
		"""Folder Should Not Exist"""
		self.osLib.folder_should_not_exist("../tests/non_existing_folder")

	def test_folder_should_not_exist_non_existing_absolute(self):
		"""Folder Should Not Exist"""
		this_dir = os.path.dirname(os.path.abspath(__file__))
		self.osLib.folder_should_not_exist(os.path.join(this_dir, str("non_existing_folder")))

	def test_get_file_size_existing_name(self):
		"""Get File Size"""
		file_size = self.osLib.get_file_size("file1.txt")
		self.assertEqual(file_size, 1)

	def test_get_file_size_non_existing_name(self):
		"""Get File Size"""
		with self.assertRaises(FileNotFoundException):
			self.osLib.get_file_size("non_existing.txt")

	def test_get_file_size_existing_relative(self):
		"""Get File Size"""
		file_size = self.osLib.get_file_size("/test_files/file.txt")
		self.assertEqual(file_size, 1)

	def test_get_file_size_existing_absolute(self):
		"""Get File Size"""
		file_size = self.osLib.get_file_size(os.path.abspath(__file__))
		self.assertGreater(file_size, 6)

	def test_list_all_files_existing_name(self):
		"""List All Files"""
		files = self.osLib.list_all_files("test_files")
		self.assertIn("file.txt", files)

	def test_list_all_files_existing_absolute(self):
		"""List All Files"""
		files = self.osLib.list_all_files(os.path.dirname(os.path.abspath(__file__)))
		self.assertIn(os.path.basename(__file__), files)

	def test_list_all_files_existing_default(self):
		"""List All Files"""
		files = self.osLib.list_all_files()
		self.assertIn(os.path.basename(__file__), files)

	def test_list_all_folders_existing_default(self):
		"""List Folders"""
		folders = self.osLib.list_folders()
		self.assertIn("test_files", folders)

	def test_list_all_folders_existing_empty(self):
		"""List Folders"""
		folders = self.osLib.list_folders("test_files")
		self.assertEqual(len(folders), 0)

	def test_list_all_folders_existing_absolute(self):
		"""List Folders"""
		folders = self.osLib.list_folders("C:/")
		self.assertIn("Windows", folders)

	def test_list_all_folders_non_existing(self):
		"""List Folders"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.list_folders("C:/non_existing_folder")

	def test_list_all_folders_non_existing_file(self):
		"""List Folders"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.list_folders("non_existing.txt")

	@classmethod
	def tearDownClass(cls):
		test_dir = os.path.dirname(__file__)
		test_file = os.path.join(test_dir, 'file1.txt')
		os.remove(os.path.join(test_dir, test_file))


class TestFileHandlerKeywords(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestFileHandlerKeywords, self).__init__(*args, **kwargs)
		self.osLib = OsProcessLibrary()
		self.test_dir = os.path.dirname(__file__)
		self.test_files_dir = os.path.join(self.test_dir, 'test_files')

	def test_create_folder_name(self):
		"""Create Folder"""
		self.osLib.create_folder("created_test_1")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_1"))
		self.assertTrue(is_dir)

	def test_delete_folder_name(self):
		"""Delete Folder"""
		self.osLib.create_folder("created_test_2")
		self.osLib.delete_folder("created_test_2")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_2"))
		self.assertFalse(is_dir)

	def test_create_folder_tree(self):
		"""Create Folder"""
		self.osLib.create_folder("created_test_3//inner")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_3//inner"))
		self.assertTrue(is_dir)

	def test_delete_folder_tree(self):
		"""Delete Folder"""
		self.osLib.create_folder("created_test_4//inner")
		self.osLib.delete_folder("created_test_4//inner")
		self.osLib.delete_folder("created_test_4")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_4"))
		self.assertFalse(is_dir)

	def test_create_folder_relative_tree(self):
		"""Create Folder"""
		self.osLib.create_folder("..//tests//created_test_5//inner")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_5//inner"))
		self.assertTrue(is_dir)

	def test_delete_folder_relative_tree(self):
		"""Delete Folder"""
		self.osLib.create_folder("created_test_6//inner")
		self.osLib.delete_folder("..//tests//created_test_6//inner")
		self.osLib.delete_folder("..//tests//created_test_6")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_6"))
		self.assertFalse(is_dir)

	def test_create_folder_already_exist(self):
		"""Create Folder"""
		self.osLib.create_folder("created_test_7")
		with self.assertRaises(DirectoryExistException):
			self.osLib.create_folder("created_test_7")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_7"))
		self.assertTrue(is_dir)

	def test_delete_folder_non_exsisting(self):
		"""Delete Folder"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.delete_folder("created_test_8")
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_8"))
		self.assertFalse(is_dir)

	def test_create_folder_absolute(self):
		"""Create Folder"""
		self.osLib.create_folder(os.path.join(self.test_dir, "created_test_9"))
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_9"))
		self.assertTrue(is_dir)

	def test_delete_folder_absolute(self):
		"""Delete Folder"""
		self.osLib.create_folder("created_test_10")
		self.osLib.delete_folder(os.path.join(self.test_dir, "created_test_10"))
		is_dir = os.path.isdir(os.path.join(self.test_dir, "created_test_10"))
		self.assertFalse(is_dir)

	# Create New File
	def test_create_new_file_name(self):
		"""Create New File"""
		self.osLib.create_new_file("created_file_1.txt")
		is_file = os.path.isfile(os.path.join(self.test_dir, "created_file_1.txt"))
		self.assertTrue(is_file)
		self.osLib.file_should_exist("created_file_1.txt")

	def test_create_new_file_non_existing_folder(self):
		"""Create New File"""
		with self.assertRaises(DirectoryNotFoundException):
			self.osLib.create_new_file("non_existing_folder//new_file.txt")
		self.osLib.file_should_not_exist("non_existing_folder//new_file.txt")

	def test_create_new_file_absolute(self):
		"""Create New File"""
		self.osLib.create_new_file(os.path.join(self.test_dir, "created_file_2.txt"))
		self.osLib.file_should_exist("created_file_2.txt")

	def test_delete_file_absolute(self):
		"""Delete File"""
		self.osLib.create_new_file("created_file_3.txt")
		self.osLib.delete_file(os.path.join(self.test_dir, str("created_file_3.txt")))

	def test_delete_file_non_existing(self):
		"""Delete File"""
		with self.assertRaises(FileNotFoundException):
			self.osLib.delete_file(os.path.join(self.test_dir, str("created_file_4.txt")))

	@classmethod
	def tearDownClass(cls):
		test_dir = os.path.dirname(__file__)
		files = os.listdir(test_dir)
		for f in files:
			if f.startswith(str("created_test_")):
				shutil.rmtree(os.path.join(test_dir, f), ignore_errors=True)
			if f.startswith(str("created_file_")):
				os.remove(os.path.join(test_dir, f))


if __name__ == '__main__':
	unittest.main()
