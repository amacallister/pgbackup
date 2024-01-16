from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Amanda MacAllister',
    description="A tutorial project from A Cloud Guru's Introduction to Python Development course",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/amacallister/pgbackup',
    packages=find_packages('src')
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ]
    }
)