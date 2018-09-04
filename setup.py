from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup_args = dict(
    name='aiorss',
    version='0.1.0',
    author='Marc Ford',
    url='https://github.com/mfdeux/aiorss',
    description='Asyncio client for interacting with rss feeds',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['aiorss'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
        'feedparser',
    ]
)

setup(**setup_args)
