Have you ever wanted to use a SKOS vocabulary as a JSON dictionary, where the key 
is the familiar code (skos:notation) and the value is the human readable label (skos:prefLabel)?
Is the SKOS available in JSON, but instead of idiomatic JSON its 
[some unusable stew of URIs](http://dvcs.w3.org/hg/rdf/raw-file/default/rdf-json/index.html)? If you answered yes to either of these perhaps skosdict is for you.

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
adding please add it, and send a pull request.
