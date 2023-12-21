import os
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

USER_GISTS_API_ENDPOINT = 'https://api.github.com/users/{}/gists'
ITEMS_PER_PAGE = 10

@app.route('/<username>')
@app.route('/')
def get_user_gists(username=None):
    try:
        if username:
            git_user = username
        else:
            git_user = os.environ.get('GIT_USER', 'octocat')

        response = requests.get(USER_GISTS_API_ENDPOINT.format(git_user))
        if response.status_code == 200:
            gists = response.json()
            page = request.args.get('page', 1, type=int)
            start_index = (page - 1) * ITEMS_PER_PAGE
            end_index = start_index + ITEMS_PER_PAGE
            current_gists = gists[start_index:end_index]
            return render_template('gists_table.html', gists=current_gists, git_user=git_user, page=page)
        else:
            return jsonify({'error': 'Failed to fetch Gists', 'message': response.json()['message']}), response.status_code
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)