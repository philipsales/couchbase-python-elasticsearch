# setup.py
from setuptools import setup, find_packages

NAME = "awh_datapipeline"
VERSION = "1.0.0"

setup(
    name='datapipeline',
    packages=find_packages()
)

REQUIRES = ["couchbase, elasticsearch"]

setup(
    name=NAME,
    version=VERSION,
    description="AWH Datapipeline",
    author_email="philip@alliedworld.healthcare, rosette@alliedworld.healthcare",
    url="",
    keywords=["python", "datapipeline"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['']},
    include_package_data=False,
    entry_points={
        'console_scripts': ['datapipeline=main.py.__init__']},
    long_description="""\
    Alliedworld Health internal datapipeline
    """
)

