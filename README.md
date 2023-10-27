# Aiia API Integration with Flask

This project demonstrates the integration of the Aiia API using Flask and the `httpx` library. The application initiates a connection to the Aiia platform, allows the user to authorize access to their accounts, and then displays a dashboard of their account details.

## Installation

1. **Clone the repository:**
    ```bash
    git clone git@github.com:mart337i/aiia_python.git
    cd aiia_python
    ```

2. **Install the required dependencies:**
    ```bash
    # NOTE:: request did not work.
    # i think it has somthing to do with the diffrence between HTTP/1.1 and HTTP/2 which is the only reason i did httpx over request
    pip install flask httpx python-dotenv
    ```

4. **Set up your environment variables:**

    Copy the provided `.env.example` to a new file named `.env`:
    ```bash
    cp .env.example .env
    ```

    Edit the `.env` file and fill in your credentials and configuration:
    ```plaintext
    CLIENT_ID=demoapp-7a5b1234-abcd-5678-efgh-9ijk0123l456
    CLIENT_SECRET=a1b2c3d8e4f5g6h7i9j0k8l7m6n5o4p3q2r1s0t2u3v4w5x6y7z8a9b0c1d2e3f4
    REDIRECT_URL=http://localhost:5000/callback
    ```

5. **Run the Application:**
    ```bash
    python main.py
    ```

Visit `http://localhost:5000` in your browser to use the application.
