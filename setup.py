from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="WonderPy",
    version="0.1.0",
    author="Orion Elenzil",
    author_email="orion@makewonder.com",
    description="Python API for working with Wonder Workshop robots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/playi/WonderPy",
    packages=find_packages(),
    package_data={'WonderPy': ['lib/WonderWorkshop/osx/*.dylib']},
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Framework :: Robot Framework",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2.7",
    ),
    keywords=['robots', 'dash', 'dot', 'cue', 'wonder workshop', 'robotics', 'sketchkit', ],
    test_suite='test',
    zip_safe=True,
    install_requires=[
        "mock",
        'Adafruit_BluefruitLE==1.9.9',
        'morseapi==1.0.1',
        'svgpathtools==1.3.3',
        'PyObjC;platform_system=="Darwin"'
    ],
    dependency_links=[
        'http://github.com/avrabe/Adafruit_Python_BluefruitLE/tarball/avrabe_master#egg=Adafruit_BluefruitLE-1.9.9',
        'http://github.com/avrabe/morseapi/tarball/master#egg=morseapi-1.0.1'
        ]
)
