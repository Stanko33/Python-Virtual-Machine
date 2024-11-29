import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class c0010():
    def __init__(self, mainclass, operation, par1, par2, reg1, reg2, instrn):
        try:
            # Handle the commands based on the provided operation (opcode)
            match operation:

                case '0000': #WND
                    self.window = tk.Tk()
                    self.window.geometry("800x800")
                    self.window.title("Stalinsoft Windows")
                    self.mainclass = mainclass
                case '0001':  #WNS
                    self.window.geometry(f"{par1}x{par2}")
                case '0010':  #WNT
                    self.window.title(par1)
                case '0011':  #WNC
                    for widget in self.window.winfo_children():
                        widget.destroy()
                case '0100':  #WDL
                    self.window.quit()
                case '0101':  #BCL
                    self.window.config(bg=par1)
                case '0110':  #SCT
                    text = tk.Text(self.window, height=10, width=30)
                    text.insert(tk.END, par1)  # Insert default text
                    scroll = tk.Scrollbar(self.window, command=text.yview)
                    text.config(yscrollcommand=scroll.set)
                    text.pack(pady=10)
                    scroll.pack(side=tk.RIGHT, fill=tk.Y)
                case '0111':  #PRB
                    from tkinter import ttk
                    progress = ttk.Progressbar(self.window, length=200, mode='indeterminate')
                    progress.pack(pady=10)
                    progress.start()
                case '1000': #BUT
                    textreg1=[mainclass.registers[int(reg1[:4],2)],mainclass.registers[int(reg1[4:8],2)],mainclass.registers[int(reg1[8:12],2)],mainclass.registers[int(reg1[12:],2)]]
                    textreg2=[mainclass.registers[int(reg2[:4],2)],mainclass.registers[int(reg2[4:8],2)],mainclass.registers[int(reg2[8:12],2)],mainclass.registers[int(reg2[12:],2)]]
                    text1,text2='', ''
                    text1+=chr(textreg1[i] for i in range(0,3))
                    text2+=chr(textreg2[i] for i in range(0,3))
                    text=text1+text2
                    button = tk.Button(self.window, text=text, command=lambda: print(par2))
                    button.pack(pady=10)
                case '1001': #TXT
                    label = tk.Label(self.window, text=par1)
                    label.pack(pady=10)
                case '1010': #TXI
                    entry = tk.Entry(self.window)
                    entry.insert(0, par1)  # Insert the default text if provided
                    entry.pack(pady=10)
                case '1011','1100','1101','1110', "1111":
                    print("Unknown operation")
            
        except Exception as e:
            print(f"Error executing GUI command: {e}")

        self.window.mainloop()
