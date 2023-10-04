# 导入tkinter模块，用于创建GUI界面
import tkinter as tk
# 导入filedialog模块，用于弹出文件选择对话框
from tkinter import filedialog
from tkinter import messagebox
# 导入os模块，用于执行系统命令
import os
# 导入pyinstaller模块，用于打包脚本 # 修改：导入pyinstaller模块
import PyInstaller
import PyInstaller.__main__
import pyperclip
import shutil
from shutil import copy
from shutil import rmtree
import win32com.client

video = 'error'
path_2 = 'error'
icon = 'error'
name = 'Python Program'
yes_or_no_i = ''
file_name_Entry_get_Prefix_name = 'Python Program'

# 获取当前文件的绝对路径
file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
file_dir = os.path.dirname(file_path)

# 切换到当前文件所在的目录
os.chdir(file_dir)

window = tk.Tk()
window.title('肥胖龟Python打包器（pyinstaller的第三方GUI界面')
window.geometry('363x373')

var = tk.StringVar()
command = tk.Label(window, textvariable=var, bg='white', font=('黑体',20), width=25, height=2)
command.place(x=0,y=0)
var.set('肥胖龟Python打包器')

title_2 = tk.Label(window, text='pyinstaller的第三方GUI界面', bg='white', font=('黑体',12), width=44, height=2)
title_2.place(x=0,y=42)

delete_bl = 1
show_bl = 0
show_bl_2 = '--noconsole'

def F5():
    global delete_bl
    global show_bl
    global show_bl_2
    delete_bl = delete.get()
    show_bl = show.get()
    if show_bl == 1:
        show_bl_2 = '--console'
    else:
        show_bl_2 = '--noconsole'
    print(delete.get())
    print(show.get())

    print('')

    print(delete_bl)
    print(show_bl_2)

print(delete_bl)
print(show_bl)


delete = tk.IntVar()
show = tk.IntVar()

show_Checkbutton = tk.Checkbutton(window,text='是否显示命令行窗口',variable=show,onvalue=1,offvalue=0,command=F5)
show_Checkbutton.place(x=0,y=90)
show.set(0)

path = tk.StringVar()
path_text = tk.Label(window, textvariable=path, bg='white', font=('黑体',12), width=38, height=2)
path_text.place(x=50,y=125)
path.set('请选择文件')

# 定义一个函数，用于调用文件选择对话框并获取文件名
def select_file():
    global video
    # 弹出文件选择对话框，并将返回值赋给file_name变量
    file_name = filedialog.askopenfilename()
    # 如果用户选择了一个文件，而不是取消或关闭对话框
    if file_name:
        global video
        # 将文件名赋值给video变量，并去掉前面的空格 # 修改：去掉空格
        video = file_name.strip()
        # 打印video变量的值，或者做其他操作
        path.set(video)
        print(video)

# 创建一个按钮，点击后弹出文件选择对话框
choose = tk.Button(window, text="选择文件", width=10, height=2, command=lambda: select_file())
choose.place(x=0,y=125)

path2 = tk.StringVar()
path_text_2 = tk.Label(window, textvariable=path2, bg='white', font=('黑体',12), width=38, height=2)
path_text_2.place(x=50,y=175)
path2.set('请选择输出目录')

def select_folder():
    global path_2
    # 创建一个tkinter窗口对象
    window = tk.Tk()
    # 隐藏窗口，只显示对话框
    window.withdraw()
    # 弹出文件选择对话框，让用户选择一个文件夹，并返回文件夹的路径
    folder_path = filedialog.askdirectory()
    # 如果用户没有取消选择，则将文件夹的路径赋值给path_2变量，并转换为字符串类型 # 修改：转换为字符串类型
    if folder_path:
        path_2 = str(folder_path)
        path2.set(path_2)
        # 打印path_2变量的值，用于测试
        print(path_2)
        # 销毁窗口对象，释放资源
        window.destroy()

choose_folder = tk.Button(window, text="选择目录", width=10, height=2, command=lambda: select_folder())
choose_folder.place(x=0,y=175)

path_icon = tk.StringVar()
path_text_icon = tk.Label(window, textvariable=path_icon, bg='white', font=('黑体',12), width=38, height=2)
path_text_icon.place(x=50,y=225)
path_icon.set('请选择图标')

# 定义一个函数，用于调用文件选择对话框并获取文件名
def select_file_icon():
    global icon
    global yes_or_no_i
    # 弹出文件选择对话框，并将返回值赋给file_name变量
    file_name = filedialog.askopenfilename()
    # 如果用户选择了一个文件，而不是取消或关闭对话框
    if file_name:
        # 将文件名赋值给icon变量，并去掉前面的空格 # 修改：去掉空格
        icon = file_name.strip()
        yes_or_no_i = '-i'
        # 打印icon变量的值，或者做其他操作
        path_icon.set(icon)
        print(icon)
    else:
        icon = ''
        yes_or_no_i = ''

# 创建一个按钮，点击后弹出文件选择对话框
choose_icon = tk.Button(window, text="选择图标", width=10, height=2, command=lambda: select_file_icon())
choose_icon.place(x=0,y=225)

text = tk.Entry(window,show=None)
text.place(x=0,y=275,width=250,height=35)

exe = tk.Label(window, text='.exe', bg='white', font=('黑体',12), width=5, height=2)
exe.place(x=251,y=275)

def set_def():
    global file_name_Entry_get_Prefix_name
    file_name_Entry_get_Prefix_name = text.get()

set = tk.Button(window, text="确定", width=7, height=2, command=set_def)
set.place(x=298,y=275)

