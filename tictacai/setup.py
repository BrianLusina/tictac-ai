import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "tictacai"
DESCRIPTION = "Tic-Tac-Toe Game created using Human, Randomized Computer & Minimax AI players"
EMAIL = "12752833+BrianLusina@users.noreply.github.com"
AUTHOR = "Brian Lusina"
REQUIRES_PYTHON = ">=3.10.0"
VERSION = "0.1.0"

if os.environ.get("CI_COMMIT_TAG"):
    VERSION = os.environ.get("CI_COMMIT_TAG")
elif os.environ.get("CI_JOB_ID"):
    VERSION = os.environ.get("CI_JOB_ID")
elif os.environ.get("GITHUB_RUN_ID"):
    # Reference
    # https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables
    VERSION = f"{os.environ.get('GITHUB_RUN_ID')}.{os.environ.get('GITHUB_RUN_NUMBER')}"

# What packages are required for this module to be executed?
REQUIRED = []

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=REQUIRED,
    setup_requires=["wheel"],
)