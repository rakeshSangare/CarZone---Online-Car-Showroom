
# CarZone-Online Car Showroom

CarZone is an online car showroom platform designed to help users explore, search for, and find their dream cars with ease. This project involves both frontend and backend development using various technologies.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

- **User Authentication:**
  - Register, login, and logout functionality.
  - Conditional navigation options based on authentication status.

- **Car Listings:**
  - Carousel of featured cars on the homepage.
  - Latest car listings section.

- **Search Functionality:**
  - Search for cars based on name, model, location, year, body style, and price range.

- **Executive Team Info:**
  - Section displaying the executive team with photos and social media links.

- **Responsive Design:**
  - Fully responsive user interface for both desktop and mobile devices.

## Technologies Used

- **Frontend:**
  - HTML, CSS, JavaScript, Bootstrap

- **Backend:**
  - Django (Python)

- **Database:**
  - SQLite (development)
  - PostgreSQL (production)

- **Deployment:**
  - Heroku

- **Version Control:**
  - Git and GitHub

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/carzone.git
   cd carzone
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- **Home Page:** Browse featured and latest car listings.
- **Search Cars:** Use the search form to find cars based on various criteria.
- **User Authentication:** Register, login, and manage account settings.

## Project Structure

```
carzone/
├── cars/                # Car listings app
├── pages/               # Static pages app (home, about, contact)
├── templates/           # HTML templates
├── static/              # Static files (CSS, JavaScript, images)
├── carzone/             # Main project directory
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL configuration
│   └── wsgi.py          # WSGI application
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
