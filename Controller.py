import os
from tkinter import INSERT, messagebox, END, filedialog

from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        self.absolute_path = os.path.dirname(__file__)
        self.is_btn = None

    def click_btn_names(self):
        self.view.txt_names.delete('1.0', END)
        self.model.open_file()
        if self.model.file_path:
            self.is_btn = 'names'
            self.model.read_file(self.is_btn)
            for line in self.model.names:
                self.view.txt_names.insert(INSERT, line + '\n')
        else:
            messagebox.showwarning("NB!", "Sa ei valinud õpilaste nimekirja. \n Nimekirja valimine on vajalik!")

    def click_btn_tasks(self):
        self.view.txt_tasks.delete('1.0', END)
        self.model.open_file()
        if self.model.file_path:
            self.is_btn = 'tasks'
            self.model.read_file(self.is_btn)
            for line in self.model.tasks:
                self.view.txt_tasks.insert(INSERT, line + '\n')
        else:
            messagebox.showwarning('NB!', 'Sa ei valinud ülesannete nimekirja! \n Nimekirja valimine on vajalik!')

    def click_btn_together(self):
        self.view.txt_together.delete('1.0', END)
        self.model.set_tasks()
        if self.model.is_tasks:
            self.model.mix_tasks_for_names()
            for line in self.model.names_tasks:
                self.view.txt_together.insert(INSERT, line + '\n')
        else:
            messagebox.showwarning('NB!', 'Selles nimekirjas on liiga vähe ülesandeid. \n Ülesandeid ei jätku kõigile. '
                                          '\n Palun vali uus ja pikem nimekiri!')

    def click_btn_save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('AllFiles', '*.*'),
                                                                                   ('txt file', '*.txt'),
                                                                                   ('csv file', '*.csv')],
                                     initialdir=self.absolute_path, title='Salvesta ülesannetete fail')
        if f:
            tasks_save = str(self.view.txt_together.get(1.0, END))
            f.write(tasks_save)
            f.close()
        else:
            messagebox.showwarning('NB!', 'Salvestamine ei õnnestunud. \n Palun proovi uuesti.')

    def main(self):
        self.view.main()
