from distutils.core import setup

setup(
  name = 'nhefner_pygame_menus',
  packages = ['nhefner_pygame_menus'],
  version = '1.0',
  license='MIT',
  description = 'Menu System for Pygame Games',
  author = 'Noah Hefner',
  author_email = 'noah.hefner127@gmail.com',
  url = 'https://github.com/noahhefner/nhefner_pygame_menus',
  download_url = 'https://github.com/noahhefner/nhefner_pygame_menus/archive/1.0.tar.gz',
  keywords = ['pygame', 'menu', 'python'],
  install_requires=[
          'pygame'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
  ]
)
