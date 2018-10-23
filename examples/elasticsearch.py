
def run_eslib():
    """https://elasticsearch-py.readthedocs.io/en/master/
    """
    import json
    from elasticsearch import Elasticsearch
    es = Elasticsearch("http://localhost:9200")
    d = es.search(index="test", body={"query": {"term":{"data.projectName":"joyw_test"}}})
    print json.dumps(d, indent=2)
    d = es.get(index="test", doc_type="data", id="AV95-WBslQj3kRu9ZCbP")
    print json.dumps(d, indent=2)

def run_requests():
    import json
    import requests
    url = "http://localhost:9200"
    # https://www.elastic.co/guide/en/elasticsearch/reference/2.4/docs-index_.html
    r = requests.get(url+"/test/data/AV95-WBslQj3kRu9ZCbP/_source")
    print json.dumps(r.json, indent=2)    
    # https://www.elastic.co/guide/en/elasticsearch/reference/2.4/search-uri-request.html
    r = requests.get(url+"/test/data/_search?q=data.projectName:joyw_test&size=1&sort=@timestamp:desc")
    print json.dumps(r.json, indent=2)
    data = {"type": "test", "msg": "hello elasticsearch"}
    r = requests.post(url+"/pba/promote/", data=json.dumps(data3))
    print r.status_code
    print r.status_code == requests.codes.created

    
if __name__=="__main__":
    run_eslib()
    run_requests()