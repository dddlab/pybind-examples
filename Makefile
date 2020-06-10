.PHONY: help build dev test test-env

# Docker image name and tag
IMAGE:=dddlab/project-template
TAG?=latest
# Shell that make should use
SHELL:=bash

help:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: DARGS?=
build: ## Make the latest build of the image
	docker build $(DARGS) --rm --force-rm -t $(IMAGE):$(TAG) .

dev: ARGS?=-d
dev: DARGS?=
dev: PORT?=8888
dev: ## Start container with docker-compose.yml
	IMAGE=$(IMAGE) PORT=$(PORT) docker-compose up $(ARGS)

test: ## Make a test run against the latest image
	pytest tests

test-env: ## Make a test environment by installing test dependencies with pip
	pip install -r requirements-test.txt
