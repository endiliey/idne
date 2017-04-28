from setuptools import setup

setup(
    name = 'Idne',
    version = '1.0',
    py_modules = ['idne', 'parse'],
    install_requires = [
        'Click','robobrowser', 'requests'
    ],
    entry_points = '''
        [console_scripts]
        idne = idne:cli
		parse = parse:main
    ''',
)
