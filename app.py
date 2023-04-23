import os
import sys
import tkinter as tk
from tkinter import ttk, LEFT, TOP, X, font, BOTH, RIGHT, Y, END
from tkinter.messagebox import askyesnocancel
from tkinter.ttk import Combobox


# ------------------------------------------- RESOURCE PATH FUNCTION -------------------------------------------------#

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# --------------------------------------------- APP CLASS ------------------------------------------------------------#

class App(tk.Tk):
    """
    App is the main class of the project
    """

    def __init__(self, container=None):
        super().__init__()

        # Setting up initial configurations
        self.title("Test application")
        self.geometry("800x600+10+10")
        self.resizable(False, False)
        self.icon = tk.PhotoImage(file=resource_path("icons/icon.png"))
        self.iconphoto(False, self.icon)
        self.style = ttk.Style()
        self.style.theme_use("vista")

        # Initialize Frames
        self.frames = {}
        self.Menu = Menu
        self.Toolbar = Toolbar
        self.Textarea = Textarea(parent=self)
        self.Statusbar = Statusbar

        # Defining frames and packing it
        for F in {Menu, Toolbar, Textarea, Statusbar}:
            frame = F(self, container)
            self.frames[F] = frame

        self.show_frame(Menu)
        self.show_frame(Toolbar)
        self.show_frame(Textarea)
        self.show_frame(Statusbar)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame_classname = frame.__class__.__name__
        match frame_classname:
            case 'Menu':
                menubar = frame.create_menubar(self)
                self.configure(menu=menubar)
            case 'Toolbar':
                frame.create_toolbar(self)
            case 'Textarea':
                frame.create_textarea(self)
            case 'Statusbar':
                frame.create_statusbar(self)
        frame.tkraise()


# -------------------------------------------- MENU CLASS -----------------------------------------------------------#

