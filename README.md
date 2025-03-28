# Resume Parser Web App

## Overview
This is a **Python-based** web application for parsing resumes and displaying extracted information. The application uses `Flask` for the backend and `resume-parser` for processing resumes. The front end dynamically presents parsed data in a structured format.

## Features
- Upload resumes in PDF/DOCX format
- Extract key details such as name, contact, skills, and experience
- Display extracted information in a user-friendly format
- Interactive UI with real-time data rendering

## Requirements
Ensure you have **Python 3.7+** installed. Install dependencies using:

```bash
pip install -r requirements.txt
```

## Installation & Running

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Manavagg2003/Resume-Scrapper-Using-Python.git
   cd Resume-Scrapper-Using-Python
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Web App**
   Open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```

## File Structure
```
📂 Project Root
├── app.py           # Flask backend
├── resumeparse.py   # Resume parsing logic
├── templates/index.html       # HTML templates
├── config.yaml
├── requirements.txt # Required dependencies
├── README.md        # Project documentation
```

## API Endpoints
- `POST /upload` - Upload a resume file
- `GET /results` - Get parsed resume data

## Notes
- Make sure `Tesseract-OCR` is installed for better text extraction.
- Modify `resumeparse.py` to add custom parsing rules as needed.

## Contributing
Feel free to fork and improve the project! Pull requests are welcome.

## License
This project is licensed under the MIT License.

