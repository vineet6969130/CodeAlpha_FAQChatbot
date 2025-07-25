import tkinter as tk
from chatbot import get_best_answer

def on_ask():
    query = entry.get()
    response = get_best_answer(query)
    chat_box.insert(tk.END, f"You: {query}\nBot: {response}\n\n")
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("FAQ Chatbot")

chat_box = tk.Text(window, height=20, width=60)
chat_box.pack()

entry = tk.Entry(window, width=50)
entry.pack()

ask_button = tk.Button(window, text="Ask", command=on_ask)
ask_button.pack()

window.mainloop()
