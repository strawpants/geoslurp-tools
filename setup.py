# setup.py  
# This file is part of geoslurp.
# geoslurp is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# geoslurp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with Frommle; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# Author Roelof Rietbroek (roelof@geod.uni-bonn.de), 2019
import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

print(find_packages("geoslurp-tools"))
setuptools.setup(
    name="geoslurptools",
    author="Roelof Rietbroek",
    author_email="roelof@wobbly.earth",
    description="Client functions to query the geoslurp database",
    long_description=long_description,
    url="https://github.com/strawpants/geoslurp-tools",
    packages=find_packages("."),
    package_dir={"":"."},
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering",
        "Development Status :: 1 - Planning"]
    
)
