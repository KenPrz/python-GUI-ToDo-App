# Python GUI App

## Introduction
This application utilizes the `customtkinter` library to create a simple to-do list. The app allows users to add daily tasks and displays them in a scrollable frame.

## Prerequisites
Before running the application, make sure you have the following installed:
- Python 3.x
- `customtkinter` library

## Installation
To install the `customtkinter` library, you can use `pip`:

```shell
pip install customtkinter
```

## Usage
To run the application, execute the Python script that contains the code you provided.

```shell
python my_app.py
```

## Functionality
The application provides the following functionality:

### Add ToDo
- To add a new task, type the task in the text box labeled "Add ToDo".
- Press the **Add** button or press Enter to add the task to the to-do list.
- The task will be displayed as a label in the scrollable frame.

## Customization
You can customize the application by modifying the code provided. Here are a few areas you can consider:

### Window Size
The window size is determined by the content width and height. You can adjust these values to fit your requirements.

```python
content_width = 600
content_height = 400
```

### Title
The title of the application can be changed by modifying the following line:

```python
root.title("My App")
```

### Styling
You can modify the styling of the application by changing the font size, weight, and other properties. For example, to change the font size of the title label, modify the following line:

```python
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
```