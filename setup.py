from setuptools import setup

with open("README.rst") as readme_file:
    long_description = readme_file.read()


setup(name="Django Geric URL Patterns",
    version="0.1",
    packages=["url_generics",],
    license="GNU GPL v3.0",
    description="Provides convenience methods for reusable generic url patterns avoiding messy regex",
    author="Gemma Hentsch",
    author_email="contact@halfapenguin.com",
    install_requires=[
    ],
    tests_require=[
        "mock",
        "coverage",
        "nose",
    ],
    long_description=long_description,
    test_suite="nose.collector",
    url="https://github.com/ladyrassilon/django-url-generics",
    keywords = ['django', 'urls'],
    download_url="https://github.com/ladyrassilon/django-url-generics/archive/",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ]
)