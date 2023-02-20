from fastapi.testclient import TestClient
from time import sleep
from . import main
import json

client = TestClient(main.app)

def test_read_main():
    response = client.get("/facebook")    
    sleep(5)
    data = json.loads(response.text)
    assert response.status_code == 200
    assert len(data.keys())== 8