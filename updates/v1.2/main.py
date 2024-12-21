import tkinter as tk
from tkinter import messagebox, ttk
import requests
import json
from datetime import datetime

class MyApp:
    def __init__(self):
        self.version = "1.2"  # Updated version
        self.github_version_url = "https://raw.githubusercontent.com/IraaMann/TestUpdate/main/version.json"

        # Create main window with new theme
        self.root = tk.Tk()
        self.root.title(f"My App v{self.version}")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')

        # Create main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Welcome label with new styling
        label = tk.Label(main_frame, 
                        text="Welcome to Version 1.2!", 
                        font=('Arial', 16, 'bold'),
                        bg='#f0f0f0',
                        fg='#2c3e50')
        label.pack(pady=20)

        # New feature: Time display
        self.time_label = tk.Label(main_frame,
                                 font=('Arial', 12),
                                 bg='#f0f0f0',
                                 fg='#34495e')
        self.time_label.pack(pady=10)
        self.update_time()

        # New feature: Progress bar
        self.progress = ttk.Progressbar(main_frame, 
                                      length=200, 
                                      mode='determinate')
        self.progress.pack(pady=20)

        # Feature button with new styling
        button = tk.Button(main_frame, 
                          text="Show Features", 
                          command=self.show_features,
                          bg='#3498db',
                          fg='white',
                          font=('Arial', 10, 'bold'),
                          relief='flat',
                          padx=20,
                          pady=10)
        button.pack(pady=10)

        # Check Update button with new styling
        update_button = tk.Button(main_frame, 
                                text="Check for Updates", 
                                command=self.check_update,
                                bg='#2ecc71',
                                fg='white',
                                font=('Arial', 10, 'bold'),
                                relief='flat',
                                padx=20,
                                pady=10)
        update_button.pack(pady=10)

        # New feature: Status display
        self.status_label = tk.Label(main_frame,
                                   text="Status: Ready",
                                   font=('Arial', 10),
                                   bg='#f0f0f0',
                                   fg='#7f8c8d')
        self.status_label.pack(pady=10)

        # Version label with new styling
        version_label = tk.Label(main_frame, 
                               text=f"Version: {self.version}",
                               font=('Arial', 10),
                               bg='#f0f0f0',
                               fg='#95a5a6')
        version_label.pack(side=tk.BOTTOM, pady=10)

        # Start progress bar animation
        self.animate_progress()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)

    def animate_progress(self):
        current = self.progress['value']
        if current >= 100:
            self.progress['value'] = 0
        else:
            self.progress['value'] += 1
        self.root.after(100, self.animate_progress)

    def show_features(self):
        features = """New Features in v1.2:
• Real-time clock display
• Animated progress bar
• Status indicator
• Modern UI design
• Improved performance"""
        messagebox.showinfo("Version 1.2 Features", features)

    def check_update(self):
        self.status_label.config(text="Status: Checking for updates...")
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
                self.status_label.config(text="Status: Up to date")
                messagebox.showinfo("Up to Date", 
                    "You have the latest version!")

        except Exception as e:
            self.status_label.config(text="Status: Update check failed")
            messagebox.showerror("Error", f"Failed to check for updates: {str(e)}")

def download_update(self, url):
    try:
        print(f"Attempting to download from: {url}")  # Debug print
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")  # Debug print
        if response.status_code == 200:
            with open("main.py", "w", encoding='utf-8') as f:
                f.write(response.text)
            messagebox.showinfo("Success", "Update downloaded! Please restart the application.")
            self.root.quit()
        else:
            print(f"Failed with status code: {response.status_code}")  # Debug print
            messagebox.showerror("Error", f"Failed to download update: Status {response.status_code}")
    except Exception as e:
        print(f"Exception occurred: {str(e)}")  # Debug print
        messagebox.showerror("Error", f"Failed to download update: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()
