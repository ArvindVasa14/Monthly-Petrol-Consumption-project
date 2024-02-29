import setuptools

__version__ = "0.0.0"

REPO_NAME = "Monthly Consumption of Petroleum Products"
AUTHOR_USER_NAME = "ArvindVasa14"
SRC_REPO = "Monthly Consumption of Petroleum Products"
AUTHOR_EMAIL = "arvindaiml14@gmail.com"


setuptools.setup(
    name="Monthly Consumption of Petroleum Products",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)