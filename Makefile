IMAGE_NAME=devops-flask
TAG=latest

.PHONY: build run push k8s

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

run:
	docker run --rm -p 5000:5000 $(IMAGE_NAME):$(TAG)

push:
	docker push $(IMAGE_NAME):$(TAG)

k8s-apply:
	kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml

k8s-delete:
	kubectl delete -f k8s/deployment.yaml -f k8s/service.yaml
