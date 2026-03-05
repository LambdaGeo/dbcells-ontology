"""
Generates HTML documentation for the DBCells vocabulary using pyLODE.
Run from the scripts/ directory.
"""

import os
from pylode import OntDoc

vocabs = ["attribute", "code", "measure"]

for name in vocabs:
    os.makedirs(f'../docs/{name}', exist_ok=True)
    od = OntDoc(ontology=f'../vocab/dbc-{name}.ttl')
    od.make_html(destination=f'../docs/{name}/index.html')
    print(f'Generated docs/{name}/index.html')

os.makedirs('../docs', exist_ok=True)
od = OntDoc(ontology='../vocab/dbcells.ttl')
od.make_html(destination='../docs/index.html')
print('Generated docs/index.html')