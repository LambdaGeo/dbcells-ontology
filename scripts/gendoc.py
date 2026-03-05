import os
from pathlib import Path
from pylode import OntDoc

# .resolve() garante o caminho absoluto real no sistema
BASE = Path(__file__).resolve().parent.parent
VOCAB = BASE / "vocab"
DOCS  = BASE / "docs"

vocabs = ["attribute", "code", "measure"]

print(f"Base path: {BASE}")

for name in vocabs:
    input_file = VOCAB / f"dbc-{name}.ttl"
    out_dir = DOCS / name
    
    if not input_file.exists():
        print(f"⚠️  Arquivo não encontrado: {input_file}")
        continue

    out_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Tente instanciar explicitamente
        od = OntDoc(ontology=str(input_file))
        od.make_html(destination=str(out_dir / "index.html"))
        print(f"✅ Gerado: docs/{name}/index.html")
    except Exception as e:
        print(f"❌ Erro ao processar {name}: {e}")

# Processo para o arquivo principal
main_vocab = VOCAB / "dbcells.ttl"
if main_vocab.exists():
    try:
        DOCS.mkdir(parents=True, exist_ok=True)
        od = OntDoc(ontology=str(main_vocab))
        od.make_html(destination=str(DOCS / "index.html"))
        print("✅ Gerado: docs/index.html")
    except Exception as e:
        print(f"❌ Erro no dbcells.ttl: {e}")