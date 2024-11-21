import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.fixture
def asgi_client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://testserver")

@pytest.mark.asyncio
async def test_demo(asgi_client):
    async with asgi_client as client:
        response = await client.get("/auth/login")
    assert response.status_code == 200