class Menu(tk.Menu):
    """
    This class defines menubar that is used in the main app
    """

    def __init__(self, parent, container=None):
        super().__init__(container)
        # Themes menu buttons images intialize
        self.light_theme_img = tk.PhotoImage(file=(resource_path("icons/light_default.png")))
        self.light_plus_theme_img = tk.PhotoImage(file=(resource_path("icons/light_plus.png")))
        self.dark_theme_img = tk.PhotoImage(file=(resource_path("icons/dark.png")))
        self.cake_theme_img = tk.PhotoImage(file=(resource_path("icons/cake.png")))
        self.monokai_theme_img = tk.PhotoImage(file=(resource_path("icons/monokai.png")))
        self.windows_theme_img = tk.PhotoImage(file=(resource_path("icons/windows.png")))
        # Themes menu "choice" variable initialize
        self.theme_choice = tk.StringVar()

        # View menu buttons images initialize
        self.tool_img = tk.PhotoImage(file=resource_path("icons/tool_bar.png"))
        self.status_img = tk.PhotoImage(file=resource_path("icons/status_bar.png"))
        # View menu "show" variables initialize
        self.show_toolbar = tk.BooleanVar()
        self.show_statusbar = tk.BooleanVar()

        # Edit menu button images initialize
        self.undo_img = tk.PhotoImage(file=resource_path("icons/undo.png"))
        self.cut_img = tk.PhotoImage(file=resource_path("icons/cut.png"))
        self.copy_img = tk.PhotoImage(file=resource_path("icons/copy.png"))
        self.paste_img = tk.PhotoImage(file=resource_path("icons/paste.png"))
        self.select_img = tk.PhotoImage(file=resource_path("icons/all.png"))
        self.clear_img = tk.PhotoImage(file=resource_path("icons/clear_all.png"))
        self.find_img = tk.PhotoImage(file=resource_path("icons/find.png"))
        self.schedule_img = tk.PhotoImage(file=resource_path("icons/schedule.png"))

        # File menu button images initialize
        self.new_img = tk.PhotoImage(file=resource_path("icons/new.png"))
        self.open_img = tk.PhotoImage(file=resource_path("icons/open.png"))
        self.save_img = tk.PhotoImage(file=resource_path("icons/save.png"))
        self.print_img = tk.PhotoImage(file=resource_path("icons/print.png"))
        self.save_as_img = tk.PhotoImage(file=resource_path("icons/save_as.png"))
        self.exit_img = tk.PhotoImage(file=resource_path("icons/exit.png"))

        # App instance initialization
        self.MenuFunctionality = MenuFunctionality()

    def create_menubar(self, parent):
        """
        Method to create a menubar
        :param parent:
        :return: menubar
        """
        menubar = tk.Menu(parent)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # File menu commands
        file_menu.add_command(label="New", accelerator="Ctrl+N", image=self.new_img, compound=LEFT,
                              command=self.MenuFunctionality.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", image=self.open_img, compound=LEFT)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", image=self.save_img, compound=LEFT)
        file_menu.add_command(label="Save As", accelerator="Ctrl+Alt+S", image=self.save_as_img, compound=LEFT)
        file_menu.add_command(label="Print", accelerator="Ctrl+P", image=self.print_img, compound=LEFT)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", image=self.exit_img, compound=LEFT)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Edit menu commands
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", image=self.undo_img, compound=LEFT)
        edit_menu.add_command(label="Cut", accelerator="Ctrl+Z", image=self.cut_img, compound=LEFT)
        edit_menu.add_command(label="Copy", accelerator="Ctrl+Z", image=self.copy_img, compound=LEFT)
        edit_menu.add_command(label="Paste", accelerator="Ctrl+Z", image=self.paste_img, compound=LEFT)
        edit_menu.add_command(label="Select all", accelerator="Ctrl+Z", image=self.select_img, compound=LEFT)
        edit_menu.add_command(label="Clear", accelerator="Ctrl+Z", image=self.clear_img, compound=LEFT)
        edit_menu.add_command(label="Find", accelerator="Ctrl+Z", image=self.find_img, compound=LEFT)
        edit_menu.add_command(label="Time/Date", accelerator="Ctrl+Z", image=self.schedule_img, compound=LEFT)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)

        # View menu commands
        view_menu.add_checkbutton(label="Tool bar", variable=self.show_toolbar, onvalue=True, offvalue=False,
                                  image=self.tool_img,
                                  compound=LEFT, command='')
        view_menu.add_checkbutton(label="Status bar", variable=self.show_statusbar, onvalue=True, offvalue=False,
                                  image=self.status_img,
                                  compound=LEFT, command='')
        self.show_toolbar.set(True)
        self.show_statusbar.set(True)

        # Themes menu
        themes_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Themes", menu=themes_menu)

        # Themes menu commands
        themes_menu.add_radiobutton(label="Light default", variable=self.theme_choice, image=self.light_theme_img,
                                    compound=LEFT,
                                    command='')
        themes_menu.add_radiobutton(label="Light plus", variable=self.theme_choice, image=self.light_plus_theme_img,
                                    compound=LEFT,
                                    command='')
        themes_menu.add_radiobutton(label="Dark", variable=self.theme_choice, image=self.dark_theme_img,
                                    compound=LEFT,
                                    command='')
        themes_menu.add_radiobutton(label="Cake", variable=self.theme_choice, image=self.cake_theme_img,
                                    compound=LEFT,
                                    command='')
        themes_menu.add_radiobutton(label="Monokai", variable=self.theme_choice, image=self.monokai_theme_img,
                                    compound=LEFT,
                                    command='')
        themes_menu.add_radiobutton(label="Windows 98", variable=self.theme_choice, image=self.windows_theme_img,
                                    compound=LEFT,
                                    command='')

        return menubar


# --------------------------------------------- TOOLBAR CLASS --------------------------------------------------------#

