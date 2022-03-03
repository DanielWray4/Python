# Workflow.py
import webbrowser
import os

#The open.new function will open the first webpage in the default web browser
webbrowser.open_new("https://www.google.co.uk")

#The open_new_tab function will open the following webpage in the already open default browser
webbrowser.open_new_tab("https://www.facebook.com")

webbrowser.open_new_tab("https://www.github.com")

#os.system can be used to open .exe applications. 
os.system("start outlook")
