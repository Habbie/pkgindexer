#!venv/bin/python
import json, subprocess
from debian.deb822 import Packages
from elasticsearch import Elasticsearch

res = dict()
for pkg in Packages.iter_paragraphs(open('packages')):
    pkgdict = dict(pkg)
    res[pkgdict["Package"]] = pkgdict

json.dump(res, open('Packages.json', 'w'))
