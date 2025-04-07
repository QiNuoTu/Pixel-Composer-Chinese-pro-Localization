import os
import shutil
import webbrowser
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkFrame
import json
from CTkMessagebox import CTkMessagebox  # 确保导入 CTkMessagebox
import sys
import win32api  # 新增[1]
import win32con
import tkinter as tk  # 新增行

# 作者名称
AUTHOR_NAME = "安尘,WWNNL"
# GitHub地址
GITHUB_URL = "https://github.com/LifeOfAc/Pixel-Composer-Chinese-Localization"  
# 获取正确的基础路径
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, "assets", "app_icon.ico")  # 新增

# 设置外观模式和默认颜色主题
ctk.set_appearance_mode("Dark")  # 设置为 Dark 模式
ctk.set_default_color_theme("dark-blue")  # 设置为 dark-blue 主题

# 获取用户的PixelComposer路径
def get_user_path():
    return os.path.join(os.path.expanduser("~"), "AppData", "Local", "PixelComposer")

# 获取用户的PixelComposer Locale路径
def get_user_locale_path():
    return os.path.join(get_user_path(), "Locale")

# 获取用户的Preferences路径
def get_preferences_path():
    return os.path.join(get_user_path(), "Preferences", "1171")

def get_install_location(app_reg_key="Steam App 2299510"):
    """通过注册表获取Steam版安装路径"""  # 新增[1]
    try:
        reg_path = rf"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{app_reg_key}"
        key = win32api.RegOpenKey(
            win32con.HKEY_LOCAL_MACHINE,
            reg_path,
            0,
            win32con.KEY_READ
        )
        install_path, _ = win32api.RegQueryValueEx(key, "InstallLocation")
        win32api.RegCloseKey(key)
        clean_path = os.path.normpath(install_path.strip('"'))
        return clean_path if os.path.exists(clean_path) else None
    except Exception as e:
        print(f"注册表操作失败: {e}")
        return None
def delete_welcome_zip(install_path):
    """删除官方教程压缩包"""  # 新增[1]
    if not install_path:
        return "未提供有效安装路径"
    
    target_path = os.path.join(install_path, "data", "Welcome files")
    if not os.path.exists(target_path):
        return f"目标路径不存在: {target_path}"
    
    zip_path = os.path.join(target_path, "Welcome files.zip")
    if not os.path.exists(zip_path):
        return f"官方英文教程压缩包不存在，可能已删除"
    
    try:
        os.remove(zip_path)
        return f"成功删除官方英文教程压缩包"
    except Exception as e:
        return f"删除文件失败: {str(e)}"

