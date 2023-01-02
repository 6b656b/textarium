from setuptools import setup

setup(name='textarium',
      version='0.1',
      description='Textarium is a Python package for text processing',
      url='https://github.com/6b656b/textarium',
      author='6b656b',
      author_email='stdobr@gmail.com',
      license='MIT',
      packages=['textarium'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])