from setuptools import setup, find_packages

setup(
    name="pykeyboard",
    version="1.0.0",
    description="Simple inline/reply keyboard wrapper for Pyrogram",
    author="PyMaster",
    packages=find_packages(),
    install_requires=[
        "pyrogram"
    ],
    python_requires=">=3.6",
)