
import sys
import requests

def query(q, endpoint="https://query.wikidata.org/sparql", f='application/json'):
    try:
        params = {'query': q}
        print(q)
        resp = requests.get(endpoint, params=params, headers={'Accept': f})
        bindings = resp.json()["results"]["bindings"]
        return [{k:d["value"] for (k, d) in item.items()} for item in bindings] 
    except Exception as e:
        print("Error running query:", q)
        print("Response:", resp.text)
        print(e)
        raise
