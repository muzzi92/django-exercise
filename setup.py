from setuptools import setup, find_packages

setup(
    name="django-exercise",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "psycopg2",
        "django",
        "djangorestframework",
        "django-rest-auth",
        "black",
    ],
)
