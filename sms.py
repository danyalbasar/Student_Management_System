from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from tkinter.scrolledtext import *
from PIL import Image, ImageTk
from sqlite3 import *
import datetime
# import geocoder
# import requests

admin_main_window, user_main_window = "", ""
count1 = 0

def general_window_setup(size, window, title, icon):
	window.title(title)
	window.iconbitmap(icon)

	window_width = size[0]
	window_height = size[1]
	window_x = int((window.winfo_screenwidth() / 2) - (window_width / 2))
	window_y = int((window.winfo_screenheight() / 2) - (window_height / 2))

	window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(window_y)
	window.geometry(window_geometry)

	window.resizable(True, True)

	return

def check_login_cred():
	if ent_username.get() == "":
		messagebox.showerror("Error", "Username field is required")
		ent_password.delete(0, END)
		ent_username.focus()
	elif ent_password.get() == "":
		messagebox.showerror("Error", "Password field is required")
		ent_username.delete(0, END)
		ent_password.focus()
	elif ent_username.get() == "admin":
		if ent_password.get() == "admin@123":
			messagebox.showinfo("Success", f"Welcome {ent_username.get()}")
			ent_username.delete(0, END)
			ent_password.delete(0, END)
			admin_home_pg()
		else:
			messagebox.showerror("Error", "Invalid Password")
			ent_password.delete(0, END)
			ent_password.focus()
	elif ent_username.get() == "user":
		if ent_password.get() == "user@123":	
			messagebox.showinfo("Success", f"Welcome {ent_username.get()}")
			ent_username.delete(0, END)
			ent_password.delete(0, END)
			user_home_pg()
		else:
			messagebox.showerror("Error", "Invalid Password")
			ent_password.delete(0, END)
			ent_password.focus()
	elif ent_username.get() != "admin" or ent_password.get() != "admin@123" or ent_username.get() != "user" or ent_password.get() != "user@123":
		messagebox.showerror("Error", "Invalid Username & password")
		ent_username.delete(0, END)
		ent_password.delete(0, END)
		ent_username.focus()

# ------------------------------ Date ------------------------------
try:
	datetime_live = datetime.datetime.now()
	date_live = datetime_live.strftime('%d-%m-%Y')

except Exception as e:
	date_live = "Error"

# ------------------------------ Time ------------------------------
# try:
# 	datetime_live = datetime.datetime.now()
# 	time_live = datetime_live.strftime('%H:%M:%S')
#
# except Exception as e:
# 	time_live = "Error"

# ------------------------------ Admin Page ------------------------------
def admin_home_pg():
	global admin_main_window
	login_window.withdraw()

	admin_main_window = Toplevel(login_window)
	admin_main_window.withdraw()
	general_window_setup((500, 500), admin_main_window, "Admin Homepage", "download.ico")

	bg_image = ImageTk.PhotoImage(file="login_home_pg_bg_img.jpg")

	admin_main_window_canvas = Canvas(admin_main_window, width=500, height=500, bd=0, highlightthickness=0)
	admin_main_window_canvas.pack(fill="both", expand=True)
	admin_main_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def admin_home_pg_sign_out():
		res = messagebox.askquestion('Confirm', 'Are you sure you want to sign out?', icon='warning')
		if res == 'yes':
			login_window.deiconify()
			admin_main_window.destroy()

	f = ("Arial", 18, "bold")

	mw_btn_add = Button(admin_main_window, text="Add", activebackground='#6162FF', activeforeground="white", bd=1, font=f, width=12, bg="#6162FF", fg="white", command=admin_home_pg_add)
	mw_btn_add.place(x=153, y=73)
	mw_btn_add.bind("<Enter>", lambda e: mw_btn_add.config(fg='white', bg='#8080ff'))
	mw_btn_add.bind("<Leave>", lambda e: mw_btn_add.config(fg='white', bg='#6162FF'))

	mw_btn_update = Button(admin_main_window, text="Update", activebackground='#6162FF', activeforeground="white", bd=1, font=f, bg="#6162FF", fg="white", width=12, command=admin_home_pg_update)
	mw_btn_update.place(x=153, y=143)
	mw_btn_update.bind("<Enter>", lambda e: mw_btn_update.config(fg='white', bg='#8080ff'))
	mw_btn_update.bind("<Leave>", lambda e: mw_btn_update.config(fg='white', bg='#6162FF'))

	mw_btn_delete = Button(admin_main_window, text="Delete", activebackground='#6162FF', activeforeground="white", bd=1, font=f, bg="#6162FF", fg="white", width=12, command=admin_home_pg_delete)
	mw_btn_delete.place(x=153, y=215)
	mw_btn_delete.bind("<Enter>", lambda e: mw_btn_delete .config(fg='white', bg='#8080ff'))
	mw_btn_delete.bind("<Leave>", lambda e: mw_btn_delete .config(fg='white', bg='#6162FF'))

	mw_btn_view = Button(admin_main_window, text="View", bd=1, activebackground='#6162FF', activeforeground="white", font=f, bg="#6162FF", fg="white", width=12, command=admin_home_pg_view)
	mw_btn_view.place(x=153, y=283)
	mw_btn_view.bind("<Enter>", lambda e: mw_btn_view.config(fg='white', bg='#8080ff'))
	mw_btn_view.bind("<Leave>", lambda e: mw_btn_view.config(fg='white', bg='#6162FF'))

	mw_btn_sign_out = Button(admin_main_window, text="Log Out", activebackground='red', activeforeground="white", bd=1, font=f, width=12, bg="red", fg="white", command=admin_home_pg_sign_out)
	mw_btn_sign_out.place(x=153, y=353)
	mw_btn_sign_out.bind("<Enter>", lambda e: mw_btn_sign_out .config(fg='white', bg='#ff6464'))
	mw_btn_sign_out.bind("<Leave>", lambda e: mw_btn_sign_out .config(fg='white', bg='red'))

	admin_main_window.deiconify()
	admin_main_window.mainloop()

