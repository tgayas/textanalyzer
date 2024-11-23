from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import re
from collections import Counter

# Window setup
window = Tk()
window.title("Text Analysis Tool")
window.geometry("500x600+700+300")
window.configure(bg="lightblue")  # Set the background color to light blue

# Function to load file data
def loadFileData(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to save file data
def saveFileData(filename, text_values):
    with open(filename, 'w') as file:
        file.write(text_values)

# Function to process file and display content
def processFile():
    name = fd.askopenfilename(filetypes=[("Text files", "*.in")])
    if name:
        content = loadFileData(name)
        file_text.delete("1.0", END)
        file_text.insert(END, content)
        analyze_button.config(state=NORMAL)

# Function to analyze text content
def analyzeText():
    text_content = file_text.get("1.0", END)
    paragraphs = text_content.strip().split('\n\n')
    sentences = re.split(r'[.!?]+', text_content)
    words = re.findall(r'\b\w+\b', text_content.lower())
    
    num_paragraphs = len(paragraphs)
    num_sentences = len(sentences)
    word_count_per_sentence = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
    word_freq = Counter(words).most_common()

    analysis_report = f"Number of paragraphs: {num_paragraphs}\n"
    analysis_report += f"Number of sentences: {num_sentences}\n"
    analysis_report += "Word count per sentence: " + ', '.join(map(str, word_count_per_sentence)) + "\n"
    analysis_report += "Frequently used words:\n"
    analysis_report += '\n'.join([f"{word} occurs {count} {'time' if count == 1 else 'times'}" for word, count in word_freq])

    report_text.delete("1.0", END)
    report_text.insert(END, analysis_report)
    save_button.config(state=NORMAL)

# Function to save analysis report
def saveReport():
    nameOfOutputFile = fd.asksaveasfilename(defaultextension=".out", filetypes=[("Output files", "*.out")])
    if nameOfOutputFile:
        saveFileData(nameOfOutputFile, report_text.get("1.0", END))
        messagebox.showinfo("Success", "Saved Successfully!")

# Custom style for buttons
button_style = {"bg": "#E0E887", "fg": "black", "activebackground": "#FFC07B", "activeforeground": "white", "relief": "groove"}

# GUI Elements
open_button = Button(window, text="Open File", command=processFile, **button_style)
open_button.grid(row=0, column=0, padx=10, pady=10)

file_text = Text(window, height=10, width=50, bg="#FFFFFF", fg="black")
file_text.grid(row=1, column=0, padx=10)

analyze_button = Button(window, text="Analyze", command=analyzeText, state=DISABLED, **button_style)
analyze_button.grid(row=2, column=0, padx=10, pady=10)

report_text = Text(window, height=10, width=50, bg="#FFFFFF", fg="black")
report_text.grid(row=3, column=0, padx=10)

save_button = Button(window, text="Save Report", command=saveReport, state=DISABLED, **button_style)
save_button.grid(row=4, column=0, padx=10, pady=10)

close_button = Button(window, text="Close", command=window.quit, **button_style)
close_button.grid(row=5, column=0, padx=10, pady=10)

# Start the application
window.mainloop()
