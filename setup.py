import json
from setuptools import setup
from pathlib import Path

with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={"Github": "https://github.com/ruslankhayrut/DashSelect"},
    install_requires=[],
    classifiers = [
        'Framework :: Dash',
    ],    
)
