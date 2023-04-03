from pylode import OntDoc


vocabs = ["attribute","code","measure"]

for name in vocabs:
    # initialise
    od = OntDoc(ontology=f'../vocab/dbc-{name}.ttl')

    # or save HTML to a file
    od.make_html(destination=f'../docs/dbc-{name}.html')