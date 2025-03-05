import os
import shutil
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import filedialog
import json
from CTkMessagebox import CTkMessagebox

class LocalizationTool(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

    def _setup_ui(self):
        CTkLabel(self, text="PixelComposer 汉化工具", font=("Microsoft YaHei", 28, "bold")).pack(pady=20)

        input_frame = CTkFrame(self)
        input_frame.pack(pady=10)

        self.locale_var = ctk.StringVar(value="zh")
        CTkLabel(input_frame, text="输入汉化名:", font=("Microsoft YaHei", 14)).pack(side="left", padx=5)
        CTkEntry(input_frame, textvariable=self.locale_var, width=100, font=("Microsoft YaHei", 14)).pack(side="left", padx=5)
        CTkButton(
            input_frame,
            text="选择汉化名",
            command=self.select_folder,
            width=100,
            font=("Microsoft YaHei", 14, "bold"),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52"
        ).pack(side="left", padx=5)

        btn_frame = CTkFrame(self)
        btn_frame.pack(pady=15)

        CTkButton(
            btn_frame,
            text="一键汉化软件",
            command=self.localize_software,
            width=180,
            font=("Microsoft YaHei", 14, "bold"),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52"
        ).pack(side="left", padx=10)

        CTkButton(
            btn_frame,
            text="一键汉化教程",
            command=self.localize_tutorial,
            width=180,
            font=("Microsoft YaHei", 14, "bold"),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52"
        ).pack(side="left", padx=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.locale_var.set(os.path.basename(folder_path))

    def localize_software(self):
        locale = self.locale_var.get().strip() or "zh"
        if not self.copy_localization_folder(locale):
            return
        if not self.modify_keys_json(locale):
            return
        CTkMessagebox(
            title="成功",
            message="汉化完成！",
            icon="check",
            button_color="#FF9166",
            button_hover_color="#E57C52",
            font=("Microsoft YaHei", 14, "bold")
        )

    def localize_tutorial(self):
        if not self.copy_tutorial_folder():
            return
        CTkMessagebox(
            title="成功",
            message="教程汉化完成！",
            icon="check",
            button_color="#FF9166",
            button_hover_color="#E57C52",
            font=("Microsoft YaHei", 14, "bold")
        )

    def copy_localization_folder(self, locale="zh"):
        source_folder = os.path.join(os.getcwd(), locale)
        target_folder = os.path.join(self.get_user_locale_path(), locale)
        
        if not os.path.exists(source_folder):
            CTkMessagebox(
                title="错误",
                message=f"汉化文件夹 '{locale}' 未找到，请确保它在工具同目录下！",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

        if not os.path.exists(self.get_user_locale_path()):
            CTkMessagebox(
                title="错误",
                message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

        try:
            shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
            return True
        except Exception as e:
            CTkMessagebox(
                title="错误",
                message=f"汉化过程中出现错误：{e}",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

    def modify_keys_json(self, locale="zh"):
        keys_path = os.path.join(self.get_preferences_path(), "keys.json")
        try:
            with open(keys_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if data.get("local") != locale:
                data["local"] = locale
                with open(keys_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                return True
            else:
                CTkMessagebox(
                    title="提示",
                    message="语言设置无需修改",
                    icon="info",
                    button_color="#FF9166",
                    button_hover_color="#E57C52",
                    button_text_color="#191925",
                    font=("Microsoft YaHei", 14, "bold")
                )
                return False
        except Exception as e:
            CTkMessagebox(
                title="错误",
                message=f"修改语言设置失败: {str(e)}",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

    def copy_tutorial_folder(self):
        source_folder = os.path.join(os.getcwd(), "Welcome files")
        target_folder = os.path.join(self.get_user_path(), "Welcome files")
        
        if not os.path.exists(source_folder):
            CTkMessagebox(
                title="错误",
                message="汉化教程文件夹 'Welcome files' 未找到，请确保它在工具同目录下！",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

        if not os.path.exists(self.get_user_path()):
            CTkMessagebox(
                title="错误",
                message="请检查PixelComposer安装路径！(多次尝试未果请手动安装)(请检查是否修改主目录路径)",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

        try:
            shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
            return True
        except Exception as e:
            CTkMessagebox(
                title="错误",
                message=f"教程汉化过程中出现错误：{e}",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return False

    def get_user_path(self):
        return os.path.join(os.path.expanduser("~"), "AppData", "Local", "PixelComposer")

    def get_user_locale_path(self):
        return os.path.join(self.get_user_path(), "Locale")

    def get_preferences_path(self):
        return os.path.join(self.get_user_path(), "Preferences", "1171")