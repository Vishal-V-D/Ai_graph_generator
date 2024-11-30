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

## Conclusion
Thank you for using the **AI-Powered Graph Generator**! This application empowers you to effortlessly visualize data, customize graphs, and gain insights using AI. Whether you're working with datasets in sales, performance metrics, or any other domain, this tool helps bring clarity to your data in just a few clicks.

## Contributing
We welcome contributions from the community. If you would like to contribute to the development of this project, please feel free to fork the repository and submit a pull request. Here’s how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **Dash** for building the interactive UI framework
- **Plotly** for the excellent charting library
- **Google Gemini** for the AI-driven insights
- **Vimeo** for video hosting

## Contact
For any inquiries or support, feel free to reach out:
- Email: support@aigraphgen.com
- GitHub Issues: [Create an Issue](https://github.com/yourusername/ai-powered-graph-generator/issues)

## Video Tutorial
For a quick tutorial on how to use the application, watch the following video:

[![Watch the video](https://img.youtube.com/vi/1034770132/maxresdefault.jpg)](https://vimeo.com/1034770132)

Click the image above to watch the full demo on Vimeo.

## Thank You!
We hope you enjoy using the AI-Powered Graph Generator. If you have any feedback or suggestions, we’d love to hear from you!

---

© 2024 AI-Powered Graph Generator | All Rights Reserved

