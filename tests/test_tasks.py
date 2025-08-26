from fastapi import status


def test_create_task(client, test_task_data):
    """Test creating a new task"""
    response = client.post("/tasks/", json=test_task_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == test_task_data["title"]
    assert data["description"] == test_task_data["description"]
    assert data["completed"] == False
    assert "id" in data
    assert "created_at" in data


def test_read_tasks(client, test_task_data):
    """Test reading all tasks"""
    # First, create a task
    client.post("/tasks/", json=test_task_data)

    response = client.get("/tasks/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == test_task_data["title"]


def test_read_task(client, test_task_data):
    """Test reading a single task"""
    create_response = client.post("/tasks/", json=test_task_data)
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == test_task_data["title"]


def test_update_task(client, test_task_data):
    """Test updating a task"""
    create_response = client.post("/tasks/", json=test_task_data)
    task_id = create_response.json()["id"]

    update_data = {"title": "Updated Task", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["completed"] == True


def test_delete_task(client, test_task_data):
    """Test deleting a task"""
    create_response = client.post("/tasks/", json=test_task_data)
    task_id = create_response.json()["id"]

    # Delete the task - should return 204 No Content
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check that the task is deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_task_validation(client):
    """Test task validation"""
    # Empty title
    response = client.post("/tasks/", json={"title": "   "})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Title is too long
    long_title = "a" * 201
    response = client.post("/tasks/", json={"title": long_title})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
