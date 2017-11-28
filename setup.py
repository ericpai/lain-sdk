from setuptools import setup, find_packages
from lain_sdk import __version__


requirements = [
    'Jinja2==2.7.3',
    'PyYAML==3.12',
    'enum34==1.0.4',
    'requests>=2.6.1',
    'websocket-client==0.32.0',
    'docker==2.6.1',
    'pytest<=3.2.5',
    'mock==1.0.1',
    'jsonschema==2.5.1',
]


setup(
    name="einplus_lain_sdk",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    data_files=[
    ],
    scripts=['lain_release'],
    install_requires=requirements,
)