# 修改keys.json文件中的local字段
def modify_keys_json(locale="zh"):
    keys_path = os.path.join(get_preferences_path(), "keys.json")
    try:
        with open(keys_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if data.get("local") != locale:
            data["local"] = locale
            with open(keys_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            create_centered_dialog(
                root,
                CTkMessagebox,
                title="成功", 
                message=f"汉化完成！已成功修改语言设置为 {locale}", 
                icon="check",
                button_color="#FF9166",  # 设置按钮颜色
                button_hover_color="#FF9166",  # 设置按钮悬停颜色
                font=("Microsoft YaHei", 14, "bold")
            )
            return True
        else:
            create_centered_dialog(
                root,
                CTkMessagebox,
                title="成功", 
                message="汉化完成！但语言设置无需修改", 
                icon="check",
                button_color="#FF9166",
                button_hover_color="#FF9166",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False
    except FileNotFoundError:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message=f"未找到keys.json文件：{keys_path}", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except json.JSONDecodeError:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="JSON文件格式错误，请检查文件内容", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except PermissionError:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="没有文件写入权限，请用管理员权限运行", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return False
    except Exception as e:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="未知错误", 
            message=str(e), 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return False

# 复制汉化文件夹
def copy_localization_folder(locale="zh"):
    # 检查工具同目录下是否存在汉化文件夹
    source_folder = os.path.join(os.getcwd(), locale)
    if not os.path.exists(source_folder):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message=f"汉化文件夹 '{locale}' 未找到，请确保它在工具同目录下！", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    # 获取目标路径
    locale_path = get_user_locale_path()
    en_folder = os.path.join(locale_path, 'en')
    target_folder = os.path.join(locale_path, locale)

    # 检查目标路径是否存在
    if not os.path.exists(locale_path):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    if not os.path.exists(en_folder):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    # 如果目标文件夹不存在，则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    try:
        shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
        modify_keys_json(locale)
    except Exception as e:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message=f"汉化过程中出现错误：{e}", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )

# 递归删除文件夹内文件
def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)
            shutil.rmtree(path_file)

# 复制教程文件夹
def copy_tutorial_folder():
    lib_path = get_user_path()
    welcome_files_folder = os.path.join(lib_path, 'Welcome files')
    
    if not os.path.exists(lib_path):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    if not os.path.exists(welcome_files_folder):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    del_file(welcome_files_folder)

    source_folder = os.path.join(os.getcwd(), 'Welcome files')

    if not os.path.exists(source_folder):
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message="汉化教程文件夹 'Welcome files' 未找到，请确保它在工具同目录下！", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        return

    try:
        shutil.copytree(source_folder, welcome_files_folder, dirs_exist_ok=True)
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="成功", 
            message="教程汉化完成！", 
            icon="check",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
    except Exception as e:
        create_centered_dialog(
            root,
            CTkMessagebox,
            title="错误", 
            message=f"教程汉化过程中出现错误：{e}", 
            icon="cancel",
            button_color="#FF9166",
            button_hover_color="#FF9166",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )

def handle_tutorial_localization():
    """带选项的教程汉化处理"""  # 新增[1]
    msg = create_centered_dialog(
        root,
        CTkMessagebox,
        title="教程清理选项",
        message="是否删除软件自动的英文教程？\n不删除会导致它在每次启动的时候，自动添加英文教程",
        icon="question",
        option_1="是",
        option_2="否",
        button_width=200,
        button_color="#FF9166",
        button_hover_color="#FF9166",
        button_text_color="#191925",
        font=("Microsoft YaHei", 14, "bold")
    )
    
    if msg.get() == "是":
        install_path = get_install_location()
        if install_path:
            result = delete_welcome_zip(install_path)
            create_centered_dialog(
                root,
                CTkMessagebox,
                title="清理结果",
                message=result,
                icon="info",
                button_color="#FF9166",
                button_hover_color="#FF9166",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
        else:
            create_centered_dialog(
                root,
                CTkMessagebox,
                title="路径错误",
                message="未找到Steam版安装路径！",
                icon="warning",
                button_color="#FF9166",
                button_hover_color="#FF9166",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
    
    copy_tutorial_folder()

# 打开浏览器进入特效交流群
def open_communication_group():
    url = "https://qm.qq.com/q/Vu9GTC4mw8"
    webbrowser.open(url)

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)
    def show_tip(self, event=None):
        if self.tip_window:
            return
        # 获取按钮在屏幕上的位置
        x = self.widget.winfo_rootx() + self.widget.winfo_width() + 10
        y = self.widget.winfo_rooty() - 10
        
        # 创建提示窗口
        self.tip_window = tk.Toplevel(self.widget)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.wm_geometry(f"+{x}+{y}")
        
        # 设置样式
        label = tk.Label(
            self.tip_window,
            text=self.text,
            background="#1a1a1a",
            foreground="#FF9166",
            relief=tk.FLAT,
            borderwidth=0,
            font=("Microsoft YaHei", 10)
        )
        label.pack()
    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = None

def open_github():  # 新增函数
    webbrowser.open(GITHUB_URL)

"""通用窗口居中函数"""
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 修正计算方式 [修改位置]
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2 - 40
    
    # 设置窗口大小和位置
    window.geometry(f"{width}x{height}+{x}+{y}")


def on_window_move(event):
    """窗口移动时更新子窗口位置"""
    if event.widget == root:
        # 获取所有子窗口
        children = [child for child in root.winfo_children() 
                  if isinstance(child, (ctk.CTkToplevel, CTkMessagebox))]

        # 更新每个子窗口位置
        for child in children:
            child.update_idletasks()
            new_x = root.winfo_rootx() + (root.winfo_width() - child.winfo_width()) // 2
            new_y = root.winfo_rooty() + (root.winfo_height() - child.winfo_height()) // 2
            child.geometry(f"+{new_x}+{new_y}")

# 创建主窗口
root = CTk()
root.geometry("500x230")  # 显式设置窗口尺寸
center_window(root, 500, 230)  # 调用修正后的居中函数
root.title("PixelComposer 汉化工具")
root.update()  # 确保窗口尺寸正确计算
root.resizable(False, False)  # 禁止调整窗口大小
root.bind("<Configure>", on_window_move)
center_window(root, 500, 230)  # 调用窗口居中函数

def create_centered_dialog(parent, dialog_type, **kwargs):
    dialog = dialog_type(master=parent, **kwargs)
    dialog.update_idletasks()
    
    # 获取坐标和尺寸
    parent_root_x = parent.winfo_rootx()
    parent_root_y = parent.winfo_rooty()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()
    dialog_width = dialog.winfo_width()
    dialog_height = dialog.winfo_height()
    
    # 带动态补偿的居中计算
    base_offset = -8  # 基础偏移量
    dynamic_offset = int(parent_height * 0.02)  # 动态偏移
    total_offset = base_offset + dynamic_offset
    
    x = parent_root_x + (parent_width - dialog_width) // 2
    y = parent_root_y + (parent_height - dialog_height) // 2 + total_offset
    
    dialog.geometry(f"+{x}+{y}")
    return dialog

# 设置窗口图标
try:
    print("尝试加载图标路径:", ICON_PATH)
    if os.path.exists(ICON_PATH):
        root.iconbitmap(ICON_PATH)
        print("图标设置成功")
    else:
        print(f"图标文件不存在: {ICON_PATH}")
except Exception as e:
    print(f"图标设置失败: {str(e)}")

# 添加标题标签
title_label = CTkLabel(root, text="PixelComposer 汉化工具", font=("Microsoft YaHei", 28, "bold"))
title_label.pack(pady=10)

# 创建输入框框架
input_frame = CTkFrame(root)
input_frame.pack(pady=5)

# 创建输入框和标签
locale_var = ctk.StringVar(value="zh")
locale_label = CTkLabel(input_frame, text="输入汉化包名(需在同目录):", font=("Microsoft YaHei", 16))
locale_label.pack(side=ctk.LEFT, padx=5)
locale_entry = CTkEntry(input_frame, textvariable=locale_var, width=100, font=("Microsoft YaHei", 16, "bold"), text_color="#FF9166")
locale_entry.pack(side=ctk.LEFT, padx=5)

# 创建按钮框架
button_frame = CTkFrame(root)
button_frame.pack(pady=5)

# 创建一键汉化按钮
def on_localize_button_click():
    locale = locale_var.get().strip() or "zh"
    copy_localization_folder(locale)

localize_button = CTkButton(button_frame, text="一键汉化软件", command=on_localize_button_click, width=150, font=("Microsoft YaHei", 14, "bold"), text_color="#191925", fg_color="#FF9166", hover_color="#FF9166")
localize_button.pack(side=ctk.LEFT, padx=5)

# 创建一键汉化教程按钮
tutorial_button = CTkButton(
    button_frame, 
    text="一键汉化教程", 
    command=handle_tutorial_localization,  # 修改[1]
    width=150,
    font=("Microsoft YaHei", 14, "bold"),
    text_color="#191925",
    fg_color="#FF9166",
    hover_color="#FF9166"
)
tutorial_button.pack(side=ctk.LEFT, padx=5)

# 创建一个空的Frame来作为新的一行
empty_frame = CTkFrame(root)
empty_frame.pack(pady=5)

# 创建加入交流群按钮
group_button = CTkButton(empty_frame, text="加入特效交流群", command=open_communication_group, width=150, font=("Microsoft YaHei", 14, "bold"), text_color="#191925", fg_color="#FF9166", hover_color="#FF9166")
group_button.pack(pady=5)

# 添加作者名称标签
# 添加作者信息框架
author_frame = CTkFrame(root, fg_color="transparent")  # 新增行
author_frame.pack(pady=5)  # 修改行

# 添加星号按钮
github_button = CTkButton(  # 新增按钮
    author_frame,
    text="★",
    width=28,
    height=28,
    command=open_github,
    font=("Microsoft YaHei", 20, "bold"),
    text_color="#FF9166",
    fg_color="transparent",
    hover_color="#2B2B2B"
)
github_button.pack(side=ctk.LEFT, padx=(0, 5))  # 新增行

# 添加Tooltip
Tooltip(github_button, "打开GitHub给作者一个Star鼓励一下") 

# 原有作者标签修改
author_label = CTkLabel(  # 修改行
    author_frame,  # 修改父容器
    text=f"作者:{AUTHOR_NAME}",
    font=("Microsoft YaHei", 16)
)
author_label.pack(side=ctk.LEFT)  # 修改行

# 显示初始提示
create_centered_dialog(
    root,
    CTkMessagebox,
    title="注意", 
    message="请在PixelComposer第一次运行后使用，请保证汉化文件夹与本程序在同一目录", 
    icon="info",
    button_color="#FF9166",
    button_hover_color="#FF9166",
    button_text_color="#191925",
    font=("Microsoft YaHei", 14, "bold")
)

# 运行主循环
root.mainloop()