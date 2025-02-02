* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/logout/`
Endpoint for logging out the current user.

#### Method: `POST`
Used for logout.

#### Request:
* **URL:** `/account/logout/`
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
            "message": "Logged out successfully"
    }
    ```
* **Error:**
    ```json
    {
            "error": "error description"
    }
    ```

#### HTTP Codes

| Code | Description                |
|------|----------------------------|
| 200  | Logged out successfully    |
| 400  | Error case                 |

