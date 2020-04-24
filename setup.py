from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
      name='catapi.py',
      packages=['catapi'],
      version='0.2.0-a',
      license='MIT',
      description='A python wrapper for thecatapi.com',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      author='Ephreal',
      author_email='contact@mylifeneeds.management',
      url='https://github.com/ephreal/catapi.py',
      download_url='https://github.com/ephreal/catapi.py/archive/0.2.0-alpha.tar.gz',
      keywords=['cats', 'catapi', ],
      install_requires=[
            'aiohttp',
      ],
      classifiers=[
                    # 'Development Status :: 5 - Production/Stable'
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3.5',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    ],
)
