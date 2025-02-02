* **[MAIN](https://github.com/7h3Y055/ft_transcendence/blob/main/backend/documentation/main.md)**

### `/account/avatar/`
Endpoint for uploading and removing avatars (set to default).

#### Method: `POST`
Upload a new avatar
* Accepted types: `.jpg`, `.png`, `.gif`, `.webp`

#### Request:
* **URL:** `/account/avatar/`
* **BODY:** 
  ```
  avatar
  ```

#### Response:
* **Success:**
  * avatar url in `Location` header
* **Error:**
  ```json
  {
    "error": "error description"
  }
  ```

#### Method: `DELETE`
Delete avatar (use default avatar).

#### Request:
* **URL:** `/account/avatar/`
* **BODY:** *None*

#### Response:
* **Success:**
  * *None*
* **Error:**
  ```json
  {
    "error": "error description"
  }
  ```

#### HTTP Codes

| Code | Description          |
|------|----------------------|
| 201  | Uploaded successfully|
| 204  | Removed successfully |