# 获取当前文件的绝对路径
file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
file_dir = os.path.dirname(file_path)

# 切换到当前文件所在的目录
os.chdir(file_dir)

def sc_def():
    # 获取当前文件的绝对路径
    file_path = os.path.abspath(__file__)

    # 获取当前文件所在的目录
    file_dir = os.path.dirname(file_path)

    # 切换到当前文件所在的目录
    os.chdir(file_dir)

    PyInstaller.__main__.run([
        (video),
        '-F',
        (show_bl_2),
        (yes_or_no_i),
        (icon),
        '--distpath',
        (path_2)
    ])

    # 使用os.path.basename函数，提取文件的名称（不包含路径）
    file_no_path = os.path.basename(video)

    # 打印变量的值
    print(file_no_path)

    # 分割文件名和扩展名
    file_name, file_ext = os.path.splitext(file_no_path)

    print(file_name)

    # 定义变量file_name_after_modify_contain_Prefix_and_suffix_name，表示新的文件名
    file_name_after_modify_contain_Prefix_and_suffix_name = file_name + ".exe"

    # 打印变量的值
    print(file_name_after_modify_contain_Prefix_and_suffix_name)

    # 拼接目录和文件名，得到完整的文件路径
    file_path = os.path.join(path_2, file_name_after_modify_contain_Prefix_and_suffix_name)

    print(file_path)

    # 判断文件是否存在，如果存在则重命名，否则打印提示信息
    if os.path.exists(file_path):
        # 分割文件名和扩展名
        file_name, file_ext = os.path.splitext(file_path)
        # 拼接新的文件名
        new_file_name = file_name_Entry_get_Prefix_name + '.exe'
        # 拼接新的文件路径
        new_file_path = os.path.join(path_2, new_file_name)
        # 重命名文件
        os.rename(file_path, new_file_path)
        print("文件已重命名")
    else:
        print("文件不存在")

sc = tk.Button(window, text="开始打包", width=25, height=2, command=sc_def)
sc.place(x=0,y=325)

def about():
    about_window = tk.Toplevel()
    about_window.title('关于"肥胖龟Python打包器（pyinstaller的第三方GUI界面）"')
    about_window.geometry('530x490')
    about_window.configure(bg='white')

    command = tk.Label(about_window, text='肥胖龟Python打包器', bg='white', fg='#0078d4', font=('微软雅黑',30,'bold'))
    command.place(x=65,y=13)

    fgx = tk.Label(about_window, text='_______________________________________________________________________', bg='white', fg='#bbbbbb', font=('黑体',10))
    fgx.place(x=14,y=73)

    text1 = tk.Label(about_window, text='肥胖龟Python打包器（pyinstaller的第三方GUI界面）', bg='white', font=('微软雅黑',9))
    text1.place(x=55,y=105)

    text2 = tk.Label(about_window, text='版本v1.0', bg='white', font=('微软雅黑',9))
    text2.place(x=55,y=126)

    text3 = tk.Label(about_window, text='© 肥胖龟 FatTurtle （隶属于肥胖龟公司、TL工作室）。保留所有权利。', bg='white', font=('微软雅黑',9))
    text3.place(x=55,y=147)

    text4 = tk.Label(about_window, text='肥胖龟Python打包器（pyinstaller的第三方GUI界面）软件及其用户界面受中', bg='white', font=('微软雅黑',9))
    text4.place(x=55,y=189)

    text5 = tk.Label(about_window, text='国大陆和其它国家/地区的商标法和其它待颁布或已颁布的知识产权法保护。', bg='white', font=('微软雅黑',9))
    text5.place(x=55,y=208)

    text6 = tk.Label(about_window, text='该软件所需最低运行环境为：Windows 7', bg='white', font=('微软雅黑',9))
    text6.place(x=55,y=250)

    text7 = tk.Label(about_window, text='如您使用的是Windows Vista及以下的操作系统，该软件可能不能正常运行', bg='white', font=('微软雅黑',9))
    text7.place(x=55,y=271)

    text8 = tk.Label(about_window, text='您可以通过以下联系方式联系开发者进行适配旧系统：', bg='white', font=('微软雅黑',9))
    text8.place(x=55,y=292)

    text9 = tk.Label(about_window, text='联系方式：qianzhemayi1234567@163.com', bg='white', font=('微软雅黑',9))
    text9.place(x=55,y=334)

    def copy_def():
        pyperclip.copy("qianzhemayi1234567@163.com")
        yes_copy = messagebox.showinfo(title="已复制", message="已复制")

    copy = tk.Button(about_window,text='复制',command=copy_def)
    copy.place(x=310, y=330)

    def juanxian():
        os.system('start https://postimg.cc/K121LGX9')

    juanxian_Button = tk.Button(about_window,text='捐献', width=27, height=1, command=juanxian)
    juanxian_Button.place(x=55, y=380)

    def kaiyuan():
        os.system('start https://github.com/FatTurtle2022/FatTurtle_Cut_End/releases')

    kaiyuan_Button = tk.Button(about_window,text='开源', width=27, height=1, command=kaiyuan)
    kaiyuan_Button.place(x=260, y=380)

    def exit_def():
        about_window.destroy()

    OK_Button = tk.Button(about_window,text='确定', width=11, height=1, command=exit_def)
    OK_Button.place(x=425, y=445)

    about_window.mainloop()

about_button = tk.Button(window, text="关于软件", width=24, height=2, command=about)
about_button.place(x=185,y=325)

window.mainloop()