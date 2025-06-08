import wx
import subprocess
import os
import sqlite3
import pygame 

class SetupApp(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Django Setup", size=(400, 450))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        pygame.mixer.init()
        music_path = "keygen.mp3"
        if os.path.exists(music_path):
            try:
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play(-1) 
            except Exception as e:
                print(f"Failed to play music: {e}")

        # Load and display image
        image_path = "hit237_logo.png"
        if os.path.exists(image_path):
            img = wx.Image(image_path, wx.BITMAP_TYPE_PNG)
            img = img.Scale(300, 150, wx.IMAGE_QUALITY_HIGH)
            bitmap = wx.StaticBitmap(panel, bitmap=wx.Bitmap(img))
            vbox.Add(bitmap, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        self.status = wx.StaticText(panel, label="Ready to set up your Django project.")
        vbox.Add(self.status, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        btn = wx.Button(panel, label="Setup!")
        btn.Bind(wx.EVT_BUTTON, self.on_setup)
        vbox.Add(btn, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_setup(self, event):
        self.status.SetLabel("Running setup...")
        wx.Yield()

        try:

            self.status.SetLabel("Installing dependencies...")
            wx.Yield()
            subprocess.check_call(["python", "-m", "pip", "install", "-r", "requirements.txt"])


            self.status.SetLabel("Applying migrations...")
            wx.Yield()
            subprocess.check_call(["python", "manage.py", "makemigrations"])
            subprocess.check_call(["python", "manage.py", "migrate"])


            self.status.SetLabel("Seeding database...")
            wx.Yield()
            with open("seed_data.sql", "r") as f:
                sql = f.read()
            conn = sqlite3.connect("db.sqlite3")
            cursor = conn.cursor()
            cursor.executescript(sql)
            conn.commit()
            conn.close()


            self.status.SetLabel("Creating admin user...")
            wx.Yield()
            subprocess.check_call(["python", "setup/create_admin.py"])

            self.status.SetLabel("Setup complete.")
        except subprocess.CalledProcessError as e:
            self.status.SetLabel(f"Setup failed: {e}")
        except Exception as e:
            self.status.SetLabel(f"Error: {str(e)}")

    def on_close(self, event):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = SetupApp()
    app.MainLoop()
