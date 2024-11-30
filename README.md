# AI-Powered Graph Generator

This project is a web-based application that leverages **AI** to generate insights and interactive graphs from user-uploaded datasets. It uses **Dash**, **Plotly**, and **Google Gemini** (Generative AI) to dynamically visualize data and generate reports based on user queries.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Set Up the API Key](#set-up-the-api-key)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Video Tutorial](#video-tutorial)
- [License](#license)

## Overview

This application allows users to:

- Upload CSV files and view their data.
- Select different chart types (e.g., line, bar, scatter, pie, histogram).
- Query AI for insights related to their data.
- Customize graph titles and row ranges for visualization.
- The backend is powered by **Google Gemini (Generative AI)**, which provides real-time insights based on user input.

## Installation

Follow these steps to set up the AI-Powered Graph Generator on your local machine.

### Clone the Repository

To get started, clone the repository using Git:

```bash
git clone https://github.com/yourusername/ai-powered-graph-generator.git
cd ai-powered-graph-generator
Install Dependencies
Install the required Python packages using pip. It's recommended to use a virtual environment to manage dependencies:

Create a virtual environment (if you don’t have one already):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file yet, you can create it by running:

bash
Copy code
pip freeze > requirements.txt
The requirements.txt should include the following packages:

Copy code
dash
dash-bootstrap-components
plotly
pandas
flask-cors
google-generativeai
Set Up the API Key
To use the Google Gemini API for generating insights, you need to set up an API key:

Visit the Google Cloud Console.
Create a project and enable the Google Gemini API.
Generate an API key and replace the api_key placeholder in the following line in app.py:
python
Copy code
genai.configure(api_key="YOUR_GOOGLE_GEMINI_API_KEY")
Make sure to securely store your API key and do not expose it in public repositories.

Running the Application
To run the web application, simply execute the following command:

bash
Copy code
python app.py
This will start the Dash server, and you can access the application in your browser by visiting:

arduino
Copy code
http://127.0.0.1:8050/
The application will allow you to upload datasets, choose chart types, query AI for insights, and view your generated graphs.

Usage
Once the application is running:

Upload Your Dataset: Click on the Upload button to upload a CSV file.
Select Graph Type: Choose from line, bar, scatter, pie, or histogram charts.
Customize Graph Title: Enter a custom title for your graph.
Select Columns: Choose which columns to plot on the X and Y axes.
Generate Insights: Enter a query to ask the AI for insights about your data.
View Insights and Graph: The AI will generate insights and update the graph based on your selections.
Video Tutorial
For a quick tutorial on how to use the application, watch the following video:


Click the image above to watch the full demo on Vimeo.
