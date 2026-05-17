import pytest

async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

async def test_list_items(client):
    response = await client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)