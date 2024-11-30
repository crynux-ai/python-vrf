import os
import shutil

import setuptools
from setuptools import Command
from setuptools.command.build import build


with open("README.md", "r") as fh:
    long_description = fh.read()


class BinaryDistribution(setuptools.Distribution):
    def has_ext_modules(_):
        return True


class BuildGoPy(Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self) -> None:
        self.spawn(
            [
                "gopy",
                "build",
                "--rename=true",
                "--no-make=true",
                "-vm=python3",
                "-output=vrf",
                "vrf",
            ]
        )
        dir_path = os.path.dirname(os.path.realpath(__file__))
        src_init_file = os.path.join(dir_path, "__init__.py")
        dst_init_file = os.path.join(dir_path, "vrf", "__init__.py")
        shutil.copyfile(src_init_file, dst_init_file)

build.sub_commands.insert(0, ("build_gopy", None))

setuptools.setup(
    name="vrf",
    version="0.1.0",
    author="iwehf",
    author_email="henry.lee@crynux.ai",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["vrf"],
    package_data={"vrf": ["*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    distclass=BinaryDistribution,
    cmdclass={"build_gopy": BuildGoPy},
)
