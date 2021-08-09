import datetime
import tkinter.messagebox as MessageBox
from sql_connect import *
from tkinter import *
from new_items import *
## INSERTING NEW ORDERS


def insert_items_po(po_id):


    global e_item_code, e_order_qntty, inserting_items_rows
    inserting_items_rows = []

    green_frame = Frame(po_scrn, height=380, width=280, bd=10, bg="green")
    green_frame.place(x=330, y=10)

    Label(green_frame, text = "ITEMS of PO: ({})".format(po_id), fg = 'black', bg = 'cyan').grid(row = 0, column = 1,  padx = 5, pady = 30)


    item_code = Label(green_frame, text="ITEM CODE: ",font=("bold", 10))
    item_code.grid(row=2, column=0, padx = 2, pady = 40)

    e_item_code = Entry(green_frame)
    e_item_code.grid(row=2, column=1, columnspan = 2, pady = 30)


    order_qntty = Label(green_frame, text="ORDER QUANTITY: ",font=("bold", 10))
    order_qntty.grid(row=3, column=0, padx = 2, pady = 40)

    e_order_qntty = Entry(green_frame)
    e_order_qntty.grid(row=3, column=1, columnspan = 2, padx = 2, pady = 30)

    row_of_items=[]

    insert_item = Button(green_frame, text="INSERT INTO PO", font=("italic", 10), bg="white", command=po_specific_items_collection)
    insert_item.grid(row=5, column=0, padx = 3, pady = 30)

    finalise_PO = Button(green_frame, text="FINALISE PO", font=("italic", 10), bg="white", command=None)
    finalise_PO.grid(row=5, column=1, padx = 3, pady = 30)

    show_inserting_items(inserting_items_rows)

# def finalising_po()
#     ###COMPLETE THE FUNCTION


def po_specific_items_collection():


    id = str(e_item_code.get())

    qntty = int(e_order_qntty.get())

    if not(item_presence_check(id)):
        MessageBox.showinfo("Insert Status", "ITEM NOT PRESENT IN ITEMS LIST!!   PLEASE ADD ITEM INTO INVENTORY FIRST!!")
        return 0
    else:
        row = [id, qntty]
        inserting_items_rows.append(row)
        show_inserting_items(inserting_items_rows)

    # except:
    #     MessageBox.showinfo("Insert Status", "Check Entries!")
    #     return 0


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


def po_insert_scrn():

    global po_scrn, e_po_num, e_po_date, e_company_name, scrollable_frame2


    po_scrn = Tk()
    po_scrn.geometry("600x700+100+100")
    po_scrn.title("NEW PURCHASE ORDER SCREEN")


    # FRAME 1
    # INSERTING PO DETAILS

    po_insert_frame = Frame(po_scrn, height=380, width=280, bd=10, bg="red")
    po_insert_frame.place(x=10, y=10)

    Label(po_insert_frame, text = "Enter PO Details: ", fg = 'black', bg = 'cyan').grid(row = 0, column = 1,  padx = 5, pady = 30)

    po_num = Label(po_insert_frame, text="PO Number: ",font=("bold", 10))
    po_num.grid(row=2, column=0, padx = 2, pady = 20)

    e_po_num = Entry(po_insert_frame)
    e_po_num.grid(row=2, column=1, columnspan = 2, pady = 20)


    company_name = Label(po_insert_frame, text="Company Name: ",font=("bold", 10))
    company_name.grid(row=3, column=0, padx = 2, pady = 20)

    e_company_name = Entry(po_insert_frame)
    e_company_name.grid(row=3, column=1, columnspan = 2, padx = 2, pady = 20)


    po_date = Label(po_insert_frame, text="Order Date: ",font=("bold", 10))
    po_date.grid(row=4, column=0, padx = 2, pady = 20)

    e_po_date = Entry(po_insert_frame)
    e_po_date.grid(row=4, column=1, columnspan = 2, padx = 2, pady = 20)

    crt_po = Button(po_insert_frame, text="CREATE PO", font=("italic", 10), bg="white", command=add_po)
    crt_po.grid(row=5, column=1, padx = 5, pady = 26)




    yellow_frame = Frame(po_scrn, height=280, width=580, bd=10, bg="yellow")
    yellow_frame.place(x=10, y=410)


    lst_box = Canvas(yellow_frame, height = 250,  width = 500, relief= GROOVE, confine = True, bd = 10)

    lst_box.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    v_scrollbar = Scrollbar(yellow_frame, orient='vertical', command=lst_box.yview)
    v_scrollbar.place(relx = 1, x =-2, y = 2, anchor = NE)


    scrollable_frame2 = Frame(lst_box)

    scrollable_frame2.bind(
    "<Configure>",
    lambda e: lst_box.configure(
        scrollregion=lst_box.bbox("all")
        )
    )

    lst_box.create_window((0, 0), window=scrollable_frame2, anchor="nw")

    lst_box.configure(yscrollcommand = v_scrollbar.set)

    flag=1
    if flag == 1:

        show_companies()

    else:

        # show_inserting_items()
        print("Line 95")


    po_scrn.mainloop()


