from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='pypi_helloworld',
    version='0.1',
    description='oissu!',
    author='ababa',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "hello",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)