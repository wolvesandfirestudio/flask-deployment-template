# Flask Deployment Template

This is a lightweight Flask backend template suitable for deployment to platforms like Render. It includes:

- CORS support for local + production frontends
- Environment variable config loading via `config.py`
- Example `.env` file
- Render deployment config (`render.yaml`)
- Health check route for uptime verification

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

## Deployment

To deploy on [Render](https://render.com):

1. Push this repo to GitHub
2. Connect your GitHub to Render
3. Choose this repo as a new Web Service
4. Use `gunicorn app:app` as the start command

## Notes

This template is based on a production setup used in a real investigative tool (Ember Relay) and follows best practices for deploying small, secure Flask APIs.

---