def add_po():

    flag = 0

    try:
        p_order_id = int(e_po_num.get())

        company = str(e_company_name.get())

        try:
            dated = e_po_date.get()
            dated = dated.split()

            x = datetime.datetime(int(dated[2]), int(dated[1]), int(dated[0]))
            dat = "{}-{}-{}".format(x.strftime("%Y"), x.strftime("%m"), x.strftime("%d"))
        except:
            MessageBox.showinfo("Insert Status", "DATE FORMAT: (DD MM YYYY)")
            return 0

    except:
        MessageBox.showinfo("Insert Status", "Check Entries!")
        return 0



    if p_order_id=='' or company=='' or dat=='':
        MessageBox.showinfo("CREATE Status", "All Fields are required")
    else:

        flag = company_presence_check(company)
        if not(flag):
            MessageBox.showinfo("Insert Status", "Company Not Present in Companies List! Add the Company first!")
            return 0
        else:

            flag = id_presence_check(p_order_id)

            if flag:
                MessageBox.showinfo("Insert Status", "Purchase Order Already Present!")

            else:

                insert_items_po(p_order_id)

        #         try:
        #
        #             con = sql_con()
        #             cursor = con.cursor()
        #
        #             cursor.execute("INSERT INTO `lace`.`items` (`item_code`, `DESCRIPTION`, `size_mm`, `color`, `rate`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(code, details, size, color, rate))
        #             cursor.execute("commit")
        #
        #
        #
        #
        #             MessageBox.showinfo("Insert Status", "Inserted Successfully")
        #         except:
        #             MessageBox.showinfo("Insert Status", "Error!")
        #     con.close()
        # show_items()
                print("Line 180")

def company_presence_check(cmpany):
    con = sql_con()
    cursor = con.cursor()
    cursor.execute("select Company_name from `lace`.`companies` WHERE (`Company_name` = '{}');".format(cmpany))
    rows = cursor.fetchall()
    con.close()
    if len(rows)==1:
        return 1
    else:
        return 0

def id_presence_check(id):
    con = sql_con()
    cursor = con.cursor()
    cursor.execute("select PO_no from `lace`.`order_master` WHERE (`PO_no` = '{}');".format(id))
    rows = cursor.fetchall()
    con.close()
    if len(rows)==1:
        return 1
    else:
        return 0

def show_companies():


    con = sql_con()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM lace.companies ORDER BY Sno ASC;")
    rows = cursor.fetchall()
    con.close()

    head_lst = ['Sno', 'Company_name', 'address', 'GSTIN', 'PAN NO']




    table = Table(scrollable_frame2, rows, head_lst)

def show_inserting_items(rows):



    #
    #
    #CORRECTIONS NEEDED I GRAPHICS
    #
    #
    head_lst = ['item_code' , 'order_quantity']

    table = Table(scrollable_frame2, rows, head_lst)
