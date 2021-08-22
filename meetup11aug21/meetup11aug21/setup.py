'''Setup file for the Bayesian Confidence module'''

from setuptools import setup, find_packages


def load_requirements():
    with open('requirements.txt', 'r') as rfile:
        return rfile.read().strip().split('\n')


setup(
    name='meetup11aug21',
    description='Python Meetup, Bayesian Statistics, Variance Estimation',
    version='1.0.0',
    author='Charles Lindsey',
    author_email='lindseycster@gmail.com',
    packages=find_packages(where='src', exclude=['tests', 'tests.*']),
    package_dir={'': 'src'},
    install_requires=load_requirements(),
)
