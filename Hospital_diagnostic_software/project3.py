import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

class SymptomDiagnosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Diagnosis System")

        self.original_symptom_data = {
            "Fever": {
                "Headache": {
                    "Nausea": "Flu",
                    "No Nausea": {
                        "Fatigue": "Dengue",
                        "No Fatigue": "Common Cold"
                    }
                },
                "No Headache": {
                    "Chills": {
                        "Sweating": "Malaria",
                        "No Sweating": "Viral Infection"
                    },
                    "No Chills": "Minor Infection"
                }
            },
            "Cough": {
                "Dry Cough": {
                    "Sore Throat": {
                        "Runny Nose": "Common Cold",
                        "No Runny Nose": "Laryngitis"
                    },
                    "No Sore Throat": "Allergies"
                },
                "Wet Cough": {
                    "Fever": {
                        "Chest Pain": "Pneumonia",
                        "No Chest Pain": "Bronchitis"
                    },
                    "No Fever": "Mild Infection"
                }
            },
            "Stomach Pain": {
                "Upper Abdomen": {
                    "Nausea": "Gastritis",
                    "No Nausea": "Indigestion"
                },
                "Lower Abdomen": {
                    "Diarrhea": "Gastroenteritis",
                    "No Diarrhea": "Constipation"
                }
            },
            "Back Pain": {
                "Upper Back": {
                    "Stiffness": "Muscle Strain",
                    "No Stiffness": "Poor Posture"
                },
                "Lower Back": {
                    "Radiating Pain": "Sciatica",
                    "No Radiating Pain": "Lumbar Strain"
                }
            }
        }

        self.symptom_data = self.original_symptom_data
        self.current_symptoms = list(self.symptom_data.keys())

        self.patient_info = {}
        self.create_widgets()

    def create_widgets(self):
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=10)

        tk.Label(self.info_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.info_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.info_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.info_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        self.symptom_frame = tk.Frame(self.root)
        self.symptom_frame.pack(pady=10)

        self.symptom_label = tk.Label(self.symptom_frame, text="Choose a symptom:")
        self.symptom_label.pack()

        self.symptom_var = tk.StringVar()
        self.symptom_menu = tk.OptionMenu(self.symptom_frame, self.symptom_var, *self.current_symptoms)
        self.symptom_menu.pack()

        self.next_button = tk.Button(self.symptom_frame, text="Next", command=self.next_symptom)
        self.next_button.pack(pady=5)

    def next_symptom(self):
        selected_symptom = self.symptom_var.get()
        if not selected_symptom:
            messagebox.showwarning("Input Error", "Please select a symptom.")
            return

        if isinstance(self.symptom_data, dict) and selected_symptom in self.symptom_data:
            next_symptom_data = self.symptom_data[selected_symptom]
            if isinstance(next_symptom_data, dict):
                self.current_symptoms = list(next_symptom_data.keys())
                self.symptom_label.config(text="Choose a related symptom:")
                self.symptom_var.set('')
                menu = self.symptom_menu["menu"]
                menu.delete(0, "end")
                for symptom in self.current_symptoms:
                    menu.add_command(label=symptom, command=lambda value=symptom: self.symptom_var.set(value))
                self.symptom_data = next_symptom_data
            else:
                self.show_diagnosis(next_symptom_data)
        else:
            messagebox.showwarning("Selection Error", "Invalid symptom selection.")

    def show_diagnosis(self, diagnosis):
        self.patient_info['Name'] = self.name_entry.get()
        self.patient_info['Age'] = self.age_entry.get()
        self.patient_info['Diagnosis'] = diagnosis

        info_message = f"Patient Name: {self.patient_info['Name']}\n"
        info_message += f"Age: {self.patient_info['Age']}\n"
        info_message += f"Diagnosis: {self.patient_info['Diagnosis']}"

        messagebox.showinfo("Diagnosis Result", info_message)
        self.save_to_excel(self.patient_info)
        self.reset_app()

    def save_to_excel(self, patient_info):
        file_path = "patient_diagnosis_records.xlsx"
        
        new_record = pd.DataFrame([patient_info])

        if os.path.exists(file_path):
            existing_records = pd.read_excel(file_path)
            updated_records = pd.concat([existing_records, new_record], ignore_index=True)
        else:
            updated_records = new_record
        
        updated_records.to_excel(file_path, index=False)
        messagebox.showinfo("Save Success", "Patient record saved successfully.")

    def reset_app(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.symptom_data = self.original_symptom_data
        self.current_symptoms = list(self.symptom_data.keys())
        self.symptom_label.config(text="Choose a symptom:")
        self.symptom_var.set('')
        menu = self.symptom_menu["menu"]
        menu.delete(0, "end")
        for symptom in self.current_symptoms:
            menu.add_command(label=symptom, command=lambda value=symptom: self.symptom_var.set(value))

if __name__ == "__main__":
    root = tk.Tk()
    app = SymptomDiagnosisApp(root)
    root.mainloop()
