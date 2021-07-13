build-docker: 
	docker build -t py-fastapi-clean-arch .

run-docker:
	docker run --network host --env-file .env -d -p 8000:8000 py-fastapi-clean-arch

run:
	uvicorn app.main:app --reload