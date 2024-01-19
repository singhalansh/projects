import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import mysql.connector


class DatabaseManager:
    def __init__(self):
        # Connect to the MySQL database (replace with your actual database details)
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jaishreeram",
            database="password_manager"
        )
        self.mycursor = self.mydb.cursor()

    def __del__(self):
        # Close the cursor and connection when the object is deleted
        self.mycursor.close()
        self.mydb.close()


class PasswordManager:
    def __init__(self, root, db_manager):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("500x500")  # Set initial window size
        self.style = Style(theme='superhero')
        self.db_manager = db_manager

        # Entry variables
        self.website_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Set custom style for labels and buttons
        self.style.configure('TLabel', font=('Helvetica', 12))  # Set label font size
        self.style.configure('TButton', font=('Helvetica', 12))  # Set button font size

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for website
        website_label = ttk.Label(self.root, text="Website:")
        website_entry = ttk.Entry(self.root, textvariable=self.website_var)

        # Label and Entry for username
        username_label = ttk.Label(self.root, text="Username:")
        username_entry = ttk.Entry(self.root, textvariable=self.username_var)

        # Label and Entry for password
        password_label = ttk.Label(self.root, text="Password:")
        password_entry = ttk.Entry(self.root, show="*", textvariable=self.password_var)

        # Button to add password
        add_button = ttk.Button(self.root, text="Add Password", command=self.add_password)

        # Button to open another window
        open_window_button = ttk.Button(self.root, text="Manage passwords", command=self.open_another_window)

        # Grid layout
        website_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        website_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        add_button.grid(row=3, column=0, columnspan=2, pady=10)
        open_window_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_password(self):
        # Retrieve values from Entry widgets
        website = self.website_var.get()
        username = self.username_var.get()
        password = self.password_var.get()

        # Insert data into the 'passwords' table
        insert_query = "INSERT INTO passwords (website, username, password) VALUES (%s, %s, %s)"
        data = (website, username, password)

        try:
            self.db_manager.mycursor.execute(insert_query, data)
            self.db_manager.mydb.commit()
            self.db_manager.mycursor.execute("SELECT * FROM passwords")
            passwords = self.db_manager.mycursor.fetchall()
            if passwords:
                messagebox.showinfo("Passwords", "Passwords saved successfully")
            else:
                messagebox.showinfo("No Passwords", "No passwords saved.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        # Clear the Entry widgets after adding the password
        self.website_var.set("")
        self.username_var.set("")
        self.password_var.set("")

    def open_another_window(self):
        # Destroy the current window
        self.root.destroy()

        # Create and run another window
        win = tk.Tk()
        WebsiteUsernamesViewer(win, self.db_manager)
        win.mainloop()


class WebsiteUsernamesViewer:
    def __init__(self, root, db_manager):
        self.root = root
        self.root.title("Website Usernames Viewer")
        self.root.geometry("400x300")  # Set initial window size
        self.style = Style(theme='superhero')
        self.db_manager = db_manager

        # Entry variable
        self.website_var = tk.StringVar()

        # Set custom style for labels and buttons
        self.style.configure('TLabel', font=('Helvetica', 12))  # Set label font size
        self.style.configure('TButton', font=('Helvetica', 12))  # Set button font size

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for website
        website_label = ttk.Label(self.root, text="Website:")
        website_entry = ttk.Entry(self.root, textvariable=self.website_var)

        # Button to show usernames
        show_usernames_button = ttk.Button(self.root, text="Show Usernames", command=self.show_usernames)

        # Text widget to display usernames
        self.usernames_text = tk.Text(self.root, height=10, width=40, wrap=tk.WORD)

        # Grid layout
        website_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        website_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        show_usernames_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.usernames_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def show_usernames(self):
        # Retrieve the website name
        website_name = self.website_var.get()

        # Fetch usernames from the database based on the website name
        select_query = "SELECT username, password FROM passwords WHERE website = %s"
        data = (website_name,)

        try:
            self.db_manager.mycursor.execute(select_query, data)
            fetched_data = self.db_manager.mycursor.fetchall()

            if fetched_data:
                # Display fetched data in the Text widget
                self.usernames_text.delete(1.0, tk.END)  # Clear previous content
                for row in fetched_data:
                    self.usernames_text.insert(tk.END, f"Username: {row[0]}\nPassword: {row[1]}\n\n")
            else:
                self.usernames_text.delete(1.0, tk.END)
                self.usernames_text.insert(tk.END, "No data found for the specified website.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    # Create a DatabaseManager instance to manage database connections
    db_manager = DatabaseManager()

    # Create the Tkinter window for PasswordManager
    root = tk.Tk()
    app = PasswordManager(root, db_manager)
    root.mainloop()
