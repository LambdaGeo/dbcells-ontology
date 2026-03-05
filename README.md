# DBCells Vocabulary

A lightweight RDF/RDFS vocabulary for publishing, reusing and integrating data from land use and land cover change models as linked data.

This vocabulary is part of the [DBCells](https://github.com/LambdaGeo) project, which proposes a methodology for reproducible spatial dynamic models based on the linked data paradigm.

---

## Canonical URI

```
https://purl.org/linked-data/dbcells
```

> ⚠️ The code examples in the paper published at V Simpósio REACT (2025) contain incorrect URIs using `http://www.purl.org/...`. The correct base is always `https://purl.org/...` (no `www`, HTTPS).

---

## Modules

The vocabulary is split into four modules, each with its own PURL and documentation page:

| Module | PURL | Documentation | Description |
|---|---|---|---|
| Root | [/dbcells](https://purl.org/linked-data/dbcells) | [HTML](https://lambdageo.github.io/dbcells-ontology) | `Cell` class and core properties |
| Measures | [/dbcells/measure](https://purl.org/linked-data/dbcells/measure) | [HTML](https://lambdageo.github.io/dbcells-ontology/measure) | Spatial aggregation operations |
| Attributes | [/dbcells/attribute](https://purl.org/linked-data/dbcells/attribute) | [HTML](https://lambdageo.github.io/dbcells-ontology/attribute) | Metadata qualifying observations |
| Code lists | [/dbcells/code](https://purl.org/linked-data/dbcells/code) | [HTML](https://lambdageo.github.io/dbcells-ontology/code) | Geographic features and land cover classes |

---

## Design

The vocabulary is built on top of the [RDF Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/) (W3C recommendation) and organises data into three components:

- **Dimensions** — identify each observation in space and time, reusing `sdmx:refArea` and `sdmx:refPeriod` from the [SDMX vocabulary](https://sdmx.org/)
- **Measures** — represent the spatial aggregation operation applied to the data (e.g. mean, distance, percentage)
- **Attributes** — qualify each observation by linking it to the geographic feature, source file and script used to compute it

The key design decision is to **separate the measure from what is being measured**. For example, "mean of forest cover" is modelled as:
- measure: `dbc-m:mean`
- attribute: `dbc-a:feature` → `dbc-c:landcover-veg`

This allows measures to be reused across different models while attributes carry the domain-specific meaning.

---

## Quick start

```turtle
@prefix qb:       <http://purl.org/linked-data/cube#> .
@prefix sdmx-dim: <http://purl.org/linked-data/sdmx/2009/dimension#> .
@prefix dcterms:  <http://purl.org/dc/terms/> .
@prefix xsd:      <http://www.w3.org/2001/XMLSchema#> .
@prefix dbc-m:    <https://purl.org/linked-data/dbcells/measure#> .
@prefix dbc-a:    <https://purl.org/linked-data/dbcells/attribute#> .
@prefix dbc-c:    <https://purl.org/linked-data/dbcells/code#> .
@prefix cells:    <https://purl.org/linked-data/dbcells/epsg4326#> .
@prefix ds:       <https://purl.org/dbcells/dataset#> .
@prefix obs:      <https://purl.org/dbcells/observation#> .

# Dataset — groups common metadata for a set of observations
ds:forest-cover-2010
    a                   qb:DataSet ;
    dcterms:title       "Forest vegetation cover — Brazil 2010"@en ;
    sdmx-dim:refPeriod  "2010"^^xsd:gYear ;
    dbc-a:feature       dbc-c:landcover-veg ;
    dbc-a:sourceFile    <https://github.com/LambdaGeo/brlucc-database/raw/main/data/mapbiomas_2010.tif> ;
    dbc-a:scriptFile    <https://github.com/LambdaGeo/brlucc-database/blob/main/scripts/fill_forest_percentage.lua> .

# Observation
obs:forest-cover-001
    a                   qb:Observation ;
    qb:dataSet          ds:forest-cover-2010 ;
    sdmx-dim:refArea    cells:R0_0830Cx-46_4583Cy-23_8881 ;
    dbc-m:percentage    87.3 .
```

See [`examples/example.ttl`](examples/example.ttl) for a complete example with multiple datasets, observations and a SPARQL query.

---

## Repository structure

```
.
├── vocab/
│   ├── dbcells.ttl          # root — Cell class and core properties
│   ├── dbc-measure.ttl      # measure properties
│   ├── dbc-attribute.ttl    # attribute properties
│   └── dbc-code.ttl         # code lists
├── examples/
│   └── example.ttl          # usage example
├── scripts/
│   ├── gendoc.py            # generates docs/ using pyLODE
│   ├── Pipfile
│   └── Pipfile.lock
├── docs/                    # auto-generated — do not edit manually
└── archive/                 # legacy files — do not use
```

---

## Generating documentation

Documentation is generated automatically via [pyLODE](https://github.com/RDFLib/pyLODE) on every push to `main` using GitHub Actions. The generated HTML pages are published via GitHub Pages at:

```
https://lambdageo.github.io/dbcells-ontology/
```

To regenerate locally:

```bash
cd scripts/
pipenv install
pipenv run python gendoc.py
```

---

## Published data

Data from land use and land cover models published using this vocabulary is available at:

| Dataset | URL |
|---|---|
| Land cover — Brazil | https://data.world/lambdageo/luccmebrlanduse |
| Drivers (distance features) | https://data.world/lambdageo/luccmebrdrivers |
| DBCells cell repository | https://data.world/dbcells/dbcells |

---

## Related projects

- [DBCells server](https://dbcells-fuseki-production.up.railway.app/) — linked data server for cell geometries
- [brlucc-database](https://github.com/LambdaGeo/brlucc-database) — raw data and scripts for the Brazil LUCC model
- [QGISSPARQL](https://github.com/LambdaGeo/qgisparql-triple2layer) — QGIS plugins for importing and exporting linked data

---

## License

This vocabulary is published under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

---

## Citation

If you use this vocabulary in your work, please cite:

> Santos Junior, N. J.; Silva, C. D. S.; Sousa, F. M.; Bezerra, D. S.; Costa, S. S. **Publishing and Reusing Land Use and Land Cover Data through RDF Data Cube**. V Simpósio REACT, 2025.