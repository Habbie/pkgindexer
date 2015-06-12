#!venv/bin/python
import json, subprocess
from elasticsearch import Elasticsearch

brew = subprocess.Popen(["brew","info","--all","--json=v1"], stdout=subprocess.PIPE)
packages = json.load(brew.stdout)
es = Elasticsearch()
# TODO create _timestamp index and move an alias, suggested by @ch2500
es.indices.delete(index='brew', ignore=[400, 404])
for p in packages:
    if p['name'] != p['full_name']:
        raise Exception('name!=full_name for %s/%s' % (p['name'], p['full_name']))

    es.index(index="brew", doc_type="package", id=p['name'], body=p)
