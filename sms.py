""" Student Management System developed by 'Nishant Patil'. Tech-Stack: Python, SQLite3, Data Science """

#*******************  # Required Libraries # ***************#

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from bs4 import *
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import requests 
from sqlite3 import *
from rnv import *
from Connection_DB import *
from datetime import *

#******************* # Root Window # *******************  # 

root =Tk()
root.title("Student Management System")
root.geometry("600x600+200+20")

# *******************  # app font # *******************  # 

f="Times new roman",18,"bold"

# *******************  # app font # *******************  # 
con=None
try:
	con=connect("sms.db")
	cursor=con.cursor()
except Exception as e:
	print('Error : ' +str(e))

# *******************  # date # *******************  # 

d=datetime.now()
day=str(d.day)
mon=str(d.month)
yr=str(d.year)
date=str(day)+"/"+str(mon)+"/"+str(yr)


# *******************  # heading # *******************  # 

lbl_heading=Label(root,text="Student Management System",font=f)
lbl_heading.pack()
lbl_date=Label(root,text=date,font=f)
lbl_date.place(x=480,y=5)

# *******************  # add button function # *******************  # 

def add_btn_fun():
	add_window.deiconify()
	root.withdraw()
	

# *******************  # view button function # *******************  #
 
def view_btn_fun():
	view_window.deiconify()
	root.withdraw()
	vw_st.delete(1.0,END)
	vw_st.insert(INSERT,"Rno\t  Name\t\t  Marks\n")
	info=conn.view()
	vw_st.insert(INSERT,info)	

# *******************  # update button function # *******************  # 

def update_btn_fun():
	update_window.deiconify()
	root.withdraw()
	
# *******************  # delete button function # *******************  # 

def del_btn_fun():
	del_window.deiconify()
	root.withdraw()	

# *******************  #  Navigation functions # *******************  # 

def f1():
	add_window.withdraw()
	root.deiconify()
	ent_rn.focus()
def f2():
	view_window.withdraw()
	root.deiconify()
def f3():
	update_window.withdraw()
	root.deiconify()
	updt_ent_rn.focus()
def f4():
	del_window.withdraw()
	root.deiconify()
	del_ent_rn.focus()	
	
# *******************  # add Window # *******************  # 

add_window=Toplevel(root)
add_window.title("Add Student")
add_window.geometry("600x600+200+10")

lbl_rn=Label(add_window,text="Enter roll number : ",font=f)
lbl_rn.pack(pady=5)
ent_rn=Entry(add_window,font=f,bd=3)
ent_rn.pack(pady=5)

lbl_name=Label(add_window,text="Enter Student Name : ",font=f)
lbl_name.pack(pady=5)
ent_name=Entry(add_window,font=f,bd=3)
ent_name.pack(pady=5)

lbl_marks=Label(add_window,text="Enter Marks : ",font=f)
lbl_marks.pack(pady=5)
ent_mark=Entry(add_window,font=f,bd=3)
ent_mark.pack(pady=5)

# *******************  # Save info function # *******************  # 

def save_info():
	try:
		ent_rn.focus()
		rn=ent_rn.get()
		#print(ent_rn.get())
		r=rn_validator(rn)
		if rn_validator(rn) is True:	
			pass	
		else:
			showerror("Error",r)
			ent_rn.delete(0,END)
			ent_rn.focus()
			return 

		name=ent_name.get()
		nm=name_validator(name)
		if name_validator(name) is True:	
			pass	
		else:
			showerror("Error",nm)
			ent_name.delete(0,END)
			ent_name.focus()
			return
			
		marks=ent_mark.get()
		m=marks_validator(marks)
		if marks_validator(marks) is True:
			pass
		else:
			showerror("Error",m)
			ent_mark.delete(0,END)
			ent_mark.focus()
			return 
		
		i=conn.insert(int(rn),name,int(marks))
		if i=="OK":
			showinfo("Success",rn+","+name+","+marks+" Record Added")
		else:
			showerror("Error","Issue : "+i)
			ent_rn.delete(0,END)
			ent_rn.focus()
		ent_name.delete(0,END)
		ent_rn.delete(0,END)
		ent_mark.delete(0,END)
		ent_rn.focus()
	except Exception as e:
		showerror("Error",str(e))
	

btn_save=Button(add_window,text="Save",bd=3,font=f,command=save_info)
btn_save.pack(pady=5)
btn_back=Button(add_window,text="<Back",bd=3,font=f,command=f1)
btn_back.pack(pady=5)

add_window.withdraw()

# *******************  # view Window # *******************  # 

view_window=Toplevel(root)
view_window.title("view Student")
view_window.geometry("600x600+200+10")


vw_st=ScrolledText(view_window,width=40,height=16,font=f)
vw_st.pack(pady=10)


btn_back=Button(view_window,text="<Back",bd=3,font=f,command=f2)
btn_back.pack(pady=5)

view_window.withdraw()


#  *******************  # update info function # ******************* #

def update_info():
	try:
		updt_ent_rn.focus()
		rn=updt_ent_rn.get()
		r=rn_validator(rn)
		if rn_validator(rn) is True:	
			pass	
		else:
			showerror("Error",r)
			updt_ent_rn.delete(0,END)
			updt_ent_rn.focus()
			return 


		name=updt_ent_name.get()

		nm=name_validator(name)
		if name_validator(name) is True:	
			pass	
		else:
			showerror("Error",nm)
			updt_ent_name.delete(0,END)
			updt_ent_name.focus()
			return
			
		marks=updt_ent_mark.get()
		m=marks_validator(marks)
		if marks_validator(marks) is True:
			pass
		else:
			showerror("Error",m)
			updt_ent_mark.delete(0,END)
			updt_ent_mark.focus()
			return 

		u=conn.update(int(rn),name,int(marks))
		if u=="OK":
			showinfo("Success",rn+","+name+","+marks+" Record Updated")
		else:
			showerror("Error","Issue : "+u)
		updt_ent_name.delete(0,END)
		updt_ent_rn.delete(0,END)
		updt_ent_mark.delete(0,END)
		updt_ent_rn.focus()
	except Exception as e:
		showerror("Error",str(e))

# *******************  # update Window # *******************  # 

update_window=Toplevel(root)
update_window.title("update Student")
update_window.geometry("600x600+200+10")

lbl_rn=Label(update_window,text="Enter roll number : ",font=f)
lbl_rn.pack(pady=5)
updt_ent_rn=Entry(update_window,font=f,bd=3)
updt_ent_rn.pack(pady=5)

lbl_name=Label(update_window,text="Enter Student Name : ",font=f)
lbl_name.pack(pady=5)
updt_ent_name=Entry(update_window,font=f,bd=3)
updt_ent_name.pack(pady=5)

lbl_marks=Label(update_window,text="Enter Marks : ",font=f)
lbl_marks.pack(pady=5)
updt_ent_mark=Entry(update_window,font=f,bd=3)
updt_ent_mark.pack(pady=5)

btn_save=Button(update_window,text="Update Record",bd=3,font=f,command=update_info)
btn_save.pack(pady=5)
btn_back=Button(update_window,text="<Back",bd=3,font=f,command=f3)
btn_back.pack(pady=5)

update_window.withdraw()

#  *******************  # delete info function # ******************* #

def del_info():
	del_ent_rn.focus()
	rn=del_ent_rn.get()
	if not rn.isdigit() :
		showerror("Roll number issue","Invalid Roll number ")
		del_ent_rn.delete(0,END)
		del_ent_rn.focus()
		return
	d=conn.delete(int(rn))
	if d=="OK":
		showinfo("Success",rn+" Record Deleted")
	else:
		showerror("Error","Issue : "+d)
		

	del_ent_rn.delete(0,END)
	del_ent_rn.focus()
