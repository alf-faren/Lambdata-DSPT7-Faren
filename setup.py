import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="Lambdata-DSPT7-Faren",   # Replace with your own username
    version="0.0.3",  # Always update this after every change
    author="Raymond Huang",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alf-faren/Lambdata-DSPT7-Faren",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )
