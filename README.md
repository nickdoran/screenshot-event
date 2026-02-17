# Screenshot Event

---

> Created by Nicklas Doran: https://github.com/nickdoran

## What is this Project?

A Python tool that reads a screenshot of an event (e.g. a flyer, invite, or schedule) from the `Images/` folder, uses the OpenAI API to extract event details, and creates an event in your Google Calendar.

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
4. Place your screenshot(s) in the `Images/` folder.

## Usage

```bash
python main.py
```

The script will read the image, send it to OpenAI for processing, and output the result.