# *******************  # delete Window # *******************  # 

del_window=Toplevel(root)
del_window.title("Delete Student")
del_window.geometry("600x600+200+10")

lbl_rn=Label(del_window,text="Enter roll number : ",font=f)
lbl_rn.pack(pady=5)
del_ent_rn=Entry(del_window,font=f,bd=3)
del_ent_rn.pack(pady=5)

btn_save=Button(del_window,text="Delete Record",bd=3,font=f,command=del_info)
btn_save.pack(pady=5)
btn_back=Button(del_window,text="<Back",bd=3,font=f,command=f4)
btn_back.pack(pady=5)

del_window.withdraw()

# *******************  # chart button function # *******************  # 

def chrt_btn_fun():
	
	con=None
	rn,name,marks=[],[],[]
	try:
		con=connect("sms.db")
		print("Connected")

		cursor=con.cursor()
		sql=" select * from student_info;"
		cursor.execute(sql)
	
		data = cursor.fetchall()
		print(data)
		for info in data:
			rn.append(info[0]),name.append(info[1])
			marks.append(info[2])
		print(rn,name,marks)
		
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
	
	plt.bar(rn,marks,label="marks",color=['orange','blue','green','yellow','red'],align = 'center')
	plt.xticks(rn,name,rotation=30,ha="right")
	plt.xlabel("names")
	plt.ylabel("marks")
	plt.title("Batch Information! ")
	plt.legend(shadow=True)
	plt.grid()
	plt.show()
	
	
#  *******************  # Buttons # *******************  # 

add_btn=Button(root,text="     ADD     ",bd=4,font=f,command=add_btn_fun)
add_btn.pack(pady=10)

view_btn=Button(root,text="    VIEW    ",bd=4,font=f,command=view_btn_fun)
view_btn.pack(pady=10)

updt_btn=Button(root,text=" UPDATE ",bd=4,font=f,command=update_btn_fun)
updt_btn.pack(pady=10)

del_btn=Button(root,text=" DELETE ",bd=4,font=f,command=del_btn_fun)
del_btn.pack(pady=10)

chrt_btn=Button(root,text="    Charts  ",bd=4,font=f,command=chrt_btn_fun)
chrt_btn.pack(pady=10)

#  *******************  # location extractor # *******************  # 

def location():
	try:
		wa="https://ipinfo.io"
		res=requests.get(wa)
		print(res,"\n")
		print(res.status_code,"\n")
		data=res.json()
		print(data,"\n")
		city_name=data["city"]
		return city_name
	except Exception as e:
		print("issue : ",e)

#  *******************  # temprature extractor # *******************  # 

def temp():

	try:
		a1="http://api.openweathermap.org/data/2.5/weather/?units=metric"
		a2="&q="+location()
		a3="&appid="+"c6e315d09197cec231495138183954bd"

		wa=a1+a2+a3
		res=requests.get(wa)
		print(res)
		data=res.json()
		print(data)
	
		des=data['weather'][0]['description']
		temp=data['main']['temp']

		print("Description : ",des,'\n','Temp : ',temp)
		return temp
	except Exception as e:
		print("issue : ",e)

	

loc_temp=Label(root,text="Location : "+location()+"      "+"Temp : "+str(temp())+'\N{DEGREE SIGN}C',font=f,bd=4)
loc_temp.pack(pady=10)


#  *******************  # QOTD extractor # *******************  # 

def qotd():
	
	try:
		wa="http://www.brainyquote.com/quote_of_the_day"
		res=requests.get(wa)
		print(res)
		data=BeautifulSoup(res.text,"html.parser")
		qotd=data.find("img",{"class":"p-qotd"})
		return qotd['alt']
		
	except Exception as e:
		print('Error',e)


QOTD=Label(root,text="QOTD : "+"\""+str(qotd())+"\"",font=f,bd=4,wrap=500) 
QOTD.pack()


#  *******************  # Exit # *******************  # 

root.mainloop()

 

