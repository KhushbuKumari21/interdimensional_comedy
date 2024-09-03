# Interdimensional Comedy Generator

## Overview
The Interdimensional Comedy Generator is a Flask-based web application that allows users to generate customized comedy shows based on their input. The application features an API for generating comedy and a front-end interface for user interaction.

## Features
- **Flask API**: Provides an endpoint to generate comedy shows based on user input.
- **Dynamic Form**: Allows users to input comedy style, performer gender, and dimension.
- **Real-time Feedback**: Displays the generated comedy show or error messages directly on the web page.
- **Responsive Design**: Ensures a modern and responsive user interface.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/interdimensional-comedy-generator.git
   cd interdimensional-comedy-generator
**2.set Up a Virtual Environment:**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
**3.Install Dependencies:**
pip install -r requirements.txt
**4.Run the Flask Application:**
python app.py
****5.Access the Application: ****
http://127.0.0.1:5000/

**API Documentation**
http://127.0.0.1:5000/docs


**Project Structure**
app.py: Main Flask application file.
templates/index.html: HTML template for the user interface.
static/css/styles.css: CSS file for styling.
static/js/script.js: JavaScript file for form handling and AJAX requests.

**Development**
Adding New Features: Implement new routes and endpoints in app.py and update the front-end as needed.
Bug Fixes: Check the JavaScript console and server logs for errors and apply fixes in the respective files