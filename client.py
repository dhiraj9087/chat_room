import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

# Global variables
client = None
nickname = None

# Connect to server function
def connect_to_server():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 55553
    try:
        client.connect((host, port))
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to server: {e}")
        return False
    return True

# Receive messages function
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                chat_history.config(state=tk.NORMAL)
                chat_history.insert(tk.END, message + "\n")
                chat_history.yview(tk.END)
                chat_history.config(state=tk.DISABLED)
        except:
            messagebox.showerror("Error", "An error occurred!")
            client.close()
            break

# Send message function
def send_message():
    message = f'{nickname}: {message_entry.get()}'
    client.send(message.encode('ascii'))
    message_entry.delete(0, tk.END)

# Leave chat function
def leave_chat():
    message = f'{nickname} has left the chat!'
    client.send(message.encode('ascii'))
    client.close()
    root.quit()

# GUI function
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        leave_chat()

# Main program
if __name__ == "__main__":
    # Ask for nickname
    root = tk.Tk()
    root.withdraw()
    nickname = simpledialog.askstring("Nickname", "Choose a nickname", parent=root)
    
    if not nickname:
        messagebox.showerror("Error", "Nickname cannot be empty")
        root.quit()
        exit()

    # Connect to the server
    if not connect_to_server():
        root.quit()
        exit()

    # Set up GUI
    root.deiconify()
    root.title("Chat Room")
    root.geometry("400x500")
    
    chat_history = scrolledtext.ScrolledText(root, state=tk.DISABLED)
    chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    message_frame = tk.Frame(root)
    message_frame.pack(padx=10, pady=10, fill=tk.X)
    
    message_entry = tk.Entry(message_frame)
    message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    send_button = tk.Button(message_frame, text="Send", command=send_message)
    send_button.pack(side=tk.LEFT)

    leave_button = tk.Button(message_frame, text="Leave", command=leave_chat)
    leave_button.pack(side=tk.RIGHT)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start receiving messages
    threading.Thread(target=receive, daemon=True).start()

    # Start Tkinter event loop
    root.mainloop()
