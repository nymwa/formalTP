from setuptools import setup, find_packages

setup(
		name = 'formalTP',
		version = '0.1.0',
		description = 'toki pona li toki pona sina jan pona mute',
		author = 'nymwa',
		entry_points = { 
			'console_scripts':[
				'dfa = formalTP.dfa:main',
				]})


