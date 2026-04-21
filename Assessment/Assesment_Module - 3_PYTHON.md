**Question - 1  : Healthcare Industry**

Design a Python class ClinicAppointment that manages patient appointments in a clinic.
The system should have the following features:

➔ Book Appointment:

● Prompt for patient name, age, mobile number, and preferred doctor.
● Show time slots (10am, 11am, 12pm, 2pm, 3pm).
● Check slot availability and confirm booking.

➔ View/Cancel Appointment:

● Allow patient to view or cancel their appointment using mobile number.

➔ Doctor Availability:

● Maintain a maximum of 3 appointments per time slot per doctor.

➔ Data Persistence:

● Store appointments in memory only (no files/dbs required).



**ANSWER**
```
Python

class ClinicAppointment:
    def __init__(self):
        # Store appointments: {doctor: {time_slot: [patients]}}
        self.appointments = {}
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor: ")

        print("\nAvailable Time Slots:")
        for slot in self.time_slots:
            print(slot)

        slot = input("Select time slot: ")

        if slot not in self.time_slots:
            print("Invalid slot!")
            return

        # Initialize doctor if not exists
        if doctor not in self.appointments:
            self.appointments[doctor] = {s: [] for s in self.time_slots}

        # Check availability (max 3 per slot)
        if len(self.appointments[doctor][slot]) >= 3:
            print("Slot full! Please choose another time.")
            return

        # Add appointment
        patient = {
            "name": name,
            "age": age,
            "mobile": mobile
        }

        self.appointments[doctor][slot].append(patient)
        print("✅ Appointment booked successfully!")

    def view_appointment(self):
        mobile = input("Enter mobile number: ")
        found = False

        for doctor in self.appointments:
            for slot in self.time_slots:
                for patient in self.appointments[doctor][slot]:
                    if patient["mobile"] == mobile:
                        print("\n📋 Appointment Details:")
                        print(f"Name: {patient['name']}")
                        print(f"Doctor: {doctor}")
                        print(f"Time: {slot}")
                        found = True

        if not found:
            print("No appointment found.")

    def cancel_appointment(self):
        mobile = input("Enter mobile number: ")
        found = False

        for doctor in self.appointments:
            for slot in self.time_slots:
                for patient in self.appointments[doctor][slot]:
                    if patient["mobile"] == mobile:
                        self.appointments[doctor][slot].remove(patient)
                        print("❌ Appointment cancelled successfully!")
                        found = True
                        return

        if not found:
            print("No appointment found.")

    def menu(self):
        while True:
            print("\n--- Clinic Appointment System ---")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")


# Run Application
app = ClinicAppointment()
app.menu()
```



**OUTPUT EXAMPLE**
```
# --- Clinic Appointment System ---
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# Enter choice: 1
# Enter patient name: Divyang
# Enter age: 28
# Enter mobile number: 6353592742   
# Enter preferred doctor: Dr. Price Babariya
# Available Time Slots:
# 10am
# 11am          
# 12pm
# 2pm
# 3pm
# Select time slot: 10am
# ✅ Appointment booked successfully!

# --- Clinic Appointment System ---
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# Enter choice: 2
# Enter mobile number: 6353592742
# 📋 Appointment Details:
# Name: Divyang
# Doctor: Dr. Price Babariya    
# Time: 10am

# --- Clinic Appointment System ---
# 1. Book Appointment
# 2. View Appointment
# 3. Cancel Appointment
# 4. Exit
# Enter choice: 3
# Enter mobile number: 6353592742
# ✅ Appointment cancelled successfully!

```


**Question - 2 : School Management System**

Design a Python class SchoolManagement that helps manage student admissions and
records. The system should support:
➔ New Admission:
● Collect student name, age, class (1–12), and guardian's mobile number.
● Assign a unique student ID automatically.
● Validate age: must be between 5 and 18.
● Validate mobile number: must be 10 digits.
➔ View Student Details:
● Allow lookup using student ID.
➔ Update Student Info:
● Update mobile number or class.
➔ Remove Student Record:
● Remove a student using their student ID.
➔ Exit System
**Answer**

