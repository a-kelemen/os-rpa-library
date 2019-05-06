#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, generators, print_function, unicode_literals
import os
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


class Base(object):

	def _get_process_source(self):
		try:
			file_p = BuiltIn().get_variable_value("${SUITE SOURCE}")
		except RobotNotRunningError as e:
			file_p = os.path.abspath(__file__)
		return file_p

	def _get_process_folder(self):
		try:
			process_dir = os.path.dirname(BuiltIn().get_variable_value("${SUITE SOURCE}"))
			return process_dir
		except RobotNotRunningError:
			base_dir = self._nth_parent_folder(__file__, 3)
			return os.path.join(base_dir, str("tests"))

	def _get_source(self, file_name):
		try:
			file_name = file_name.lstrip("\\").lstrip("/")
		except UnicodeDecodeError:
			pass
		if file_name == str("default_"):
			return self._get_process_folder()
		else:
			file_full_path = os.path.abspath(file_name)
			if not Base._is_absolute_path(file_name):
				return os.path.join(self._get_process_folder(), str(os.path.normpath(file_name)))
			else:
				return file_full_path

	def _nth_parent_folder(self, file_source, n):
		if n > 0:
			return self._nth_parent_folder(os.path.dirname(file_source), n-1)
		else:
			return file_source

	@staticmethod
	def _is_absolute_path(path):
		return os.path.normpath(path) == os.path.abspath(path)
