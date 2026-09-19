"""
Validates all Turtle files in vocab/ and examples/:

  1. Syntax — every file must parse as valid Turtle (rdflib.Graph.parse).
  2. Sanity check — dbc:row and dbc:col are defined as grid indices
     (xsd:integer, counted from the origin), not geographic coordinates.
     This check catches values that look like decimal-degree longitude/
     latitude (e.g. "-46.4583") being used where an integer index is
     expected, which is the class of error that slipped into an earlier
     revision of examples/example.ttl.

Exits with a non-zero status (failing the CI job) if any file fails to
parse or any dbc:row / dbc:col value is not a plain integer.
"""

import sys
from pathlib import Path

from rdflib import Graph, Namespace, URIRef

BASE = Path(__file__).resolve().parent.parent
DBC = Namespace("https://purl.org/linked-data/dbcells#")

GRID_INDEX_PROPERTIES = [DBC.row, DBC.col]


def find_ttl_files():
    files = []
    for folder in ("vocab", "examples"):
        files.extend(sorted((BASE / folder).glob("*.ttl")))
    return files


def check_syntax(path: Path) -> Graph:
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


def check_grid_indices(path: Path, g: Graph) -> list:
    errors = []
    for prop in GRID_INDEX_PROPERTIES:
        for s, p, o in g.triples((None, prop, None)):
            lexical = str(o)
            try:
                # Must round-trip as a base-10 integer with no fractional part.
                if lexical != str(int(lexical)):
                    raise ValueError
            except ValueError:
                errors.append(
                    f"{path.name}: {s} {p} \"{lexical}\" is not a valid "
                    f"integer grid index (dbc:row/dbc:col must be xsd:integer, "
                    f"not a decimal-degree coordinate)."
                )
    return errors


def main() -> int:
    files = find_ttl_files()
    if not files:
        print("⚠️  No .ttl files found under vocab/ or examples/.")
        return 1

    had_errors = False

    for path in files:
        try:
            g = check_syntax(path)
        except Exception as exc:
            print(f"❌ Syntax error in {path.relative_to(BASE)}: {exc}")
            had_errors = True
            continue

        print(f"✅ {path.relative_to(BASE)} — {len(g)} triples parsed OK")

        for error in check_grid_indices(path, g):
            print(f"❌ {error}")
            had_errors = True

    return 1 if had_errors else 0


if __name__ == "__main__":
    sys.exit(main())
