## OCR with Gemini

This project utilizes Optical Character Recognition (OCR) to digitize scanned books using Google Gemini. It aims to convert physical text into editable and searchable digital formats, enhancing accessibility and usability. The project focuses on providing accurate text extraction from images of printed materials, making it easier to manage and reference content. By leveraging advanced OCR technology, users can efficiently archive and retrieve information from their scanned books.


## Setup

To set up this project, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/). Once Python is installed, you can set up a virtual environment and install the required packages.

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   ```bash
   cp -r .env.example .env
   ```
   Then edit the `.env` file with your configuration settings.

## Usage

To use the OCR functionality, follow these steps:

1. Place your scanned image in the project directory or specify the correct path in the script.
2. Run the script using the following command:
   ```bash
   python main.py
   ```
3. The extracted text will be printed to the console.

Make sure to adjust the `image_path` variable in `main.py` to point to your image file. 