from setuptools import setup

setup(
    name="darkdown",
    version="1.0.0",
    packages=["darkdown"],  # Specify the package explicitly
    package_dir={"darkdown": "src"},  # Map 'darkdown' package to 'src' directory
    include_package_data=True,
    install_requires=[
        "yt-dlp>=2024.10.7",
        "requests>=2.32.3",
        "websockets>=13.0",
        "mutagen>=1.47.0",
    ],
    entry_points={
        "console_scripts": [
            "darkdown=darkdown.main:main",
        ],
    },
    author="0xRach",
    author_email="0xxrach@gmail.com",
    description="A powerful YouTube video and playlist and audio downloader using yt-dlp",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="git@github.com:OxRachid/darkdown.git",
    python_requires=">=3.6",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Video",
        "Environment :: Console",
    ],
)
