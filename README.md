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
        source venv/Scripts/activate
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
