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
# Clone the repository
git clone https://github.com/yourusername/ai-powered-graph-generator.git

# Navigate to the project directory
cd ai-powered-graph-generator

# Create a virtual environment (if you don't have one already)
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# If you don't have a requirements.txt file, create one with the installed packages
pip freeze > requirements.txt

# Set up the Google Gemini API Key in app.py
# Replace the api_key placeholder with your API key
genai.configure(api_key="YOUR_GOOGLE_GEMINI_API_KEY")

# Run the application
python app.py
 to watch the full demo on Vimeo.