class Toolbar(tk.Frame):
    """
    Class to define a toolbar
    """

    def __init__(self, parent, container):
        super().__init__(container)
        # Font families combobox variables initialize
        self.font_families = font.families()
        self.font_families_variable = tk.StringVar()

        # Font size combobox variables intialize
        self.fontsize = tuple(range(8, 72, 2))
        self.fontsize_variable = tk.IntVar()

        # Buttons images initialize
        self.bold_img = tk.PhotoImage(file=resource_path("icons/bold.png"))
        self.italic_img = tk.PhotoImage(file=resource_path("icons/italic.png"))
        self.underline_img = tk.PhotoImage(file=resource_path("icons/underline.png"))
        self.font_color_img = tk.PhotoImage(file=resource_path("icons/font_color.png"))
        self.left_align_img = tk.PhotoImage(file=resource_path("icons/left.png"))
        self.center_align_img = tk.PhotoImage(file=resource_path("icons/center.png"))
        self.right_align_img = tk.PhotoImage(file=resource_path("icons/right.png"))

    def create_toolbar(self, parent):
        """
        Method to creat a toolbar
        :param parent:
        :return: toolbar
        """
        toolbar = tk.Frame(parent)
        toolbar.pack(side=TOP, fill=X)

        # Font families combobox
        fontfamily_combobox = Combobox(toolbar, width=30, values=self.font_families, state='readonly',
                                       textvariable=self.font_families_variable)
        fontfamily_combobox.grid(row=0, column=0, padx=5)
        fontfamily_combobox.current(self.font_families.index('Arial'))

        # Font families combobox selected event
        # fontfamily_combobox.bind('<<ComboboxSelected>>', set_font_style) DESCOMENTAR AL CREAR FUNCION

        # Font size combobox
        fontsize_combobox = Combobox(toolbar, width=15, values=self.fontsize, state='readonly',
                                     textvariable=self.fontsize_variable)
        fontsize_combobox.grid(row=0, column=1, padx=5)
        fontsize_combobox.current(2)

        # Font size combobox selected event
        # font_size_combobox.bind('<<ComboboxSelected>>', set_font_size) DESCOMENTAR AL CREAR FUNCION

        # Text transformation buttons
        bold_btn = tk.Button(toolbar, image=self.bold_img)
        bold_btn.grid(row=0, column=2, padx=5)
        italic_btn = tk.Button(toolbar, image=self.italic_img)
        italic_btn.grid(row=0, column=3, padx=5)
        underline_btn = tk.Button(toolbar, image=self.underline_img)
        underline_btn.grid(row=0, column=4, padx=5)
        font_color_btn = tk.Button(toolbar, image=self.font_color_img)
        font_color_btn.grid(row=0, column=5, padx=5)
        left_align_btn = tk.Button(toolbar, image=self.left_align_img)
        left_align_btn.grid(row=0, column=6, padx=5)
        center_align_btn = tk.Button(toolbar, image=self.center_align_img)
        center_align_btn.grid(row=0, column=7, padx=5)
        right_align_btn = tk.Button(toolbar, image=self.center_align_img)
        right_align_btn.grid(row=0, column=8, padx=5)

        # DEFINIR DE QUE MANERA VOY A ALMACENAR LOS BOTONES Y SI SU USO ES CORRECTO
        # buttons = [bold_button, italic_button, underline_button, fontcolor_button, leftalign_button, centeralign_button,
        #            rightalign_button]
        #
        # for button in buttons:
        #     button.config(bg='#F5FBEF', cursor='hand2', relief='ridge')

        return toolbar


# --------------------------------------------- TEXTAREA CLASS -------------------------------------------------------#

class Textarea(tk.Frame, tk.Text):
    """
    Class to define a textarea
    """

    def __init__(self, parent=None, container=None):
        super().__init__(container)
        self.scrollbar = tk.Scrollbar(parent)
        self.textarea = tk.Text(parent, undo=True, yscrollcommand=self.scrollbar.set, font=('arial', 12))

    def create_textarea(self, parent):
        """
        Create text area function
        :param parent:
        :return: textarea
        """
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.textarea.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=self.textarea.yview)

        # Modified event. DESCOMENTAR CUANDO CREE LA FUNCION
        # textarea.bind('<<Modified>>', status_bar)

        return self.textarea


# --------------------------------------------- STATUSBAR CLASS ------------------------------------------------------#

class Statusbar(tk.Frame):

    def __init__(self, parent, container):
        super().__init__(container)

    def create_statusbar(self, parent):
        statusbar = tk.Frame(parent)

        return statusbar


# --------------------------------------------- MENUFUNCTIONALITY CLASS ----------------------------------------------#

class MenuFunctionality:

    def __init__(self):
        self.url = ''
        self.modified_flag = False

    def new_file(self=None):
        self.textarea.textarea.delete(1.0, END)
        # if self.modified_flag:
        #     save = askyesnocancel(title='Warning', message='Do you want to save the file before exit?')
        #     if not save:
        #         self.app.Textarea.delete(1.0, END)
        #         self.url = ''
        #     elif save:
        #         pass


# --------------------------------------------- RUN APP --------------------------------------------------------------#

if __name__ == "__main__":
    app = App()
    app.mainloop()
