# AI Chatbox with Python and OpenAI API

This project demonstrates how to create a simple AI-powered chatbox using Python, the OpenAI API, and Tkinter (a standard GUI library in Python). The chatbox allows users to interact with an AI model from OpenAI's GPT series directly from a desktop application.

## Features

- Real-time conversation with OpenAI's GPT model.
- A user-friendly graphical interface built with Tkinter.
- Easily customizable to add more functionalities or integrate with other services.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (sign up and obtain from [OpenAI](https://platform.openai.com/))
- Basic knowledge of Python programming

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ai-chatbox.git
    cd ai-chatbox
    ```

2. **Install the required packages:**
    Make sure you have `pip` installed and run:
    ```bash
    pip install openai
    ```

3. **Set up your OpenAI API Key:**

    Set your OpenAI API key as an environment variable:
    - **Windows:**
      Open Command Prompt and run:
      ```bash
      setx OPENAI_API_KEY "your_openai_api_key"
      ```
    - **macOS/Linux:**
      Open Terminal and run:
      ```bash
      export OPENAI_API_KEY="your_openai_api_key"
      ```
    Replace `"your_openai_api_key"` with your actual OpenAI API key.

## Usage

1. **Run the Chatbox Application:**

    Execute the script in your terminal or command prompt:
    ```bash
    python chatbox.py
    ```

2. **Interact with the AI:**

    - Type your message in the input box and press "Send".
    - The AI will respond, and the conversation will be displayed in the chat area.

## Example

![Chatbox Screenshot](path/to/screenshot.png)

## Code Overview

### Main Components

- **`chatbox.py`**: The main script containing the Python code to create the GUI and interact with the OpenAI API.
- **Tkinter**: Used to build the graphical user interface.
- **OpenAI API**: Handles sending messages and receiving responses from the AI model.

### Key Functions

- **`get_ai_response(prompt)`**: Sends a prompt to the OpenAI API and returns the AI's response.
- **`send_message()`**: Handles the sending of messages from the input box to the AI and displays the conversation in the chat area.

## Error Handling

The application includes error handling for common issues like:
- Invalid or missing API keys
- Rate limits
- Connection problems

## Troubleshooting

- **API Key Issues**: Make sure your API key is correct and set as an environment variable.
- **Dependencies**: Ensure all required packages are installed correctly.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [OpenAI](https://openai.com) for providing the GPT API.
- Inspired by various Python and AI projects from the open-source community.

