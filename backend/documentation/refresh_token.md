* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/login/refresh/`
Endpoint for refreshing the access token using 42/Google authentication.

#### Method: `POST`
Used to refresh the access token.

#### Request:
* **URL:** `/account/login/refresh/`
* **Body:**
```json
{
    "refresh": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"
}
```

#### Response:
* **Success:**
```json
{
    "access": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9",
    "refresh": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
* **Error:**
```json
{
    "detail": "reason why is not valid",
    "code": "token_not_valid"
}
```
* **Validation Error:**
```json
{
  "refresh": [
    "This field is required."
  ]
}
```

#### HTTP Codes

| Code | Description                |
|------|----------------------------|
| 200  | Token refreshed successfully |
| 400  | Error in request            |



