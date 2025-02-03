* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/whoami/`
Endpoint for retrieving information about the currently authenticated user.

#### Method: `GET`
Used to retrieve user information.

#### Request:
* **URL:** `/account/whoami/`

#### Response:
* **Success:**
```json
{
    "id": 1,
    "username": "ybouchma",
    "first_name": "Youssef",
    "last_name": "Bouchmama",
    "bio": "blabla",
    "avatar_url": "http://localhost:8000/profile_images/ybouchma.jpg",
    "status": "ON",
    "created_at": "2025-02-03T08:49:17.271769Z"
}
```

#### HTTP Codes

| Code | Description                |
|------|----------------------------|
| 200  | User information retrieved successfully |



