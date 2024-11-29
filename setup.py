import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


class BinaryDistribution(setuptools.Distribution):
    def has_ext_modules(_):
        return True


setuptools.setup(
    name="vrf",
    version="0.1.0",
    author="iwehf",
    author_email="henry.lee@crynux.ai",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["build"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    distclass=BinaryDistribution,
)
