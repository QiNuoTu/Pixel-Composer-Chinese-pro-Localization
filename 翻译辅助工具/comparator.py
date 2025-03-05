import os
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton, CTkEntry, CTkLabel
from tkinter import filedialog
import json
from CTkMessagebox import CTkMessagebox
from datetime import datetime

class FileComparator(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

    def _setup_ui(self):
        CTkLabel(self, text="双语文件对比工具", font=("Microsoft YaHei", 28, "bold")).pack(pady=20)

        input_frame = CTkFrame(self)
        input_frame.pack(pady=15, padx=30, fill="x")

        self.old_file_var = ctk.StringVar()
        self._create_file_entry(input_frame, "旧文件路径:", self.old_file_var)
        self.new_file_var = ctk.StringVar()
        self._create_file_entry(input_frame, "新文件路径:", self.new_file_var)

        CTkButton(
            self,
            text="开始对比",
            command=self.compare_files,
            width=200,
            font=("Microsoft YaHei", 14, "bold"),
            text_color="#191925",
            fg_color="#FF9166",
            hover_color="#E57C52"
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
            hover_color="#E57C52"
        ).pack(side="right")

    def compare_files(self):
        old_path = self.old_file_var.get().strip()
        new_path = self.new_file_var.get().strip()
        if not all([os.path.exists(old_path), os.path.exists(new_path)]):
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
            with open(old_path, 'r', encoding='utf-8') as f:
                old_data = json.load(f)
            with open(new_path, 'r', encoding='utf-8') as f:
                new_data = json.load(f)
        except json.JSONDecodeError:
            CTkMessagebox(
                title="错误",
                message="JSON格式错误",
                icon="cancel",
                button_color="#FF9166",
                button_hover_color="#E57C52",
                button_text_color="#191925",
                font=("Microsoft YaHei", 14, "bold")
            )
            return

        differences = self.analyze_differences(old_data, new_data)
        self.generate_report(old_path, new_path, differences)

        resp = CTkMessagebox(
            title="完成",
            message="对比报告已生成，是否查看？",
            icon="question",
            option_1="取消",
            option_2="打开",
            button_color="#FF9166",
            button_hover_color="#E57C52",
            button_text_color="#191925",
            font=("Microsoft YaHei", 14, "bold")
        )
        if resp.get() == "打开":
            os.startfile("对比报告.txt")

    def analyze_differences(self, old, new):
        return {
            "added": [k for k in new if k not in old],
            "modified": [k for k in new if k in old and new[k] != old[k]],
            "removed": [k for k in old if k not in new]
        }

    def generate_report(self, old_path, new_path, differences):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        old_name = os.path.basename(old_path)
        new_name = os.path.basename(new_path)
        total = f"[+{len(differences['added'])}] [~{len(differences['modified'])}] [-{len(differences['removed'])}]"

        with open("对比报告.txt", "w", encoding="utf-8") as f:
            f.write(f"节点变更清单报告 ({timestamp})\n旧版本：{old_name}\n新版本：{new_name}\n{'='*50}\n总变更数：{total}\n{'='*50}\n")
            if differences["added"]:
                f.write(f"\n[+ 新增节点 ({len(differences['added'])}]\n" + "\n".join(f"{i}. {node}" for i, node in enumerate(differences["added"], 1)))
            if differences["modified"]:
                f.write(f"\n\n[~ 修改节点 ({len(differences['modified'])}]\n" + "\n".join(f"{i}. {node}" for i, node in enumerate(differences["modified"], 1)))
            if differences["removed"]:
                f.write(f"\n\n[- 删除节点 ({len(differences['removed'])}]\n" + "\n".join(f"{i}. {node}" for i, node in enumerate(differences["removed"], 1)))
            f.write(f"\n\n{'—'*60}")