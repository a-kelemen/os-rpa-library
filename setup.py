import setuptools

setuptools.setup(
	name='osprocesslibrary',
	version='0.1',
	description='Library for file handling automation.',
	url='',
	author='Andras Kelemen',
	author_email='kelemenandras11@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(exclude=['OsProcessLibrary.tests']),

	install_requires=[
		'robotframework',
	],
	test_suite="tests",
	tests_require=['nose'],
	zip_safe=False
)
