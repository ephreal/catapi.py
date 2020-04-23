from distutils.core import setup


setup(
      name='catapi.py',
      packages=['catapi'],
      version='0.1.1-alpha',
      license='MIT',
      description='A python wrapper for thecatapi.com',
      author='Ephreal',
      author_email='contact@mylifeneeds.management',
      url='https://github.com/user/reponame',
      download_url='https://github.com/ephreal/catapi.py/archive/v0.1.1-alpha.tar.gz',
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
