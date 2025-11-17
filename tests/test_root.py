"""
Tests for the root endpoint
"""
import pytest


def test_root_redirect(client):
    """Test that root endpoint redirects to static index"""
    response = client.get("/", follow_redirects=False)
    
    assert response.status_code == 307
    assert "/static/index.html" in response.headers["location"]


def test_root_follow_redirect(client):
    """Test that root endpoint can be followed to index.html"""
    response = client.get("/", follow_redirects=True)
    
    # Should get a 200 if the static file is served
    assert response.status_code == 200
