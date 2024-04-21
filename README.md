# Documentation

## Development Environment

To set up your development environment, start by creating a Python virtual environment. This will isolate your project's dependencies.

```bash
python3 -m venv backEnv
```

Activate the virtual environment with the following command:

- On macOS and Linux:
  ```bash
  source backEnv/bin/activate
  ```

- On Windows:
  ```cmd
  backEnv\Scripts\activate
  ```

Once the virtual environment is activated, you can install all the required dependencies locally within this environment:

```bash
pip install -r requirements.txt
```

### Database

#### Start

To start the database, use Docker Compose. Ensure Docker and Docker Compose are installed on your system. Then, run:

```bash
docker compose up -d
```
