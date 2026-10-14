from app import app


def test_hoteis_endpoint_returns_list():
    client = app.test_client()

    response = client.get('/hoteis')

    assert response.status_code == 200
    assert response.is_json
    payload = response.get_json()
    assert 'hoteis' in payload
    assert isinstance(payload['hoteis'], list)
    assert len(payload['hoteis']) > 0
