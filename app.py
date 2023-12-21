import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)


USER_GISTS_API_ENDPOINT = 'https://api.github.com/users/{}/gists'
@app.route('/<username>')
@app.route('/')
def get_user_gists(username=None):
    try:
        if username: GIT_USER = username
        else: GIT_USER = os.environ.get('GIT_USER', 'octocat')
        response = requests.get(USER_GISTS_API_ENDPOINT.format(GIT_USER))
        if response.status_code == 200:
            gists = response.json()
            return render_template('gists_table.html', gists=gists,git_user=GIT_USER)
        else:
            return jsonify({'error': 'Failed to fetch Gists', 'message': response.json()['message']}), response.status_code
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)