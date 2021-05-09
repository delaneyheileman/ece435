# ************************************************************************
# * This modules is a Graphical User Interface (GUI) that launches Inout and Scheduler modules
# * based on user input
# *
# * COMPONENT NAME: GUI.py
# *
# * VERSION: 3.0 (April 2021)
# *
# * Module Description
# * This module serves as the systems launch point. When executed by the
# * user. Values are passed to Inout and Scheduler.
# * **********************************************************************/

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import scheduler
import inout


# This function saves the file path of the provider file passed to it by the operating system's file system
def open_provider():
    global provider_filepath
    provider_filepath = askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if not provider_filepath:
        return
    lbl_provider["text"] = provider_filepath


# This function saves the file path of the clinic file passed to it by the operating system's file system
def open_clinic():
    global clinic_filepath
    """Open a file for editing."""
    clinic_filepath = askopenfilename(
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if not clinic_filepath:
        return
    lbl_clinic["text"] = clinic_filepath


#  This function takes the saved file paths and passes them to inout. Inout returns arrays which are then passed
#  to the scheduler function. An output message is created.
def run():
    providerlist = inout.populateProviders(provider_filepath)
    cliniclist = inout.populateClinics(clinic_filepath)
    scheduler.scheduler(providerlist, cliniclist)
    lbl_result["text"] = f"Scheduler Ran Successfully"


# This is where the GUI is created with tkinter

window = tk.Tk()
window.title("Crownpoint Scheduler")
window.rowconfigure(0, minsize=45, weight=1)
window.rowconfigure(1, minsize=45, weight=1)
window.rowconfigure(2, minsize=45, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

# Here functions are assigned to buttons

btn_open_provider = tk.Button(master=window, text="Open Provider File", command=open_provider)
btn_open_clinic = tk.Button(master=window, text="Open Clinic File", command=open_clinic)
btn_run_scheduler = tk.Button(master=window, text="Run Scheduler", command=run)

lbl_provider = tk.Label(master=window, relief=tk.SUNKEN)
lbl_clinic = tk.Label(master=window, relief=tk.SUNKEN)
lbl_result = tk.Label(master=window, relief=tk.SUNKEN)

btn_open_provider.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open_clinic.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_run_scheduler.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

lbl_provider.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
lbl_clinic.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
lbl_result.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

window.mainloop()
