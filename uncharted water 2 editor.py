from tkinter import *
from tkinter import ttk


def entry_transformation(entry):
    entry = str(hex(int(entry)))
    entry = entry[:2] + "0" * (6 - len(entry)) + entry[2:]
    entry = "B9" + " " + entry[4:] + " " + entry[2:4]
    return entry


def edit(file, offset, code):
    file.seek(offset)
    file.write(code)


def code_formation(code):
    list2 = code.split()
    result = "b'"
    for j in range(len(list2)):
        result = result + "\\x" + list2[j]
    result = result + "'"
    result = eval(result)
    return result


def modification_purchase():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_purchase.offset, code_formation(mod_purchase.update))
        edit(f, mod_purchase_1.offset, code_formation(mod_purchase_1.update))
        edit(f, mod_purchase_2.offset, code_formation(mod_purchase_2.update))

        mod_purchase_parameter1 = NewCode(0x29833, "B9 0A 00", entry_transformation((entry_parameter1.get())))
        edit(f, mod_purchase_parameter1.offset, code_formation(mod_purchase_parameter1.update))


def modification_selling():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_selling.offset, code_formation(mod_selling.update))
        edit(f, mod_selling_1.offset, code_formation(mod_selling_1.update))
        edit(f, mod_selling_2.offset, code_formation(mod_selling_2.update))


def modification_purchase_original():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_purchase.offset, code_formation(mod_purchase.original_code))
        edit(f, mod_purchase_1.offset, code_formation(mod_purchase_1.original_code))
        edit(f, mod_purchase_2.offset, code_formation(mod_purchase_2.original_code))


def modification_selling_original():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_selling.offset, code_formation(mod_selling.original_code))
        edit(f, mod_selling_1.offset, code_formation(mod_selling_1.original_code))
        edit(f, mod_selling_2.offset, code_formation(mod_selling_2.original_code))


def modification_recruit():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_recruit.offset, code_formation(mod_recruit.update))


def modification_recruit_original():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_recruit.offset, code_formation(mod_recruit.original_code))


def modification_artillery_display():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_artillery_display.offset, code_formation(mod_artillery_display.update))


def modification_artillery_display_original():
    with open('main.exe', 'r+b') as f:
        edit(f, mod_artillery_display.offset, code_formation(mod_artillery_display.original_code))


class NewCode:
    def __init__(self, offset, original_code, update):
        self.offset = offset
        self.original_code = original_code
        self.update = update


class Buttons:
    def __init__(self):
        self.button_purchase = Button(tab_commence, text="修改", command=modification_purchase)
        self.button_purchase.grid(row=0, column=7)
        self.button_purchase_original = Button(tab_commence, text="恢复原始设置", command=modification_purchase_original)
        self.button_purchase_original.grid(row=0, column=8)

        self.button_purchase = Button(tab_commence, text="修改", command=modification_selling)
        self.button_purchase.grid(row=2, column=7)
        self.button_purchase_original = Button(tab_commence, text="恢复原始设置", command=modification_selling_original)
        self.button_purchase_original.grid(row=2, column=8)

        self.button_recruit = Button(recruit_function_unit, text="修改", command=modification_recruit)
        self.button_recruit.pack(side="right")
        self.button_recruit_original = Button(recruit_function_unit, text="恢复原始设置", command=modification_recruit_original)
        self.button_recruit_original.pack(side="right")

        self.button_artillery_display = Button(artillery_display_function_unit, text="修改", command=modification_artillery_display)
        self.button_artillery_display.pack(side="right")
        self.button_artillery_display_original = Button(artillery_display_function_unit, text="恢复原始设置",
                                                        command=modification_artillery_display_original)
        self.button_artillery_display_original.pack(side="right")


# 主程序
root = Tk()
root.resizable(width=False, height=False)
root.title("大航海时代2修改器")
notebook = ttk.Notebook(root)
notebook.pack()
# 交易选项卡
tab1 = Frame(notebook)
tab_commence = Frame(tab1)
tab_commence.pack()
notebook.add(tab1, text="交易")
# 其他选项卡
tab2 = Frame(notebook)
tab_other_functions = Frame(tab2)
tab_other_functions.pack(fill="x")
notebook.add(tab2, text="其他")
tab_other_functions.columnconfigure(1, weight=1)
# recruit
recruit_function_unit = Frame(tab_other_functions)
label_recruit = Label(tab_other_functions, text="爵位bug修复")
label_recruit.grid(row=0, )
recruit_function_unit.grid(row=0, column=1, sticky="E")
# artillery display
artillery_display_function_unit = Frame(tab_other_functions)
label_artillery_display = Label(tab_other_functions, text="火炮显示倒转")
label_artillery_display.grid(row=1)
artillery_display_function_unit.grid(row=1, column=1, sticky="E")
# purchase
label_purchase = Label(tab_commence, text="买入")
label_purchase.grid(row=0, column=0)
# purchase parameter 1
label_purchase_parameter1 = Label(tab_commence, text="系数一")
label_purchase_parameter1.grid(row=0, column=1)
entry_parameter1 = (Entry(tab_commence, width=5))
entry_parameter1.insert(END, "10")
entry_parameter1.grid(row=0, column=2)
# purchase parameter 2
label_purchase_parameter2 = Label(tab_commence, text="系数二")
label_purchase_parameter2.grid(row=0, column=3)
entry_parameter2 = Entry(tab_commence, width=5)
entry_parameter2.insert(END, "1000")
entry_parameter2.grid(row=0, column=4)
# purchase comment
label_purchase_comment = Label(tab_commence,
                               text="修改后买入：\n"
                                    "非同类交易品：(积载量/系数一*商品买价/系数二)%\n"
                                    "同类交易品：积载量/系数一*商品买价/商业值)%+非同类交易品浮动\n",
                               justify=LEFT)
