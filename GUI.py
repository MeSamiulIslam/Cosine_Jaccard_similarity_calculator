# Import necessary libraries
import tkinter as tk
from PIL import ImageTk, Image
import math

# Create the application main window
root = tk.Tk()
root.title("Text Similarity Calculator")

#icon of window
icon = tk.PhotoImage(file = 'calculator-icon.png')
root.iconphoto(False, icon)

root.geometry('350x500') #window size
root.configure(background='#06283D') #Background color of paghe

# Load and resize an image for a logo
img = Image.open('diu.png')
resized_img = img.resize((100,100)) #logo size
img = ImageTk.PhotoImage(resized_img)

#display the logo
img_label = tk.Label(root, image=img)
img_label.pack(pady=(10,10))

# Create labels for the input fields
label_1 = tk.Label(root, text="Enter Your First Content", fg='white', bg='#33BBC5')
label_1.pack(pady=(10,10)) #PAcked
label_1.config(font=('verdana', 14))

# Create entry widgets for user input
entry_1 = tk.Entry(root, width=50, bg='#F1F0E8')
entry_1.pack(ipady=6, pady=(1,18))


label_2 = tk.Label(root, text="Enter Your Second Content", fg='white', bg='#33BBC5')
label_2.pack(pady=(10,10))
label_2.config(font=('Verdana', 14))

entry_2 = tk.Entry(root, width=50, bg='#F1F0E8')
entry_2.pack(ipady=6, pady=(1,18))

# Function to compute cosine similarity
def calculator_cosine_similarity(text1, text2):
    #Tokenize the input text
    words1 = text1.split()
    words2 = text2.split()

    #create a set of all unique words in both text
    intersection = set(words1 + words2)
    numerator = sum(words1.count(word) * words2.count(word) for word in intersection)

    #calculate the magnitudes of the vectors
    magnitude1 = math.sqrt(sum(words1.count(word) ** 2 for word in intersection))
    magnitude2 = math.sqrt(sum(words2.count(word) ** 2 for word in intersection))

    # Calculate the cosine similarity
    cosine_sim = numerator / (magnitude1 * magnitude2)

    return cosine_sim

# Function to calculate and display similarities
def calculate_similarity():
    # Get the text from the user
    text1 = entry_1.get()
    text2 = entry_2.get()

    #Calculate cosine similarity
    cosine_sim = calculator_cosine_similarity(text1, text2)

    # Calculate Jaccard similarity
    words1 = set(text1.split())
    words2 = set(text2.split())

    intersection2 = len(words1.intersection(words2))
    union = len(words1.union(words2))

    if union == 0:
        jaccard_sim = 0.0
    else:
        jaccard_sim = intersection2 / union

    # Display the results
    result_cosine.config(text=f"Cosine Similarity: {cosine_sim:.2f}")
    result_jaccard.config(text=f"Jaccard Similarity: {jaccard_sim:.2f}")

# Create a button to calculate similarities
calculate_btn = tk.Button(root, text="Calculate Similarity", bg='#E3DFFD', fg='black', width=20, height=2, command=calculate_similarity)
calculate_btn.pack(pady=(10,20))
calculate_btn.config(font=('verdana', 10))

# Create labels to display the results
result_cosine = tk.Label(root, text="", bg='#468B97')
result_cosine.pack()
result_cosine.config(font=22)

result_jaccard = tk.Label(root, text="", bg='#A1CCD1')
result_jaccard.pack()
result_jaccard.config(font=22)

#label for the author name
text_label = tk.Label(root,text='@Md. Samiul Islam', fg='#F2F7A1', bg='#0A4D68') #add txt with background & forground color
text_label.pack(pady=(20,10))
text_label.config(font=('verdana', 8))

root.mainloop()

