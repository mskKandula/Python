from tkinter import Entry
import tkinter as tk

root = tk.Tk()
root.title("GUI")
root.geometry('300x200+646+220')

def shift_focus(event):
    event.widget.tk_focusNext().focus()

fmuOffset = 0
metaBlock = 0
mDie = 0
MFMUblockType = 0
fmuInBlock = 0
PFMUblockType = 0
plane = 0
die = 0
block = 0
global PFMU_Die_dec

def main2(event):
    global fmuOffset, metaBlock, mDie, MFMUblockType, fmuInBlock, die, block, plane
    event.widget.tk_focusNext().focus_set()
    D17 = int(C17.get(),16) & 262143
    D18 = (int(C18.get(),16)&2047)<<18
    e1= ((1<<2)-1)
    e2=int(C19.get(),16)&e1
    D19 = e2<<29
    e3 = ((1<<1)-1)
    e4 = int(C20.get(),16) &e3
    D20 = e4<<31

    E18 = D17|D18
    E19 = E18 | D19
    E20 = E19 | D20

    F17 = hex(D17)[2:]
    F18 = hex(D18)[2:]
    F19 = hex(D19)[2:]
    F20 = hex(D20)[2:-1]

    G18 = hex(E18)[2:]
    G19 = hex(E19)[2:]
    G20 = hex(E20)[2:-1]

    MFMU_String = tk.Label(root, text="MFMU String = %X"% int(G20,16)).place(x=10,y=120)
def button1_click():
    root = tk.Tk()
    root.title("MFMU PHY")
    root.geometry('630x250+486+486')

    global MFMU_Offset_dec, user_input, binary_Val, MFMU_MetaBlock_Dec, MFMU_String, MFMU_WL, MFMU_Plane, MFMU_Die, MFMU_Page
    def hex_to_dec(event):
        try:
            hex_value = input_entry_hex.get().strip()
            dec_value = int(hex_value,16)
            input_entry_dec.delete(0,tk.END)
            input_entry_dec.insert(0, str(dec_value))
        except ValueError:
            input_entry_dec.delete(0, tk.END)
    def dec_to_hex(event):
        try:
            dec_value = input_entry_dec.get().strip()
            hex_value = hex(int(dec_value))[2:].upper()
            input_entry_hex.delete(0,tk.END)
            input_entry_hex.insert(0, hex_value)
        except ValueError:
            input_entry_hex.delete(0, tk.END)

    # Hexadecimal Entry
    hex_label = tk.Label(root, text="Hexadecimal:")
    hex_label.place(x=15, y=20)
    input_entry_hex = tk.Entry(root)
    input_entry_hex.insert(0,G20)
    input_entry_hex.bind('<KeyRelease>', hex_to_dec)
    input_entry_hex.place(x=100, y=20)
    input_entry_hex.bind('<Return>', shift_focus)

    # Decimal Entry
    dec_label = tk.Label(root, text="Decimal:")
    dec_label.place(x=15, y=20)
    input_entry_dec = tk.Entry(root)
    input_entry_dec.insert(0,E20)
    input_entry_dec.place(x=100, y=20)
    input_entry_dec.bind('<KeyRelease>', hex_to_dec)
    input_entry_dec.bind('<Return>', shift_focus)

    def convert_to_binary():
        root.title('Convert')
        root.geometry('630x250+486+486')
        user_input = input_entry_hex.get()
        binary_Val = bin(int(user_input,16))[2:].zfill(32)

        e0 = tk.Label(root, text="USer entered MFMU is = ").place(x=40, y=100)
        label = tk.Label(root, text=user_input).place(x=200,y=100)
        e1 = tk.Label(root, text="MFMU in Binary = ").place(x=40, y=120)
        label = tk.Label(root, text=binary_Val).place(x=200,y=120)

        MFMU_BlockType = binary_Val[:-31]
        if MFMU_BlockType == "0":
            e9= tk.Label(root, text="MFMU Block Type = ").place(x=40, y=160)
            label = tk.Label(root, text="SLC").place(x=200,y=160)
        else:
            e1 = tk.Label(root, text="MFMU in Binary = ").place(x=40, y=160)
            label = tk.Label(root, text="TLC").place(x=200,y=160)
        MFMU_Offset_bin = binary_Val[-18:]
        MFMU_Offset_hex=hex(int(MFMU_Offset_bin,2))[2:]
        MFMU_Offset_dec=int(MFMU_Offset_bin,2)
        e4="MFMU Offset = "
        e4_val=str(MFMU_Offset_dec) + "    [  HEX = " + MFMU_Offset_hex + "  ]"
        label = tk.Label(root, text=e4).place(x=40, y=140)
        label = tk.Label(root, text=e4_val).place(x=200,y=140)

        MFMU_MetaBlock_bin = binary_Val[-29:-18]
        MFMU_MetaBlock_hex = hex(int(MFMU_MetaBlock_bin,2))[2:]
        MFMU_MetaBlock_Dec = int(MFMU_MetaBlock_bin,2)

        if MFMU_BlockType == "0":
            MFMU_LWL = int(MFMU_Offset_dec/64)
        else:
            MFMU_LWL = int(MFMU_Offset_dec/(24*8))
        
        MFMU_String = MFMU_LWL%4

        if MFMU_BlockType == "0":
            MFMU_WL = int(MFMU_Offset_dec/256)
        else:
            MFMU_WL = int(MFMU_Offset_dec/(192*4))

        MFMU_WL_hex = hex(MFMU_WL)[2:]

        if MFMU_BlockType == "0":
            MFMU_Page = 0
        else:
            MFMU_Page = (MFMU_Offset_dec/8)%3
        
        if MFMU_BlockType == "0":
            MFMU_Die = (MFMU_Offset_dec/8)%8
        else:
            MFMU_Die = (MFMU_Offset_dec/24)%8

        if MFMU_BlockType == "0":
            MFMU_Plane = (MFMU_Offset_dec/4)%2
        else:
            MFMU_Plane = (MFMU_Offset_dec/4)%2
        
        output_text = "Die =   " + str(MFMU_Die) +   "   //  Plane =  " + str(MFMU_Plane) +   "   //  Block =  " + str(MFMU_MetaBlock_Dec) +   "  [ HEX =  " + format(MFMU_MetaBlock_hex.upper()) + " ]  " + " //  WL =  " + str(MFMU_WL) +   "  [ HEX =  " + format(MFMU_WL_hex.upper()) + " ]  "  "   //  String =  " + str(MFMU_String) +   "   //  Page =  " + str(MFMU_Page)
        output_label = tk.Label(root, text=output_text).place(x=40, y=200)
    button = tk.Button(root, text="Convert", command=convert_to_binary).place(x=200,y=80)

