"""
Pytest configuration and fixtures for FastAPI tests
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture to provide a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Fixture to reset activities to initial state before each test"""
    from src.app import activities
    
    # Store original state
    original_state = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Club": {
            "description": "Practice drills, scrimmages, and local matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Team practices and inter-school competitions",
            "schedule": "Mondays, Wednesdays, 4:30 PM - 6:30 PM",
            "max_participants": 15,
            "participants": ["ava@mergington.edu", "isabella@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and mixed media projects",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu", "charlotte@mergington.edu"]
        },
        "Drama Club": {
            "description": "Acting exercises, scene work, and school productions",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["sophia@mergington.edu", "jack@mergington.edu"]
        },
        "Debate Team": {
            "description": "Learn formal debate formats and compete in tournaments",
            "schedule": "Mondays, 3:45 PM - 5:15 PM",
            "max_participants": 20,
            "participants": ["oliver@mergington.edu", "amelia@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Prepare for hands-on science and engineering competitions",
            "schedule": "Fridays, 3:30 PM - 5:30 PM",
            "max_participants": 24,
            "participants": ["ethan@mergington.edu", "harper@mergington.edu"]
        }
    }
    
    # Clear and reset
    activities.clear()
    activities.update(original_state)
    
    yield
    
    # Cleanup - reset to original state after test
    activities.clear()
    activities.update(original_state)
