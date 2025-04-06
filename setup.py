from setuptools import setup, find_packages

setup(
    name="resicli",
    version="1.0.1",
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
)