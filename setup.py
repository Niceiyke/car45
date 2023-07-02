from setuptools import find_packages,setup


setup(
    name='scraper',
    version='1.0.0',
    author='niceiyke',
    author_email='niceiyke04@gmail.com',
    packages=find_packages(),
    install_requires=['aiohttp','bs4','beautifulsoup4','panadas']
)
