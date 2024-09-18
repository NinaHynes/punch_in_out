from setuptools import setup, find_packages

setup(
    name='punchcard',
    version='0.1',
    packages=find_packages(),
    install_requires=['toga'],
    entry_points={
        'console_scripts': [
            'punchcard = punchcard.app:main',
        ],
    },
)
