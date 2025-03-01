import pytest
from rest_framework.test import APIClient
from tasks.models import Task


# Create your tests here.
@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_task():
    def _create_task(title: str, completed: bool = False):
        return Task.objects.create(title=title, completed=completed)

    return _create_task


@pytest.mark.django_db
def test_get_tasks(api_client, create_task):
    create_task("Task 1")
    create_task("Task 2")
    response = api_client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 2

