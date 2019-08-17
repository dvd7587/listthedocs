from setuptools import setup, find_packages

setup(
    name='listthedocs',
    version='1.0.3',
    description='List your documentations',
    author='Alessandro Bacchini',
    author_email='allebacco@gmail.com',
    url='https://github.com/allebacco/listthedocs',
    packages=find_packages(),
    install_requires=[
        'natsort',
        'requests',
        'attrs',
        'python-dateutil',
        'Flask-SQLAlchemy',
        'Flask',
    ],
    tests_require=[
        'pytest'
    ]
)
