import os
import shutil
import tempfile
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.sdist import sdist
from setuptools.command.bdist_egg import bdist_egg

CUSTOM_DIST_DIR = tempfile.mkdtemp(prefix="resicli_dist_")
CUSTOM_BUILD_DIR = tempfile.mkdtemp(prefix="resicli_build_")
CUSTOM_EGG_INFO_DIR = tempfile.mkdtemp(prefix="resicli_egg_info_")

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        print(f"Installation complete. Distribution files are located in: {CUSTOM_DIST_DIR}")
        print(f"Build files are located in: {CUSTOM_BUILD_DIR}")
        
        # Clean up build artifacts
        try:
            if os.path.exists('build'):
                shutil.rmtree('build')
            if os.path.exists('resicli.egg-info'):
                shutil.rmtree('resicli.egg-info')
            print("Cleaned up build artifacts successfully.")
        except Exception as e:
            print(f"Warning: Could not clean up build artifacts: {e}")

class CustomSdistCommand(sdist):
    def run(self):
        self.dist_dir = CUSTOM_DIST_DIR
        sdist.run(self)

class CustomBdistEggCommand(bdist_egg):
    def run(self):
        self.dist_dir = CUSTOM_DIST_DIR
        self.build_base = CUSTOM_BUILD_DIR
        self.egg_base = CUSTOM_EGG_INFO_DIR
        bdist_egg.run(self)

setup(
    name="resicli",
    version="1.0.0",
    author="Yash Gaikwad",
    author_email="gaikwadyash905@gmail.com",
    description="A CLI tool for bulk image resizing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gaikwadyash905/ResiCLI",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        "Pillow>=9.0.0",
        "click>=8.0.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": ["resicli=resicli.cli:main"],
    },
    package_data={
        "resicli": ["resicli_config.json"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    keywords="image resize bulk cli pillow",
    cmdclass={
        'install': CustomInstallCommand,
        'sdist': CustomSdistCommand,
        'bdist_egg': CustomBdistEggCommand,
    },
)