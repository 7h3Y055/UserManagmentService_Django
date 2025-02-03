* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

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
            "bio": "blabla",
            "avatar_url": "http://localhost:8000/profile_images/default.jpeg",
            "status": "ON",
            "created_at": "2025-02-02T14:40:12.882146Z"
        },
        {
            "id": 3,
            "username": "7h3_Yosef",
            "first_name": "7h3",
            "last_name": "Yosef",
            "bio": "blabla",
            "avatar_url": "http://localhost:8000/profile_images/7h3_Yosef.png",
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

