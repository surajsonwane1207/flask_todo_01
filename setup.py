from setuptools import find_packages, setup # type: ignore

setup(
    name='flask_todo-01',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)