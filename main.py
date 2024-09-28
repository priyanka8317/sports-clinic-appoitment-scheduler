class Patient:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Appointment:
    def _init_(self, patient, date, time):
        self.patient = patient
        self.date = date
        self.time = time

class Scheduler:
    def _init_(self):
        self.patients = {}
        self.appointments = {}

    def add_patient(self, name, phone, email):
        patient = Patient(name, phone, email)
        self.patients[name] = patient

    def schedule_appointment(self, name, date, time):
        patient = self.patients.get(name)
        if patient:
            appointment = Appointment(patient, date, time)
            self.appointments[name] = appointment
            print(f"Appointment scheduled for {name} on {date} at {time}")
        else:
            print("Patient not found")

    def cancel_appointment(self, name):
        if name in self.appointments:
            del self.appointments[name]
            print(f"Appointment cancelled for {name}")
        else:
            print("Appointment not found")

    def reschedule_appointment(self, name, new_date, new_time):
        if name in self.appointments:
            appointment = self.appointments[name]
            appointment.date = new_date
            appointment.time = new_time
            print(f"Appointment rescheduled for {name} on {new_date} at {new_time}")
        else:
            print("Appointment not found")


# Usage
scheduler = Scheduler()

while True:
    print("\nSports Clinic Appointment Scheduler")
    print("1. Add Patient")
    print("2. Schedule Appointment")
    print("3. Cancel Appointment")
    print("4. Reschedule Appointment")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter patient name: ")
        phone = input("Enter patient phone: ")
        email = input("Enter patient email: ")
        scheduler.add_patient(name, phone, email)
    elif choice == "2":
        name = input("Enter patient name: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")
        scheduler.schedule_appointment(name, date, time)
    elif choice == "3":
        name = input("Enter patient name: ")
        scheduler.cancel_appointment(name)
    elif choice == "4":
        name = input("Enter patient name: ")
        new_date = input("Enter new appointment date (YYYY-MM-DD): ")
        new_time = input("Enter new appointment time (HH:MM): ")
        scheduler.reschedule_appointment(name, new_date, new_time)
    elif choice == "5":
        break
    else:
        print("Invalid option")
