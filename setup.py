from setuptools import setup, find_packages

setup(
    name='restful_booker_api_tests',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'requests',
        'allure-pytest',
        # Add any other dependencies your project requires
    ],
    entry_points={
        'console_scripts': [
            'restful_booker_api_tests=restful_booker_api_tests.cli:main',
        ],
    },
)
