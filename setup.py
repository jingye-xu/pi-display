from setuptools import setup, find_packages

setup(
    name='pidisplay',
    version='0.0.0',
    description='Easily make projects with NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'Adafruit_SSD1306'
    ],
)