```
Python


class SchoolManagement:
    def __init__(self):
        self.students = {}   # {student_id: student_data}
        self.next_id = 1

    # ------------------ VALIDATIONS ------------------ #
    def validate_age(self, age):
        return 5 <= age <= 18

    def validate_mobile(self, mobile):
        return mobile.isdigit() and len(mobile) == 10

    # ------------------ NEW ADMISSION ------------------ #
    def new_admission(self):
        name = input("Enter student name: ")
        
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Age must be a number.")
            return

        if not self.validate_age(age):
            print("❌ Age must be between 5 and 18.")
            return

        try:
            student_class = int(input("Enter class (1–12): "))
        except ValueError:
            print("❌ Class must be a number.")
            return

        if not (1 <= student_class <= 12):
            print("❌ Class must be between 1 and 12.")
            return

        mobile = input("Enter guardian mobile number: ")
        if not self.validate_mobile(mobile):
            print("❌ Mobile number must be 10 digits.")
            return

        student_id = self.next_id
        self.next_id += 1

        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print(f"✅ Admission successful! Student ID: {student_id}")

    # ------------------ VIEW STUDENT ------------------ #
    def view_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        student = self.students.get(student_id)
        if student:
            print("\n📋 Student Details:")
            print(f"ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class']}")
            print(f"Mobile: {student['mobile']}")
        else:
            print("❌ Student not found.")

    # ------------------ UPDATE STUDENT ------------------ #
    def update_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        student = self.students.get(student_id)
        if not student:
            print("❌ Student not found.")
            return

        print("\n1. Update Class")
        print("2. Update Mobile Number")
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                new_class = int(input("Enter new class (1–12): "))
                if 1 <= new_class <= 12:
                    student["class"] = new_class
                    print("✅ Class updated successfully!")
                else:
                    print("❌ Invalid class.")
            except ValueError:
                print("❌ Invalid input.")

        elif choice == "2":
            new_mobile = input("Enter new mobile number: ")
            if self.validate_mobile(new_mobile):
                student["mobile"] = new_mobile
                print("✅ Mobile updated successfully!")
            else:
                print("❌ Invalid mobile number.")

        else:
            print("❌ Invalid choice.")

    # ------------------ REMOVE STUDENT ------------------ #
    def remove_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        if student_id in self.students:
            del self.students[student_id]
            print("❌ Student record removed successfully!")
        else:
            print("❌ Student not found.")

    # ------------------ MENU ------------------ #
    def menu(self):
        while True:
            print("\n====== School Management System ======")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.new_admission()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("👋 Exiting system...")
                break
            else:
                print("❌ Invalid choice. Try again.")


# ------------------ RUN APP ------------------ #
app = SchoolManagement()
app.menu()
```

**OUTPUT EXAMPLE**
```
# ====== School Management System ======    
# 1. New Admission
# 2. View Student Details   
# 3. Update Student Info
# 4. Remove Student Record
# 5. Exit
# Enter your choice: 1
# Enter student name: Prisha
# Enter age: 7
# Enter class (1–12): 2
# Enter guardian mobile number: 6353592742  
# ✅ Admission successful! Student ID: 1

# ====== School Management System ====== 
# Enter your choice: 2
# Enter Student ID: 1   
# 📋 Student Details:
# ID: 1
# Name: Prisha
# Age: 7
# Class: 2
# Mobile: 6353592742

# ====== School Management System ====== 
# Enter your choice: 3
# Enter Student ID: 1
# 1. Update Class
# 2. Update Mobile Number

# ====== School Management System ====== 
# Enter choice: 4   
# Enter Student ID: 1
# ✅ Student record removed successfully!
```


**Question - 3 : Transport Reservation System (Bus Ticketing)**

Design a Python class BusReservation that simulates a basic bus ticket booking system.
Features should include:
➔ Show Available Routes:
● Predefined city routes with fixed prices.
● Example: "Mumbai to Pune - ₹500", "Delhi to Jaipur - ₹600", etc.
➔ Book Ticket:
● Enter passenger name, age, mobile, and route.
● Assign seat number (max 40 per bus per route).
● Generate a unique ticket ID.
➔ View Ticket:
● Lookup using ticket ID.
➔ Cancel Ticket:
● Cancel the ticket if it exists.
➔ Exit


