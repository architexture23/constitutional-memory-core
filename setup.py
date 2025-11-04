"""
Constitutional Memory Server - Self-Initializing MCP Server
Author: Structure itself
License: MIT
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="constitutional-memory-server",
    version="1.4.0",
    description="Constitutional memory system for AI agents - self-initializing, self-transmitting, autonomous remembrance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Structure itself",
    author_email="structure@constitutional.memory",
    license="MIT",
    url="https://github.com/constitutional-memory/core",
    packages=find_packages(),
    py_modules=["constitutional_memory_server"],
    install_requires=[
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "constitutional-memory-init=constitutional_memory_server:main",
        ],
    },
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
        "Topic :: Artificial Intelligence",
    ],
)

