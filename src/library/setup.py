from setuptools import find_packages, setup

setup(
    name='alingeo',
    version='1.0.0',
    author='Algeo02-20103',
    author_email='13520103@std.stei.itb.ac.id',
    description=''.join([
        'Pepega',
    ]),
    url='https://github.com/clumsyyyy/Algeo02-20103',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'numpy',
    ],
    python_requires='>=3.7',
)