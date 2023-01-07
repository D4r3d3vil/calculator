import tkinter as tk
import tkinter.font as tkFont

global string, GLabel_322
string = ""

class App:
    def __init__(self, root):
        #setting title
        root.title("calculator")
        #setting window size
        width=600
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_136=tk.Button(root)
        GButton_136["bg"] = "#000000"
        ft = tkFont.Font(family='Times New Roman',size=28)
        GButton_136["font"] = ft
        GButton_136["fg"] = "#ffffff"
        GButton_136["justify"] = "center"
        GButton_136["text"] = "1"
        GButton_136.place(x=0,y=50,width=160,height=150)
        GButton_136["command"] = self.GButton_136_command
        global GLabel_322
        GLabel_322=tk.Label(root)
        GLabel_322["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=38)
        GLabel_322["font"] = ft
        GLabel_322["fg"] = "#ffffff"
        GLabel_322["justify"] = "center"
        GLabel_322["text"] = ""
        GLabel_322.place(x=0,y=0,width=597,height=55)

        GButton_728=tk.Button(root)
        GButton_728["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_728["font"] = ft
        GButton_728["fg"] = "#ffffff"
        GButton_728["justify"] = "center"
        GButton_728["text"] = "2"
        GButton_728.place(x=160,y=50,width=160,height=150)
        GButton_728["command"] = self.GButton_728_command

        GButton_996=tk.Button(root)
        GButton_996["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_996["font"] = ft
        GButton_996["fg"] = "#ffffff"
        GButton_996["justify"] = "center"
        GButton_996["text"] = "3"
        GButton_996.place(x=320,y=50,width=160,height=150)
        GButton_996["command"] = self.GButton_996_command

        GButton_234=tk.Button(root)
        GButton_234["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_234["font"] = ft
        GButton_234["fg"] = "#000000"
        GButton_234["justify"] = "center"
        GButton_234["text"] = "Button"
        GButton_234.place(x=90,y=270,width=70,height=25)
        GButton_234["command"] = self.GButton_234_command

        GButton_827=tk.Button(root)
        GButton_827["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_827["font"] = ft
        GButton_827["fg"] = "#ffffff"
        GButton_827["justify"] = "center"
        GButton_827["text"] = "7"
        GButton_827.place(x=0,y=350,width=160,height=150)
        GButton_827["command"] = self.GButton_827_command

        GButton_915=tk.Button(root)
        GButton_915["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=48)
        GButton_915["font"] = ft
        GButton_915["fg"] = "#ffffff"
        GButton_915["justify"] = "center"
        GButton_915["text"] = "-"
        GButton_915.place(x=480,y=380,width=119,height=93)
        GButton_915["command"] = self.GButton_915_command

        GButton_936=tk.Button(root)
        GButton_936["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_936["font"] = ft
        GButton_936["fg"] = "#ffffff"
        GButton_936["justify"] = "center"
        GButton_936["text"] = "+"
        GButton_936.place(x=480,y=470,width=122,height=92)
        GButton_936["command"] = self.GButton_936_command

        GButton_989=tk.Button(root)
        GButton_989["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_989["font"] = ft
        GButton_989["fg"] = "#ffffff"
        GButton_989["justify"] = "center"
        GButton_989["text"] = "4"
        GButton_989.place(x=0,y=200,width=160,height=150)
        GButton_989["command"] = self.GButton_989_command

        GButton_73=tk.Button(root)
        GButton_73["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#ffffff"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "="
        GButton_73.place(x=320,y=560,width=280,height=90)
        GButton_73["command"] = self.GButton_73_command

        GButton_105=tk.Button(root)
        GButton_105["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_105["font"] = ft
        GButton_105["fg"] = "#ffffff"
        GButton_105["justify"] = "center"
        GButton_105["text"] = "/"
        GButton_105.place(x=480,y=200,width=135,height=91)
        GButton_105["command"] = self.GButton_105_command

        GButton_2=tk.Button(root)
        GButton_2["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_2["font"] = ft
        GButton_2["fg"] = "#ffffff"
        GButton_2["justify"] = "center"
        GButton_2["text"] = "6"
        GButton_2.place(x=320,y=200,width=160,height=150)
        GButton_2["command"] = self.GButton_2_command

        GButton_307=tk.Button(root)
        GButton_307["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_307["font"] = ft
        GButton_307["fg"] = "#ffffff"
        GButton_307["justify"] = "center"
        GButton_307["text"] = "5"
        GButton_307.place(x=160,y=200,width=160,height=150)
        GButton_307["command"] = self.GButton_307_command

        GButton_446=tk.Button(root)
        GButton_446["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_446["font"] = ft
        GButton_446["fg"] = "#ffffff"
        GButton_446["justify"] = "center"
        GButton_446["text"] = "x"
        GButton_446.place(x=480,y=290,width=125,height=90)
        GButton_446["command"] = self.GButton_446_command

        GButton_31=tk.Button(root)
        GButton_31["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_31["font"] = ft
        GButton_31["fg"] = "#ffffff"
        GButton_31["justify"] = "center"
        GButton_31["text"] = "8"
        GButton_31.place(x=160,y=350,width=160,height=150)
        GButton_31["command"] = self.GButton_31_command

        GButton_205=tk.Button(root)
        GButton_205["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_205["font"] = ft
        GButton_205["fg"] = "#ffffff"
        GButton_205["justify"] = "center"
        GButton_205["text"] = "9"
        GButton_205.place(x=320,y=350,width=160,height=150)
        GButton_205["command"] = self.GButton_205_command

        GButton_779=tk.Button(root)
        GButton_779["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#ffffff"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "0"
        GButton_779.place(x=0,y=500,width=163,height=150)
        GButton_779["command"] = self.GButton_779_command

        GButton_247=tk.Button(root)
        GButton_247["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=18)
        GButton_247["font"] = ft
        GButton_247["fg"] = "#ffffff"
        GButton_247["justify"] = "center"
        GButton_247["text"] = "delete"
        GButton_247.place(x=480,y=50,width=120,height=152)
        GButton_247["command"] = self.GButton_247_command

        GButton_195=tk.Button(root)
        GButton_195["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=28)
        GButton_195["font"] = ft
        GButton_195["fg"] = "#ffffff"
        GButton_195["justify"] = "center"
        GButton_195["text"] = "."
        GButton_195.place(x=160,y=500,width=167,height=153)
        GButton_195["command"] = self.GButton_195_command

        GButton_188=tk.Button(root)
        GButton_188["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=23)
        GButton_188["font"] = ft
        GButton_188["fg"] = "#ffffff"
        GButton_188["justify"] = "center"
        GButton_188["text"] = "clear"
        GButton_188.place(x=320,y=500,width=162,height=61)
        GButton_188["command"] = self.GButton_188_command

    def GButton_136_command(self):
        global string, GLabel_322 
        string = str(string) + "1"
        refresh()

    def GButton_728_command(self):
        global string 
        string = str(string) + "2"
        refresh()

    def GButton_996_command(self):
        global string 
        string = str(string) + "3"
        refresh()

    def GButton_234_command(self):
        global string 
        string = str(string) + "4"
        refresh()

    def GButton_827_command(self):
        global string 
        string = str(string) + "7"
        refresh()

    def GButton_915_command(self):
        global string 
        string = str(string) + " - "
        refresh()

    def GButton_936_command(self):
        global string 
        string = str(string) + " + "
        refresh()

    def GButton_989_command(self):
        global string 
        string = str(string) + "4"
        refresh()

    def GButton_73_command(self):
        global string
        string = eval(string)
        string = str(string)
        if "." in string[:2]:
            if len(string) > 19:
                string = string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6] + string[7] + string[8] + string[9] + string[10] + string[11] + string[12] + string[13] + string[14] + string[15] + string[16] + string[17] + string[18] + string[19]
        refresh()
    def GButton_105_command(self):
        global string 
        string = str(string) + " / "
        refresh()

    def GButton_2_command(self):
        global string 
        string = str(string) + "6"
        refresh()

    def GButton_307_command(self):
        global string 
        string = str(string) + "5"
        refresh()

    def GButton_446_command(self):
        global string 
        string = str(string) + " * "
        refresh()

    def GButton_31_command(self):
        global string 
        string = str(string) + "8"
        refresh()

    def GButton_205_command(self):
        global string 
        string = str(string) + "9"
        refresh()

    def GButton_779_command(self):
        global string 
        string = str(string) + "0"
        refresh()

    def GButton_247_command(self):
        global string
        string = string[:-1]
        refresh()

    def GButton_195_command(self):
        global string
        string = string + "."
        refresh()

    def GButton_188_command(self):
        global string
        string = ""
        refresh()

def refresh():
        global string, GLabel_322
        GLabel_322["text"] = string

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
