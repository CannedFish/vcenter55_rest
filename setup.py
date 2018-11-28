from setuptools import setup, find_packages

setup(
    name='vcenter55_rest',
    version='0.0.1',
    description='The RESTful API for vcenter 5.5 based on Flask-RESTPlus',
    url='',
    author='CannedFish',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='rest restful api flask swagger openapi flask-restplus vsphere',

    packages=find_packages(),

    install_requires=[
        'Flask==1.0.2',
        'flask-restplus==0.12.1',
        'Flask-SQLAlchemy==2.3.2'
    ],
)
