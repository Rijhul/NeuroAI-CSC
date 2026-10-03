from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="NeuroAI-CSC",
    version="0.1.0",
    author="Rijhul Lahariya",
    author_email="contact@rijhullahariya.com",
    description="Computational Stem Cells (CSC) for Autonomous Neural Network Self-Repair",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rijhul/NeuroAI-CSC",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "torch>=1.10.0",
    ],
)
