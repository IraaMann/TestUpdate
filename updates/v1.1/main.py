import tkinter as tk
from tkinter import messagebox
import requests
import json

class MyApp:
    def __init__(self):
        self.version = "1.1"  # Updated version
        self.github_version_url = "https://raw.githubusercontent.com/IraaMann/TestUpdate/main/version.json"

        # Create main window
        self.root = tk.Tk()
        self.root.title(f"My App v{self.version}")
        self.root.geometry("300x200")

        # Welcome label with new text
        label = tk.Label(self.root, text="Welcome to My Updated App!")
        label.pack(pady=20)

        # Test button with new text
        button = tk.Button(self.root, text="New Button!", command=self.button_click)
        button.pack(pady=10)

        # Check Update button
        update_button = tk.Button(self.root, text="Check for Updates", 
                                command=self.check_update)
        update_button.pack(pady=10)

        # Version label
        version_label = tk.Label(self.root, text=f"Version: {self.version}")
        version_label.pack(side=tk.BOTTOM, pady=10)

    def button_click(self):
        messagebox.showinfo("Hello!", "This is the updated version 1.1!")

    def check_update(self):
        try:
            response = requests.get(self.github_version_url)
            data = response.json()
            latest_version = data['latest_version']

            if latest_version > self.version:
                update_msg = f"New version {latest_version} available!\n\nChangelog:\n"
                for change in data['changelog']:
                    update_msg += f"• {change}\n"

                if messagebox.askyesno("Update Available", 
                    update_msg + "\nWould you like to update?"):
                    self.download_update(data['download_url'])
            else:
                messagebox.showinfo("Up to Date", 
                    "You have the latest version!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to check for updates: {str(e)}")

    def download_update(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open("main.py", "w", encoding='utf-8') as f:
                    f.write(response.text)
                messagebox.showinfo("Success", "Update downloaded! Please restart the application.")
                self.root.quit()
            else:
                messagebox.showerror("Error", "Failed to download update")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download update: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()
