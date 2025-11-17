"""
Tests for the activities endpoints
"""
import pytest


def test_get_activities(client, reset_activities):
    """Test retrieving all activities"""
    response = client.get("/activities")
    
    assert response.status_code == 200
    data = response.json()
    
    # Check that we have activities
    assert len(data) > 0
    
    # Check that Chess Club exists with expected structure
    assert "Chess Club" in data
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_contains_expected_activities(client, reset_activities):
    """Test that all expected activities are present"""
    response = client.get("/activities")
    data = response.json()
    
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Club",
        "Basketball Team",
        "Art Club",
        "Drama Club",
        "Debate Team",
        "Science Olympiad"
    ]
    
    for activity in expected_activities:
        assert activity in data


def test_signup_for_activity_success(client, reset_activities):
    """Test successful signup for an activity"""
    response = client.post(
        "/activities/Chess%20Club/signup?email=newstudent@mergington.edu"
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Signed up" in data["message"]


def test_signup_adds_participant(client, reset_activities):
    """Test that signup actually adds the participant to the activity"""
    # Get initial participant count
    response = client.get("/activities")
    initial_count = len(response.json()["Chess Club"]["participants"])
    
    # Sign up
    client.post("/activities/Chess%20Club/signup?email=newstudent@mergington.edu")
    
    # Check participant was added
    response = client.get("/activities")
    final_count = len(response.json()["Chess Club"]["participants"])
    
    assert final_count == initial_count + 1
    assert "newstudent@mergington.edu" in response.json()["Chess Club"]["participants"]


def test_signup_for_nonexistent_activity(client, reset_activities):
    """Test signup for an activity that doesn't exist"""
    response = client.post(
        "/activities/NonExistent%20Activity/signup?email=newstudent@mergington.edu"
    )
    
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


def test_signup_already_registered(client, reset_activities):
    """Test signup for an activity the student is already registered for"""
    # Try to sign up with a student who is already registered
    response = client.post(
        "/activities/Chess%20Club/signup?email=michael@mergington.edu"
    )
    
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"].lower()


def test_signup_multiple_students(client, reset_activities):
    """Test multiple students signing up for the same activity"""
    students = [
        "student1@mergington.edu",
        "student2@mergington.edu",
        "student3@mergington.edu"
    ]
    
    for student in students:
        response = client.post(
            f"/activities/Programming%20Class/signup?email={student}"
        )
        assert response.status_code == 200
    
    # Verify all were added
    response = client.get("/activities")
    participants = response.json()["Programming Class"]["participants"]
    
    for student in students:
        assert student in participants
