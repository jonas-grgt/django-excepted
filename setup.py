from distutils.core import setup

setup(name='django-excepted',
        version='0.1',
        description=("Middleware that catches and exception and excecutes it's render method"),
        author='Jonas Geiregat',
        author_email='jonas@geiregat.org',
        packages=['django_excepted']
        )
