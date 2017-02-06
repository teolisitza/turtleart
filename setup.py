from setuptools import setup

setup(name='turtleart',
      version='0.2',
      description='Library to facilitate Turtle Art',
      author='Ava and Teo Lisitza',
      author_email='mlisitza+github@gmail.com',
      packages=['turtleart', 'turtleart.scripts'],
      entry_points={
          'console_scripts': [
              'qturtle = turtleart.scripts.qturtle:main'
          ]
      },
     )
