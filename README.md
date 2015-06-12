pkgindexer
==========

idea: collect package information from as many sources as possible
(brew, apt, various port systems, gems, github, etc. etc.), match
those together *automatically* and make it easy to search.

For bonus points, also include package contents, so we can answer 'how do I get
tool `dnssec-signzone` onto my system?'

Doing this because I miss an up-to-date version of freshmeat but also don't feel
like moderating a big database of submissions.

Brew
----

contents: fetch bottles, tar tf. Or ask that the bottle building bots publish lists.

Name suggestions
----------------

fossball (Robe)
flossball, flosser; flossball, BADY (Brew Apt DNF Yum), yassir (Yet Another Super|Silly|Sexy Software Index cRawler)

Credits
-------

* Robe (for thinking out loud with me)
* @zeha (for help with the Debian importer)
* Bram Heerink (for suggesting Elasticsearch)

Scope creep requests
--------------------

* automatically find Chef cookbooks on github and index them (pzt)
* sexiness-score for various things (last commit, number of commits, etc.) (Robe)

Backend/Storage
---------------

ElasticSearch is really really cool, but maybe overkill? I'd like to propose
CouchDB, a document database with a REST interface (also UI in form of Futon)
which out to be lighter on system resources as well. It replicates (subsets) of
documents, etc. A companion project, PouchDB JavaScript, runs in Web browser
and can be used with (or without) CouchDB to replicate a (subset) of documents
into mobile offline-first Web apps.

Oh, and before I forget: this *must* [RFC 2119] be made available over DNS:

```
dig powerdns.habbie.package.list TXT

; ANSWER
powerdns.habbie.package.list  ....... http://
```


