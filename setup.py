from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='simplehello',
    version='0.0.1',
    description='Say hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anawas/simplehello",
    author="Andreas Wassmer",
    author_email="me.example.com",
    py_modules=["hello"],
    package_dir={'': 'src'},
    classifiers=[
        "Programmming Language :: Python :: 3",
        "Programmming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent"
    ]
)
