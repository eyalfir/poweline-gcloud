from setuptools import setup

setup(name='powerline-gcloud',
      description='powerline plugin to display gcloud current project',
      author='Eyal Firstenberg',
      author_email='eyalfir@gmail.com',
      classifiers=['Development Status :: 3 - Production'],
      packages=['powerline_gcloud'],
      install_requires=['python-jenkins', 'pygit', 'requests'],
      version='1.0.0')
