# README.md

# DeSoPedia CherryPy Web Application

DeSoPedia is a simple web application built using CherryPy. This project serves as a basic template for creating web applications with CherryPy, featuring an index page titled "DeSoPedia".

## Project Structure

```
cherrypy-app
├── src
│   ├── app.py          # Entry point of the application
│   ├── views
│   │   └── index.html  # HTML structure for the index page
│   └── static
│       ├── css
│       │   └── style.css # CSS styles for the application
│       └── js
│           └── main.js   # JavaScript code for client-side functionality
├── requirements.txt      # List of dependencies
└── README.md             # Documentation for the project
```

## Requirements

To run this application, you need to have Python installed along with the required packages. You can install the necessary packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

To start the CherryPy server, run the following command:

```
python src/app.py
```

Once the server is running, you can access the application by navigating to `http://localhost:8080` in your web browser.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.