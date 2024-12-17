# StarWars Blog API

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=python&logoColor=white)

A RESTful API for managing a Star Wars blog with user favorites functionality, built with Flask and SQLAlchemy.

[Features](#features) • [Getting Started](#getting-started) • [API Endpoints](#api-endpoints) • [Project Structure](#project-structure) • [Database Model](#database-model)

</div>

## Features

- Browse Star Wars characters and planets
- User management system
- Favorites functionality for saving planets and characters
- SQLite database with SQLAlchemy ORM
- RESTful API architecture
- Database migrations with Alembic
- Flask Admin integration for database management

* Full CRUD operations for planets and people

## Getting Started

### Prerequisites

- Python 3.x
- pip or pipenv

### Installation

```bash
# Clone the repository
git clone https://github.com/maxdenuevo/4g24-REST-API

# Install dependencies using pipenv
pipenv install

# Activate the virtual environment
pipenv shell

# Start the development server
python app.py
```

## API Endpoints

### Characters and Planets

- `GET /people` - Get all characters
- `GET /people/<int:people_id>` - Get specific character
- `POST /people` - Create new character
- `PUT /people/<int:people_id>` - Update character
- `DELETE /people/<int:people_id>` - Delete character
- `GET /planets` - Get all planets
- `GET /planets/<int:planet_id>` - Get specific planet
- `POST /planets` - Create new planet
- `PUT /planets/<int:planet_id>` - Update planet
- `DELETE /planets/<int:planet_id>` - Delete planet

### Users and Favorites

- `GET /users` - Get all users
- `GET /users/favorites` - Get current user's favorites
- `POST /favorite/planet/<int:planet_id>` - Add planet to favorites
- `POST /favorite/people/<int:people_id>` - Add character to favorites
- `DELETE /favorite/planet/<int:planet_id>` - Remove planet from favorites
- `DELETE /favorite/people/<int:people_id>` - Remove character from favorites

## Project Structure

```
.
├── app.py                # Application entry point
├── config.py             # Configuration settings
├── models.py             # Database models
├── routes.py             # API endpoints
├── instance/
│   └── starwars_blog.db  # SQLite database
└── requirements.txt      # Project dependencies
```

## Database Model

### Models

- `User`: Manages blog users
- `People`: Stores Star Wars characters
- `Planet`: Stores Star Wars planets
- `Favorite`: Manages user favorites

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Sources

This exercise is part of the complete 4Geeks Academy Full Stack course:

[![4Geeks Academy](https://img.shields.io/badge/4Geeks%20Academy-blue.svg)](https://4geeks.com/syllabus/santiago-pt-49/project/exercise-starwars-blog-api)
