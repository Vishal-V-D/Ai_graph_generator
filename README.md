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
 
```

## Video Tutorial
For a quick tutorial on how to use the application, watch the following video:

### Watch the Demo

[![Watch the video](https://img.youtube.com/vi/1034770132/maxresdefault.jpg)](https://vimeo.com/1034770132)

Click the image above to watch the full demo on Vimeo.

Alternatively, you can embed the video directly in the README (if supported by your platform):

<div style="padding:53.13% 0 0 0;position:relative;">
    <iframe src="https://player.vimeo.com/video/1034770132?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" 
            frameborder="0" 
            allow="autoplay; fullscreen; picture-in-picture; clipboard-write" 
            style="position:absolute;top:0;left:0;width:100%;height:100%;" 
            title="AI-Powered Graph Generator - Demo Video"></iframe>
</div>
<script src="https://player.vimeo.com/api/player.js"></script>

