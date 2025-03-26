from unittest.mock import patch


def test_create_todo(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.post(
            "/api/v1/todos",
            json={"title": "test_todo", "description": "test description"},
            headers={"Authorization": f"Bearer {get_token}"},
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["title"] == "test_todo"
        assert data["description"] == "test description"
        assert "id" in data


def test_get_todo(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.get(
            "/api/v1/todos/1", headers={"Authorization": f"Bearer {get_token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["title"] == "test_todo"
        assert "id" in data


def test_get_todo_not_found(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.get(
            "/api/v1/todos/2", headers={"Authorization": f"Bearer {get_token}"}
        )
        assert response.status_code == 404, response.text
        data = response.json()
        assert data["detail"] == "Todo not found"


def test_get_todos(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.get("/api/v1/todos", headers={"Authorization": f"Bearer {get_token}"})
        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)
        assert data[0]["title"] == "test_todo"
        assert "id" in data[0]


def test_update_todo(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.put(
            "/api/v1/todos/1",
            json={"title": "new_test_todo", "description": "new description"},
            headers={"Authorization": f"Bearer {get_token}"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["title"] == "new_test_todo"
        assert data["description"] == "new description"
        assert "id" in data


def test_update_todo_not_found(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.put(
            "/api/v1/todos/2",
            json={"title": "new_test_todo"},
            headers={"Authorization": f"Bearer {get_token}"},
        )
        assert response.status_code == 404, response.text
        data = response.json()
        assert data["detail"] == "Todo not found"


def test_delete_todo(client, get_token):
    with patch("src.services.auth.redis_client") as redis_mock:
        redis_mock.exists.return_value = False
        response = client.delete(
            "/api/v1/todos/1", headers={"Authorization": f"Bearer {get_token}"}
        )
        assert response.status_code == 204, response.text
