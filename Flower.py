
import turtle
import random
import tkinter as tk
from tkinter import messagebox

# Function to draw a flower using turtle
def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("pink")
    pen = turtle.Turtle()
    pen.speed(0)
    
    colors = ["red", "purple", "violet", "magenta", "orange"]
    
    for i in range(36):
        pen.color(random.choice(colors))
        pen.circle(100)
        pen.right(10)

    # Draw a stem
    pen.color("green")
    pen.right(90)
    pen.forward(200)
    pen.left(90)

    # Draw leaves
    for _ in range(2):
        pen.begin_fill()
        pen.color("lightgreen")
        pen.circle(40, 90)
        pen.left(90)
        pen.circle(40, 90)
        pen.end_fill()
        pen.left(180)

    pen.hideturtle()
    turtle.done()

# Function to create the Yes/No pop-up
def yes_no_popup():
    def move_no_button(event):
        """Moves the 'No' button to a random position"""
        new_x = random.randint(50, 300)
        new_y = random.randint(50, 300)
        no_button.place(x=new_x, y=new_y)

    def yes_clicked():
        """Displays a love message when 'Yes' is clicked"""
        messagebox.showinfo("Yay!", "I knew you'd say Yes! ❤️ Happy Valentine's!")
        root.destroy()

    # Create pop-up window
    root = tk.Tk()
    root.title("Valentine's Question")
    root.geometry("400x400")
    root.config(bg="lightpink")

    # Add label with question
    label = tk.Label(root, text="Will you be my Valentine? 💕", font=("Arial", 14), bg="lightpink")
    label.pack(pady=50)

    # Create buttons
    yes_button = tk.Button(root, text="Yes", font=("Arial", 12), command=yes_clicked)
    yes_button.place(x=120, y=200)

    no_button = tk.Button(root, text="No", font=("Arial", 12))
    no_button.place(x=200, y=200)
    no_button.bind("<Enter>", move_no_button)  # Move 'No' when hovered

    root.mainloop()

# Run both functions
if __name__ == "__main__":
    draw_flower()
    yes_no_popup()

# Function to move the "No" button away
def move_no_button(event):
    new_x = random.randint(50, 300)
    new_y = random.randint(150, 300)
    no_button.place(x=new_x, y=new_y)

# Function when "Yes" is clicked
def yes_clicked():
    message_label.config(text="Yay! 💖 Happy Valentine's Day! 💖", fg="red")
    yes_button.place_forget()
    no_button.place_forget()

# Create main window
root = tk.Tk()
root.title("Valentine's Surprise")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="pink")

# Create a Canvas for the flower animation
canvas = tk.Canvas(root, width=400, height=200, bg="pink", highlightthickness=0)
canvas.pack()

# Draw the flower (simple)
canvas.create_oval(160, 50, 240, 130, fill="red")  # Petal 1
canvas.create_oval(120, 90, 200, 170, fill="red")  # Petal 2
canvas.create_oval(200, 90, 280, 170, fill="red")  # Petal 3
canvas.create_oval(160, 130, 240, 210, fill="red")  # Petal 4
canvas.create_oval(180, 90, 220, 130, fill="yellow")  # Flower center
canvas.create_line(200, 210, 200, 350, fill="green", width=5)  # Stem
canvas.create_oval(170, 270, 210, 310, fill="green")  # Leaf Left
canvas.create_oval(190, 270, 230, 310, fill="green")  # Leaf Right

# Question label
question_label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 14, "bold"), bg="pink")
question_label.pack(pady=10)

# Buttons
yes_button = tk.Button(root, text="Yes", font=("Arial", 12, "bold"), bg="lightgreen", command=yes_clicked)
yes_button.place(x=120, y=300)

no_button = tk.Button(root, text="No", font=("Arial", 12, "bold"), bg="red")
no_button.place(x=220, y=300)
no_button.bind("<Enter>", move_no_button)  # Move the button when hovered

# Message label
message_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="pink")
message_label.pack(pady=20)

# Credit label
credit_label = tk.Label(root, text="By Jmadthemaedenless", font=("Arial", 10, "italic"), bg="pink", fg="black")
credit_label.pack(side="bottom", pady=10)

# Run the Tkinter loop
root.mainloop()		
