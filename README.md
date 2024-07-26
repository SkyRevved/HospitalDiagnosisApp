# Hospital Diagnosis System

This Python project is a hospital diagnostic system that allows users to input their symptoms and receive a possible diagnosis. It features a graphical user interface (GUI) created with Tkinter and can be converted into a standalone executable using PyInstaller.

## Features

- User-friendly GUI for symptom selection.
- Dynamic symptom navigation based on user input.
- Diagnosis results displayed to the user.
- Patient information (name, age) and diagnosis saved to an Excel file.
- Standalone executable created with PyInstaller.

## Prerequisites

- Python 3.x
- `pandas`
- `tkinter`
- `PyInstaller` (for creating the executable)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/hospital-diagnosis-system.git
   cd hospital-diagnosis-system
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install pandas
   ```

4. **Run the Application**

   To run the application, execute:

   ```bash
   python project.py
   ```

## Creating a Standalone Executable

To create a standalone executable from the Python script, follow these steps:

1. **Install PyInstaller**

   With your virtual environment activated, install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable**

   Run the following command to create the executable. This will generate the executable in a `dist` directory:

   ```bash
   pyinstaller --name "HospitalDiagnosisApp" --onefile --windowed project.py
   ```

   - `--name "HospitalDiagnosisApp"`: Sets the name of the executable.
   - `--onefile`: Bundles everything into a single executable file.
   - `--windowed`: Prevents a command-line window from appearing (useful for GUI applications).

3. **Locate the Executable**

   After the build process is complete, find the executable in the `dist` directory within your project folder. The executable will be named `HospitalDiagnosisApp.exe`.

## Usage

1. **Launch the Application**:
   Run `project.py` or the created executable `HospitalDiagnosisApp.exe`.

2. **Enter Patient Information**:
   Fill in the patient's name and age in the provided fields.

3. **Select Symptoms**:
   Use the dropdown menu to choose symptoms. The application will guide you through related symptoms until a diagnosis is reached.

4. **View Diagnosis**:
   The application will display the diagnosis based on the selected symptoms and save the record to an Excel file named `patient_diagnosis_records.xlsx`.

5. **Reset for New Patient**:
   After viewing the diagnosis, the application resets, allowing you to enter new patient details and symptoms.

## Screenshots

Below are some screenshots of the application in action:

![image](https://github.com/user-attachments/assets/b1416b10-901a-4aed-b645-132f47b66e82)

*The main window of the application showing symptom selection.*

![image](https://github.com/user-attachments/assets/76e81b02-e70f-4177-baf4-d6fab032045c)

*The form for entering patient information.*

![image](https://github.com/user-attachments/assets/33e1cf78-83ec-4181-a6fc-3d113dc6d5fa)

*The diagnosis results screen.*

To add your own screenshots, replace `path/to/screenshotX.png` with the actual paths to your image files in the repository. Ensure that the screenshots are included in the repository for proper display.

## File Structure

- `project.py`: Main application script.
- `patient_diagnosis_records.xlsx`: Excel file where patient records are saved.
- `dist/`: Directory containing the standalone executable (not included in the repository).
- `venv/`: Virtual environment directory (not included in the repository).
- `build/`: Directory created by PyInstaller during the build process (not included in the repository).

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Please ensure that any changes are well-documented and tested.

## Contact

For any questions or feedback, please contact [srini.baruah@gmail.com].

---
