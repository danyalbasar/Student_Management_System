from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt
from sqlite3 import *
import requests
import bs4

def f1():
	add_window.deiconify()
	main_window.withdraw()
	
def f2():
	main_window.deiconify()
	add_window.withdraw()
	
def view():
	view_window.deiconify()
	main_window.withdraw()
	
	vw_st_data.delete(1.0, END)
	info = ""
	con = None
	try:
		con = connect("student_data.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		
		if len(data) != 0:
			for d in data:
				info = info + "Roll No:" + str(d[0]) + " |" + " Name:" + str(d[1]) + " |" + " Marks:" + str(d[2]) + "\n\n"
				
			vw_st_data.insert(INSERT, info)
		else:
			showerror("Error", "No data")
	except Exception as e:
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()
			
def f4():
	main_window.deiconify()
	view_window.withdraw()
	
def f5():
	update_window.deiconify()
	main_window.withdraw()
	
def f6():
	main_window.deiconify()
	update_window.withdraw()
	
def f7():
	delete_window.deiconify()
	main_window.withdraw()
	
def f8():
	main_window.deiconify()
	delete_window.withdraw()
	
def charts():
	try:
		con = connect("student_data.db")
		cursor = con.cursor()
		sql = "select name, marks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		
		if len(data) != 0:
			name = []
			marks = []
			
			for d in data:
				name.append(d[0])
				marks.append(d[1])
				
			plt.bar(name, marks, width=0.7, color=["red", "green", "blue"])
			plt.ylim(0, 105)
			plt.xlabel("Students")
			plt.ylabel("Marks")
			plt.title("Batch Information")
			plt.show()
		else:
			showerror("Error", "No data")
	except Exception as e:
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()
			
def add():
	con = None
	try:
		con = connect("student_data.db")
		cursor = con.cursor()
		sql ="insert into student values('%s', '%s', '%s')"
		rno = aw_ent_rno.get()
		name = aw_ent_name.get()
		marks = aw_ent_marks.get()
		
		if (not rno.isdigit()) or (len(rno) == 0) or (int (rno) <= 0):
			showerror("Roll No Issue", "Invalid roll no") 		
			aw_ent_rno.delete(0, END)
			aw_ent_rno.focus()
			return
		if (not name.isalpha()) or (len(name) == 0) or (len(name) < 2):
			showerror("Name Issue", "Invalid name") 
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
		if (not marks.isdigit()) or (len(marks) == 0) or (int (marks) < 0) or (int (marks) > 100): 
			showerror("Marks Issue", "Invalid marks")
			aw_ent_marks.delete(0, END)
			aw_ent_marks.focus()
			return
		
		cursor.execute(sql % (rno, name, marks))
		con.commit()
		showinfo("Success","record created")
		
		aw_ent_rno.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_marks.delete(0, END)
		aw_ent_rno.focus()
	except Exception as e:
		con.rollback()
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()
			
def update():
	con = None
	try:
		con = connect("student_data.db")
		cursor = con.cursor()
		sql ="update student set name='%s', marks='%s' where rno='%s'"
		name = uw_ent_name.get()
		marks = uw_ent_marks.get()
		rno = uw_ent_rno.get()
		
		if (not rno.isdigit()) or (len(rno) == 0) or (int (rno) <= 0):
			showerror("Roll No Issue", "Invalid roll no") 		
			uw_ent_rno.delete(0, END)
			uw_ent_rno.focus()
			return
		if (not name.isalpha()) or (len(name) == 0) or (len(name) < 2):
			showerror("Name Issue", "Invalid name") 
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return
		if (not marks.isdigit()) or (len(marks) == 0) or (int (marks) < 0) or (int (marks) > 100):
			showerror("Marks Issue", "Invalid marks")
			uw_ent_marks.delete(0, END)
			uw_ent_marks.focus()
			return
		
		cursor.execute(sql % (name, marks, rno))
		
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","record updated")
		else:
			showerror("Error", "record does not exists")
			
		uw_ent_rno.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_marks.delete(0, END)
		uw_ent_rno.focus()
	except Exception as e:
		con.rollback()
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()

def delete():
	con = None
	try:
		con = connect("student_data.db")
		cursor = con.cursor()
		sql ="delete from student where rno = '%s'"
		rno = dw_ent_rno.get()
		
		if (not rno.isdigit()) or (len(rno) == 0) or (int (rno) <= 0):
			showerror("Roll No Issue", "Invalid roll no") 		
			dw_ent_rno.delete(0, END)
			dw_ent_rno.focus()
			return
		
		cursor.execute(sql % (rno))
		
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","record deleted")
		else:
			showerror("Error","record not found")
			
		dw_ent_rno.delete(0, END)
		dw_ent_rno.focus()
	except Exception as e:
		con.rollback()
		showerror("Error", str(e))
	finally:
		if con is not None:
			con.close()

main_window = Tk()
main_window.title("S. M. S")
main_window.geometry("500x530+650+225")
main_window.configure(bg="DarkSeaGreen1")

try:
	wa = "https://ipinfo.io/"
	res = requests.get(wa)
	data = res.json()

	location_name = "Location: " + data['city'] + "," + " " + data['country']
except Exception as e:
	print("Issue", e)
	location_name = "Location: Error\t "
	
try:
	api_key = "6aec4029e4a643f15b82009ac24ae555"
	base_url = "http://api.openweathermap.org/data/2.5/weather?q="
	city_name = "Mumbai"

	complete_url = base_url + city_name + "&appid=" + api_key + "&units=metric"

	res = requests.get(complete_url)
	data = res.json()

	tmp = " Temp: " + str(data['main']['temp']) + " °C"
except Exception as e:
	print("Issue", e)
	tmp = "       Temp: Error"
	
try:
	wa = "https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(wa)
	
	data = bs4.BeautifulSoup(res.text, "html.parser")

	info = data.find("img", {"class":"p-qotd"})

	quote = "QOTD: " + info["alt"]
except Exception as e:
	print("Issue", e)
	quote = "QOTD: Error "

fa = ("Arial", 15)

mw_frm_loc_tmp = Frame(main_window, bd=2, relief=SOLID, bg="DarkSeaGreen1")
mw_frm_loc_tmp.place(x=11.5, y=370, width=475, height=50)
mw_lbl_loc = Label(mw_frm_loc_tmp, text=location_name + "                    " + tmp, font=fa, bg="DarkSeaGreen1", pady=7, padx=5)
mw_lbl_loc.grid(pady=3)
mw_frm_qotd = Frame(main_window, bd=2, relief=SOLID, bg="DarkSeaGreen1")
mw_frm_qotd.place(x=11.5, y=430, width=475, height=90)
mw_lbl_qotd = Label(mw_frm_qotd, text=quote, font=fa, bg="DarkSeaGreen1", wraplength=475, pady=7, padx=5)
mw_lbl_qotd.grid(pady=2)

f = ("Arial", 18, "bold")

mw_btn_add = Button(main_window, text="Add", bd=3.5, font=f, width=10, command=f1)
mw_btn_view = Button(main_window, text="View", bd=3.5, font=f, width=10, command=view)
mw_btn_update = Button(main_window, text="Update", bd=3.5, font=f, width=10, command=f5)
mw_btn_delete = Button(main_window, text="Delete", bd=3.5, font=f, width=10, command=f7)
mw_btn_charts = Button(main_window, text="Charts", bd=3.5, font=f, width=10, command=charts)
mw_btn_add.place(x=158.5, y=20)
mw_btn_view.place(x=158.5, y=90)
mw_btn_update.place(x=158.5, y=160)
mw_btn_delete.place(x=158.5, y=230)
mw_btn_charts.place(x=158.5, y=300)

add_window = Toplevel(main_window, bg="lightblue1")
add_window.title("Add Stu.")
add_window.geometry("500x530+650+225")

aw_lbl_rno = Label(add_window, text="Enter Roll No:", font=f, bg="lightblue1")
aw_ent_rno = Entry(add_window, bd=5, width=29, font=f)
aw_lbl_name = Label(add_window, text="Enter Name:", font=f, bg="lightblue1")
aw_ent_name = Entry(add_window, bd=5, width=29, font=f)
aw_lbl_marks = Label(add_window, text="Enter Marks:", font=f, bg="lightblue1")
aw_ent_marks = Entry(add_window, width=29, bd=5, font=f)
aw_btn_save = Button(add_window, text=" Save ", width=10, bd=3.5, font=f, command=add)
aw_btn_back = Button(add_window, text="Back", width=10, bd=3.5, font=f, command=f2)
aw_lbl_rno.pack(pady=8)
aw_ent_rno.pack(pady=8)
aw_lbl_name.pack(pady=8)
aw_ent_name.pack(pady=8)
aw_lbl_marks.pack(pady=8)
aw_ent_marks.pack(pady=8)
aw_btn_save.pack(pady=12)
aw_btn_back.pack(pady=3)

add_window.withdraw()

view_window = Toplevel(main_window, bg="lemon chiffon")
view_window.title("View Stu.")
view_window.geometry("500x530+650+225")

vw_st_data = ScrolledText(view_window, width=33, height=12, font=f, bg="white")
vw_btn_back = Button(view_window, text="Back", width=10, bd=3.5, font=f, command=f4)
vw_st_data.pack(pady=20)
vw_btn_back.pack(pady=8)

view_window.withdraw()

update_window = Toplevel(main_window, bg="misty rose")
update_window.title("Update Stu.")
update_window.geometry("500x530+650+225")

uw_lbl_rno = Label(update_window, text="Enter Roll No:", font=f, bg="misty rose")
uw_ent_rno = Entry(update_window, width=29, bd=5, font=f)
uw_lbl_name = Label(update_window, text="Enter Name:", font=f, bg="misty rose")
uw_ent_name = Entry(update_window, width=29, bd=5, font=f)
uw_lbl_marks = Label(update_window, text="Enter Marks:", font=f, bg="misty rose")
uw_ent_marks = Entry(update_window, width=29, bd=5, font=f)
uw_btn_update = Button(update_window, text="Update", width=10, bd=3.5, font=f, command=update)
uw_btn_back = Button(update_window, text="Back", width=10, bd=3.5, font=f, command=f6)
uw_lbl_rno.pack(pady=8)
uw_ent_rno.pack(pady=8) 
uw_lbl_name.pack(pady=8) 
uw_ent_name.pack(pady=8)
uw_lbl_marks.pack(pady=8) 
uw_ent_marks.pack(pady=8)
uw_btn_update.pack(pady=12)
uw_btn_back.pack(pady=3)

update_window.withdraw()

delete_window = Toplevel(main_window, bg="lightblue1")
delete_window.title("Delete Stu.")
delete_window.geometry("500x530+650+225")

dw_lbl_rno = Label(delete_window, text="Enter Roll No:", font=f, bg="lightblue1")
dw_ent_rno = Entry(delete_window, width=29, bd=5, font=f)
dw_btn_delete = Button(delete_window, text="Delete", width=10, bd=3.5, font=f, command=delete)
dw_btn_back = Button(delete_window, text="Back", width=10, bd=3.5, font=f, command=f8)
dw_lbl_rno.pack(pady=8)
dw_ent_rno.pack(pady=8) 
dw_btn_delete.pack(pady=12)
dw_btn_back.pack(pady=3)

delete_window.withdraw()

main_window.mainloop()
