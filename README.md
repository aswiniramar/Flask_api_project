# Flask_api_project
Flask User Management API

Overview

A simple REST API built with Flask to manage users with basic CRUD operations using an in-memory dictionary.

Endpoints

GET /users — List all users

GET /users/<id> — Get user by ID

POST /users — Add new user

PUT /users/<id> — Update user by ID

DELETE /users/<id> — Delete user by ID


Run

pip install flask
python app.py

Test Examples (using curl)

curl http://127.0.0.1:5000/users
curl -X POST -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com"}' http://127.0.0.1:5000/users
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Alice Smith"}' http://127.0.0.1:5000/users/1
curl -X DELETE http://127.0.0.1:5000/users/1

Notes

Data stored in-memory; resets on server restart.

For learning API basics only

