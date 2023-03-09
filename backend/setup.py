import setuptools


setuptools.setup(
    python_requires=">=3.8",
    name="labelit",
    version="1.0.0",
    author="LeVoiceLab",
    author_email="contact@batvoice.com",
    description="Labelit is an extensible web-based annotation tool.",
    long_description_content_type="text/markdown",
    url="https://github.com/voicelab-org/labelit",
    include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "appdirs >= 1.4.4",
        "asgiref >= 3.3.1",
        "attrs >= 20.3.0",
        "audeer >= 1.18.0",
        "audiofile >= 1.1.0",
        "audioread >= 2.1.9",
        "boto3 >= 1.17.27",
        "botocore >= 1.20.27",
        "certifi >= 2020.12.5",
        "cffi >= 1.14.5",
        "chardet >= 4.0.0",
        "click >= 7.1.2",
        "coloredlogs >= 15.0.1",
        "decorator >= 4.4.2",
        "django-cors-headers >= 3.7.0",
        "django-extensions >= 3.1.1",
        "django-filter >= 2.4.0",
        "django-polymorphic >= 3.0.0",
        "django-rest-polymorphic >= 0.1.9",
        "django-storages >= 1.11.1",
        "Django >= 3.1.7",
        "djangorestframework-simplejwt >= 4.5.0",
        "djangorestframework >= 3.12.2",
        "et-xmlfile >= 1.0.1",
        "idna >= 2.10",
        "importlib-metadata >= 3.4.0",
        "iniconfig >= 1.1.1",
        "jmespath >= 0.10.0",
        "joblib >= 1.0.1",
        "JSON-log-formatter >= 0.5.1",
        "librosa >= 0.6.0",
        "llvmlite >= 0.31.0",
        "m3u8 >= 1.0.0",
        "Markdown >= 3.3.3",
        "nltk >= 3.5",
        "numba >= 0.48.0",
        "numpy >= 1.20.1",
        "packaging >= 20.9",
        "pandas >= 1.2.2",
        "patsy >= 0.5.1",
        "Pillow >= 8.1.0",
        "pluggy >= 0.13.1",
        "pooch >= 1.3.0",
        "psycopg2 >= 2.8.6",
        "py >= 1.10.0",
        "pycparser >= 2.20",
        "PyJWT >= 1.7.1",
        "pyparsing >= 2.4.7",
        "pytest-django >= 4.1.0",
        "pytest >= 6.2.2",
        "python-dateutil >= 2.8.1",
        "pytz >= 2021.1",
        "PyYAML >= 5.4.1",
        "regex >= 2020.11.13",
        "requests >= 2.25.1",
        "resampy >= 0.2.2",
        "s3transfer >= 0.3.4",
        "scikit-learn >= 0.24.1",
        "scipy >= 1.6.1",
        "six >= 1.15.0",
        "SoundFile >= 0.10.3.post1",
        "sox >= 1.4.1",
        "sqlparse >= 0.4.1",
        "statsmodels >= 0.12.2",
        "threadpoolctl >= 2.1.0",
        "toml >= 0.10.2",
        "tqdm >= 4.58.0",
        "typing-extensions >= 3.7.4.3",
        "uritemplate >= 4.1.1",
        "urllib3 >= 1.26.4",
        "whitenoise >= 5.2.0",
        "zipp >= 3.4.0",
        "zope.dottedname >= 4.3",
    ],
    extras_require={
        "dev": [
            # Do not forget to update .pre-commit.yaml
            "black >= 23.1.0",
            "pip-tools >= 6.12.3",
        ],
    },
)