def admin_home_pg_add():
	global admin_main_window

	admin_main_window.withdraw()

	admin_window =Toplevel(admin_main_window)
	admin_window.withdraw()
	general_window_setup((1280, 768), admin_window, "Admin Add Page", "download.ico")

	bg_image = ImageTk.PhotoImage(file="add_update_view_pg_bg_img.jpg")

	admin_window_canvas = Canvas(admin_window, width=1280, height=768, bd=0, highlightthickness=0)
	admin_window_canvas.pack(fill="both", expand=True)
	admin_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def admin_add_exit():	
		res = messagebox.askquestion('Confirm', 'Are you sure you want to exit?', icon='warning')
		if res == 'yes':
			admin_window.destroy()
			admin_main_window.deiconify()

	def admin_add_clear():
		ent_ref_no.delete(0, END)
		ent_date.delete(0, END)
		combo_issue_reported.delete(0, END)
		scr_issue_reported.delete(1.0, END)
		combo_issue_diagnosed.delete(0, END)
		scr_issue_diagnosed.delete(1.0, END)
		ent_issue_logged_by.delete(0, END)
		combo_machine_type.delete(0, END)
		ent_machine_model.delete(0, END) 
		ent_machine_sr_no.delete(0, END)
		scr_machine_details.delete(1.0, END)

	def admin_add_next():
		ref_no = ent_ref_no.get()

		if len(ref_no) == 0:
			showerror("Ref. No. Issue", "Ref. No. cannot be empty") 
			ent_ref_no.delete(0, END)
			ent_ref_no.focus()
			return

		admin_window.withdraw()

		admin_add_next_window =Toplevel(admin_window)
		admin_add_next_window.withdraw()
		general_window_setup((1280, 768), admin_add_next_window, "Admin Add Page", "download.ico")

		bg_image = ImageTk.PhotoImage(file="add_update_view_pg_bg_img.jpg")

		admin_add_next_window_canvas = Canvas(admin_add_next_window, width=1280, height=768, bd=0, highlightthickness=0)
		admin_add_next_window_canvas.pack(fill="both", expand=True)
		admin_add_next_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

		def admin_add_next_back():
			admin_window.deiconify()
			admin_add_next_window.withdraw()		

		def admin_add_next_clear():
			ent_first_name.delete(0, END)
			ent_last_name.delete(0, END)
			ent_email_1.delete(0, END)
			ent_email_2.delete(0, END)
			ent_mobile_no_1.delete(0, END)
			ent_mobile_no_2.delete(0, END)
			ent_co_name.delete(0, END)
			ent_co_loc.delete(0, END)
			ent_customer_of.delete(0, END)
			ent_address.delete(1.0, END) 
			ent_city.delete(0, END)
			combo_state.delete(0, END)
			ent_pincode.delete(0, END)

		def admin_add_next_2():
			con = None
			try:
				con = connect("customer_data.db")
				cursor = con.cursor()
				cursor.execute("""CREATE TABLE if not exists customers (
					ref_no int primary key,
					issue_reported_date text,
					issue_reported text,
					issue_reported_details text,
					issue_diagnosed text,
					issue_diagnosed_details text,
					issue_logged_by text,
					machine_type text,
					machine_model text,
					machine_sr_no text,
					machine_details text,
					f_name text,
					l_name text,
					email text,
					second_email text,
					mob_no int,
					alter_mob_no int,
					company_name text,
					company_loc text,
					customer_of text,
					address text,
					city text,
					state text,
					country text,
					pincode text)
					""")
				sql ="insert into customers values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"

				ref_no = ent_ref_no.get()
				issue_reported_date = ent_date.get()
				issue_reported = combo_issue_reported.get()
				issue_reported_details = scr_issue_reported.get("1.0", 'end-1c')
				issue_diagnosed = combo_issue_diagnosed.get()
				issue_diagnosed_details = scr_issue_diagnosed.get("1.0", 'end-1c')
				issue_logged_by = ent_issue_logged_by.get()
				machine_type = combo_machine_type.get()
				machine_model =ent_machine_model.get()
				machine_sr_no = ent_machine_sr_no.get()
				machine_details = scr_machine_details.get("1.0", 'end-1c')
				f_name = ent_first_name.get()
				l_name = ent_last_name.get()
				email = ent_email_1.get()
				second_email = ent_email_2.get()
				mob_no = ent_mobile_no_1.get()
				alter_mob_no = ent_mobile_no_2.get()
				company_name = ent_co_name.get()
				company_loc = ent_co_loc.get()
				customer_of = ent_customer_of.get()
				address = ent_address.get("1.0", 'end-1c')
				city = ent_city.get()
				state = combo_state.get()
				country = ent_country.get()
				pincode = ent_pincode.get()
	
				if len(f_name) == 0:
					showerror("First Name Issue", "Name cannot be empty") 
					ent_first_name.delete(0, END)
					ent_first_name.focus()
					return
				if not f_name.isalpha():
					showerror("First Name Issue", "Name cannot be a number") 
					ent_first_name.delete(0, END)
					ent_first_name.focus()
					return
				if len(f_name) < 2:
					showerror("First Name Issue", "Name cannot be less than two letters") 
					ent_first_name.delete(0, END)
					ent_first_name.focus()
					return
				if (not l_name.isalpha()) and (len(l_name) != 0):
					showerror("Last Name Issue", "Name cannot be a number") 
					ent_last_name.delete(0, END)
					ent_last_name.focus()
					return
				if (len(l_name) < 2) and (len(l_name) != 0):
					showerror("Last Name Issue", "Name cannot be less than two letters") 
					ent_last_name.delete(0, END)
					ent_last_name.focus()
					return
				if len(mob_no) == 0:
					showerror("Mobile No Issue", "Mobile No cannot be empty") 
					ent_mobile_no_1.delete(0, END)
					ent_mobile_no_1.focus()
					return
				if not mob_no.isdigit():
					showerror("Mobile No Issue", "Mobile No should be in digits only") 		
					ent_mobile_no_1.delete(0, END)
					ent_mobile_no_1.focus()
					return
				if len(mob_no) < 10:
					showerror("Mobile No Issue", "Mobile No cannot be less than 10 digits")
					ent_mobile_no_1.delete(0, END)
					ent_mobile_no_1.focus()
					return
				if len(mob_no) > 10:
					showerror("Mobile No Issue", "Mobile No cannot be more than 10 digits")
					ent_mobile_no_1.delete(0, END)
					ent_mobile_no_1.focus()
					return
				if (not alter_mob_no.isdigit()) and (len(alter_mob_no) != 0):
					showerror("Alternate Mobile No Issue", "Mobile No should be in digits only") 		
					ent_mobile_no_2.delete(0, END)
					ent_mobile_no_2.focus()
					return
				if (len(alter_mob_no) < 10) and (len(alter_mob_no) != 0):
					showerror("Alternate Mobile No Issue", "Mobile No cannot be less than 10 digits")
					ent_mobile_no_2.delete(0, END)
					ent_mobile_no_2.focus()
					return
				if len(alter_mob_no) > 10:
					showerror("Alternate Mobile No Issue", "Mobile No cannot be more than 10 digits")
					ent_mobile_no_2.delete(0, END)
					ent_mobile_no_2.focus()
					return

				cursor.execute(sql % (ref_no, issue_reported_date, issue_reported, issue_reported_details, issue_diagnosed, issue_diagnosed_details, issue_logged_by, machine_type, machine_model, machine_sr_no, machine_details, f_name, l_name, email, second_email, mob_no, alter_mob_no, company_name, company_loc, customer_of, address, city, state, country, pincode))
				con.commit()
				showinfo("Success", "Record added successfully")

			except Exception as e:
				con.rollback()
				showerror("Error", str(e))

			finally:
				if con is not None:
					con.close()

		option = StringVar()
	
		admin_add_next_window_canvas.create_text(180, 40, text="Contact Details", font=("Impact", 35, "bold"), fill="#6162FF")
		admin_add_next_window_canvas.create_text(152, 95, text="Enter Contact Information", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
		admin_add_next_window_canvas.create_text(82, 140, text="First Name", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(401, 140, text="Last Name", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(55, 225, text="Email", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(430, 225, text="Secondary Email", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(81, 310, text="Mobile No.", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(447, 310, text="Alternate Mobile No.", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(104, 395, text="Company Name", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(118, 480, text="Company Location", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(91, 565, text="Customer of", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(820, 95, text="Address for Machine Location", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
		admin_add_next_window_canvas.create_text(720, 140, text="Address", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(700, 395, text="City", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(1015, 395, text="State", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(719, 480, text="Country", font=("Goudy old style", 15, "bold"), fill="grey")
		admin_add_next_window_canvas.create_text(1029, 480, text="Pincode", font=("Goudy old style", 15, "bold"), fill="grey")

		ent_first_name = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_first_name.place(x=30, y=160, width=275, height=35)
	
		ent_last_name = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_last_name.place(x=350, y=160, width=275, height=35)

		ent_email_1 = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_email_1.place(x=30, y=245, width=275, height=35)

		ent_email_2 = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_email_2.place(x=350, y=245, width=275, height=35)

		ent_mobile_no_1 = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_mobile_no_1.place(x=30, y=330, width=275, height=35)

		ent_mobile_no_2 = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_mobile_no_2.place(x=350, y=330, width=275, height=35)
	
		ent_co_name = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_co_name.place(x=30, y=415, width=600, height=35)

		ent_co_loc = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_co_loc.place(x=30, y=500, width=600, height=35)

		ent_customer_of = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_customer_of.place(x=30, y=587, width=600, height=35)
	
		ent_address = ScrolledText(admin_add_next_window, width=50, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_address.place(x=680, y=160)
	
		ent_city = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_city.place(x=680, y=415, width=275, height=35)

		f = ("Goudy old style", 15)

		style = ttk.Style()
		style.configure('combo_state.TCombobox', selectbackground='blue', arrowsize=15)

		combo_state = ttk.Combobox(admin_add_next_window, textvariable=option, style='combo_state.TCombobox', font=("Goudy old style", 15))
		combo_state["values"] = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu', 'Jharkhand', 'Karnataka', 'Kashmir', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
		combo_state.option_add("*TCombobox*Listbox*Font", f)
		combo_state.place(x=990, y=415, width=260, height=35)
		combo_state.set("")

		ent_country = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_country.insert(END, "India")
		# ent_country.bind("<Key>", lambda a: "break")
		ent_country.place(x=680, y=500, width=275, height=35)

		ent_pincode = Entry(admin_add_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
		ent_pincode.place(x=990, y=500, width=260, height=35)
	
		admin_add_next_btn = Button(admin_add_next_window, text="Next", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_next_2)
		admin_add_next_btn.place(x=1125, y=685)
		admin_add_next_btn.bind("<Enter>", lambda e: admin_add_next_btn.config(fg='white', bg='#8080ff'))
		admin_add_next_btn.bind("<Leave>", lambda e: admin_add_next_btn.config(fg='white', bg='#6162FF'))

		admin_add_back_btn = Button(admin_add_next_window, text="Back", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_next_back)
		admin_add_back_btn.place(x=977, y=685)	
		admin_add_back_btn.bind("<Enter>", lambda e: admin_add_back_btn.config(fg='white', bg='#8080ff'))
		admin_add_back_btn.bind("<Leave>", lambda e: admin_add_back_btn.config(fg='white', bg='#6162FF'))

		admin_add_clear_btn = Button(admin_add_next_window, text="Clear", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_next_clear)
		admin_add_clear_btn.place(x=830, y=685)
		admin_add_clear_btn.bind("<Enter>", lambda e: admin_add_clear_btn.config(fg='white', bg='#8080ff'))
		admin_add_clear_btn.bind("<Leave>", lambda e: admin_add_clear_btn.config(fg='white', bg='#6162FF'))

		admin_exit_btn = Button(admin_add_next_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_exit)
		admin_exit_btn.place(x=682, y=685)
		admin_exit_btn.bind("<Enter>", lambda e: admin_exit_btn.config(fg='white', bg='#ff6464'))
		admin_exit_btn.bind("<Leave>", lambda e: admin_exit_btn.config(fg='white', bg='red'))

		admin_add_next_window.deiconify()
		admin_add_next_window.mainloop()

	option1 = StringVar()
	option2 = StringVar()
	option3 = StringVar()

	admin_window_canvas.create_text(256, 40, text="Issue/Machine Details", font=("Impact", 35, "bold"), fill="#6162FF")
	admin_window_canvas.create_text(120, 95, text="Enter Issue Details ", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
	admin_window_canvas.create_text(69, 140, text="Ref. No.", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(113, 138, text="*", font=("Goudy old style", 15, "bold"), fill="red")
	admin_window_canvas.create_text(438, 140, text="Issue Reported on", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(103, 225, text="Issue Reported", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(430, 225, text="Issue Diagnosed", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(63, 315, text="Details", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(384, 315, text="Details", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(205, 563, text="Issue Logged By (Engineers's Name)", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(752, 95, text="Machine Details", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
	admin_window_canvas.create_text(747, 140, text="Machine Type", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(752, 225, text="Machine Model", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(1061, 225, text="Machine Sr. No.", font=("Goudy old style", 15, "bold"), fill="grey")
	admin_window_canvas.create_text(820, 315, text="Machine Details & Accesories", font=("Goudy old style", 15, "bold"), fill="grey")	

	ent_ref_no = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_ref_no.place(x=30, y=160, width=275, height=35)

	con = None	
	try:
		con = connect("customer_data.db")
		cursor = con.cursor()

		sql = "select ref_no from customers"
		cursor.execute(sql)
		data = cursor.fetchall()
		if len(data) != 0:
			count = len(data) + 1
		else:
			count = 1
	except Exception as e:
		con.rollback()
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()

	ent_ref_no.insert(END, count)

	ent_date = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_date.insert(END, date_live)
	ent_date.place(x=350, y=160, width=275, height=35)

	f = ("Goudy old style", 15)
	
	style = ttk.Style()
	style.configure('combo_issue_reported.TCombobox', selectbackground='blue', arrowsize=15)

	combo_issue_reported = ttk.Combobox(admin_window, textvariable=option1, style='combo_issue_reported.TCombobox', font=("Goudy old style", 15))
	combo_issue_reported["values"] = ['Video Display Issue', 'Power & Startup', 'Operating System Errors & Blue Screen', 'Hard Drive Related', 'Keyboard Mouse & Accessories', 'Internet Connectivity Issues', 'Battery & Adapter', 'Audio & Speakers', 'USB Port Issues', 'Bluetooth & Wifi', 'Software & 3rd Party Applications', 'System Hardware Performance', 'Status Updates', 'Other Issues']
	combo_issue_reported.option_add("*TCombobox*Listbox*Font", f)
	combo_issue_reported.place(x=30, y=245, width=276, height=35)
	combo_issue_reported.set("")

	scr_issue_reported = ScrolledText(admin_window, width=23, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	scr_issue_reported.place(x=30, y=335)

	style.configure('combo_issue_diagnosed.TCombobox', selectbackground='blue', arrowsize=15)

	combo_issue_diagnosed = ttk.Combobox(admin_window, textvariable=option2, style='combo_issue_diagnosed.TCombobox', font=("Goudy old style", 15))
	combo_issue_diagnosed["values"] = ['Video Display Issue', 'Power & Startup', 'Operating System Errors & Blue Screen', 'Hard Drive Related', 'Keyboard, Mouse & Accessories', 'Internet Connectivity Issues', 'Battery & Adapter', 'Audio & Speakers', 'USB Port Issues', 'Bluetooth & Wifi', 'Software & 3rd Party Applications', 'System Hardware Performance', 'Status Updates', 'Other Issues']
	combo_issue_diagnosed.option_add("*TCombobox*Listbox*Font", f)
	combo_issue_diagnosed.place(x=350, y=245, width=276, height=35)
	combo_issue_diagnosed.set("")

	scr_issue_diagnosed = ScrolledText(admin_window, width=23, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	scr_issue_diagnosed.place(x=350, y=335)

	ent_issue_logged_by = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_issue_logged_by.place(x=30, y=586, width=600, height=35)

	style.configure('combo_machine_type.TCombobox', selectbackground='blue', arrowsize=15)

	combo_machine_type = ttk.Combobox(admin_window, textvariable=option3, style='combo_machine_type.TCombobox', font=("Goudy old style", 15))
	combo_machine_type["values"] = ['Desktop', 'Laptop', 'All-In-One', 'Tablet', 'Server', 'Switch', 'Router', 'NAS', 'UPS', 'External HDD', 'Modem', 'Printer', 'Scanner', 'Projector', 'Speakers', 'Headphones', 'Mouse', 'Keyboard', 'Others']
	combo_machine_type.option_add("*TCombobox*Listbox*Font", f)
	combo_machine_type.place(x=680, y=160, width=270, height=35)
	combo_machine_type.set("")

	ent_machine_model = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_machine_model.place(x=680, y=245, width=270, height=35)

	ent_machine_sr_no = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_machine_sr_no.place(x=985, y=245, width=270, height=35)

	scr_machine_details = ScrolledText(admin_window, width=50, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	scr_machine_details.place(x=680, y=335)
				
	admin_next_btn = Button(admin_window, text="Next", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_next)
	admin_next_btn.place(x=1125, y=685)
	admin_next_btn.bind("<Enter>", lambda e: admin_next_btn.config(fg='white', bg='#8080ff'))
	admin_next_btn.bind("<Leave>", lambda e: admin_next_btn.config(fg='white', bg='#6162FF'))

	admin_clear_btn = Button(admin_window, text="Clear", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_clear)
	admin_clear_btn.place(x=977, y=685)
	admin_clear_btn.bind("<Enter>", lambda e: admin_clear_btn.config(fg='white', bg='#8080ff'))
	admin_clear_btn.bind("<Leave>", lambda e: admin_clear_btn.config(fg='white', bg='#6162FF'))

	admin_exit_btn = Button(admin_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_add_exit)
	admin_exit_btn.place(x=830, y=685)
	admin_exit_btn.bind("<Enter>", lambda e: admin_exit_btn.config(fg='white', bg='#ff6464'))
	admin_exit_btn.bind("<Leave>", lambda e: admin_exit_btn.config(fg='white', bg='red'))
	
	admin_window.deiconify()
	admin_window.mainloop()

def admin_home_pg_update():
	global admin_main_window, date_live, time_live, ent_ref_no
	admin_main_window.withdraw()

	admin_select_window =Toplevel(admin_main_window)
	admin_select_window .withdraw()
	general_window_setup((480, 360), admin_select_window , "Admin Update Page", "download.ico")

	bg_image = ImageTk.PhotoImage(file="update_delete_pg_bg_img.jpg")

	admin_select_window_canvas = Canvas(admin_select_window, width=480, height=360, bd=0, highlightthickness=0)
	admin_select_window_canvas.pack(fill="both", expand=True)
	admin_select_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")
	
	def admin_select_exit():
		admin_main_window.deiconify()
		admin_select_window.destroy()

	def admin_update():
		ref_no_typed = ent_ref_no_typed.get()

		if len(ref_no_typed) == 0:
			showerror("Error", "No Ref No. provided")
			ent_ref_no_typed.focus()
			return
		if not ref_no_typed.isdigit():
			showerror("Error", "Ref No. only accepts digits as input")
			ent_ref_no_typed.focus()
			return

		con = None	
		try:
			con = connect("customer_data.db")
			cursor = con.cursor()

			sql = "select ref_no from customers"
			cursor.execute(sql)
			data = cursor.fetchall()
			new_data = str(data).strip('[]')

			
			if not ref_no_typed in new_data:
				showerror("Error", "Ref. No. does not exist")
			else:	
				sql_2 = "select * from customers where ref_no=?"
				cursor.execute(sql_2, (ref_no_typed,))
				data_2 = cursor.fetchall()

				for d in data_2:
					ref_no = str(d[0])
					issue_reported_date = str(d[1])
					issue_reported = str(d[2])
					issue_reported_details = str(d[3])
					issue_diagnosed = str(d[4])
					issue_diagnosed_details = str(d[5])
					issue_logged_by = str(d[6])
					machine_type = str(d[7])
					machine_model = str(d[8])
					machine_sr_no = str(d[9])
					machine_details = str(d[10])
					f_name = str(d[11])
					l_name = str(d[12])
					email = str(d[13])
					second_email = str(d[14])
					mob_no = str(d[15])
					alter_mob_no = str(d[16])
					company_name = str(d[17])
					company_loc = str(d[18])
					customer_of = str(d[19])
					address = str(d[20])
					city = str(d[21])
					state = str(d[22])
					country = str(d[23])
					pincode = str(d[24])
					
				admin_select_window.withdraw()

				admin_window =Toplevel(admin_select_window)
				admin_window.withdraw()
				general_window_setup((1280, 720), admin_window, "Admin Update Page", "download.ico")

				bg_image = ImageTk.PhotoImage(file="add_update_view_pg_bg_img.jpg")

				admin_window_canvas = Canvas(admin_window, width=1280, height=720, bd=0, highlightthickness=0)
				admin_window_canvas.pack(fill="both", expand=True)
				admin_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

				def admin_update_exit():	
					res = messagebox.askquestion('Confirm', 'Are you sure you want to exit?', icon='warning')
					if res == 'yes':
						admin_select_window.deiconify()
						admin_window.destroy()

				def admin_update_clear():
					ent_ref_no.delete(0, END)
					ent_date.delete(0, END)
					combo_issue_reported.delete(0, END)
					scr_issue_reported.delete(1.0, END)
					combo_issue_diagnosed.delete(0, END)
					scr_issue_diagnosed.delete(1.0, END)
					ent_issue_logged_by.delete(0, END)
					combo_machine_type.delete(0, END)
					ent_machine_model.delete(0, END) 
					ent_machine_sr_no.delete(0, END)
					scr_machine_details.delete(1.0, END)

				def admin_update_next():
					admin_window.withdraw()

					admin_update_next_window =Toplevel(admin_window)
					admin_update_next_window.withdraw()
					general_window_setup((1280, 720), admin_update_next_window, "Admin Update Page", "download.ico")

					bg_image = ImageTk.PhotoImage(file="add_update_view_pg_bg_img.jpg")

					admin_update_next_window_canvas = Canvas(admin_update_next_window, width=1280, height=720, bd=0, highlightthickness=0)
					admin_update_next_window_canvas.pack(fill="both", expand=True)
					admin_update_next_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")
	
					def admin_update_next_back():
						admin_window.deiconify()
						admin_update_next_window.withdraw()

					def admin_update_next_clear():
						ent_first_name.delete(0, END)
						ent_last_name.delete(0, END)
						ent_email_1.delete(0, END)
						ent_email_2.delete(0, END)
						ent_mobile_no_1.delete(0, END)
						ent_mobile_no_2.delete(0, END)
						ent_co_name.delete(0, END)
						ent_co_loc.delete(0, END)
						ent_customer_of.delete(0, END)
						ent_address.delete(1.0, END) 
						ent_city.delete(0, END)
						combo_state.delete(0, END)
						ent_pincode.delete(0, END)

					def admin_update_next_2():
						con = None
						try:
							con = connect("customer_data.db")
							cursor = con.cursor()
							sql ="update customers set issue_reported_date='%s', issue_reported='%s', issue_reported_details='%s', issue_diagnosed='%s', issue_diagnosed_details='%s', issue_logged_by='%s', machine_type='%s', machine_model='%s', machine_sr_no='%s', machine_details='%s', f_name='%s', l_name='%s', email='%s', second_email='%s', mob_no='%s', alter_mob_no='%s', company_name='%s', company_loc='%s', customer_of='%s', address='%s', city='%s', state='%s', country='%s', pincode='%s' where ref_no ='%s'"
							issue_reported_date = ent_date.get()
							issue_reported = combo_issue_reported.get()
							issue_reported_details = scr_issue_reported.get("1.0", 'end-1c')
							issue_diagnosed = combo_issue_diagnosed.get()
							issue_diagnosed_details = scr_issue_diagnosed.get("1.0", 'end-1c')
							issue_logged_by = ent_issue_logged_by.get()
							machine_type = combo_machine_type.get()
							machine_model =ent_machine_model.get()
							machine_sr_no = ent_machine_sr_no.get()
							machine_details = scr_machine_details.get("1.0", 'end-1c')
							f_name = ent_first_name.get()
							l_name = ent_last_name.get()
							email = ent_email_1.get()
							second_email = ent_email_2.get()
							mob_no = ent_mobile_no_1.get()
							alter_mob_no = ent_mobile_no_2.get()
							company_name = ent_co_name.get()
							company_loc = ent_co_loc.get()
							customer_of = ent_customer_of.get()
							address = ent_address.get("1.0", 'end-1c')
							city = ent_city.get()
							state = combo_state.get()
							country = ent_country.get()
							pincode = ent_pincode.get()
							ref_no = ent_ref_no.get()
	
							if len(f_name) == 0:
								showerror("First Name Issue", "Name cannot be empty") 
								ent_first_name.delete(0, END)
								ent_first_name.focus()
								return
							if not f_name.isalpha():
								showerror("First Name Issue", "Name cannot be a number") 
								ent_first_name.delete(0, END)
								ent_first_name.focus()
								return
							if len(f_name) < 2:
								showerror("First Name Issue", "Name cannot be less than two letters") 
								ent_first_name.delete(0, END)
								ent_first_name.focus()
								return
							if (not l_name.isalpha()) and (len(l_name) != 0):
								showerror("Last Name Issue", "Name cannot be a number") 
								ent_last_name.delete(0, END)
								ent_last_name.focus()
								return
							if (len(l_name) < 2) and (len(l_name) != 0):
								showerror("Last Name Issue", "Name cannot be less than two letters") 
								ent_last_name.delete(0, END)
								ent_last_name.focus()
								return
							if len(mob_no) == 0:
								showerror("Mobile No Issue", "Mobile No cannot be empty") 
								ent_mobile_no_1.delete(0, END)
								ent_mobile_no_1.focus()
								return
							if not mob_no.isdigit():
								showerror("Mobile No Issue", "Mobile No should be in digits only") 		
								ent_mobile_no_1.delete(0, END)
								ent_mobile_no_1.focus()
								return
							if len(mob_no) < 10:
								showerror("Mobile No Issue", "Mobile No cannot be less than 10 digits")
								ent_mobile_no_1.delete(0, END)
								ent_mobile_no_1.focus()
								return
							if len(mob_no) > 10:
								showerror("Mobile No Issue", "Mobile No cannot be more than 10 digits")
								ent_mobile_no_1.delete(0, END)
								ent_mobile_no_1.focus()
								return
							if (not alter_mob_no.isdigit()) and (len(alter_mob_no) != 0):
								showerror("Alternate Mobile No Issue", "Mobile No should be in digits only") 		
								ent_mobile_no_2.delete(0, END)
								ent_mobile_no_2.focus()
								return
							if (len(alter_mob_no) < 10) and (len(alter_mob_no) != 0):
								showerror("Alternate Mobile No Issue", "Mobile No cannot be less than 10 digits")
								ent_mobile_no_2.delete(0, END)
								ent_mobile_no_2.focus()
								return
							if len(alter_mob_no) > 10:
								showerror("Alternate Mobile No Issue", "Mobile No cannot be more than 10 digits")
								ent_mobile_no_2.delete(0, END)
								ent_mobile_no_2.focus()
								return

							cursor.execute(sql % (issue_reported_date, issue_reported, issue_reported_details, issue_diagnosed, issue_diagnosed_details, issue_logged_by, machine_type, machine_model, machine_sr_no, machine_details, f_name, l_name, email, second_email, mob_no, alter_mob_no, company_name, company_loc, customer_of, address, city, state, country, pincode, ref_no))
							if cursor.rowcount == 1:
								con.commit()
								showinfo("Success", "Record updated successfully")

						except Exception as e:
							con.rollback()
							showerror("Error", str(e))

						finally:
							if con is not None:
								con.close()

					option = StringVar()
	
					admin_update_next_window_canvas.create_text(180, 40, text="Contact Details", font=("Impact", 35, "bold"), fill="#6162FF")
					admin_update_next_window_canvas.create_text(152, 95, text="Enter Contact Information", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
					admin_update_next_window_canvas.create_text(82, 140, text="First Name", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(401, 140, text="Last Name", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(55, 225, text="Email", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(430, 225, text="Secondary Email", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(81, 310, text="Mobile No.", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(447, 310, text="Alternate Mobile No.", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(104, 395, text="Company Name", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(118, 480, text="Company Location", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(91, 565, text="Customer Of", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(820, 95, text="Address for Machine Location", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
					admin_update_next_window_canvas.create_text(720, 140, text="Address", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(700, 395, text="City", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(1015, 395, text="State", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(719, 480, text="Country", font=("Goudy old style", 15, "bold"), fill="grey")
					admin_update_next_window_canvas.create_text(1029, 480, text="Pincode", font=("Goudy old style", 15, "bold"), fill="grey")

					ent_first_name = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_first_name.place(x=30, y=160, width=275, height=35)

					ent_last_name = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_last_name.place(x=350, y=160, width=275, height=35)

					ent_email_1 = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_email_1.place(x=30, y=245, width=275, height=35)
	
					ent_email_2 = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_email_2.place(x=350, y=245, width=275, height=35)

					ent_mobile_no_1 = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_mobile_no_1.place(x=30, y=330, width=275, height=35)

					ent_mobile_no_2 = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_mobile_no_2.place(x=350, y=330, width=275, height=35)
	
					ent_co_name = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_co_name.place(x=30, y=415, width=600, height=35)

					ent_co_loc = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_co_loc.place(x=30, y=500, width=600, height=35)

					ent_customer_of = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_customer_of.place(x=30, y=587, width=600, height=35)

					ent_address = ScrolledText(admin_update_next_window, width=50, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_address.place(x=680, y=160)
		
					ent_city = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_city.place(x=680, y=415, width=275, height=35)
	
					f = ("Goudy old style", 15)

					style = ttk.Style()
					style.configure('combo_state.TCombobox', selectbackground='blue', arrowsize=15)

					combo_state = ttk.Combobox(admin_update_next_window, textvariable=option, style='combo_state.TCombobox', font=("Goudy old style", 15))
					combo_state["values"] = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu', 'Jharkhand', 'Karnataka', 'Kashmir', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal']
					combo_state.option_add("*TCombobox*Listbox*Font", f)
					combo_state.place(x=990, y=415, width=260, height=35)
					combo_state.set("")

					ent_country = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_country.insert(END, 'India')
					# ent_country.bind("<Key>", lambda a: "break")
					ent_country.place(x=680, y=500, width=275, height=35)

					ent_pincode = Entry(admin_update_next_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
					ent_pincode.place(x=990, y=500, width=260, height=35)

					ent_first_name.insert(END, f_name)
					ent_last_name.insert(END, l_name)
					ent_email_1.insert(END, email)
					ent_email_2.insert(END, second_email)
					ent_mobile_no_1.insert(END, mob_no)
					ent_mobile_no_2.insert(END, alter_mob_no)
					ent_co_name.insert(END, company_name)
					ent_co_loc.insert(END, company_loc)
					ent_customer_of.insert(END, customer_of)
					ent_address.insert(END, address) 
					ent_city.insert(END, city)
					combo_state.insert(END, state)
					ent_pincode.insert(END, pincode)
				

					admin_update_next_btn = Button(admin_update_next_window, text="Next", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_next_2)
					admin_update_next_btn.place(x=1125, y=625)
					admin_update_next_btn.bind("<Enter>", lambda e: admin_update_next_btn.config(fg='white', bg='#8080ff'))
					admin_update_next_btn.bind("<Leave>", lambda e: admin_update_next_btn.config(fg='white', bg='#6162FF'))

					admin_update_back_btn = Button(admin_update_next_window, text="Back", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_next_back)
					admin_update_back_btn.place(x=977, y=625)
					admin_update_back_btn .bind("<Enter>", lambda e: admin_update_back_btn .config(fg='white', bg='#8080ff'))
					admin_update_back_btn .bind("<Leave>", lambda e: admin_update_back_btn .config(fg='white', bg='#6162FF'))

					admin_update_clear_btn = Button(admin_update_next_window, text="Clear", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_next_clear)
					admin_update_clear_btn.place(x=830, y=625)
					admin_update_clear_btn.bind("<Enter>", lambda e: admin_update_clear_btn.config(fg='white', bg='#8080ff'))
					admin_update_clear_btn.bind("<Leave>", lambda e: admin_update_clear_btn.config(fg='white', bg='#6162FF'))

					admin_update_exit_btn = Button(admin_update_next_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_exit)
					admin_update_exit_btn.place(x=682, y=625)
					admin_update_exit_btn.bind("<Enter>", lambda e: admin_update_exit_btn.config(fg='white', bg='#ff6464'))
					admin_update_exit_btn.bind("<Leave>", lambda e: admin_update_exit_btn.config(fg='white', bg='red'))
	
					admin_update_next_window.deiconify()
					admin_update_next_window.mainloop()
	
				option1 = StringVar()
				option2 = StringVar()
				option3 = StringVar()

				admin_window_canvas.create_text(256, 40, text="Issue/Machine Details", font=("Impact", 35, "bold"), fill="#6162FF")
				admin_window_canvas.create_text(120, 95, text="Enter Issue Details ", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
				admin_window_canvas.create_text(69, 140, text="Ref. No.", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(438, 140, text="Issue Reported on", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(103, 225, text="Issue Reported", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(430, 225, text="Issue Diagnosed", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(63, 315, text="Details", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(384, 315, text="Details", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(205, 563, text="Issue Logged By (Engineers's Name)", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(752, 95, text="Machine Details", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
				admin_window_canvas.create_text(747, 140, text="Machine Type", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(752, 225, text="Machine Model", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(1061, 225, text="Machine Sr. No.", font=("Goudy old style", 15, "bold"), fill="grey")
				admin_window_canvas.create_text(820, 315, text="Machine Details & Accesories", font=("Goudy old style", 15, "bold"), fill="grey")	
	
				ent_ref_no = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				ent_ref_no.place(x=30, y=160, width=275, height=35)

				ent_date = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				ent_date.bind("<Key>", lambda a: "break")
				ent_date.place(x=350, y=160, width=275, height=35)
		
				f = ("Goudy old style", 15)

				style = ttk.Style()
				style.configure('combo_issue_reported.TCombobox', selectbackground='blue', arrowsize=15)

				combo_issue_reported = ttk.Combobox(admin_window, textvariable=option1, style='combo_issue_reported.TCombobox', font=("Goudy old style", 15))
				combo_issue_reported["values"] = ['Video Display Issue', 'Power & Startup', 'Operating System Errors & Blue Screen', 'Hard Drive Related', 'Keyboard Mouse & Accessories', 'Internet Connectivity Issues', 'Battery & Adapter', 'Audio & Speakers', 'USB Port Issues', 'Bluetooth & Wifi', 'Software & 3rd Party Applications', 'System Hardware Performance', 'Status Updates', 'Other Issues']
				combo_issue_reported.option_add("*TCombobox*Listbox*Font", f)
				combo_issue_reported.place(x=30, y=245, width=276, height=35)
				combo_issue_reported.set("")

				scr_issue_reported = ScrolledText(admin_window, width=23, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				scr_issue_reported.place(x=30, y=335)

				style.configure('combo_issue_diagnosed.TCombobox', selectbackground='blue', arrowsize=15)

				combo_issue_diagnosed = ttk.Combobox(admin_window, textvariable=option2, style='combo_issue_diagnosed.TCombobox', font=("Goudy old style", 15))
				combo_issue_diagnosed["values"] = ['Video Display Issue', 'Power & Startup', 'Operating System Errors & Blue Screen', 'Hard Drive Related', 'Keyboard, Mouse & Accessories', 'Internet Connectivity Issues', 'Battery & Adapter', 'Audio & Speakers', 'USB Port Issues', 'Bluetooth & Wifi', 'Software & 3rd Party Applications', 'System Hardware Performance', 'Status Updates', 'Other Issues']
				combo_issue_diagnosed.option_add("*TCombobox*Listbox*Font", f)
				combo_issue_diagnosed.place(x=350, y=245, width=276, height=35)
				combo_issue_diagnosed.set("")

				scr_issue_diagnosed = ScrolledText(admin_window, width=23, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				scr_issue_diagnosed.place(x=350, y=335)

				ent_issue_logged_by = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				ent_issue_logged_by.place(x=30, y=586, width=600, height=35)

				style.configure('combo_machine_type.TCombobox', selectbackground='blue', arrowsize=15)
		
				combo_machine_type = ttk.Combobox(admin_window, textvariable=option3, style='combo_machine_type.TCombobox', font=("Goudy old style", 15))
				combo_machine_type["values"] = ['Desktop', 'Laptop', 'All-In-One', 'Server', 'Switch', 'Router', 'UPS', 'External HDD', 'Modem', 'Printer', 'Scanner', 'Projector', 'Speakers', 'Headphones', 'Mouse', 'Keyboard', 'Others']
				combo_machine_type.option_add("*TCombobox*Listbox*Font", f)
				combo_machine_type.place(x=680, y=160, width=270, height=35)
				combo_machine_type.set("")

				ent_machine_model = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				ent_machine_model.place(x=680, y=245, width=270, height=35)
	
				ent_machine_sr_no = Entry(admin_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				ent_machine_sr_no.place(x=985, y=245, width=270, height=35)

				scr_machine_details = ScrolledText(admin_window, width=50, height=8.45, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
				scr_machine_details.place(x=680, y=335)

				ent_ref_no.insert(END, ref_no)
				ent_date.insert(END, issue_reported_date)
				combo_issue_reported.insert(END, issue_reported)
				scr_issue_reported.insert(END, issue_reported_details)
				combo_issue_diagnosed.insert(END, issue_diagnosed)
				scr_issue_diagnosed.insert(END, issue_diagnosed_details)
				ent_issue_logged_by.insert(END, issue_logged_by)
				combo_machine_type.insert(END, machine_type)
				ent_machine_model.insert(END, machine_model) 
				ent_machine_sr_no.insert(END, machine_sr_no)
				scr_machine_details.insert(END, machine_details)

				admin_next_btn = Button(admin_window, text="Next", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_next)
				admin_next_btn.place(x=1125, y=625)
				admin_next_btn.bind("<Enter>", lambda e: admin_next_btn.config(fg='white', bg='#8080ff'))
				admin_next_btn.bind("<Leave>", lambda e: admin_next_btn.config(fg='white', bg='#6162FF'))

				admin_clear_btn = Button(admin_window, text="Clear", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_clear)
				admin_clear_btn.place(x=977, y=625)
				admin_clear_btn.bind("<Enter>", lambda e: admin_clear_btn.config(fg='white', bg='#8080ff'))
				admin_clear_btn.bind("<Leave>", lambda e: admin_clear_btn.config(fg='white', bg='#6162FF'))

				admin_exit_btn = Button(admin_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=8, bd=1, font=("Arial", 18, "bold"), command=admin_update_exit)
				admin_exit_btn.place(x=830, y=625)
				admin_exit_btn.bind("<Enter>", lambda e: admin_exit_btn.config(fg='white', bg='#ff6464'))
				admin_exit_btn.bind("<Leave>", lambda e: admin_exit_btn.config(fg='white', bg='red'))
				
				admin_window.deiconify()
				admin_window.mainloop()

		except Exception as e:
			con.rollback()
			showerror("Error", str(e))

		finally:
			if con is not None:
				con.close()

	admin_select_window_canvas.create_text(237, 80, text="Enter the Ref. No. to update:", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")

	ent_ref_no_typed = Entry(admin_select_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_ref_no_typed.place(x=95, y=110, width=290, height=35)

	admin_select_update_btn = Button(admin_select_window, text="Update", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=10, bd=1, font=("Arial", 17, "bold"), command=admin_update)
	admin_select_update_btn.place(x=162, y=172)
	admin_select_update_btn.bind("<Enter>", lambda e: admin_select_update_btn.config(fg='white', bg='#8080ff'))
	admin_select_update_btn.bind("<Leave>", lambda e: admin_select_update_btn.config(fg='white', bg='#6162FF'))

	admin_select_exit_btn = Button(admin_select_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=10, bd=1, font=("Arial", 17, "bold"), command=admin_select_exit)
	admin_select_exit_btn.place(x=162, y=240)
	admin_select_exit_btn.bind("<Enter>", lambda e: admin_select_exit_btn.config(fg='white', bg='#ff6464'))
	admin_select_exit_btn.bind("<Leave>", lambda e: admin_select_exit_btn.config(fg='white', bg='red'))

	admin_select_window.deiconify()
	admin_select_window.mainloop()
	
def admin_home_pg_delete():
	global admin_main_window
	admin_main_window.withdraw()

	admin_delete_window =Toplevel(admin_main_window)
	admin_delete_window.withdraw()
	general_window_setup((480, 360), admin_delete_window, "Admin Delete Page", "download.ico")

	bg_image = ImageTk.PhotoImage(file="update_delete_pg_bg_img.jpg")

	admin_delete_window_canvas = Canvas(admin_delete_window, width=1600, height=900, bd=0, highlightthickness=0)
	admin_delete_window_canvas.pack(fill="both", expand=True)
	admin_delete_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def admin_delete():
		ref_no_typed = ent_ref_no_typed.get()

		if len(ref_no_typed) == 0:
			showerror("Error", "No Ref No. provided")
			ent_ref_no_typed.focus()
			return
		if not ref_no_typed.isdigit():
			showerror("Error", "Ref No. only accepts digits as input")
			ent_ref_no_typed.focus()
			return

		con = None
		try:
			con = connect("customer_data.db")
			cursor = con.cursor()

			sql = "select ref_no from customers"
			cursor.execute(sql)
			data = cursor.fetchall()
			new_data = str(data).strip('[]')

			if not ref_no_typed in new_data:
				showerror("Error", "Ref. No. does not exist")
				ent_ref_no_typed.delete(0, END)
				ent_ref_no_typed.focus()
			else:
				sql_2 = "delete from customers where ref_no=?"
				cursor.execute(sql_2, (ref_no_typed,))
				if cursor.rowcount == 1:
					con.commit()
					showinfo("Success", "Ref. No. deleted")
					ent_ref_no_typed.delete(0, END)

		except Exception as e:
			con.rollback()
			showerror("Error", str(e))

		finally:
			if con is not None:
				con.close()

	def admin_delete_exit():
		admin_main_window.deiconify()
		admin_delete_window.destroy()

	admin_delete_window_canvas.create_text(237, 80, text="Enter the Ref. No. to delete:", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")

	ent_ref_no_typed = Entry(admin_delete_window, font=("Goudy old style", 15), bd=1, bg="white", fg="black")
	ent_ref_no_typed.place(x=95, y=110, width=290, height=35)

	admin_delete_btn = Button(admin_delete_window, text="Delete", activebackground='#6162FF', activeforeground="white", bg="#6162FF", fg="white", width=10, bd=1, font=("Arial", 17, "bold"), command=admin_delete)
	admin_delete_btn.place(x=162, y=172)
	admin_delete_btn.bind("<Enter>", lambda e: admin_delete_btn.config(fg='white', bg='#8080ff'))
	admin_delete_btn.bind("<Leave>", lambda e: admin_delete_btn.config(fg='white', bg='#6162FF'))

	admin_delete_exit_btn = Button(admin_delete_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=10, bd=1, font=("Arial", 17, "bold"), command=admin_delete_exit)
	admin_delete_exit_btn.place(x=162, y=240)
	admin_delete_exit_btn.bind("<Enter>", lambda e: admin_delete_exit_btn.config(fg='white', bg='#ff6464'))
	admin_delete_exit_btn.bind("<Leave>", lambda e: admin_delete_exit_btn.config(fg='white', bg='red'))

	admin_delete_window.deiconify()
	admin_delete_window.mainloop()

def admin_home_pg_view():
	global admin_main_window
	admin_main_window.withdraw()

	admin_window = Toplevel(admin_main_window)
	admin_window.withdraw()
	general_window_setup((1280, 720), admin_window, "Admin View Page", "download.ico")

	bg_image = ImageTk.PhotoImage(file="add_update_view_pg_bg_img.jpg")

	admin_window_canvas = Canvas(admin_window, width=1280, height=720, bd=0, highlightthickness=0)
	admin_window_canvas.pack(fill="both", expand=True)
	admin_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def admin_exit():
		admin_main_window.deiconify()
		admin_window.destroy()

	style = ttk.Style()

	# Add a Treeview widget
	tree = ttk.Treeview(admin_window_canvas, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=25)
	tree.column("# 1", anchor=CENTER)
	tree.heading("# 1", text="ID")
	tree.column("# 2", anchor=CENTER)
	tree.heading("# 2", text="Company")
	tree.column("# 3", anchor=CENTER)
	tree.heading("# 3", text="ID")
	tree.column("# 4", anchor=CENTER)
	tree.heading("# 4", text="Company")
	tree.column("# 5", anchor=CENTER)
	tree.heading("# 5", text="ID")

	# Insert the data in Treeview widget
	tree.insert('', 'end', text="1", values=('1', 'Honda'))
	tree.insert('', 'end', text="2", values=('2', 'Hyundai'))
	tree.insert('', 'end', text="3", values=('3', 'Tesla'))
	tree.insert('', 'end', text="4", values=('4', 'Wolkswagon'))
	tree.insert('', 'end', text="5", values=('5', 'Tata Motors'))
	tree.insert('', 'end', text="6", values=('6', 'Renault'))

	tree.place(x=20, y=20, width=1235)

	admin_exit_btn = Button(admin_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", width=12, bd=1, font=("Arial", 18, "bold"), command=admin_exit)
	admin_exit_btn.place(x=550, y=600)
	admin_exit_btn.bind("<Enter>", lambda e: admin_exit_btn.config(fg='white', bg='#ff6464'))
	admin_exit_btn.bind("<Leave>", lambda e: admin_exit_btn.config(fg='white', bg='red'))

	admin_window.deiconify()
	admin_window.mainloop()

# ------------------------------ User Page ------------------------------
def user_home_pg():
	global user_main_window
	login_window.withdraw()

	user_main_window = Toplevel(login_window)
	user_main_window.withdraw()
	general_window_setup((500, 530), user_main_window, "Admin Homepage", "download.ico")

	bg_image = ImageTk.PhotoImage(file="home_pg_bg_img.jpg")

	user_main_window_canvas = Canvas(user_main_window, width=500, height=530, bd=0, highlightthickness=0)
	user_main_window_canvas.pack(fill="both", expand=True)
	user_main_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def user_home_pg_exit():
		res = messagebox.askquestion('Confirm', 'Are you sure you want to sign out?', icon='warning')
		if res == 'yes':
			login_window.deiconify()
			user_main_window.destroy()

	f = ("Arial", 18, "bold")

	mw_btn_view = Button(user_main_window, text="View", bd=1, font=f, bg="#6162FF", fg="white", width=12)
	mw_btn_view.place(x=154, y=20)
	mw_btn_exit = Button(user_main_window, text="Log Out", bd=1, font=f, width=12, bg="red", fg="white", command=user_home_pg_exit)
	mw_btn_exit.place(x=154, y=90)

	user_main_window.deiconify()
	user_main_window.mainloop()

def user_home_view():
	global user_main_window
	user_main_window.withdraw()

	user_window = Toplevel(user_main_window)
	user_window.withdraw()
	general_window_setup((1280, 720), user_window, "User Homepage", "download.ico")
	
	bg_image = ImageTk.PhotoImage(file="add_update_view_bg_img.jpg")

	user_window_canvas = Canvas(user_window, width=1280, height=720, bd=0, highlightthickness=0)
	user_window_canvas.pack(fill="both", expand=True)
	user_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

	def user_exit():
		res = messagebox.askquestion('Confirm', 'Are you sure you want to exit?', icon='warning')
		if res == 'yes':
			user_main_window.deiconify()
			user_window.destroy()

	user_exit_btn = Button(user_window, text="Exit", activebackground='red', activeforeground="white", bg="red", fg="white", font=("Arial", 25, "bold"), command=user_exit)
	user_exit_btn.place(x=550, y=600)
	user_exit_btn.bind("<Enter>", lambda e: user_exit_btn.config(fg='white', bg='#ff6464'))
	user_exit_btn.bind("<Leave>", lambda e: user_exit_btn.config(fg='white', bg='red'))

	user_window.deiconify()
	user_window.mainloop()

# ------------------------------ Login Page ------------------------------
login_window = Tk()
login_window.withdraw()
general_window_setup((500, 500), login_window, "Login Page", "download.ico")

bg_image = ImageTk.PhotoImage(file="login_home_pg_bg_img.jpg")

login_window_canvas = Canvas(login_window, width=500, height=500, bd=0, highlightthickness=0)
login_window_canvas.pack(fill="both", expand=True)
login_window_canvas.create_image(0, 0, image=bg_image, anchor="nw")

login_window_canvas.create_text(144, 80, text="Login", font=("Impact", 35, "bold"), fill="#6162FF")
login_window_canvas.create_text(191, 130, text="Employee Login Area", font=("Goudy old style", 15, "bold"), fill="#1d1d1d")
login_window_canvas.create_text(138, 173, text="Username", font=("Goudy old style", 15, "bold"), fill="grey")
login_window_canvas.create_text(138, 244, text="Password", font=("Goudy old style", 15, "bold"), fill="grey")

ent_username = Entry(login_window, font=("Goudy old style", 15), bg="white", fg="black")
ent_username.place(x=90, y=190, width=320, height=35)
ent_username.focus()

ent_password = Entry(login_window, font=("Goudy old style", 15), bg="white", fg="black", show="*")
ent_password.place(x=90, y=260, width=320, height=35)

# btn_forgot_pass = Button(login_window, text="forgot password?", font=("Goudy old style", 12), bd=0, fg="#6162FF")
# btn_forgot_pass.place(x=90, y=280)

btn_login = Button(login_window, text="Login", activebackground='#6162FF', activeforeground="white", font=("Goudy old style", 15, "bold"), bd=1, bg="#6162FF", fg="white", command=check_login_cred)
btn_login.place(x=90, y=320, width=180, height=40)
btn_login.bind("<Enter>", lambda e: btn_login.config(fg='white', bg='#8080ff'))
btn_login.bind("<Leave>", lambda e: btn_login.config(fg='white', bg='#6162FF'))

login_window.deiconify()
login_window.mainloop()
