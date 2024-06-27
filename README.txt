# SpeakItApp

Speak-It is a Django application designed to handle text extraction, web scraping, and audio output generation. 
The app allows users to create text objects through a form, scrape content from web pages, extract text from images and convert text to audio in various languages.

## Features

- Create and manage Speak objects through a form.
- Scrape content from web pages.
- Extract text from images using OCR (Optical Character Recognition).
- Translate text to different languages.
- Generate audio output from text using Google Text-to-Speech (gTTS).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Lingual.git
    cd Lingual
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### Create Speak Object

1. Navigate to the Speak creation page:

    ```
    http://127.0.0.1:8000/
    ```

2. Fill out the form with the necessary information and submit it.

### Generate Audio Output

1. Navigate to the audio output page:

    ```
    http://127.0.0.1:8000/content
    ```

2. The application will retrieve the content from the last Speak object, translate it, and generate an audio file.

## Code Overview

### `views.py`

- `text_create_view(request)`: Handles the creation of a new Speak object via a form.
- `web_scrape()`: Scrapes content from a webpage specified in the last Speak object.
- `audio_output_view(request)`: Generates an audio output from the content of the last Speak object, translates it, and returns the audio file URL.

### `forms.py`

- `SpeakForm`: A Django ModelForm for creating and updating Speak objects. It includes fields for content, a URL to access, an image, and the language for translation.

### `urls.py`

- URL routing configuration for the application. Routes include:
  - `path('', views.text_create_view, name="content-create")`: Route for creating Speak objects.
  - `path('content', views.audio_output_view, name="content-speak")`: Route for generating audio output from Speak objects.
  - `path('admin/', admin.site.urls)`: Admin site route.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

