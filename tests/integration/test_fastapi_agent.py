import time
import random
from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_chat_addition():
    time.sleep(random.randint(25, 30))
    response = client.post("/chat", json={"query": "What is 5 + 3?"})
    assert response.status_code == 200
    assert "8" in response.json()["response"]

def test_chat_subtraction():
    time.sleep(random.randint(25, 30))
    response = client.post("/chat", json={"query": "What is 10 - 4?"})
    assert response.status_code == 200
    assert "6" in response.json()["response"]

def test_chat_invalid_operation():
    time.sleep(random.randint(25, 30))
    response = client.post("/chat", json={"query": "What is 5 multiplied by 3?"})
    assert response.status_code == 200
    assert "I can only perform addition and subtraction" in response.json()["response"]

def test_chat_invalid_input():
    time.sleep(random.randint(25, 30))
    response = client.post("/chat", json={"query": "Add 'hello' and 3."})
    assert response.status_code == 200
    assert "cannot add" in response.json()["response"] and ("numerical values" in response.json()["response"] or "numbers" in response.json()["response"])
