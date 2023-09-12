# Meituan Vision AI Department YOLOv6 🚀, GPL-3.0 license

import re
from pathlib import Path

import pkg_resources as pkg
from setuptools import find_packages, setup

# Settings
FILE = Path(__file__).resolve()
PARENT = FILE.parent  # root directory
README = (PARENT / "README.md").read_text(encoding="utf-8")
REQUIREMENTS = [
    f"{x.name}{x.specifier}"
    for x in pkg.parse_requirements((PARENT / "requirements.txt").read_text())
]


setup(
    name="yolov6",  # name of pypi package
    version="4.0",  # version of pypi package
    python_requires=">=3.8",
    license="GPL-3.0",
    description=(
        "YOLOv6: a single-stage object detection framework dedicated to industrial applications.."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/meituan/YOLOv6",
    project_urls={
        "Bug Reports": "https://github.com/meituan/YOLOv6/issues",
        "Source": "https://github.com/meituan/YOLOv6",
    },
    author="Ultralytics",
    author_email="hello@ultralytics.com",
    packages=find_packages(),  # required
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": [
            "ipython",
            "check-manifest",
            "pytest",
            "pytest-cov",
            "coverage",
            "mkdocs-material",
            "mkdocstrings[python]",
            "mkdocs-redirects",  # for 301 redirects
            "mkdocs-ultralytics-plugin>=0.0.27",  # for meta descriptions and images, dates and authors
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="machine-learning, deep-learning, vision, ML, DL, AI, YOLO, YOLOv3, YOLOv5, YOLOv8, HUB, Ultralytics",
)
