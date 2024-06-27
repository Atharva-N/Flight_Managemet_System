import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def connect(username, password):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='flight_reservation_system',
            user='root',
            password='password'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)

def fetch_airports(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT airport_id, airport_name FROM airports')
        airports = cursor.fetchall()
        return airports
    except Error as e:
        print(e)

def fetch_flights(conn, origin_id, destination_id, departure_date):
    try:
        cursor = conn.cursor()
        query = ('SELECT flight_id, flight_name FROM flights '
                 'WHERE origin = %s AND destination = %s AND departure_date = %s')
        cursor.execute(query, (origin_id, destination_id, departure_date))
        flights = cursor.fetchall()
        return flights
    except Error as e:
        print(e)

def fetch_passengers(conn, flight_id):
    try:
        cursor = conn.cursor()
        query = ('SELECT passenger_id, name, age, gender FROM passengers '
                 'WHERE flight_id = %s')
        cursor.execute(query, (flight_id,))
        passengers = cursor.fetchall()
        return passengers
    except Error as e:
        print(e)

def book_flight(conn, name, age, gender, flight_id):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passengers (name, age, gender, flight_id) '
                       'VALUES (%s, %s, %s, %s)',
                       (name, age, gender, flight_id))
        conn.commit()
        messagebox.showinfo("Success", "Booking successful!")
    except Error as e:
        messagebox.showinfo("Success", "Booking successful!")
        
def update_booking(conn, passenger_id, name, age, gender, flight_id):
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE passengers SET name=%s, age=%s, gender=%s, flight_id=%s WHERE passenger_id=%s',
                       (name, age, gender, flight_id, passenger_id))
        conn.commit()
        messagebox.showinfo("Success", "Booking details updated successfully!")
    except Error as e:
        print(e)
        messagebox.showerror("Error", "Update failed!")


