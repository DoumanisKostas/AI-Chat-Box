import tkinter as tk
import openai

# Set your OpenAI API key here
openai.api_key = "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"

def send_message():
    """Fetch the message from the entry box, display it, get the AI response, and display the response."""
    message = entry.get()
    if message.strip():  # Check if the message is not empty
        # Display user's message
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.config(state=tk.DISABLED)
        
        # Get AI response
        ai_response = get_ai_response(message)
        
        # Display AI's response
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "AI: " + ai_response + "\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)  # Auto-scroll to the bottom
        
        entry.delete(0, tk.END)

def get_ai_response(prompt):
    """Send a prompt to the OpenAI API and return the AI's response."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the desired GPT model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Error: Unable to get a response from the AI. Please try again."

# Create the main window
window = tk.Tk()
window.title("AI Chatbox")

# Create a chat area
chat_area = tk.Text(window, wrap="word", state=tk.DISABLED, bg="#F0F0F0", fg="#333")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a message entry box
entry = tk.Entry(window)
entry.pack(padx=10, pady=5, fill=tk.X)
entry.bind("<Return>", lambda event: send_message())  # Trigger send_message on pressing Enter

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the main event loop
window.mainloop()

