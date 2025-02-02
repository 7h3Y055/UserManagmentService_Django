
### `/account/search/`
Endpoint to get all users matching the keyword (can search by username, first name, or last name).

#### Method: `GET`

#### Request:
* **URL:** `/account/search/`
* **Parameters:**
  * `q` - keyword
  * `limit` - optional (default 10)
  * `offset` - optional (default 0)

#### Response:
* **Success:**
```json
{
    "result": [
        {
            "id": 2,
            "username": "ybouchma",
            "first_name": "Youssef",
            "last_name": "Bouchmama",
            "avatar_url": "http://localhost:8000/profile_images/default.jpeg",
            "two_FA": false,
            "status": "ON",
            "created_at": "2025-02-02T14:40:12.882146Z"
        },
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
    ]
}
```

* **Error:**
```json
{
  "error": "Invalid parameters",
  "details": "Please provide a valid 'q'"
}
```
* **Error:**
```json
{
  "error": "Invalid value in 'limit' and/or 'offset'"
}
```

#### HTTP Codes

| Code | Description                              |
|------|------------------------------------------|
| 200  | User information retrieved successfully  |