def cancel_booking(conn, passenger_id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM passengers WHERE passenger_id=%s', (passenger_id,))
        conn.commit()
        messagebox.showinfo("Success", "Booking canceled successfully!")
    except Error as e:
        print(e)
        messagebox.showerror("Error", "Cancellation failed.")

def fetch_all_flights(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT flight_id, flight_name FROM flights')
        flights = cursor.fetchall()
        return flights
    except Error as e:
        print(e)

def add_flight(conn, flight_name, origin_id, destination_id, departure_date, capacity):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO flights (flight_name, origin, destination, departure_date, capacity) '
                       'VALUES (%s, %s, %s, %s, %s)',
                       (flight_name, origin_id, destination_id, departure_date, capacity))
        conn.commit()
        messagebox.showinfo("Success", "Flight added successfully!")
    except Error as e:
        print(e)
        messagebox.showerror("Error", "Failed to add flight.")

def fetch_all_passengers(conn, flight_id):
    try:
        cursor = conn.cursor()
        query = ('SELECT passenger_id, name, age, gender FROM passengers '
                 'WHERE flight_id = %s')
        cursor.execute(query, (flight_id,))
        passengers = cursor.fetchall()
        return passengers
    except Error as e:
        print(e)

def update_flight(conn, flight_id, new_arrival, new_departure, new_date):
    try:
        cursor = conn.cursor()
        if new_arrival:
            cursor.execute('UPDATE flights SET arrival=%s WHERE flight_id=%s', (new_arrival, flight_id))
        if new_departure:
            cursor.execute('UPDATE flights SET departure=%s WHERE flight_id=%s', (new_departure, flight_id))
        if new_date:
            cursor.execute('UPDATE flights SET departure_date=%s WHERE flight_id=%s', (new_date, flight_id))
        conn.commit()
        messagebox.showinfo("Success", "Flight details updated successfully!")
    except Error as e:
        print(e)
        messagebox.showerror("Error", "Update failed!")

def delete_flight(conn, flight_id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM flights WHERE flight_id=%s', (flight_id,))
        conn.commit()
        messagebox.showinfo("Success", "Flight canceled successfully!")
    except Error as e:
        print(e)
        messagebox.showerror("Error", "Cancellation failed.")

def create_main_window():
    main_window = tk.Tk()
    main_window.title("Flight Reservation System")

    def switch_to_user_section():
        main_window.destroy()
        create_user_section()

    def switch_to_admin_section():
        main_window.destroy()
        create_admin_section()

    user_button = ttk.Button(main_window, text="User", command=switch_to_user_section)
    user_button.pack(pady=20)

    admin_button = ttk.Button(main_window, text="Admin", command=switch_to_admin_section)
    admin_button.pack(pady=20)

    main_window.mainloop()

def create_user_section():
    user_window = tk.Tk()
    user_window.title("User Section")

    def go_back():
        user_window.destroy()
        create_main_window()

    back_button = ttk.Button(user_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(user_window, text="User Options", font=('Arial', 18)).pack(pady=20)

    def book_ticket():
        user_window.destroy()
        create_book_ticket_window()

    def view_booking():
        user_window.destroy()
        create_view_booking_window()

    def update_booking_user():
        user_window.destroy()
        create_update_booking_window()
        
    def cancel_booking_user():
        user_window.destroy()
        create_cancel_booking_window()

    book_ticket_button = ttk.Button(user_window, text="Book Ticket", command=book_ticket)
    book_ticket_button.pack(pady=10)

    view_booking_button = ttk.Button(user_window, text="View Booking", command=view_booking)
    view_booking_button.pack(pady=10)

    update_booking_button = ttk.Button(user_window, text="Update Booking", command=update_booking_user)
    update_booking_button.pack(pady=10)

    cancel_booking_button = ttk.Button(user_window, text="Cancel Booking", command=cancel_booking_user)
    cancel_booking_button.pack(pady=10)

    user_window.mainloop()

def create_admin_section():
    admin_window = tk.Tk()
    admin_window.title("Admin Section")

    def go_back():
        admin_window.destroy()
        create_main_window()

    back_button = ttk.Button(admin_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(admin_window, text="Admin Options", font=('Arial', 18)).pack(pady=20)

    def add_flight_admin():
        admin_window.destroy()
        create_add_flight_window()

    def view_passenger_details():
        admin_window.destroy()
        create_view_passenger_details_window()

    def update_plane_details():
        admin_window.destroy()
        create_update_plane_details_window()

    def cancel_flight_admin():
        admin_window.destroy()
        create_cancel_flight_window()

    add_flight_button = ttk.Button(admin_window, text="Add Flight", command=add_flight_admin)
    add_flight_button.pack(pady=10)

    view_passenger_details_button = ttk.Button(admin_window, text="View Passenger Details", command=view_passenger_details)
    view_passenger_details_button.pack(pady=10)

    update_plane_details_button = ttk.Button(admin_window, text="Update Plane Details", command=update_plane_details)
    update_plane_details_button.pack(pady=10)

    cancel_flight_button = ttk.Button(admin_window, text="Cancel Flight", command=cancel_flight_admin)
    cancel_flight_button.pack(pady=10)

    admin_window.mainloop()

def create_book_ticket_window():
    book_ticket_window = tk.Tk()
    book_ticket_window.title("Book Ticket")

    def go_back():
        book_ticket_window.destroy()
        create_user_section()

    back_button = ttk.Button(book_ticket_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(book_ticket_window, text="Name:").pack(pady=5)
    name_entry = ttk.Entry(book_ticket_window, width=30)
    name_entry.pack()

    ttk.Label(book_ticket_window, text="Age:").pack(pady=5)
    age_entry = ttk.Entry(book_ticket_window, width=10)
    age_entry.pack()

    ttk.Label(book_ticket_window, text="Gender:").pack(pady=5)
    gender_entry = ttk.Entry(book_ticket_window, width=10)
    gender_entry.pack()

    conn = connect('root', 'password')
    airports = fetch_airports(conn)
    conn.close()

    origin_label = ttk.Label(book_ticket_window, text="Origin:")
    origin_label.pack(pady=5)
    origin_var = tk.StringVar()
    origin_dropdown = ttk.Combobox(book_ticket_window, width=27, textvariable=origin_var, state='readonly')
    origin_dropdown['values'] = airports
    origin_dropdown.pack()

    destination_label = ttk.Label(book_ticket_window, text="Destination:")
    destination_label.pack(pady=5)
    destination_var = tk.StringVar()
    destination_dropdown = ttk.Combobox(book_ticket_window, width=27, textvariable=destination_var, state='readonly')
    destination_dropdown['values'] = airports
    destination_dropdown.pack()

    ttk.Label(book_ticket_window, text="Date of Departure (YYYY-MM-DD):").pack(pady=5)
    departure_date_entry = ttk.Entry(book_ticket_window, width=30)
    departure_date_entry.pack()
    
    def book_ticket_action():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        origin_id = origin_dropdown.get().split(',')[0]
        destination_id = destination_dropdown.get().split(',')[0]
        departure_date = departure_date_entry.get()

        if not (name and age and gender and origin_id and destination_id and departure_date):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect('root', 'password')
        flights = fetch_flights(conn, origin_id, destination_id, departure_date)
        conn.close()

        if not flights:
            messagebox.showinfo("No Flights", "No flights available for selected route and date.")
            return

        select_flight_window = tk.Toplevel()
        select_flight_window.title("Select Flight")

        def select_flight():
            selected_flight = flights_listbox.get(tk.ACTIVE)
            flight_id = selected_flight.split(',')[0]

            book_flight(conn, name, age, gender, flight_id)

            select_flight_window.destroy()
            book_ticket_window.destroy()
            create_user_section()

        ttk.Label(select_flight_window, text="Select a Flight:").pack(pady=10)
        flights_listbox = tk.Listbox(select_flight_window, width=50)
        flights_listbox.pack(pady=10)

        for flight in flights:
            flights_listbox.insert(tk.END, f"{flight[0]}, {flight[1]}")

        select_flight_button = ttk.Button(select_flight_window, text="Select Flight", command=select_flight)
        select_flight_button.pack(pady=10)

        select_flight_window.mainloop()

    book_ticket_button = ttk.Button(book_ticket_window, text="Book Ticket", command=book_ticket_action)
    book_ticket_button.pack(pady=10)

    book_ticket_window.mainloop()

def create_view_booking_window():
    view_booking_window = tk.Tk()
    view_booking_window.title("View Booking")

    def go_back():
        view_booking_window.destroy()
        create_user_section()

    back_button = ttk.Button(view_booking_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(view_booking_window, text="Passenger ID:").pack(pady=5)
    passenger_id_entry = ttk.Entry(view_booking_window, width=30)
    passenger_id_entry.pack()

    def view_booking_action():
        passenger_id = passenger_id_entry.get()

        if not passenger_id:
            messagebox.showerror("Error", "Please enter Passenger ID.")
            return

        conn = connect('root', 'password')
        cursor = conn.cursor()
        cursor.execute('SELECT name, age, gender, flight_id FROM passengers WHERE passenger_id=%s', (passenger_id,))
        booking_details = cursor.fetchone()
        conn.close()

        if not booking_details:
            messagebox.showinfo("No Booking", "No booking found for the given Passenger ID.")
            return

        display_booking_window = tk.Toplevel()
        display_booking_window.title("Booking Details")

        ttk.Label(display_booking_window, text=f"Passenger ID: {passenger_id}").pack(pady=5)
        ttk.Label(display_booking_window, text=f"Name: {booking_details[0]}").pack(pady=5)
        ttk.Label(display_booking_window, text=f"Age: {booking_details[1]}").pack(pady=5)
        ttk.Label(display_booking_window, text=f"Gender: {booking_details[2]}").pack(pady=5)

        flight_id = booking_details[3]
        conn = connect('root', 'password')
        cursor = conn.cursor()
        cursor.execute('SELECT flight_name, origin, destination, departure_date FROM flights WHERE flight_id=%s', (flight_id,))
        flight_details = cursor.fetchone()
        conn.close()

        if flight_details:
            ttk.Label(display_booking_window, text=f"Flight: {flight_details[0]}").pack(pady=5)
            ttk.Label(display_booking_window, text=f"Origin: {flight_details[1]}").pack(pady=5)
            ttk.Label(display_booking_window, text=f"Destination: {flight_details[2]}").pack(pady=5)
            ttk.Label(display_booking_window, text=f"Departure Date: {flight_details[3]}").pack(pady=5)

        display_booking_window.mainloop()

    view_booking_button = ttk.Button(view_booking_window, text="View Booking", command=view_booking_action)
    view_booking_button.pack(pady=10)

    view_booking_window.mainloop()

def create_update_booking_window():
    update_booking_window = tk.Tk()
    update_booking_window.title("Update Booking")

    def go_back():
        update_booking_window.destroy()
        create_user_section()

    back_button = ttk.Button(update_booking_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(update_booking_window, text="Passenger ID:").pack(pady=5)
    passenger_id_entry = ttk.Entry(update_booking_window, width=30)
    passenger_id_entry.pack()

    ttk.Label(update_booking_window, text="Name:").pack(pady=5)
    name_entry = ttk.Entry(update_booking_window, width=30)
    name_entry.pack()

    ttk.Label(update_booking_window, text="Age:").pack(pady=5)
    age_entry = ttk.Entry(update_booking_window, width=10)
    age_entry.pack()

    ttk.Label(update_booking_window, text="Gender:").pack(pady=5)
    gender_entry = ttk.Entry(update_booking_window, width=10)
    gender_entry.pack()

    def fetch_booking_details():
        passenger_id = passenger_id_entry.get()

        if not passenger_id:
            messagebox.showerror("Error", "Please enter Passenger ID.")
            return

        conn = connect('root', 'password')
        cursor = conn.cursor()
        cursor.execute('SELECT name, age, gender, flight_id FROM passengers WHERE passenger_id=%s', (passenger_id,))
        booking_details = cursor.fetchone()
        conn.close()

        if not booking_details:
            messagebox.showinfo("No Booking", "No booking found for the given Passenger ID.")
            return

        name_entry.delete(0, tk.END)
        name_entry.insert(0, booking_details[0])
        age_entry.delete(0, tk.END)
        age_entry.insert(0, booking_details[1])
        gender_entry.delete(0, tk.END)
        gender_entry.insert(0, booking_details[2])

    fetch_booking_button = ttk.Button(update_booking_window, text="Fetch Booking Details", command=fetch_booking_details)
    fetch_booking_button.pack(pady=10)

    def update_booking_action():
        passenger_id = passenger_id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()

        if not (passenger_id and name and age and gender):
            messagebox.showerror("Error", "Please fetch booking details and enter all fields.")
            return

        conn = connect('root', 'password')
        update_booking(conn, passenger_id, name, age, gender, None)
        conn.close()

        update_booking_window.destroy()
        create_user_section()

    update_booking_button = ttk.Button(update_booking_window, text="Update Booking", command=update_booking_action)
    update_booking_button.pack(pady=10)

    update_booking_window.mainloop()

def create_cancel_booking_window():
    cancel_booking_window = tk.Tk()
    cancel_booking_window.title("Cancel Booking")

    def go_back():
        cancel_booking_window.destroy()
        create_user_section()

    back_button = ttk.Button(cancel_booking_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(cancel_booking_window, text="Passenger ID:").pack(pady=5)
    passenger_id_entry = ttk.Entry(cancel_booking_window, width=30)
    passenger_id_entry.pack()

    def cancel_booking_action():
        passenger_id = passenger_id_entry.get()

        if not passenger_id:
            messagebox.showerror("Error", "Please enter Passenger ID.")
            return

        conn = connect('root', 'password')
        cancel_booking(conn, passenger_id)
        conn.close()

        cancel_booking_window.destroy()
        create_user_section()

    cancel_booking_button = ttk.Button(cancel_booking_window, text="Cancel Booking", command=cancel_booking_action)
    cancel_booking_button.pack(pady=10)

    cancel_booking_window.mainloop()

def create_add_flight_window():
    add_flight_window = tk.Tk()
    add_flight_window.title("Add Flight")

    def go_back():
        add_flight_window.destroy()
        create_admin_section()

    back_button = ttk.Button(add_flight_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(add_flight_window, text="Flight Name:").pack(pady=5)
    flight_name_entry = ttk.Entry(add_flight_window, width=30)
    flight_name_entry.pack()

    conn = connect('root', 'password')
    airports = fetch_airports(conn)
    conn.close()

    origin_label = ttk.Label(add_flight_window, text="Origin:")
    origin_label.pack(pady=5)
    origin_var = tk.StringVar()
    origin_dropdown = ttk.Combobox(add_flight_window, width=27, textvariable=origin_var, state='readonly')
    origin_dropdown['values'] = airports
    origin_dropdown.pack()

    destination_label = ttk.Label(add_flight_window, text="Destination:")
    destination_label.pack(pady=5)
    destination_var = tk.StringVar()
    destination_dropdown = ttk.Combobox(add_flight_window, width=27, textvariable=destination_var, state='readonly')
    destination_dropdown['values'] = airports
    destination_dropdown.pack()

    ttk.Label(add_flight_window, text="Date of Departure (YYYY-MM-DD):").pack(pady=5)
    departure_date_entry = ttk.Entry(add_flight_window, width=30)
    departure_date_entry.pack()

    ttk.Label(add_flight_window, text="Capacity:").pack(pady=5)
    capacity_entry = ttk.Entry(add_flight_window, width=10)
    capacity_entry.pack()

    def add_flight_action():
        flight_name = flight_name_entry.get()
        origin_id = origin_dropdown.get().split(',')[0]
        destination_id = destination_dropdown.get().split(',')[0]
        departure_date = departure_date_entry.get()
        capacity = capacity_entry.get()

        if not (flight_name and origin_id and destination_id and departure_date and capacity):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect('root', 'password')
        add_flight(conn, flight_name, origin_id, destination_id, departure_date, capacity)
        conn.close()

        add_flight_window.destroy()
        create_admin_section()

    add_flight_button = ttk.Button(add_flight_window, text="Add Flight", command=add_flight_action)
    add_flight_button.pack(pady=10)

    add_flight_window.mainloop()

def create_view_passenger_details_window():
    view_passenger_details_window = tk.Tk()
    view_passenger_details_window.title("View Passenger Details")

    def go_back():
        view_passenger_details_window.destroy()
        create_admin_section()

    back_button = ttk.Button(view_passenger_details_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(view_passenger_details_window, text="Flight ID:").pack(pady=5)
    flight_id_entry = ttk.Entry(view_passenger_details_window, width=30)
    flight_id_entry.pack()

    def view_passenger_details_action():
        flight_id = flight_id_entry.get()

        if not flight_id:
            messagebox.showerror("Error", "Please enter Flight ID.")
            return

        conn = connect('root', 'password')
        passengers = fetch_all_passengers(conn, flight_id)
        conn.close()

        if not passengers:
            messagebox.showinfo("No Passengers", "No passengers found for the given Flight ID.")
            return

        display_passengers_window = tk.Toplevel()
        display_passengers_window.title("Passenger Details")

        passengers_listbox = tk.Listbox(display_passengers_window, width=80)
        passengers_listbox.pack(pady=10)

        for passenger in passengers:
            passengers_listbox.insert(tk.END, f"{passenger[0]}, {passenger[1]}, {passenger[2]}, {passenger[3]}")

        display_passengers_window.mainloop()

    view_passenger_details_button = ttk.Button(view_passenger_details_window, text="View Passenger Details", command=view_passenger_details_action)
    view_passenger_details_button.pack(pady=10)

    view_passenger_details_window.mainloop()
    
def create_view_passengers_on_plane_window():
    view_passengers_on_plane_window = tk.Tk()
    view_passengers_on_plane_window.title("View Passengers on a Plane")

    def go_back():
        view_passengers_on_plane_window.destroy()
        create_admin_section()

    back_button = ttk.Button(view_passengers_on_plane_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    conn = connect('root', 'password')
    flights = fetch_all_flights(conn)
    conn.close()

    def view_passengers_action():
        selected_flight = flights_listbox.get(tk.ACTIVE)
        flight_id = selected_flight.split(',')[0]

        conn = connect('root', 'password')
        passengers = fetch_passengers(conn, flight_id)
        conn.close()

        if not passengers:
            messagebox.showinfo("No Passengers", "No passengers found for the selected flight.")
            return

        display_passengers_window = tk.Toplevel()
        display_passengers_window.title("Passengers on Plane")

        passengers_listbox = tk.Listbox(display_passengers_window, width=80)
        passengers_listbox.pack(pady=10)

        for passenger in passengers:
            passengers_listbox.insert(tk.END, f"{passenger[0]}, {passenger[1]}, {passenger[2]}, {passenger[3]}")

        display_passengers_window.mainloop()

    ttk.Label(view_passengers_on_plane_window, text="Select a Flight:").pack(pady=10)
    flights_listbox = tk.Listbox(view_passengers_on_plane_window, width=80)
    flights_listbox.pack(pady=10)

    for flight in flights:
        flights_listbox.insert(tk.END, f"{flight[0]}, {flight[1]}, {flight[2]}, {flight[3]}")

    view_passengers_button = ttk.Button(view_passengers_on_plane_window, text="View Passengers", command=view_passengers_action)
    view_passengers_button.pack(pady=10)

    view_passengers_on_plane_window.mainloop()

def create_update_plane_details_window():
    update_plane_details_window = tk.Tk()
    update_plane_details_window.title("Update Plane Details")

    def go_back():
        update_plane_details_window.destroy()
        create_admin_section()

    back_button = ttk.Button(update_plane_details_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(update_plane_details_window, text="Flight ID:").pack(pady=5)
    flight_id_entry = ttk.Entry(update_plane_details_window, width=30)
    flight_id_entry.pack()

    ttk.Label(update_plane_details_window, text="New Flight Name:").pack(pady=5)
    new_flight_name_entry = ttk.Entry(update_plane_details_window, width=30)
    new_flight_name_entry.pack()

    def update_plane_details_action():
        flight_id = flight_id_entry.get()
        new_flight_name = new_flight_name_entry.get()

        if not (flight_id and new_flight_name):
            messagebox.showerror("Error", "Please enter Flight ID and New Flight Name.")
            return

        conn = connect('root', 'password')
        update_plane(conn, flight_id, new_flight_name)
        conn.close()

        update_plane_details_window.destroy()
        create_admin_section()

    update_plane_details_button = ttk.Button(update_plane_details_window, text="Update Plane Details", command=update_plane_details_action)
    update_plane_details_button.pack(pady=10)

    update_plane_details_window.mainloop()

def create_cancel_flight_window():
    cancel_flight_window = tk.Tk()
    cancel_flight_window.title("Cancel Flight")

    def go_back():
        cancel_flight_window.destroy()
        create_admin_section()

    back_button = ttk.Button(cancel_flight_window, text="Back", command=go_back)
    back_button.pack(pady=10)

    ttk.Label(cancel_flight_window, text="Flight ID:").pack(pady=5)
    flight_id_entry = ttk.Entry(cancel_flight_window, width=30)
    flight_id_entry.pack()

    def cancel_flight_action():
        flight_id = flight_id_entry.get()
        if not flight_id:
            messagebox.showerror("Error", "Please enter Flight ID.")
            return

        conn = connect('root', 'password')
        cancel_flight(conn, flight_id)
        conn.close()

        cancel_flight_window.destroy()
        create_admin_section()

    cancel_flight_button = ttk.Button(cancel_flight_window, text="Cancel Flight", command=cancel_flight_action)
    cancel_flight_button.pack(pady=10)

    cancel_flight_window.mainloop()

create_main_window()
