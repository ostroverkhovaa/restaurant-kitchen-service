🧑‍🍳 Restaurant Kitchen Service

A Django web app for managing a restaurant’s kitchen operations — 
including dish management, cook assignments, and dish type classification.

📦 Features

- Full CRUD for:
  - Dishes
  - Dish Types
  - Cooks
- User authentication (login/logout)
- Assign/remove cooks from dishes
- Dish filtering by type
- Responsive design with custom styles and background image
- Admin panel support

 🛠 Tech Stack

- Python 3 & Django
- Bootstrap 4 + custom CSS
- Crispy Forms for clean form rendering

📁 Setup

1. Clone the repo
git clone https://github.com/ostroverkhovaa/restaurant-kitchen-service/
cd restaurant-kitchen-service

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create superuser
python manage.py createsuperuser

6. Start the server
python manage.py runserver

👤 Test User

Use the following credentials to log in as a test user:

Login: user
Password: user12345
