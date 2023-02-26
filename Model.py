import random
from tkinter import filedialog


class Model:

    def __init__(self):
        self.file_path = None
        self.longest_name = 0
        self.names_tasks = []
        self.names = []
        self.tasks = []
        self.is_tasks = False

    def open_file(self):
        self.file_path = filedialog.askopenfilename()

    def read_file(self, is_btn):
        if is_btn == 'names':
            self.names = []
        elif is_btn == 'tasks':
            self.tasks = []
        f = open(self.file_path, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if is_btn == 'names':
                self.names.append(line)
                if len(line) > self.longest_name:
                    self.longest_name = len(line)
            elif is_btn == 'tasks':
                self.tasks.append(line)
        f.close()

    def mix_tasks_for_names(self):
        self.names_tasks = []
        random.shuffle(self.tasks)
        x = 0
        for s in self.names:
            self.names_tasks.append(str(s).ljust(self.longest_name) + " - " + self.tasks[x])
            x += 1

    def set_tasks(self):
        if len(self.tasks) < len(self.names):
            self.is_tasks = False
        else:
            self.is_tasks = True
