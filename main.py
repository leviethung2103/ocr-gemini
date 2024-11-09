import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Constants
MODEL_NAME = "gemini-1.5-flash-002"
GENERATION_CONFIG = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

JSON_SCHEMA = """
{
    "content": str,
    "page_number": str
}
"""


def initialize_gemini():
    """Initialize Gemini API with environment variables."""
    load_dotenv()
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config=GENERATION_CONFIG,
    )


def upload_file(path, mime_type=None):
    """Upload a file to Gemini API.

    Args:
        path (str): Path to the file
        mime_type (str, optional): MIME type of the file

    Returns:
        GenerativeModel.FileData: Uploaded file object
    """
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file


def extract_text_from_image(model, image_path):
    """Extract text from an image using Gemini API.

    Args:
        model: Initialized Gemini model
        image_path (str): Path to the image file

    Returns:
        dict: Extracted text content and page number
    """
    uploaded_file = upload_file(image_path)

    prompt = f"This is a scanned image of a book. Extract the text from image, ignore the headings, just extract the main content and page number using this JSON schema: {JSON_SCHEMA}"

    result = model.generate_content([uploaded_file, "\n\n", prompt])
    return json.loads(result.text)


def save_to_json(data, output_file="response.json"):
    """Save data to a JSON file.

    Args:
        data: Data to save
        output_file (str): Output file path
    """
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    # Initialize Gemini
    model = initialize_gemini()

    # Process image
    image_path = "/Users/hunglv/Library/Mobile Documents/com~apple~CloudDocs/Scanned PDf/Khi ban dang mo/Khi ban Dang Mo Ghi Nguoi Khac Dang No Luc - 60.jpg"
    response = extract_text_from_image(model, image_path)

    # Print and save results
    print(response)
    save_to_json(response)


if __name__ == "__main__":
    main()
