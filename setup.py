from pathlib import Path

from setuptools import find_packages, setup

meta = {}
exec(open("./gsrace/version.py").read(), meta)
meta["long_description"] = open("./README.md").read()


setup(
    name="gsrace",
    version=meta["__version__"],
    description="Python library to show the journal race for a user on Google Scholar.",
    long_description=meta["long_description"],
    long_description_content_type="text/markdown",
    keywords="google scholar race cli",
    author="Farid Rashidi",
    author_email="farid.rsh@gmail.com",
    url="https://github.com/faridrashidi/gscholar-race",
    project_urls={
        "Source": "https://github.com/faridrashidi/gscholar-race",
    },
    python_requires=">=3.6",
    install_requires=[
        "tqdm",
        "pandas",
        "click",
        "arrow",
        "beautifulsoup4",
        "bibtexparser",
        "deprecated",
        "fake_useragent",
        "free-proxy",
        "python-dotenv",
        "requests[socks]",
        "selenium",
        "stem",
        "bar_chart_race @ git+ssh://git@github.com/dexplo/bar_chart_race.git",
    ],
    packages=find_packages(),
    entry_points={"console_scripts": ["gsrace = gsrace.__main__:main"]},
    license="MIT",
)
