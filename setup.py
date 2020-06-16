"""
A setuptools based on setup module for MADIS.
"""

# Always prefer setuptools over distutils
import os
from setuptools import setup, find_packages

setup(
    name="mma845x-sensor",
    version="0.1",
    description="A python driver for the MMA845x accel/gyro.",
    # The project's main homepage.
    url="https://github.com/m1ch3al/mma845x_accelerometer.git",
    # Author details
    author="Renato Sirola",
    author_email="renato.sirola@gmail.com",
    # Choose your license
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    # What does your project relate to?
    keywords="sensors ros hardware drone autonomy",
    include_package_data=False,
    install_requires=[
        'setuptools',
        'smbus2',
    ],
    py_modules=["mma845x"],
)

