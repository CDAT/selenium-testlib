from setuptools import setup, find_packages
import os
from subprocess import Popen, PIPE

Version = "1.0"
p = Popen(
    ("git",
     "describe",
     "--tags"),
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE)
try:
    descr = p.stdout.readlines()[0].strip().decode("utf-8")
    Version = "-".join(descr.split("-")[:-2])
    if Version == "":
        Version = descr
except:
    descr = Version

setup(name="selenium-testlib",
      version=descr,
      description="Selenium base test libraries",
      url="http://github.com/cdat/selenium-testlib",
      packages=find_packages(),
      zip_safe=True
)
