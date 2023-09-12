# NeoFIChat

## Local Server Setup

To set up the NeoFIChat project locally, follow these steps:

1. Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv/Scripts/activate.bat
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Docker and Redis

Ensure that Docker is installed, and the Redis Docker image is available.

You can start a Redis container using the following command:

```bash
docker run --rm -p 6379:6379 redis:7
```

## Steps to run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



## NEOFI CHAT APP


## 1.Friends Recommendation: Endpoint: GET  /api/suggested-friends/<user_id>
```bash
  Functionality: Allows to send a GET request to the application with a user_id and it should return the top 5 recommended friends for that user. 

This api returns the top 5 friends using Jacard Indexing .
Jaccard Index Calculation: To find the similarity between two users, you calculate the Jaccard Index between their interest sets. The Jaccard Index is defined as:
J(A, B) = (|A ∩ B|) / (|A ∪ B|)
Where:
A and B are sets of interests of two users.
|A ∩ B| is the size of the intersection of the sets (i.e., the number of common interests).
|A ∪ B| is the size of the union of the sets (i.e., the total number of unique interests from both users).
The Jaccard Index ranges from 0 to 1, where 0 means no similarity, and 1 means the sets are identical.
```
![image](https://github.com/raaz252/NeoFIChat/assets/63297432/14eec1cc-4bc2-4fdc-bac6-340b3354fa43)



## 2.	User Login: Endpoint: POST /api/login/
```bash
    Functionality: Allows users to log in to their account by providing their credentials (username/email and password).
  Output:  If the login is successful, return an authentication token or a success message with the user details.

```
![image](https://github.com/raaz252/NeoFIChat/assets/63297432/98199ac9-6dad-4715-9647-0f0cccf0a0bf)



## 3.	Get Online Users: Endpoint: GET /api/online-users/
 ```bash
   Functionality: Retrieves a list of all online users who are currently available for chat.
Note: Every user comes online when he's logged in. The user can be classified as offline when either he triggers logout himself, or due to the authentication token expiry caused by the user's inaction for the token expiry time.
    Output:
        Returns a list of online user objects with their details, such as username and status.
```
![image](https://github.com/raaz252/NeoFIChat/assets/63297432/35260e6a-ea8d-45d7-8900-a27a49dc9b65)

 

## 4.Send a Message: Endpoint: WEBSOCKET /api/chat/send/
 ```bash
   Functionality: Allows a user to send and receive instant messages to another user who is online.
        Output:
            If the recipient is online and available, send the message to the recipient in JSON and return a success message or status code.
            If the recipient is offline or unavailable, return an error message or status code.
```
![image](https://github.com/raaz252/NeoFIChat/assets/63297432/1bcdf7cc-0674-4252-b66c-d14334806cb3)
 

