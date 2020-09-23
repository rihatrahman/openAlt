''' TODO
# This prints a lot of information but importantly it has: 'author': [ and then all the authors and an ending brace ]
# Should be able to use regex or json to find the keywords 'given:' and 'family:'
# Then we can send that to our database for the associated DOI
'''
import re
import json
doi = '10.1016/j.ymthe.2019.04.002'

try:
    from crossref.restful import Works
    works = Works()
    print ("Working...")
    # Request data from the crossref API, save json as x
    x = works.doi(doi)
    if (x['author']):
        x = x['author']
        # Example of what the x (json object) now looks like:
        # [{'given': 'Tushar H.', 'family': 'Ganjawala', 'sequence': 'first', 'affiliation': []}, {'given': 'Qi', 'family': 'Lu', 'sequence': 'additional', 'affiliation': []}, {'given': 'Mitchell D.', 'family': 'Fenner', 'sequence': 'additional', 'affiliation': []}, {'given': 'Gary W.', 'family': 'Abrams', 'sequence': 'additional', 'affiliation': []}, {'given': 'Zhuo-Hua', 'family': 'Pan', 'sequence': 'additional', 'affiliation': []}]

        # need to find the pattern 'given': then grab what is inside the '', then repeat until no more 'given': sequences
        #authorList = re.findall("^[a-zA-Z0-9\s]+$", x)

except ImportError:
    print("You need to install the crossref api with 'pip install crossrefapi' first")
except:
    print("Unspecified error, exiting")