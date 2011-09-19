#!/usr/bin/env python

"""
Turn a SKOS RDF file into a dictionary, or chunk of JSON.

    skosdict.py http://id.loc.gov/vocabulary/relators.rdf
  
"""

import sys
import json

from rdflib import Graph, RDF, Namespace

skos = Namespace("http://www.w3.org/2004/02/skos/core#")

def skosdict(url, lang="en"):
    """
    Pass in a URL (can be a file protocol) for a SKOS file and get 
    back a dictionary of code => values.
    """
    graph = Graph()
    graph.parse(url)

    dictionary = {}
    for concept in graph.subjects(RDF.type, skos.Concept):

        # determine the code
        code = graph.value(concept, skos.notation)
        # hack for loc vocabularies that currenctly lack skos:notation
        if not code:
            code = concept.split("/")[-1]

        # get the preferred language label, there could be more than one
        labels = list(graph.objects(concept, skos.prefLabel))
        if len(labels) > 1:
            for label in labels: 
                if label.language == lang:
                    break
        else:
            label = labels[0]

        dictionary[code] = label
    return dictionary


def skosjson(url, lang="en"):
    return json.dumps(skosdict(url, lang), indent=2)


if __name__ == "__main__":
    url = sys.argv[1]
    print skosjson(url).encode('utf-8')
