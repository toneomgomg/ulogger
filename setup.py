from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="ulogger",
    version='0.0.1',
    description="Simple UDP logger.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tone Hellström, Henrik Pira",
    author_email="tone.hellstrom@inter.ikea.com, henrik.pira@inter.ikea.com",
    packages=[
        "ulogger"
    ],
    include_package_data=True,
)
