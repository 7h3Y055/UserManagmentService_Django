* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/users/`
Get top 'n' users sorted by 'sort'

#### Method: `GET`

#### Request:
* **URL:** `/account/users/`
* **Parameters:**
  * `n` - Number of users
  * `sort` - Type of sorting {'newest', 'oldest'}

#### Response:
* **Success:**
```json
[
    {
        "id": 2,
        "username": "7h3_Yosef",
        "first_name": "7h3",
        "last_name": "Yosef",
        "bio": "blabla",
        "avatar_url": "http://localhost:8000/profile_images/7h3_Yosef.png",
        "two_FA": false,
        "status": "ON",
        "created_at": "2025-02-03T08:13:03.854518Z"
    },
    {
        "id": 1,
        "username": "ybouchmama",
        "first_name": "123545",
        "last_name": "Bouchmama",
        "bio": "blabla",
        "avatar_url": "http://localhost:8000/profile_images/ybouchma.jpg",
        "two_FA": false,
        "status": "ON",
        "created_at": "2025-02-03T07:27:50.874484Z"
    }
]
```

* **Error:**
```json
{
    "error": "reason"
}
```
```json
{
    "error": "sort must be either ['newest', 'oldest']"
}
```

#### HTTP Codes

| Code | Description                              |
|------|------------------------------------------|
| 200  | Success                                  |
| 400  | Bad request                              |
