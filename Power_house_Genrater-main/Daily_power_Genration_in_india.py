import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib

# Load trained model and columns
model = joblib.load("model_kdk.pkl")
X_columns = joblib.load("x_columns_kdk.pkl")

# ----------------- Main Window -----------------
root = tk.Tk()
root.title("🌟 Power Generation Prediction 🌟")
root.geometry("600x500")
root.config(bg="#f0f8ff")  # Light blue background

# ----------------- Title -----------------
title = tk.Label(root, text="Power Generation Prediction", 
                 font=("Helvetica", 20, "bold"), bg="#4B9CD3", fg="white", pady=15)
title.pack(fill="x", pady=(0, 10))

# ----------------- Input Frame -----------------
frame = tk.Frame(root, bg="#e6f2ff", bd=3, relief="ridge", padx=20, pady=20)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# ----------------- Input Fields -----------------
# Labels and entries
labels = ["Year", "Month", "Day of Week (0=Mon..6=Sun)", 
          "Region", "Thermal Estimated (MU)", "Nuclear Estimated (MU)", "Hydro Estimated (MU)"]

# Year
tk.Label(frame, text="Year:", bg="#e6f2ff", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry_year = tk.Entry(frame, font=("Arial", 12))
entry_year.grid(row=0, column=1, pady=5)

# Month
tk.Label(frame, text="Month:", bg="#e6f2ff", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
entry_month = tk.Entry(frame, font=("Arial", 12))
entry_month.grid(row=1, column=1, pady=5)

# Day of Week
tk.Label(frame, text="Day of Week:", bg="#e6f2ff", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
entry_day = tk.Entry(frame, font=("Arial", 12))
entry_day.grid(row=2, column=1, pady=5)

# Region
tk.Label(frame, text="Region:", bg="#e6f2ff", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5)
region_combo = ttk.Combobox(frame, values=["NorthEastern", "Northern", "Southern", "Western"], font=("Arial", 12))
region_combo.grid(row=3, column=1, pady=5)

# Thermal Estimated
tk.Label(frame, text="Thermal Estimated:", bg="#e6f2ff", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5)
entry_thermal = tk.Entry(frame, font=("Arial", 12))
entry_thermal.grid(row=4, column=1, pady=5)

# Nuclear Estimated
tk.Label(frame, text="Nuclear Estimated:", bg="#e6f2ff", font=("Arial", 12)).grid(row=5, column=0, sticky="w", pady=5)
entry_nuclear = tk.Entry(frame, font=("Arial", 12))
entry_nuclear.grid(row=5, column=1, pady=5)

# Hydro Estimated
tk.Label(frame, text="Hydro Estimated:", bg="#e6f2ff", font=("Arial", 12)).grid(row=6, column=0, sticky="w", pady=5)
entry_hydro = tk.Entry(frame, font=("Arial", 12))
entry_hydro.grid(row=6, column=1, pady=5)

# ----------------- Custom Popup -----------------
def show_popup(title, message, bg_color="#DDFFDD", fg_color="#009900"):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("400x150")
    popup.config(bg=bg_color)
    popup.resizable(False, False)

    tk.Label(popup, text=title, font=("Helvetica", 14, "bold"), bg=bg_color, fg=fg_color).pack(pady=(10,5))
    tk.Label(popup, text=message, font=("Arial", 12), bg=bg_color, fg=fg_color).pack(pady=5)
    tk.Button(popup, text="OK", font=("Arial", 12, "bold"), bg=fg_color, fg="white", command=popup.destroy).pack(pady=10)

    popup.grab_set()  # Modal popup

# ----------------- Predict Function -----------------
def predict():
    try:
        year = int(entry_year.get())
        month = int(entry_month.get())
        day = int(entry_day.get())
        region = region_combo.get()
        thermal = float(entry_thermal.get())
        nuclear = float(entry_nuclear.get())
        hydro = float(entry_hydro.get())

        df = pd.DataFrame([{
            "Year": year,
            "Month": month,
            "DayOfWeek": day,
            "Region": region,
            "Thermal Generation Estimated (in MU)": thermal,
            "Nuclear Generation Estimated (in MU)": nuclear,
            "Hydro Generation Estimated (in MU)": hydro
        }])

        df = pd.get_dummies(df, columns=["Region"], drop_first=True)
        df = df.reindex(columns=X_columns, fill_value=0)

        preds = model.predict(df)[0]

        # Show result
        show_popup("Prediction Result",
                   f"Thermal Actual: {preds[0]:.2f} MU\n"
                   f"Nuclear Actual: {preds[1]:.2f} MU\n"
                   f"Hydro Actual: {preds[2]:.2f} MU",
                   bg_color="#DDFFDD", fg_color="#009900")

    except Exception as e:
        show_popup("Error", str(e), bg_color="#FFDDDD", fg_color="#C70039")

# ----------------- Predict Button -----------------
btn = tk.Button(root, text="Predict 🔥", command=predict,
                font=("Arial", 14, "bold"), bg="#FF5733", fg="white", 
                activebackground="#C70039", padx=10, pady=5)
btn.pack(pady=20)

# ----------------- Footer -----------------
footer = tk.Label(root, text="Developed by Mangesh Sambare", font=("Arial", 10), 
                  bg="#f0f8ff", fg="#555555")
footer.pack(side="bottom", pady=5)

# ----------------- Run App -----------------
root.mainloop()
