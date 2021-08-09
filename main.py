from tkinter import *
from insert_po import *
from new_items import *
from show_frame import *


def master_scr():
    global main_scr
    main_scr = Tk()
    main_scr.geometry("1300x800+50+25")
    main_scr.configure(bg='white')
    main_scr.title("WELCOME")


    wlcm_scr()
    main_scr.mainloop()


def wlcm_scr():

    wlcm_frame = Frame(main_scr, height=790, width=1290, bg="grey").grid(row = 0, column = 0, padx = 5, pady=5, rowspan=4, columnspan=3)


    yellow_frame = Frame(wlcm_frame, height=250, width=1280, bg="yellow").grid(row = 0, column = 0, padx = 5, pady=10, rowspan=3, columnspan=3)

    green_frame = Frame(wlcm_frame, height=500, width=1280, bg="green").grid(row = 3, column = 0, padx = 5, pady=5, columnspan=3)

    Label(yellow_frame, text = "SHREE LACE INDUSTRIES", bg='cyan').grid(row = 0, column = 1)
    Label(yellow_frame, text = "WELCOME TO THE SOFTWARE!", bg='cyan').grid(row = 1, column = 1)

    view_orders_button = Button(yellow_frame, text = "VIEW ORDERS", fg = "blue",command = None).grid(row = 2, column = 0)

    insert_order_button = Button(yellow_frame, text = "NEW PURCHASE ORDER", fg = "red",command = po_insert_scrn).grid(row = 2, column = 1)

    insert_item_button = Button(yellow_frame, text = "ITEMS", fg = "black",command = all_items_scrn).grid(row = 2, column = 2)

if __name__ == '__main__':
    master_scr()
