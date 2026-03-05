
"""
Este é um exemplo de arquivo Python para documentação com PyloDe.
Ele inclui imports do PyloDe.
"""

from pylode import OntDoc


vocabs = ["attribute","code","measure"]

for name in vocabs:
    # initialise
    od = OntDoc(ontology=f'../vocab/dbc-{name}.ttl')

    # or save HTML to a file
    od.make_html(destination=f'../docs/{name}/index.html')


od = OntDoc(ontology='../vocab/dbcells.ttl')

od.make_html(destination=f'../docs/index.html')

