Maybe you want to use a SKOS vocabulary as a JSON dictionary, where the key 
is a skos:notation and the value is the skos:prefLabel. For example the
[MARC Relators](http://id.loc.gov/vocabulary/relators.html) from the
Library of Congress. skosdict is a simple tool tool that does that for you.
    ./skosdict.py http://id.loc.gov/vocabulary/relators.rdf
    
    {
      "scl": "Sculptor", 
      "cot": "Contestant-appellant", 
      "ivr": "Interviewer", 
      "pth": "Patent holder", 
      "uvp": "University place", 
      "lso": "Licensor", 
      "drm": "Draftsman", 
      "rth": "Research team head", 
      "pta": "Patent applicant", 
      "dln": "Delineator", 
      "ldr": "Laboratory director", 
      "mfr": "Manufacturer", 
      "lse": "Licensee", 
      "tch": "Teacher", 
      "dbp": "Distribution place", 
      "tcd": "Technical director", 
      "ptt": "Plaintiff-appellant", 
      "itr": "Instrumentalist", 
      "scr": "Scribe", 
      "cll": "Calligrapher", 
      "mrb": "Marbler"
      ...
    }

Some examples are included in the examples sub-directory, as well as an
update.py file to pull them down. If you know of a SKOS file that would be worth
adding please add it :-)
