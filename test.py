#!/usr/bin/env python

import unittest

import skosdict

class SimpleTest(unittest.TestCase):

    def test_dict(self):
        d = skosdict.skosdict("http://id.loc.gov/vocabulary/relators.rdf")

    def test_json(self):
        j = skosdict.skosjson("http://id.loc.gov/vocabulary/relators.rdf")

if __name__ == "__main__":
    unittest.main()