button1 = tk.Button(root, text="MP ADD", width=int(35), command=button1_click)
button1.place(x=10, y=160)

def hex_to_dec(event, entry_dec, entry):
        try:
            hex_value1 = entry.get().strip()
            dec_value1 = int(hex_value1,16)
            entry_dec.delete(0,tk.END)
            entry_dec.insert(0, str(dec_value1))
        except ValueError:
            entry_dec.delete(0, tk.END)
def dec_to_hex(event, entry, entry_dec):
        try:
            dec_value1 = entry_dec.get().strip()
            hex_value1 = hex(int(dec_value1))[2:].upper()
            entry.delete(0,tk.END)
            entry.insert(0, hex_value1)
        except ValueError:
            entry.delete(0, tk.END)

""" MFMU_Lael = tk.Label(root, text="Enter MFMU Details in Hex").place(x=0, y=160)
MFMU_Lael_dec = tk.Label(root, text="Enter MFMU details in dec").place(x=500, y=160) """

C17 = tk.Entry(root)
C17.place(x=10,y=20)
C17.bind('<KeyRelease>', lambda event:hex_to_dec(event, C17_dec,C17))
C17.bind('<Return>', shift_focus)
C17.bind('<Return>', main2)

C18 = tk.Entry(root)
C18.place(x=10,y=40)
C18.bind('<KeyRelease>', lambda event:hex_to_dec(event, C18_dec,C18))
C18.bind('<Return>', shift_focus)
C18.bind('<Return>', main2)

C19 = tk.Entry(root)
C19.place(x=10,y=60)
C19.bind('<KeyRelease>', lambda event:hex_to_dec(event, C19_dec,C19))
C19.bind('<Return>', shift_focus)
C19.bind('<Return>', main2)

C20 = tk.Entry(root)
C20.place(x=10,y=80)
C20.bind('<KeyRelease>', lambda event:hex_to_dec(event, C20_dec,C20))
C20.bind('<Return>', shift_focus)
C20.bind('<Return>', main2)

C17_dec = tk.Entry(root)
C17_dec.place(x=150,y=20)
C17_dec.bind('<KeyRelease>', lambda event:dec_to_hex(event, C17,C17_dec))
C17_dec.bind('<Return>', shift_focus)
C17_dec.bind('<Return>', main2)

C18_dec = tk.Entry(root)
C18_dec.place(x=150,y=40)
C18_dec.bind('<KeyRelease>', lambda event:dec_to_hex(event, C18,C18_dec))
C18_dec.bind('<Return>', shift_focus)
C18_dec.bind('<Return>', main2)

C19_dec = tk.Entry(root)
C19_dec.place(x=150,y=60)
C19_dec.bind('<KeyRelease>', lambda event:dec_to_hex(event, C19,C19_dec))
C19_dec.bind('<Return>', shift_focus)
C19_dec.bind('<Return>', main2)

C20_dec = tk.Entry(root)
C20_dec.place(x=150,y=80)
C20_dec.bind('<KeyRelease>', lambda event:dec_to_hex(event, C20,C20_dec))
C20_dec.bind('<Return>', shift_focus)
C20_dec.bind('<Return>', main2)

root.mainloop()