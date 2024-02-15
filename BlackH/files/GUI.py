import os
import tkinter as tk
from tkinter import scrolledtext
import subprocess

def inject_exploit():
    subprocess.run(["exploit.exe", "--inject"])
    open_file()

def execute_script(script_content):
    with open("script.lua", "w") as f:
        f.write(script_content)
    subprocess.run(["exploit.exe", "--exec", "script.lua"])
    open_file()

def make_fly():
    script = """
    local Player = game:GetService("Players").LocalPlayer
    local Character = Player.Character or Player.CharacterAdded:Wait()
    local Humanoid = Character:WaitForChild("Humanoid")

    Humanoid.PlatformStand = false
    Humanoid:ChangeState(11)
    """
    execute_script(script)

def bypass_anticheat():
    script = """
    -- Insert your bypass script here
    """
    execute_script(script)

def kill_process():
    subprocess.run(["taskkill", "/f", "/im", "roblox.exe"])
    open_file()

def open_website():
    subprocess.run(["start", "https://www.roblox.com"])
    open_file()

def open_file():
    file_path = os.path.join(os.path.dirname(__file__), "BlackHawkFiles")
    subprocess.run(["notepad.exe", file_path])

# Create the main window
root = tk.Tk()
root.title("BlackH")
root.configure(bg="black")

# Create text widget for script writing
script_text = scrolledtext.ScrolledText(root, width=50, height=10, bg="white", fg="black")
script_text.pack(pady=10)

# Create buttons for exploit commands
inject_button = tk.Button(root, text="Inject Exploit", command=inject_exploit, bg="red", fg="white")
inject_button.pack(side=tk.LEFT, padx=10)

execute_button = tk.Button(root, text="Execute Script", command=lambda: execute_script(script_text.get("1.0", tk.END)), bg="green", fg="white")
execute_button.pack(side=tk.LEFT, padx=10)

make_fly_button = tk.Button(root, text="Make Me Fly", command=make_fly, bg="blue", fg="white")
make_fly_button.pack(side=tk.LEFT, padx=10)

bypass_button = tk.Button(root, text="Bypass Anticheat 😈", command=bypass_anticheat, bg="black", fg="red")
bypass_button.pack(side=tk.LEFT, padx=10)

kill_button = tk.Button(root, text="Kill Roblox Process", command=kill_process, bg="yellow", fg="black")
kill_button.pack(side=tk.LEFT, padx=10)

open_button = tk.Button(root, text="Open Roblox Website", command=open_website, bg="orange", fg="black")
open_button.pack(side=tk.LEFT, padx=10)

# Run the GUI
root.mainloop()
