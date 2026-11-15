
from app import app

client = app.test_client()



def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert b"DeployX" in response.data
    assert b"Ship software." in response.data
    assert b"Application overview" in response.data
    assert b"Pipeline" in response.data
    assert b"Application endpoints" in response.data

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_info():
    response = client.get("/api/info")
    body = response.get_json()

    assert body["app"] == "cicd-demo"
    assert "version" in body
    assert "commit" in body


def test_echo_ok():
    response = client.post(
        "/api/echo",
        json={"name": "test"}
    )

    assert response.status_code == 201
    assert response.get_json() == {
        "received": {"name": "test"}
    }


def test_echo_bad_body():
    response = client.post(
        "/api/echo",
        data="not json"
    )

    assert response.status_code == 400


def test_unknown_path():
    response = client.get("/nope")
    assert response.status_code == 404
