import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="ex47",
    version="0.0.1",
    author="Julio Pochet Edmead",
    author_email="jrpochetedmead192@stevenscollege.edu",
    url="https://github.com/jpochetedmead/ex47",
    description="what does yourproject do? ex47",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
