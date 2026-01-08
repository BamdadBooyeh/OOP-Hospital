class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def show_info(self):
        return (
            f"Name: {self.name}\n"
            f"ID: {self.user_id}\n"
        )


class Doctor(User):
    def __init__(self, name, user_id, specialization):
        super().__init__(name, user_id)
        self.specialization = specialization
        self.appointments = []  # List of appointments specific to the doctor

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    
    def show_info(self):
        return (
            f"--- Doctor Information ---\n"
            f"{super().show_info()}"
            f"Specialization: {self.specialization}\n"
            f"Appointments: {len(self.appointments)}\n"
        )

class Nurse(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.tasks = []  # List of tasks assigned to the nurse

    def assign_task(self, task):
        self.tasks.append(task)

    def show_info(self):
        return (
            f"--- Nurse Information ---\n"
            f"{super().show_info()}"
            f"Tasks: {', '.join(self.tasks) if self.tasks else 'No tasks assigned'}\n"
        )
class Patient(User):
    def __init__(self, name, user_id, medical_history=None):
        super().__init__(name, user_id)
        self.medical_history = medical_history if medical_history else []
        self.appointments = []  # List of appointments specific to the patient

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_info(self):
               return (
            f"--- Patient Information ---\n"
            f"{super().show_info()}"
            f"Medical History: {', '.join(self.medical_history) if self.medical_history else 'No medical history available'}\n"
            f"Appointments: {len(self.appointments)}\n"
        )

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def show_info(self):
         return (
            f"--- Appointment Information ---\n"
            f"Patient: {self.patient.name}\n"
            f"Doctor: Dr. {self.doctor.name}\n"
            f"Date: {self.date}\n"
            f"Time: {self.time}\n"
        )



class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.nurses = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        if doctor not in self.doctors:
            self.doctors.append(doctor)

    def add_nurse(self, nurse):
        if nurse not in self.nurses:  
            self.nurses.append(nurse)

    def add_patient(self, patient):
        if patient not in self.patients:  
            self.patients.append(patient)

    def add_appointment(self, appointment):
        if appointment not in self.appointments:  # Prevent duplicate appointments
            self.appointments.append(appointment)
            appointment.doctor.add_appointment(appointment)
            appointment.patient.add_appointment(appointment)

    def show_info(self):
     return (
            f"--- Hospital Information ---\n"
            f"Hospital: {self.name}\n"
            f"Doctors: {len(self.doctors)}\n"
            f"Nurses: {len(self.nurses)}\n"
            f"Patients: {len(self.patients)}\n"
            f"Appointments: {len(self.appointments)}\n"
        )
    
hospital = Hospital("City Hospital")


doc1 = Doctor("Dr. Smith", "D1001", "Cardiologist")
doc2 = Doctor("Dr. Johnson", "D1002", "Neurologist")
hospital.add_doctor(doc1)
hospital.add_doctor(doc2)


nurse1 = Nurse("Nurse Lisa", "N2001")
nurse2 = Nurse("Nurse Tom", "N2002")
hospital.add_nurse(nurse1)
hospital.add_nurse(nurse2)


patient1 = Patient("John Doe", "P3001")
patient2 = Patient("Alice Brown", "P3002")
hospital.add_patient(patient1)
hospital.add_patient(patient2)


patient1.add_medical_record("Diabetes")
patient2.add_medical_record("High Blood Pressure")


appt1 = Appointment(patient1, doc1, "2025-01-20", "10:00 AM")
appt2 = Appointment(patient2, doc2, "2025-01-22", "2:00 PM")
hospital.add_appointment(appt1)
hospital.add_appointment(appt2)


print(hospital.show_info()) 
print(doc1.show_info())  
print(patient1.show_info())  
print(appt1.show_info())  

import csv

def load_from_csv(file_path, hospital):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
          
            if row['class'] == 'Doctor':
                doctor = Doctor(row['name'], row['user_id'], row['specialization_or_medical_history'])
                hospital.add_doctor(doctor)


hospital = Hospital("City Hospital")


csv_file_path = '/Users/bamdadbooyeh/Desktop/doctors_data.csv'  # Replace 'your-username' with your actual Mac username

load_from_csv(csv_file_path, hospital)


print(hospital.show_info())
for doctor in hospital.doctors:
    print(doctor.show_info())
