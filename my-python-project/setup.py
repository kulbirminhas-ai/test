from setuptools import setup, find_packages

setup(
    name='my-python-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # add your project dependencies here
        # for example:
        # 'numpy',
        # 'pandas',
    ],
    entry_points={
        'console_scripts': [
            # add any scripts you want to run from the command line here
            # for example:
            # 'my-script = my_python_project.main:main',
        ],
    },
)