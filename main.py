import os
import httpx
from flask import Flask, request, redirect, render_template_string, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URL = os.environ.get('REDIRECT_URL')

AIIA_CONNECT_URL = 'https://api-sandbox.aiia.eu/v1/oauth/connect'
AIIA_TOKEN_URL = 'https://api-sandbox.aiia.eu/v1/oauth/token'
AIIA_ACCOUNTS_URL = 'https://api-sandbox.aiia.eu/v1/accounts'
AIIA_TRANSACTIONS_URL = 'https://api-sandbox.aiia.eu/v1/accounts/{accountId}/transactions'

@app.route('/')
def home():
    return 'Welcome to Aiia API Integration! <a href="/connect">Connect to Aiia</a>'

# Initiate Connection to Aiia
@app.route('/connect')
def connect():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URL,
        'scope': 'accounts%20offline_access',
        'response_type': 'code'
    }
    response = httpx.get(AIIA_CONNECT_URL, params=params)
    return redirect(response.headers.get('location'))

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_data = get_tokens(code)
    access_token = token_data.get('access_token')

    data = get_accounts(access_token)
    return render_template('dashboard.html', accounts=data['accounts'])

def get_tokens(code):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URL
    }
    response = httpx.post(AIIA_TOKEN_URL, auth=(CLIENT_ID, CLIENT_SECRET), headers=headers, json=data)
    return response.json()

def get_accounts(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = httpx.get(AIIA_ACCOUNTS_URL, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)