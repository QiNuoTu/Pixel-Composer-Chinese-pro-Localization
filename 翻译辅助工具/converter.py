import os
import json
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkLabel, CTkComboBox
from tkinter import filedialog
import copy
from CTkMessagebox import CTkMessagebox

class BilingualConverter(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

    def _setup_ui(self):
        CTkLabel(self, text="双语转换工具", font=("Microsoft YaHei", 28, "bold")).pack(pady=20)

        input_frame = CTkFrame(self)
        input_frame.pack(pady=15, padx=30, fill="x")

        self.file_var = ctk.StringVar()
        self._create_file_entry(input_frame, "输入文件路径:", self.file_var)

        self.lang_var = ctk.StringVar(value="全部")
        CTkComboBox(
            input_frame,
            values=["全部", "ce-zh (中文-英文)", "ec-zh (英文-中文)"],
            variable=self.lang_var,
            font=("Microsoft YaHei", 14),
            text_color="#191925",  # 灰色字体
            fg_color="#FF9166",  # 黑色背景
            button_color="#FF9166",  # 橙色按钮
            border_color="#FF9166",  # 橙色边框
            dropdown_font=("Microsoft YaHei", 12),
            dropdown_fg_color="#FF9166",  # 黑色背景
            dropdown_text_color="#191925",
            dropdown_hover_color="#E57C52",  # 浅橙色悬停
            corner_radius=10
        ).pack(pady=10, ipadx=10, ipady=5)

        CTkButton(
            self,
            text="开始转换",
            command=self.convert_files,
            width=200,
            font=("Microsoft YaHei", 14, "bold"),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52",
            corner_radius=8
        ).pack(pady=20)

    def _create_file_entry(self, parent, label_text, var):
        frame = CTkFrame(parent)
        frame.pack(fill="x", pady=8)
        CTkLabel(frame, text=label_text, width=80).pack(side="left")
        CTkEntry(frame, textvariable=var, width=300).pack(side="left", padx=5, fill="x", expand=True)
        CTkButton(
            frame,
            text="浏览",
            width=60,
            command=lambda: var.set(filedialog.askopenfilename()),
            font=("Microsoft YaHei", 12),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52",
            corner_radius=6
        ).pack(side="right")

    def convert_files(self):
        input_path = self.file_var.get().strip() or "nodes.json"
        if not os.path.exists(input_path):
            CTkMessagebox(
                title="错误",
                message="文件不存在",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                original_data = json.load(f)
        except Exception as e:
            CTkMessagebox(
                title="错误",
                message=f"文件读取失败: {str(e)}",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return

        lang_order = self.lang_var.get()
        try:
            if lang_order in ["全部", "ce-zh (中文-英文)"]:
                data_ce = self.process_data(original_data, "ce-zh")
                os.makedirs("ce-zh", exist_ok=True)
                with open("ce-zh/nodes.json", 'w', encoding='utf-8') as f:
                    json.dump(data_ce, f, ensure_ascii=False, indent=2)

            if lang_order in ["全部", "ec-zh (英文-中文)"]:
                data_ec = self.process_data(original_data, "ec-zh")
                os.makedirs("ec-zh", exist_ok=True)
                with open("ec-zh/nodes.json", 'w', encoding='utf-8') as f:
                    json.dump(data_ec, f, ensure_ascii=False, indent=2)

            CTkMessagebox(
                title="完成",
                message="转换完成",
                icon="check",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
        except Exception as e:
            CTkMessagebox(
                title="错误",
                message=f"转换失败: {str(e)}",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )

    def process_data(self, original_data, language_order):
        data = copy.deepcopy(original_data)
        lang_key = language_order.split("-")[0]
        for node_key in original_data:
            if node_key.startswith("Node_"):
                english = node_key.replace("Node_", "", 1).replace("_", " ")
                chinese = original_data[node_key].get("name", "")
                
                if lang_key == "ce":
                    combined_name = f"{chinese}_{english}"
                else:
                    combined_name = f"{english}_{chinese}"
                
                data[node_key]["name"] = combined_name if chinese != english else chinese
        return data