def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Item API"}

def test_create_item(client):
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "This is a test item", "price": 9.99}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert data["price"] == 9.99
    assert "id" in data
    return data["id"]

def test_read_item(client):
    # First create an item
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "This is a test item", "price": 9.99}
    )
    item_id = response.json()["id"]
    
    # Then test reading it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["id"] == item_id

def test_read_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404

def test_read_items(client):
    # Create a few items first
    client.post(
        "/items/",
        json={"name": "Item 1", "description": "First test item", "price": 9.99}
    )
    client.post(
        "/items/",
        json={"name": "Item 2", "description": "Second test item", "price": 19.99}
    )
    
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2  # At least the two items we just created

def test_update_item(client):
    # Create item first
    response = client.post(
        "/items/",
        json={"name": "Original Item", "description": "This needs updating", "price": 9.99}
    )
    item_id = response.json()["id"]
    
    # Update the item
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Item", "description": "This is updated", "price": 19.99}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item"
    assert data["description"] == "This is updated"
    assert data["price"] == 19.99
    assert data["id"] == item_id

def test_update_item_not_found(client):
    response = client.put(
        "/items/999",
        json={"name": "Not Found Item", "description": "This won't be found", "price": 0.0}
    )
    assert response.status_code == 404

def test_delete_item(client):
    # Create item first
    response = client.post(
        "/items/",
        json={"name": "Item to Delete", "description": "This will be deleted", "price": 9.99}
    )
    item_id = response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}
    
    # Verify it's gone
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404

def test_delete_item_not_found(client):
    response = client.delete("/items/999")
    assert response.status_code == 404