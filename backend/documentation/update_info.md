* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/update-profile/`
Endpoint to update informations 

#### Method: `PATCH`

#### Request:
* **URL:** `/account/update-profile/`
* **BODY:**
``` json
{
  "id": 2,
  "username": "ybouchma",
  "first_name": "Youssef",
  "last_name": "Bouchmama",
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
  "avatar_url": "http://localhost:8000/profile_images/default.jpeg",
  "two_FA": false,
  "status": "ON",
  "created_at": "2025-02-02T14:40:12.882146Z"
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

