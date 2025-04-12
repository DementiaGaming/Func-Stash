from setuptools import setup, find_packages

setup(
    name="funcstash",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    author="Dementia Gaming",
    description="A package that adds useful functions to Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DementiaGaming/py-plus-plus",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)