from setuptools import setup, find_packages

setup(
    name="django-exercise",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "psycopg2-2.7.6.1",
        "Django-2.1.3",
        "requests-2.20.1",
        "djangorestframework-3.9.0",
        "django-rest-auth-0.9.3",
        "black-18.9b0",
    ],
)
