# Deployment

## Containerization
- Dockerized FastAPI backend
- Docker Compose support

## CI/CD
- GitHub Actions CI
- GitHub Actions CD

## Known Issue
Docker build downloads large Torch/CUDA packages.
Future optimization:
- CPU-only Torch
- Multi-stage Docker build
- Smaller production image