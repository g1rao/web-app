import pytest
from app import app

# Fixture to initialize the app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test cases
def test_get_user_gists_default(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'octocat' in response.data  # Check if default user 'octocat' is present in response

def test_get_user_gists_specific_user(client):
    response = client.get('/octocat')
    assert response.status_code == 200
    assert b'octocat' in response.data  # Check if the specified username is present in response

def test_invalid_route(client):
    response = client.get('/invalid_route')
    assert response.status_code == 404  # Ensure that accessing an invalid route returns a 404 error
