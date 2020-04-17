# -*- coding:utf-8 -*-
# @Time      :2019/12/29 23:03
# @Author    :小栗旬

import tkinter as tk
from tkinter import ttk

# 存放选项
num_list = [[0] * 4 for _ in range(21)]
# 修改问题列表
question = [
    "问题1",
    "问题2",
    "问题3",
    "问题4",
    "问题5",
    "问题6",
    "问题7",
    "问题8",
    "问题9",
    "问题10",
    "问题11",
    "问题12",
    "问题13",
    "问题14",
    "问题15",
    "问题16",
    "问题17",
    "问题18",
    "问题19",
    "问题20",
    "问题21"
]

# 每个问题的答案
question_selectoptions = [
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"],
    ["A选项", "B选项", "C选项", "D选项"]
]


# 点击 下一题 的操作，第21题之后是第1题
def hit_me():
    global question_index
    num_list[question_index][var.get()] += 1
    question_index += 1
    if question_index == 21:
        question_index = 0
    var.set(-1)

    global l
    global r1
    global r2
    global r3
    global r4

    l.pack_forget()
    r1.pack_forget()
    r2.pack_forget()
    r3.pack_forget()
    r4.pack_forget()

    l = tk.Label(window, bg='yellow', width=20, text=question[question_index])
    l.pack()
    # 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
    r1 = tk.Radiobutton(window, text=question_selectoptions[question_index][0], variable=var, value=0)
    r1.pack()
    r2 = tk.Radiobutton(window, text=question_selectoptions[question_index][1], variable=var, value=1)
    r2.pack()
    r3 = tk.Radiobutton(window, text=question_selectoptions[question_index][2], variable=var, value=2)
    r3.pack()
    r4 = tk.Radiobutton(window, text=question_selectoptions[question_index][3], variable=var, value=3)
    r4.pack()


# 点击结束生成表格
def over_hit():
    print(num_list)
    tree = ttk.Treeview(window)
    tree['columns'] = ['A', 'B', 'C', 'D']
    tree.pack()
    tree.column("A", width=100)
    tree.column("B", width=100)
    tree.column("C", width=100)
    tree.column("D", width=100)

    tree.heading('A', text='A')
    tree.heading('B', text='B')
    tree.heading('C', text='C')
    tree.heading('D', text='D')

    for i in range(len(num_list)):
        tree.insert('', i, text=str(question[i]),
                    values=(str(num_list[i][0]), str(num_list[i][1]), str(num_list[i][2]), str(num_list[i][3])))


# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1200x900')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
var = tk.IntVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
var.set(-2)
question_index = 0



# 在窗口界面设置放置Button按键
b = tk.Button(window, text='下一个', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

over = tk.Button(window, text='结束', font=('Arial', 12), width=10, height=1, command=over_hit)
over.pack()

# 上面的提示，现在是第几题
l = tk.Label(window, bg='yellow', width=20, text=question[question_index])
l.pack()
# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text=question_selectoptions[question_index][0], variable=var, value=0)
r1.pack()
r2 = tk.Radiobutton(window, text=question_selectoptions[question_index][1], variable=var, value=1)
r2.pack()
r3 = tk.Radiobutton(window, text=question_selectoptions[question_index][2], variable=var, value=2)
r3.pack()
r4 = tk.Radiobutton(window, text=question_selectoptions[question_index][3], variable=var, value=3)
r4.pack()


# 第7步，主窗口循环显示
window.mainloop()
