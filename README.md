# NanoPad: Your Instant Shared Notebook

A lightweight, real-time notepad application built with Python Flask that allows instant note sharing and collaboration.

## Features

- ✨ Real-time character and word counting
- 🌓 Dark/Light mode toggle
- 💾 Automatic saving
- 🔗 Shareable note links
- 📋 Quick copy buttons for note content and share URL
- 📱 Responsive design
- 🆔 Automatic note ID generation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open `http://localhost:5000` in your browser

## How It Works

- Visit the main page to get automatically redirected to a new note with a unique ID
- Share the URL with others to collaborate on the same note
- Notes are saved automatically as you type
- Use the copy buttons to quickly share either the note content or the URL
- Toggle between dark and light modes for comfortable viewing

## Tech Stack

- Backend: Python Flask
- Frontend: Vanilla JavaScript
- Storage: File-based system
- Styling: CSS with CSS Variables for theming

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/         
│   └── notepad.html   # Main template
└── notes/             # Directory for stored notes
```

## License

This project is licensed under the MIT License.
