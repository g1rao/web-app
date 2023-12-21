# GitHub Gists API

This project provides a simple HTTP API that interacts with the GitHub API to retrieve a user's publicly available Gists.

## Setup

### Prerequisites

- Python 3.x installed
- Docker installed

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/g1rao/github-gists-api.git
    cd github-gists-api
    ```

2. Install required Python libraries:

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

### Running the API Locally

To run the API locally:

```bash
python app.py
```

### Running in Docker

To build a Docker image:

```bash
docker build -t github-gists-api .
```

Run the Docker container:

```bash
docker run -p 8080:8080 github-gists-api
```

The API will be available at http://localhost:8080/.