import pytest

from fastapi.testclient import TestClient

from api.app import app
from api.db import get_db_session
from api.models import User

client = TestClient(app)


@pytest.fixture(scope="module")
def testdb():
    db = get_db_session()
    return db


@pytest.fixture()
def single_user(testdb):
    user = User(name="Ziutek")
    testdb.add(user)
    testdb.commit()
    yield user
    testdb.delete(user)
    testdb.commit()


def test_get_users(single_user):
    response = client.get("/users")

    assert response.status_code == 200
    response_payload = response.json()

    assert len(response_payload) == 1
    assert response_payload[0]['name'] == "Ziutek"
