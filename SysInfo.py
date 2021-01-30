import tkinter as tk
import psutil
import cpuinfo

window = tk.Tk()
window.title("System Info")
window.configure(bg="white")

cpu = tk.Label(
    text="",
    foreground="black",
    background="white",
    width=40,
    height=10,
    font="Arial",
    justify="left"
    )
cpu.pack()

mem = tk.Label(
    text="",
    foreground="black",
    background="white",
    width=40,
    height=10,
    font="Arial",
    justify="left"
    )
mem.pack()

def Refresh():
    cpu["text"]=(
        cpuinfo.get_cpu_info()["brand_raw"]
        +"\n\n Cores: "+str(psutil.cpu_count(logical=False))
        +"\n Threads: "+str(psutil.cpu_count(logical=True))
        +"\n Speed: "+cpuinfo.get_cpu_info()["hz_actual_friendly"]
        )

    totalmem = str(round(psutil.virtual_memory().total / (1024 ** 3),2))+" GB"
    MemUsed = str(round(psutil.virtual_memory().used / (1024 ** 3),2))+" GB"
    MemUsedPercent = str(round(psutil.virtual_memory().percent,1))

    mem["text"]=(
        "Memory"
        +f"\n\nTotal: {totalmem}"
        +f"\nIn Use: {MemUsed} ({MemUsedPercent}%)"
        )
    
    window.after(1000,Refresh) 

Refresh()
window.mainloop()
