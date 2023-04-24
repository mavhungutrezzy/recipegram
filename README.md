# recipegram


<p align="center">
<img src="https://img.shields.io/badge/python-3.8-blue">
<img src="https://img.shields.io/badge/fastapi-0.63.0-green">
<img src="https://img.shields.io/badge/license-MIT-green">
<img src="https://img.shields.io/badge/contributions-welcome-green">
<img src="https://img.shields.io/badge/PRs-welcome-green">
<img src="https://img.shields.io/badge/author-mavhungutrezzy-blue">
</p>


## Description
RecipeGram API is a RESTful API built with [FastAPI]() and [MongoDB]() using [Beanie]() as an ODM. It provides endpoints for performing CRUD operations on recipes, following recipe authors, viewing recipes by author, and adding recipes to favorites.

## Features
- JWT-based authentication for protected routes
- Secure password hashing using bcrypt
- Input validation and error handling with FastAPI's built-in tools
- Scalable MongoDB database integration with Beanie
- Flexible data modeling with Pydantic models


## Documentation
The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc) after running the application.

## Installation
1. Clone the repository
```bash
git clone https://github.com/mavhungutrezzy/recipegram.git
```

2. Create a virtual environment
```bash
python3 -m venv env
```

3. Activate the virtual environment
```bash
source env/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the application
```bash
    python main.py --reload
```

## Testing
1. Run the tests
```bash
pytest
```

## License
This project is licensed under the terms of the MIT license.