from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_chat_addition():
    response = client.post("/chat", json={"query": "What is 5 + 3?"})
    assert response.status_code == 200
    assert response.json() == {"response": "The sum of 5 and 3 is 8."}

def test_chat_subtraction():
    response = client.post("/chat", json={"query": "What is 10 - 4?"})
    assert response.status_code == 200
    assert response.json() == {"response": "The difference between 10 and 4 is 6."}

def test_chat_invalid_operation():
    response = client.post("/chat", json={"query": "What is 5 multiplied by 3?"})
    assert response.status_code == 200
    assert "Multiplication is not supported" in response.json()["response"]

def test_chat_invalid_input():
    response = client.post("/chat", json={"query": "Add 'hello' and 3."})
    assert response.status_code == 200
    assert "inputs must be numbers" in response.json()["response"]
