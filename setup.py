from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()
# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]


setup (
    name = 'datrics',
    description = 'CLI for datrics.ai platform that allows you to create and manage custom bricks',
    version = '0.0.3',
    packages = find_packages(), # list of all packages
    package_data={
        "datrics": ["services/template_brick/*.json", "services/template_brick/{{cookiecutter.brick_directory_name}}/*"],
    },
    install_requires = install_requires,
    python_requires='>=2.7', # any python greater than 2.7
    entry_points={
        'console_scripts': ['datrics=datrics.__main__:main'],
    },
    author="Roman Malkevych",
    keyword="Datrics, cli, data science, ML, AI",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/datrics-ai/datrics-cli',
    dependency_links=dependency_links,
    author_email='rm@datrics.ai',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)

# python3 -m setup.py sdist bdist_wheel
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python3 -m pip install -i https://test.pypi.org/simple/ datrics==0.0.{version}