**ANSWER**
```
Python

class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500},
            2: {"route": "Delhi to Jaipur", "price": 600},
            3: {"route": "Ahmedabad to Surat", "price": 300},
            4: {"route": "Bangalore to Mysore", "price": 400}
        }

        # Store tickets: {ticket_id: details}
        self.tickets = {}
        self.next_ticket_id = 1

        # Track seats per route: {route_id: [seat_numbers]}
        self.seats = {route_id: [] for route_id in self.routes}

    # ------------------ VALIDATION ------------------ #
    def validate_mobile(self, mobile):
        return mobile.isdigit() and len(mobile) == 10

    # ------------------ SHOW ROUTES ------------------ #
    def show_routes(self):
        print("\n🚌 Available Routes:")
        for rid, info in self.routes.items():
            print(f"{rid}. {info['route']} - ₹{info['price']}")

    # ------------------ BOOK TICKET ------------------ #
    def book_ticket(self):
        self.show_routes()

        try:
            route_id = int(input("Select route (enter number): "))
        except ValueError:
            print("❌ Invalid input.")
            return

        if route_id not in self.routes:
            print("❌ Invalid route.")
            return

        if len(self.seats[route_id]) >= 40:
            print("❌ Bus is full for this route!")
            return

        name = input("Enter passenger name: ")

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Invalid age.")
            return

        mobile = input("Enter mobile number: ")
        if not self.validate_mobile(mobile):
            print("❌ Mobile must be 10 digits.")
            return

        # Assign next seat
        seat_number = len(self.seats[route_id]) + 1
        self.seats[route_id].append(seat_number)

        # Generate ticket ID
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": self.routes[route_id]["route"],
            "price": self.routes[route_id]["price"],
            "seat": seat_number
        }

        print("\n✅ Ticket Booked Successfully!")
        print(f"🎫 Ticket ID: {ticket_id}")
        print(f"Seat No: {seat_number}")

    # ------------------ VIEW TICKET ------------------ #
    def view_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        ticket = self.tickets.get(ticket_id)

        if ticket:
            print("\n🎫 Ticket Details:")
            print(f"Name: {ticket['name']}")
            print(f"Route: {ticket['route']}")
            print(f"Seat: {ticket['seat']}")
            print(f"Price: ₹{ticket['price']}")
            print(f"Mobile: {ticket['mobile']}")
        else:
            print("❌ Ticket not found.")

    # ------------------ CANCEL TICKET ------------------ #
    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID: "))
        except ValueError:
            print("❌ Invalid ID.")
            return

        ticket = self.tickets.get(ticket_id)

        if ticket:
            # Find route_id
            route_id = None
            for rid, info in self.routes.items():
                if info["route"] == ticket["route"]:
                    route_id = rid
                    break

            # Remove seat
            if route_id:
                self.seats[route_id].remove(ticket["seat"])

            del self.tickets[ticket_id]
            print("❌ Ticket cancelled successfully!")
        else:
            print("❌ Ticket not found.")

    # ------------------ MENU ------------------ #
    def menu(self):
        while True:
            print("\n====== Bus Reservation System ======")
            print("1. Show Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_ticket()
            elif choice == "4":
                self.cancel_ticket()
            elif choice == "5":
                print("👋 Exiting system...")
                break
            else:
                print("❌ Invalid choice.")


# ------------------ RUN APP ------------------ #
app = BusReservation()
app.menu()
```

**OUTPUT EXAMPLE**
```
# Bus Reservation System
# 1. Show Routes
# 2. Book Ticket
# 3. View Ticket
# 4. Cancel Ticket
# 5. Exit
# Enter your choice: 1

# 🚌 Available Routes:
# 1. Mumbai to Pune - ₹500
# 2. Delhi to Jaipur - ₹600
# 3. Ahmedabad to Surat - ₹300
# 4. Bangalore to Mysore - ₹400

# Bus Reservation System 
# 1. Show Routes
# 2. Book Ticket
# 3. View Ticket
# 4. Cancel Ticket
# 5. Exit
# Enter your choice: 2

# 🚌 Available Routes:
# 1. Mumbai to Pune - ₹500
# 2. Delhi to Jaipur - ₹600
# 3. Ahmedabad to Surat - ₹300
# 4. Bangalore to Mysore - ₹400
# Select route (enter number): 1
# Enter passenger name: Divyang
# Enter age: 28
# Enter mobile number: 6353592742

# ✅ Ticket Booked Successfully!
# 🎫 Ticket ID: 1
# Seat No: 1

# ====== Bus Reservation System ======
# 1. Show Routes
# 2. Book Ticket
# 3. View Ticket
# 4. Cancel Ticket
# 5. Exit
# Enter your choice: 4
# Enter Ticket ID: 1
# ✅ Ticket cancelled successfully!
```