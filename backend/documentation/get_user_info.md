
### `/account/{user_id}`
Endpoint to get information of a user by their ID.

#### Method: `GET`

#### Request:
* **URL:** `/account/{user_id}`

#### Response:
* **Success:**
```json
{
  "id": 3,
  "username": "7h3_Yosef",
  "first_name": "7h3",
  "last_name": "Yosef",
  "avatar_url": "http://localhost:8000/profile_images/7h3_Yosef.png",
  "two_FA": false,
  "status": "ON",
  "created_at": "2025-02-02T14:56:27.811185Z"
}
```

* **Error:**
```json
{
  "error": "user not found"
}
```

#### HTTP Codes

| Code | Description                              |
|------|------------------------------------------|
| 200  | User information retrieved successfully  |
| 404  | User not found                           |

