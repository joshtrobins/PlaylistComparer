import datetime
import os

import PlaylistAnalyzer

full_path = input("Path: ").strip("\"")
for directory in os.scandir(full_path):
    recent_date = datetime.date.min
    recent_file = ""
    if directory.is_dir():
        for file in os.scandir(directory):
            if file.name.endswith("csv"):
                date = datetime.datetime.strptime(file.name[18:26], "%m%d%Y").date()
                if date > recent_date:
                    recent_date = date
                    recent_file = file
        print("Analyzing \"" + directory.name + "\" from archive \"" + str(recent_date) + "\"")
        PlaylistAnalyzer.analyze(recent_file.path)
print("Done")
