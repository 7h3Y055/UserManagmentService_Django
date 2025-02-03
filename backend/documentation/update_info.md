* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/update-profile/`
Endpoint to update information

#### Method: `PATCH`

#### Request:
* **URL:** `/account/update-profile/`
* **BODY:**
```json
{
  "id": 2,
  "username": "ybouchma",
  "first_name": "Youssef",
  "last_name": "Bouchmama",
  "bio": "blabla",
  "avatar_url": "http://localhost:8000/profile_images/default.jpeg",
  "two_FA": false,
  "status": "ON",
  "created_at": "2025-02-02T14:40:12.882146Z"
}
```

#### Response:
* **Success:**
```json
{
  "id": 2,
  "username": "ybouchma",
  "first_name": "Youssef",
  "last_name": "Bouchmama",
  "bio": "blabla",
  "avatar_url": "http://localhost:8000/profile_images/default.jpeg",
  "two_FA": false,
  "status": "ON",
  "created_at": "2025-02-02T14:40:12.882146Z"
}
```

* **Error:**
```json
{
    "first_name": "a"
}
=>
{
    "first_name": [
        "First name too short"
    ]
}
```

#### HTTP Codes

| Code | Description                              |
|------|------------------------------------------|
| 200  | User information updated successfully    |
| 400  | Bad request                              |
