import tkinter as tk
import psutil
import cpuinfo

window = tk.Tk()
window.title("System Info")
window.configure(bg="white")

#Set labels
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

drives = tk.Label(
    text="",
    foreground="black",
    background="white",
    width=40,
    height=10,
    font="Arial",
    justify="left"
    )
drives.pack()

#Refreshing for usage
def Refresh():
    #CPU Info
    cpu["text"]=(
        cpuinfo.get_cpu_info()["brand_raw"]
        +"\n\n Cores: "+str(psutil.cpu_count(logical=False))
        +"\n Threads: "+str(psutil.cpu_count(logical=True))
        +"\n Speed: "+cpuinfo.get_cpu_info()["hz_actual_friendly"]
        +f"\nUsage: {psutil.cpu_percent()}%"
        )

    #Memory Info
    totalmem = str(round(psutil.virtual_memory().total / (1024 ** 3),2))+" GB"
    MemUsed = str(round(psutil.virtual_memory().used / (1024 ** 3),2))+" GB"
    MemUsedPercent = str(round(psutil.virtual_memory().percent,1))
    MemAvailPercent = round(100-psutil.virtual_memory().percent,1)
    MemAvail = str(round(psutil.virtual_memory().available / (1024 ** 3),2))+" GB"
    

    mem["text"]=(
        "Memory"
        +f"\n\nTotal: {totalmem}"
        +f"\nIn Use: {MemUsed} ({MemUsedPercent}%)"
        +f"\nAvailable: {MemAvail} ({MemAvailPercent}%)"
        )

    #Disk Info (*** Figure out how to check multiple disks if there's more than one)
    TotalDisk = str(round(psutil.disk_usage("C://").total / (1024 ** 3),2))+" GB"
    UsedDisk = str(round(psutil.disk_usage("C://").used / (1024 ** 3),2))+" GB"+f" ({str(psutil.disk_usage('C://').percent)}%)"
    AvailDisk = str(round(psutil.disk_usage("C://").free / (1024 ** 3),2))+" GB"

    drives["text"]=(
        "Drive(s)"
        +f"\nTotal Space: {TotalDisk} \n Used Space: {UsedDisk} \n Available Space: {AvailDisk}"
        )
    
    window.after(500,Refresh) 

Refresh()
window.mainloop()
