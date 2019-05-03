from __future__ import absolute_import, division, generators, print_function, unicode_literals


class OsLibraryException(Exception):
	pass
	#ROBOT_SUPPRESS_NAME = True


class FileNotFoundException(OsLibraryException):
	pass


class FileExistException(OsLibraryException):
	pass


class DirectoryNotFoundException(OsLibraryException):
	pass


class DirectoryExistException(OsLibraryException):
	pass
