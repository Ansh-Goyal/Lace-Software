import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as MessageBox
from sql_connect import *

class LaceGUI():

    # Fields - Attributes

    # Constructors
    def __init__(self):
        print("Building app")
        # Build my GUI
        # Capitalize Methods are Constructors
        self.main_scr = tk.Tk()
        self.main_scr.geometry("1300x800+50+25")
        self.main_scr.configure(bg='#4E4187')
        self.main_scr.title("WELCOME")

        self.wlcm_frame = tk.Frame(self.main_scr, padx = 20, pady = 20, bg = "#4E4187", relief = tk.SUNKEN)
        self.down_frame = tk.Frame(self.main_scr, padx = 20, pady = 20, bg = "black", relief = tk.SUNKEN)

        self.lab1 = tk.Label(self.wlcm_frame, text = "SHREE LACE INDUSTRIES", bg='cyan', width = 30, height = 1, borderwidth = 2, relief = tk.GROOVE, fg="black")
        self.lab2 = tk.Label(self.wlcm_frame, text = "WELCOME TO THE SOFTWARE!", bg='cyan')

        self.view_orders_button = tk.Button(self.wlcm_frame, text = "VIEW ORDERS", fg = "#4E4187", width = 10, height = 1, borderwidth = 2, relief = tk.GROOVE, command = None)
        self.insert_order_button = tk.Button(self.wlcm_frame, text = "NEW PURCHASE ORDER", fg = "red", width = 20, height = 1, borderwidth = 2, relief = tk.GROOVE,command = None)
        self.insert_item_button = tk.Button(self.wlcm_frame, text = "ITEMS", fg = "green", width = 10, height = 1, borderwidth = 2, relief = tk.GROOVE,command = self.items_screen)


        self.lab1.grid(row = 0, column = 1)
        self.lab2.grid(row = 1, column = 1)

        self.view_orders_button.grid(row = 2, column = 0, pady=10)
        self.insert_order_button.grid(row = 2, column = 1, pady=10)
        self.insert_item_button.grid(row = 2, column = 2, pady=10)

        self.wlcm_frame.pack()
        self.down_frame.pack()






        self.main_scr.mainloop()


    # Methods - Behaviours

    def items_screen(self):
        print("wlcm to items screen")
        self.down_frame.pack_forget()


        self.items_frame_1 = tk.Frame(self.main_scr, height=200, padx = 20, pady = 20, bg="#4E4187", relief = tk.SUNKEN)
        self.items_frame_2 = tk.Frame(self.main_scr, height=400, bg="#4E4187", padx = 20, pady = 20, relief = tk.SUNKEN)

        # FRAME 1-------


        self.item_code = tk.Label(self.items_frame_1, text="Item Code",font=("bold", 10))
        self.item_details = tk.Label(self.items_frame_1, text="Description",font=("bold", 10))
        self.item_size = tk.Label(self.items_frame_1, text="Size",font=("bold", 10))
        self.item_color = tk.Label(self.items_frame_1, text="Color",font=("bold", 10))
        self.item_rate = tk.Label(self.items_frame_1, text="Rate",font=("bold", 10))

        self.e_item_code = tk.Entry(self.items_frame_1)
        self.e_item_details = tk.Entry(self.items_frame_1)
        self.e_item_size = tk.Entry(self.items_frame_1)
        self.e_item_color = tk.Entry(self.items_frame_1)
        self.e_item_rate = tk.Entry(self.items_frame_1)

        self.add_item_button = tk.Button(self.items_frame_1, text="ADD ITEM", font=("italic", 10), bg="white", command= self.add_items)
        self.del_item_button = tk.Button(self.items_frame_1, text="DELETE", font=("italic", 10), bg="white", command= self.del_item)
        self.update_item_button = tk.Button(self.items_frame_1, text="UPDATE", font=("italic", 10), bg="white", command= self.update_item)
        self.get_item_button = tk.Button(self.items_frame_1, text="GET", font=("italic", 10), bg="white", command= self.get_item)
        self.clear_button = tk.Button(self.items_frame_1, text="CLEAR", font=("italic", 10), bg="white", command= self.clear_entryboxes)


        self.item_code.grid(row = 0, column = 0)
        self.item_details.grid(row = 1, column = 0)
        self.item_size.grid(row = 2, column = 0)
        self.item_color.grid(row = 3, column = 0)
        self.item_rate.grid(row = 4, column = 0)

        self.e_item_code.grid(row = 0, column = 1)
        self.e_item_details.grid(row = 1, column = 1)
        self.e_item_size.grid(row = 2, column = 1)
        self.e_item_color.grid(row = 3, column = 1)
        self.e_item_rate.grid(row = 4, column = 1)

        self.add_item_button.grid(row = 5, column = 0)
        self.del_item_button.grid(row = 5, column = 1)
        self.update_item_button.grid(row = 5, column = 2)
        self.get_item_button.grid(row = 2, column = 2)
        self.clear_button.grid(row = 4, column = 2)

        # Frame 2------
        self.lst_box = tk.Canvas(self.items_frame_2, height = 400,  width = 1000, relief= tk.GROOVE, confine = True, bd = 10)

        self.lst_box.grid(row=0,column=0) # .place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        self.v_scrollbar = tk.Scrollbar(self.items_frame_2, orient='vertical', command=self.lst_box.yview)
        self.v_scrollbar.grid(row=0,column=1) # .place(relx = 1, x =-2, y = 2, anchor = tk.NE)
        #
        #
        self.scrollable_frame = tk.Frame(self.lst_box)
        #
        self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.lst_box.configure(
            scrollregion=self.lst_box.bbox("all")
            )
        )
        #
        self.lst_box.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        #
        self.lst_box.configure(yscrollcommand = self.v_scrollbar.set)
        #
        #



        self.items_frame_1.pack()
        self.show_items()
        self.items_frame_2.pack()

    def show_items(self):


        self.con = sql_con()
        self.cursor = self.con.cursor()
        self.cursor.execute("select * from items ORDER BY Sno ASC")
        self.rows = self.cursor.fetchall()
        self.con.close()

        self.head_lst = ['Sno', 'item_code', 'DESCRIPTION', 'size_mm', 'color', 'rate']


        self.table = Table(self.scrollable_frame, self.rows, self.head_lst)


    def item_presence_check(self, cde):

        con = sql_con()
        cursor = con.cursor()
        cursor.execute("select item_code from `lace`.`items` WHERE (`item_code` = '{}');".format(cde))
        rows = cursor.fetchall()
        con.close()
        if len(rows)==1:
            return 1
        else:
            return 0

    def clear_entryboxes(self):
        self.e_item_code.delete(0, 'end')

        self.e_item_details.delete(0, 'end')

        self.e_item_size.delete(0, 'end')

        self.e_item_color.delete(0, 'end')

        self.e_item_rate.delete(0, 'end')

    def add_items(self):


        try:
            code = str(self.e_item_code.get())

            details = str(self.e_item_details.get())

            size = int(self.e_item_size.get())

            color = str(self.e_item_color.get())

            rate = float(self.e_item_rate.get())
        except:
            MessageBox.showinfo("Insert Status", "Check Entries!")




        if code=='' or details=="" or size=="" or color == '' or rate == '':
            MessageBox.showinfo("CREATE Status", "All Fields are required")
        else:
            flag = self.item_presence_check(code)
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

        self.show_items()




    def del_item(self):


        try:
            code = str(self.e_item_code.get())
        except:
            MessageBox.showinfo("Delete Status", "Check Entries!")

        if code=='':
            MessageBox.showinfo("Delete Status", "Check Item Code")
        else:
            flag = self.item_presence_check(code)
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

        self.show_items()




    def update_item(self):

        try:
            code = str(self.e_item_code.get())

            flag = self.item_presence_check(code)
            if not(flag):
                MessageBox.showinfo("UPDATE Status", "Item Code Not Present!")

                return 0

            details = str(self.e_item_details.get())

            size = int(self.e_item_size.get())

            color = str(self.e_item_color.get())

            rate = float(self.e_item_rate.get())
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

        self.show_items()


    def get_item(self):
        try:
            code = str(self.e_item_code.get())
        except:
            MessageBox.showinfo("Insert Status", "Check Entries!")

        if code == "" :
            MessageBox.showinfo("Fetch Status", "Item ID Needed")
        else:
            flag = self.item_presence_check(code)

            if flag:


                con = sql_con()
                try:

                    cursor = con.cursor()
                    cursor.execute("SELECT `DESCRIPTION`, `size_mm`, `color`, `rate` FROM `lace`.`items` where (`item_code` = '{}')".format(code))
                    row = cursor.fetchone()

                    self.e_item_details.insert(0, row[0])
                    self.e_item_size.insert(0, row[1])
                    self.e_item_color.insert(0, row[2])
                    self.e_item_rate.insert(0, row[3])
                except:
                    MessageBox.showinfo("GET Status", "Error")
                con.close()
            else:
                MessageBox.showinfo("GET Status", "Item Code Not Present!")









class Table:

    def __init__(self,root, inp_rows, inp_head_lst):


        self.total_rows = len(inp_rows)
        self.total_columns = len(inp_head_lst)



        for i in range(self.total_columns):

            if i==2 or i ==4:

                self.head_entry = tk.Entry(root, width=30, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(tk.END, inp_head_lst[i])
            elif i==1:
                self.head_entry = tk.Entry(root, width=15, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(tk.END, inp_head_lst[i])
            else:
                self.head_entry = tk.Entry(root, width=10, fg='black', font=('Arial',16,'bold'))

                self.head_entry.grid(row=0, column=i)
                self.head_entry.insert(tk.END, inp_head_lst[i])


        # code for creating table
        for i in range(self.total_rows):

            for j in range(self.total_columns):

                if j==2 or j ==4:

                    self.e = tk.Entry(root, width=30, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, inp_rows[i][j])

                elif j==1:
                    self.e = tk.Entry(root, width=15, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, inp_rows[i][j])
                else:
                    self.e = tk.Entry(root, width=10, fg='blue',
                                   font=('Arial',16,'bold'))

                    self.e.grid(row=i+1, column=j)
                    self.e.insert(tk.END, inp_rows[i][j])




a = LaceGUI()
