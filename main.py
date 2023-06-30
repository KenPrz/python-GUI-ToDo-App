import customtkinter as ctk

def add_todo():
    todo = entry.get()
    if not todo:
        return
    else:
        label = ctk.CTkLabel(scrollable_frame,text=todo)
        label.pack()
        entry.delete(0, ctk.END)

root = ctk.CTk()
# Determine the width and height based on the content
content_width = 600
content_height = 400

# Calculate the window size by adding some padding
window_width = content_width + 20
window_height = content_height + 20

# Set the window size dynamically
window_size = f"{window_width}x{window_height}"
root.geometry(window_size)
root.title("My App")

title_label = ctk.CTkLabel(root,text="Daily Tasks", font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=(30,20))

scrollable_frame = ctk.CTkScrollableFrame(root,width=500,height=200)
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame,placeholder_text="Add ToDo")
entry.pack(fill="x")

add_button = ctk.CTkButton(root,text="Add",width=100, command=add_todo)
add_button.pack(pady=(8,12))

root.mainloop()