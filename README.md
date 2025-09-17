# FlavorFlow

## Project Overview

FlavorFlow is a web application that helps users find the closest recipes based on a set of available ingredients. Users can favorite recipes, receive suggestions for new recipes, and expand the recipe database through webscraping. The app also supports using a camera to scan the fridge for ingredients, making it easier to input what you have on hand.

## Core Features

- **Ingredient-Based Recipe Search:** Find recipes that best match the ingredients you have.
- **Favorite Recipes:** Mark and manage your favorite recipes for quick access.
- **Recipe Suggestions:** Get suggestions for new recipes based on your preferences and history.
- **Webscraping for Recipes:** Automatically discover and store new recipes from the web.
- **Camera Integration:** Use your camera to scan your fridge and detect available ingredients.

## Tech Stack

- **Backend:** Python (Django)
- **Frontend:** React, CSS
- **Database:** MongoDB
- **Deployment:** Azure

## Learning Focus

The primary goal of this project is to learn and implement the following:

- Integrating Django with MongoDB
- Building RESTful APIs
- Webscraping with Python
- Image processing for ingredient detection
- Building a modern React frontend
- Deploying full-stack applications to Azure

## Folder Structure

```
FlavorFlow/
  backend/         # Django backend
  frontend/        # React frontend
  README.md
  .gitignore
```

## Getting Started

### Backend (Django)

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install django pymongo
   ```
3. Start a new Django project:
   ```bash
   django-admin startproject core .
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend (React)

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Create a new React app (if not already created):
   ```bash
   npx create-react-app .
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

## Deployment

- The backend and frontend will be deployed to Azure.
- MongoDB will be hosted using Azure Cosmos DB or another managed MongoDB service.

## License
