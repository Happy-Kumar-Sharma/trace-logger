import os

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> list[str]:
    "This function will return the list of packages"
    print(f"Looking for requirements file at: {os.path.abspath(file_path)}")
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements = [
        requirement.replace("\n", "") for requirement in requirements
    ]  # noqa
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements


setup(
    name="api-x-trace-logger",
    version="0.0.1",
    description="A logging library with trace ID support and FastAPI middleware.",  # noqa
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Happy Sharma",
    author_email="happycse54@gmail.com",
    url="https://github.com/Happy-Kumar-Sharma/trace-logger",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
