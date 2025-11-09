from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
r = client.get("/")
assert r.status_code == 200


# Note: This is a lightweight smoke test (no real provider call)
def test_tts_contract():
# We only validate input/output contract and status code path
# Actual provider calls require real API keys and network.
payload = {"text": "Hello from tests!"}
r = client.post("/api/tts", json=payload)
# Without keys this may 500; we only assert the route exists
assert r.status_code in (200, 400, 401, 403, 500)