from owlready2 import *
from contextlib import suppress

onto_path.append("/oe-ontology")


onto = get_ontology("https://raw.githubusercontent.com/TRADOC-G2/oe-ontology/master/OEOntology.owl").load()

print("Classes are loading!")

classes = list(onto.classes())
print(classes)