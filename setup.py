from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
	long_description = f.read()

setup(
	name="nhentai-api",
	version="1.0.1",
	packages=find_packages(),
	author="moka",
	long_description=long_description,
	long_description_content_type='text/x-rst',
	url='github.com/moe-ka/nhentai-api-wrapper'
)