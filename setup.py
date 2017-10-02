from setuptools import setup, find_packages

setup(
	name="Nor2qml",
	version="0.1",
	py_modules=find_packages(),
	include_package_data=True,
	install_requires=[
		"Click",
	],
	entry_points='''
		[console_scripts]
		Nor2qml=bin.Nor2qml:nor2qml
	''',
)
