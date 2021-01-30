import tkinter as tk
import psutil
import cpuinfo

window = tk.Tk()

cpu = tk.Label(
    text=cpuinfo.get_cpu_info()["brand_raw"]
    +"\n Cores: "+str(psutil.cpu_count(logical=False))
    +"\n Threads: "+str(psutil.cpu_count(logical=True))
    +"\n Speed: "+cpuinfo.get_cpu_info()["hz_actual_friendly"],
    foreground="black",
    background="white",
    width=40,
    height=20,
    font="Arial"
    )
cpu.pack()
window.mainloop()
