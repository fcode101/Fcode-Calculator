from setuptools import setup, find_packages

setup(
    name="Py_Science_Calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="F-Code 101",
    author_email="techwbro@example.com",
    description="A Python package for scientific and electronic calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/f-code101/Py_Science_Calculator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
