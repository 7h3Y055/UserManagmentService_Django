
### `/account/login/{PROVIDER}/`
Endpoint for logging in with 42/Google authentication.

#### Method: `GET`
Used for login requests.

#### Request:
* `/account/login/42/`
* `/account/login/google/`

#### Response:
```json
{
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9",
    "refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
or in case of an error:
```json
{
    "error": "error",
    "error_description": "error description"
}
```

#### HTTP Codes

| Code | Description                |
|------|----------------------------|
| 201  | Problem from the provider  |

