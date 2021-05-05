import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import scheduler
import inout



def open_provider():
    global provider_filepath
    provider_filepath = askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if not provider_filepath:
        return
    lbl_provider["text"] = provider_filepath



def open_clinic():
    global clinic_filepath
    """Open a file for editing."""
    clinic_filepath = askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if not clinic_filepath:
        return
    # cliniclist = populateClinics(clinic_filepath)
    lbl_clinic["text"] = clinic_filepath

def run():
    providerlist = inout.populateProviders(provider_filepath)
    cliniclist = inout.populateClinics(clinic_filepath)
    scheduler.scheduler(providerlist, cliniclist)
    lbl_result["text"] = f"Scheduler Ran Successfully"


window = tk.Tk()
window.title("Crownpoint Scheduler")
window.rowconfigure(0, minsize=45, weight=1)
window.rowconfigure(1, minsize=45, weight=1)
window.rowconfigure(2, minsize=45, weight=1)
window.columnconfigure(1, minsize=300, weight=1)


btn_open_provider = tk.Button(master=window, text="Open Provider File",command=open_provider)
btn_open_clinic = tk.Button(master=window, text="Open Clinic File", command=open_clinic)
btn_run_scheduler = tk.Button(master=window, text="Run Scheduler", command=run)

lbl_provider = tk.Label(master=window,relief=tk.SUNKEN)
lbl_clinic = tk.Label(master=window,relief=tk.SUNKEN)
lbl_result = tk.Label(master=window,relief=tk.SUNKEN)

btn_open_provider.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open_clinic.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_run_scheduler.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

lbl_provider.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
lbl_clinic.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
lbl_result.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

window.mainloop()
