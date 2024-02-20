from src.main import app

STATUS_OK = 200
CREATED = 201
NO_CONTENT = 204
NOT_FOUND = 404


def test_get_users_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/users")
    assert actual.status_code == STATUS_OK


def test_get_user_by_id_endpoint() -> None:
    client = app.test_client()

    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}

    create_response = client.post("/users", json=user_data)
    created_user_id = create_response.json.get("id")

    actual = client.get(f"/users/{created_user_id}")
    assert actual.status_code == STATUS_OK


def test_post_users_endpoint() -> None:
    client = app.test_client()

    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}

    actual = client.post("/users", json=user_data)
    assert actual.status_code == CREATED


def test_patch_users_endpoint() -> None:
    client = app.test_client()

    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}

    create_response = client.post("/users", json=user_data)
    created_user_id = create_response.json.get("id")

    actual = client.patch(f"/users/{created_user_id}", json=user_data)
    assert actual.status_code == STATUS_OK


def test_delete_user_endpoint() -> None:
    client = app.test_client()

    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}

    create_response = client.post("/users", json=user_data)
    created_user_id = create_response.json.get("id")

    actual = client.delete(f"/users/{created_user_id}")
    assert actual.status_code == NO_CONTENT
