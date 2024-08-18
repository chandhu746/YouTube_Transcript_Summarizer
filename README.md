# YouTube Transcript Summarizer

## Overview

**YouTube Transcript Summarizer** is a web application that extracts transcripts from YouTube videos and generates a concise summary of the content. Built using Streamlit, Google Gemini Pro, and various Python libraries, this tool helps users quickly grasp the key points from video transcripts.

## Features

- **Transcript Extraction**: Extracts transcripts from YouTube videos using the YouTube Transcript API.
- **Content Summarization**: Summarizes the extracted transcript using Google Gemini Pro for a concise overview.
- **Export Options**: Allows users to download the summary in multiple formats including PDF, Word Document, and Markdown.
- **User Interface**: Simple and intuitive interface built with Streamlit for ease of use.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/chandhu746/YouTube_Transcript_Summarizer.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd YouTube_Transcript_Summarizer
    ```

3. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**:
    Create a `.env` file in the root directory of the project and add your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

2. **Open the Application**:
   Navigate to `http://localhost:8501` in your web browser.

3. **Enter the YouTube Video Link**:
   Provide the URL of the YouTube video you want to summarize.

4. **Get Detailed Notes**:
   Click the "Get Detailed Notes" button to extract the transcript, generate the summary, and download it in your preferred format.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for creating an easy-to-use web application framework.
- [Google Gemini Pro](https://developers.google.com/gemini) for advanced content generation.
- [YouTube Transcript API](https://github.com/jdepoe/youtube-transcript-api) for providing video transcripts.
- [FPDF](http://www.fpdf.org/) for PDF generation.
- [python-docx](https://python-docx.readthedocs.io/) for Word Document generation.

## Contact

For any inquiries or issues, please contact me at (mailto:mchandrasekhar746@gmail.com).
