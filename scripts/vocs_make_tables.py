from rdflib import Graph

g = Graph().parse("../vocabularies/addrcm-req.ttl")

q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT *
    WHERE {
        ?c a skos:Concept ;
            skos:notation ?n ;
            skos:prefLabel ?pl ;
            skos:definition ?d ;
        .           
    }
    ORDER BY ?n
    """

print('[cols="1,4,10"]')
print("|===")
print("| ID | Label | Definition")
print("")
for r in g.query(q):
    print(f'| {r["n"]} | {r["c"]}[{r["pl"]}] | {r["d"]}')
print("|===")