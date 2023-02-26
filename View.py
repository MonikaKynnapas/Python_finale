from tkinter import *


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model
        self.geometry('1330x490')
        self.title('Viimane kodune töö')

        self.frame_top, self.frame_middle, self.frame_bottom = self.create_frames()
        self.btn_names, self.btn_tasks, self.btn_together, self.btn_save = self.create_buttons()
        self.txt_names, self.txt_tasks, self.txt_together = self.create_textboxes()

    def create_frames(self):
        frame_top = Frame(self, bg='#fcfc6f')
        frame_middle = Frame(self, bg='#fcfc6f')
        frame_bottom = Frame(self, bg='#fcfc6f')

        frame_top.pack(fill=BOTH)
        frame_middle.pack(expand=True, fill=BOTH)
        frame_bottom.pack(expand=True, fill=BOTH)
        return frame_top, frame_middle, frame_bottom

    def create_buttons(self):
        btn_names = Button(self.frame_top, text='Vajuta, et valida nimekiri', height=2, width=25,
                           command=self.controller.click_btn_names)
        btn_tasks = Button(self.frame_top, text='Vajuta, et valida ülesanded', height=2, width=25,
                           command=self.controller.click_btn_tasks)
        btn_together = Button(self.frame_top, text='Vajuta, et määrata nimedele ülesanded', height=2, width=30,
                              command=self.controller.click_btn_together)
        btn_save = Button(self.frame_bottom, text='Salvesta nimede ja ülesannete loend', height=2, width=30,
                          command=self.controller.click_btn_save)
        btn_names.grid(row=0, column=0, padx=10, pady=10)
        btn_tasks.grid(row=0, column=1, padx=130, pady=10)
        btn_together.grid(row=0, column=2, padx=200, pady=10)
        btn_save.grid(row=4, column=0, padx=850, pady=10)
        return btn_names, btn_tasks, btn_together, btn_save

    def create_textboxes(self):
        txt_names = Text(self.frame_middle, height=22, width=25)
        txt_tasks = Text(self.frame_middle, height=22, width=55)
        txt_together = Text(self.frame_middle, height=22, width=80, wrap='none')

        txt_names.grid(row=0, column=0, padx=5, pady=7)
        txt_tasks.grid(row=0, column=1, padx=5, pady=7)
        txt_together.grid(row=0, column=2, padx=5, pady=7)

        return txt_names, txt_tasks, txt_together

    def main(self):
        self.mainloop()
