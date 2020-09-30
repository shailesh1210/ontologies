from owlready2 import *
from contextlib import suppress

onto_path.append("/oe-ontology")


onto = get_ontology("https://raw.githubusercontent.com/shailesh1210/ontologies/master/oe-onto/OEOntology.owl").load()

print("Classes are loading!")

classes = list(onto.classes())
print(classes)