label_purchase_comment.grid(row=1, columnspan=9, sticky=W)

# selling
label_selling = Label(tab_commence, text="卖出")
label_selling.grid(row=2)
# selling parameter 1
label_selling_parameter1 = Label(tab_commence, text="系数一")
label_selling_parameter1.grid(row=2, column=1)
entry_selling_parameter1 = (Entry(tab_commence, width=5))
entry_selling_parameter1.insert(END, "20")
entry_selling_parameter1.grid(row=2, column=2)
# selling parameter 2
label_selling_parameter2 = Label(tab_commence, text="系数二")
label_selling_parameter2.grid(row=2, column=3)
entry_selling_parameter2 = Entry(tab_commence, width=5)
entry_selling_parameter2.insert(END, "500")
entry_selling_parameter2.grid(row=2, column=4)
# selling parameter 3
label_selling_parameter3 = Label(tab_commence, text="系数三")
label_selling_parameter3.grid(row=2, column=5)
entry_selling_parameter3 = Entry(tab_commence, width=5)
entry_selling_parameter3.insert(END, "10")
entry_selling_parameter3.grid(row=2, column=6)
# selling comment
label_selling_comment = Label(tab_commence,
                              text="修改后卖出：\n"
                                   "非同类交易品：(商品卖价/系数一*积载量/系数二)%\n"
                                   "同类交易品：(积载量*商品卖价/(商业值*系数三))%+非同类交易品浮动\n",
                              justify=LEFT)
label_selling_comment.grid(row=3, columnspan=9, sticky=W)

# buttons
buttons = Buttons()

# authors
author = Frame(tab1)
author.pack(fill="x", side=BOTTOM)
label_author = Label(author, text="(C) 2020 by st174929@stud.uni-stuttgart.de")
label_author.pack(side="right")

author = Frame(tab2)
author.pack(fill="x", side=BOTTOM)
label_author = Label(author, text="(C) 2020 by st174929@stud.uni-stuttgart.de")
label_author.pack(side="right")
# 数据段
mod_purchase = NewCode(0x29830, "8B 46 F4 F7 66 F0 8B 1E DC C2 8B 0F 81 C1 F4 01 8B F0 2B D2",
                                "8B 46 F4 B9 0A 00 99 F7 F9 F7 66 F0 8B 1E DC C2 8B 0F 8B F0")
mod_purchase_1 = NewCode(0x29849, "0A", "32")
mod_purchase_2 = NewCode(0x29876, "03", "32")
mod_selling = NewCode(0x2A076, "05 F4 01 2B D2", "B9 0A 00 F7 E1")
mod_selling_1 = NewCode(0x2A0A3, "0A", "32")
mod_selling_2 = NewCode(0x2A0DE, "F7 66 F2 B9 E8 03 2B D2 F7 F1 8B D0 B8 03 00",
                                 "B9 14 00 F7 F1 F7 66 F2 B9 F4 01 F7 F1 8B D0")
mod_recruit = NewCode(0x2B9D9, "2A F6 03 C2 2A FF F7 EB 8B D8 F7 E9 B9 0A 00 99 F7 F9",
                               "03 C2 2A FF F7 EB 8B D8 51 B9 0A 00 99 F7 F9 59 F7 E9")
mod_artillery_display = NewCode(0x313F5,
                                "C7 46 F6 00 00 EB 10 8B 46 F6 40 8B 5E F6 D1 E3 89 87 38 05 89 46 F6 8B 46 EE 39 46 "
                                "F6 7C E8",
                                "2B D2 EB 14 8B DA 42 D1 E3 B9 07 00 81 FA 07 00 74 02 2B CA 89 8F 38 05 8B 46 EE 3B "
                                "D0 7C E5")

root.mainloop()
