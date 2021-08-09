from tkinter import *
import tkinter.messagebox as MessageBox
from sql_connect import *
# from insert_po import *


class Table:

    def __init__(self,root, inp_rows, inp_head_lst):


        self.total_rows = len(inp_rows)
        self.total_columns = len(inp_head_lst)



        for i in range(self.total_columns):

            if i==2 or i ==4:

                self.head_entry = Entry(root, width=30, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(END, inp_head_lst[i])
            elif i==1:
                self.head_entry = Entry(root, width=15, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(END, inp_head_lst[i])
            else:
                self.head_entry = Entry(root, width=10, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(END, inp_head_lst[i])


        # code for creating table
        for i in range(self.total_rows):

            for j in range(self.total_columns):

                if j==2 or j ==4:

                    self.e = Entry(root, width=30, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(END, inp_rows[i][j])

                elif j==1:
                    self.e = Entry(root, width=15, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(END, inp_rows[i][j])
                else:
                    self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(END, inp_rows[i][j])







def show_items():


    con = sql_con()
    cursor = con.cursor()
    cursor.execute("select * from items ORDER BY Sno ASC")
    rows = cursor.fetchall()
    con.close()

    head_lst = ['Sno', 'item_code', 'DESCRIPTION', 'size_mm', 'color', 'rate']


    table = Table(scrollable_frame, rows, head_lst)





def all_items_scrn():

    global items_scrn, e_item_code, e_item_details, e_item_size, e_item_color, e_item_rate, scrollable_frame



    items_scrn = Tk()
    items_scrn.geometry("1300x800+20+20")
    items_scrn.title("ITEMS SCREEN!")

    master_frame = Frame(items_scrn, height=210, width=400, bd=10, bg="blue")
    master_frame.place(x=0, y=0)

    item_code = Label(master_frame, text="Item Code",font=("bold", 10))
    item_code.place(x=20, y=30)

    e_item_code = Entry(master_frame)
    e_item_code.place(x=150, y=30)

    item_details = Label(master_frame, text="Description",font=("bold", 10))
    item_details.place(x=20, y=60)

    e_item_details = Entry(master_frame)
    e_item_details.place(x=150, y=60)

    item_size = Label(master_frame, text="Size",font=("bold", 10))
    item_size.place(x=20, y=90)

    e_item_size = Entry(master_frame)
    e_item_size.place(x=150, y=90)

    item_color = Label(master_frame, text="Color",font=("bold", 10))
    item_color.place(x=20, y=120)

    e_item_color = Entry(master_frame)
    e_item_color.place(x=150, y=120)

    item_rate = Label(master_frame, text="Rate",font=("bold", 10))
    item_rate.place(x=20, y=150)

    e_item_rate = Entry(master_frame)
    e_item_rate.place(x=150, y=150)


    add_item_button = Button(master_frame, text="ADD ITEM", font=("italic", 10), bg="white", command=add_items)
    add_item_button.place(x=20, y=180)

    del_item_button = Button(master_frame, text="DELETE", font=("italic", 10), bg="white", command=del_item)
    del_item_button.place(x=130, y=180)

    update_item_button = Button(master_frame, text="UPDATE", font=("italic", 10), bg="white", command=update_item)
    update_item_button.place(x=250, y=180)

    get_item_button = Button(master_frame, text="GET", font=("italic", 10), bg="white", command=get_item)
    get_item_button.place(x=320, y=180)

    clear_button = Button(master_frame, text="CLEAR", font=("italic", 10), bg="white", command=clear_entryboxes)
    clear_button.place(x=350, y=180)
    #create Frame and scrollbar listbox

    lst_box_frame = Frame(items_scrn, height=500, width=1200, bd=10, bg="green")
    lst_box_frame.place(x=50, y=230)


    lst_box = Canvas(lst_box_frame, height = 400,  width = 1000, relief= GROOVE, confine = True, bd = 10)

    lst_box.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    v_scrollbar = Scrollbar(lst_box_frame, orient='vertical', command=lst_box.yview)
    v_scrollbar.place(relx = 1, x =-2, y = 2, anchor = NE)


    scrollable_frame = Frame(lst_box)

    scrollable_frame.bind(
    "<Configure>",
    lambda e: lst_box.configure(
        scrollregion=lst_box.bbox("all")
        )
    )

    lst_box.create_window((0, 0), window=scrollable_frame, anchor="nw")

    lst_box.configure(yscrollcommand = v_scrollbar.set)



    show_items()


def item_presence_check(cde):
    con = sql_con()
    cursor = con.cursor()
    cursor.execute("select item_code from `lace`.`items` WHERE (`item_code` = '{}');".format(cde))
    rows = cursor.fetchall()
    con.close()
    if len(rows)==1:
        return 1
    else:
        return 0

def clear_entryboxes():
    e_item_code.delete(0, 'end')

    e_item_details.delete(0, 'end')

    e_item_size.delete(0, 'end')

    e_item_color.delete(0, 'end')

    e_item_rate.delete(0, 'end')

def add_items():


    try:
        code = str(e_item_code.get())

        details = str(e_item_details.get())

        size = int(e_item_size.get())

        color = str(e_item_color.get())

        rate = float(e_item_rate.get())
    except:
        MessageBox.showinfo("Insert Status", "Check Entries!")




    if code=='' or details=="" or size=="" or color == '' or rate == '':
        MessageBox.showinfo("CREATE Status", "All Fields are required")
    else:
        flag = item_presence_check(code)
        if flag:

            MessageBox.showinfo("Insert Status", "Item Code Already Present!")
        else:
            try:

                con = sql_con()
                cursor = con.cursor()

                cursor.execute("INSERT INTO `lace`.`items` (`item_code`, `DESCRIPTION`, `size_mm`, `color`, `rate`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(code, details, size, color, rate))
                cursor.execute("commit")




                MessageBox.showinfo("Insert Status", "Inserted Successfully")
            except:
                MessageBox.showinfo("Insert Status", "Error!")
        con.close()
    show_items()




def del_item():


    try:
        code = str(e_item_code.get())
    except:
        MessageBox.showinfo("Delete Status", "Check Entries!")

    if code=='':
        MessageBox.showinfo("Delete Status", "Check Item Code")
    else:
        flag = item_presence_check(code)
        if flag:
            con = sql_con()
            try:

                cursor = con.cursor()
                cursor.execute("DELETE FROM `lace`.`items` WHERE (`item_code` = '{}');".format(code))
                cursor.execute("commit")


                MessageBox.showinfo("Delete Status", "Deleted Successful")



            except:

                MessageBox.showinfo("Delete Status", "Error")
            con.close()
        else:
            MessageBox.showinfo("Delete Status", "Item Code Not Present!")

    show_items()




def update_item():

    try:
        code = str(e_item_code.get())

        flag = item_presence_check(code)
        if not(flag):
            MessageBox.showinfo("UPDATE Status", "Item Code Not Present!")

            return 0

        details = str(e_item_details.get())

        size = int(e_item_size.get())

        color = str(e_item_color.get())

        rate = float(e_item_rate.get())
    except:
        MessageBox.showinfo("UPDATE Status", "Check Entries!")


    if code == "" or details == "" or size == "" or color == "" or rate == "":
        MessageBox.showinfo("UPDATE Status", "All Fields are required")


    else:
        con = sql_con()
        try:

            cursor = con.cursor()
            cursor.execute("UPDATE `lace`.`items` SET `DESCRIPTION` = '{}', `size_mm` = '{}', `color` = '{}',  `rate` = '{}' WHERE (`item_code` = '{}');".format(details, size, color, rate, code))
            cursor.execute("commit")


            MessageBox.showinfo("UPDATE Status", "Updated Successfully")

        except:


            MessageBox.showinfo("UPDATE Status", "Error")
        con.close()

    show_items()


def get_item():
    try:
        code = str(e_item_code.get())
    except:
        MessageBox.showinfo("Insert Status", "Check Entries!")

    if code == "" :
        MessageBox.showinfo("Fetch Status", "Item ID Needed")
    else:
        flag = item_presence_check(code)

        if flag:


            con = sql_con()
            try:

                cursor = con.cursor()
                cursor.execute("SELECT `DESCRIPTION`, `size_mm`, `color`, `rate` FROM `lace`.`items` where (`item_code` = '{}')".format(code))
                row = cursor.fetchone()

                e_item_details.insert(0, row[0])
                e_item_size.insert(0, row[1])
                e_item_color.insert(0, row[2])
                e_item_rate.insert(0, row[3])
            except:
                MessageBox.showinfo("GET Status", "Error")
            con.close()
        else:
            MessageBox.showinfo("GET Status", "Item Code Not Present!")






    items_scrn.mainloop()
