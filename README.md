# Sentiment Analyzer 

*frontend not complete 

This is a simple web application built with Flask for performing sentiment analysis on text inputs using VADER (Valence Aware Dictionary and sEntiment Reasoner).

## Features

- **Sentiment Analysis**: Analyze the sentiment (positive, negative, neutral) of text inputs.
- **VADER Sentiment Analysis**: Utilizes the VADER sentiment analysis tool for accurate sentiment classification.
- **Web Interface**: Provides a user-friendly web interface for interacting with the sentiment analyzer.

## Technologies Used

- **Flask**: Python web framework used for building the backend of the application.
- **VADER Sentiment**: Python library for sentiment analysis.
- **HTML/CSS/JavaScript**: Frontend technologies for building the user interface.

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/sentiment-analyzer.git
   cd sentiment-analyzer
   ```

2. **Install Dependencies**:

   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:

   Start the Flask development server:

   ```bash
   flask run
   ```

   Navigate to `http://localhost:5000` in your web browser to view the application.

4. **Usage**:

   - Enter text in the input field.
   - Click the "Analyze Sentiment" button to see the sentiment analysis results.

## Deployment

This application can be easily deployed to platforms like Heroku for production use. Make sure to set environment variables and configure your production server accordingly.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **VADER Sentiment**: Developed by Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14).
