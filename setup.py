from setuptools import setup

setup(
    name='taxjar',
    version='1.0.0',
    description='Sales tax API client for Python',
    author='TaxJar',
    author_email='support@taxjar.com',
    url='https://github.com/taxjar/taxjar-python',
    download_url='https://github.com/taxjar/taxjar-python/archive/v1.0.0.zip',
    packages=['taxjar'],
    install_requires=[
        'requests >= 2.13.0'
    ],
    tests_require=[
        'mock'
    ]
)
