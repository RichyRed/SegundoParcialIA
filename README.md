# project-template-generator
template generator for final projects

## run with docker

build: `docker build -t llm_service .`
run: `docker run --rm -p 8000:8000 --env-file .env llm_service`

## run with docker compose

build and run: `docker compose up`