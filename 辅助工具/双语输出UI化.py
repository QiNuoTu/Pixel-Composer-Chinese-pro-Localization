# 文件名: bilingual_gui_final.py
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import os
import json
import copy
from tkinter import filedialog
from collections import OrderedDict

# ====================== 常量定义 ======================
AUTHOR_NAME = "安尘,WWNNL"
GITHUB_URL = "https://github.com/LifeOfAc/Pixel-Composer-Chinese-Localization"

# ====================== 主题配置 ======================
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# ====================== 核心功能 ======================
def is_valid_node(node_data):
    """验证是否为有效节点（name后紧跟outputs）"""
    keys = list(node_data.keys())
    try:
        name_index = keys.index("name")
        return "outputs" in keys[name_index+1:]
    except (ValueError, IndexError):
        return False

def convert_bilingual(zh_json_path, en_json_path, output_folder_ce, output_folder_ec):
    try:
        # 读取基础文件（中文翻译文件）
        with open(zh_json_path, 'r', encoding='utf-8') as f:
            base_data = json.load(f, object_pairs_hook=OrderedDict)
        
        # 读取英文参考文件
        with open(en_json_path, 'r', encoding='utf-8') as f:
            en_data = json.load(f, object_pairs_hook=OrderedDict)

        # 创建输出目录
        os.makedirs(output_folder_ce, exist_ok=True)
        os.makedirs(output_folder_ec, exist_ok=True)

        # 处理有效节点
        valid_count = 0
        data_ce = copy.deepcopy(base_data)
        data_ec = copy.deepcopy(base_data)
        
        for node_key in base_data:
            if node_key.startswith("Node_") and is_valid_node(base_data[node_key]):
                # 获取中文名称
                zh_name = base_data[node_key].get("name", "")
                # 获取对应英文名称
                en_name = en_data.get(node_key, {}).get("name", "")
                
                if zh_name and en_name:
                    # 生成双语名称
                    data_ce[node_key]["name"] = f"{zh_name}_{en_name}"
                    data_ec[node_key]["name"] = f"{en_name}_{zh_name}"
                    valid_count += 1

        # 保存文件
        for data, folder in [(data_ce, output_folder_ce), (data_ec, output_folder_ec)]:
            output_path = os.path.join(folder, "nodes.json")
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ': '))
        
        return True, valid_count
    except Exception as e:
        return False, str(e)

# ====================== UI界面 ======================
class BilingualUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("双语输出工具 v3.0")
        self.geometry("700x500")
        self._center_window()
        self.resizable(False, False)
        
        # 变量初始化
        self.zh_json_path = ctk.StringVar()
        self.en_json_path = ctk.StringVar()
        self.output_ce = ctk.StringVar(value="ce-zh")
        self.output_ec = ctk.StringVar(value="ec-zh")
        
        self._create_widgets()
    
    def _center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 700) // 2
        y = (screen_height - 500) // 2 - 40
        self.geometry(f"+{x}+{y}")
    
    def _create_widgets(self):
        # 标题
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(pady=(15, 10))
        ctk.CTkLabel(
            title_frame,
            text="中英双语生成工具",
            font=("Microsoft YaHei", 24, "bold")
        ).pack()
        
        # 文件选择区域
        self._create_file_selector("中文基础文件:", self.zh_json_path)
        self._create_file_selector("英文参考文件:", self.en_json_path)
        
        # 输出设置
        output_frame = ctk.CTkFrame(self, fg_color="transparent")
        output_frame.pack(pady=15, fill="x", padx=20)
        
        ctk.CTkLabel(
            output_frame,
            text="输出模式:",
            font=("Microsoft YaHei", 14)
        ).grid(row=0, column=0, padx=5, sticky="w")
        
        ctk.CTkEntry(
            output_frame,
            textvariable=self.output_ce,
            placeholder_text="中英模式目录",
            width=150,
            font=("Microsoft YaHei", 12)
        ).grid(row=0, column=1, padx=5)
        
        ctk.CTkEntry(
            output_frame,
            textvariable=self.output_ec,
            placeholder_text="英中模式目录",
            width=150,
            font=("Microsoft YaHei", 12)
        ).grid(row=0, column=2, padx=5)
        
        # 操作按钮
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)
        
        ctk.CTkButton(
            btn_frame,
            text="生成双语文件",
            command=self._convert,
            width=200,
            height=40,
            fg_color="#FF9166",
            hover_color="#FF9166",
            font=("Microsoft YaHei", 16, "bold")
        ).pack()
        
        # 状态信息
        self.status_label = ctk.CTkLabel(
            self,
            text="就绪",
            font=("Microsoft YaHei", 12),
            text_color="#AAAAAA"
        )
        self.status_label.pack(pady=5)
        
        # 作者信息
        author_frame = ctk.CTkFrame(self, fg_color="transparent")
        author_frame.pack(pady=10)
        
        ctk.CTkButton(
            author_frame,
            text="项目地址",
            command=lambda: self._open_url(GITHUB_URL),
            width=80,
            fg_color="transparent",
            border_width=1,
            border_color="#FF9166",
            font=("Microsoft YaHei", 12)
        ).pack(side="left", padx=5)
        
        ctk.CTkLabel(
            author_frame,
            text=f"作者: {AUTHOR_NAME}",
            font=("Microsoft YaHei", 12)
        ).pack(side="left", padx=5)
    
    def _create_file_selector(self, label_text, path_var):
        """创建文件选择组件"""
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, fill="x", padx=20)
        
        ctk.CTkLabel(
            frame,
            text=label_text,
            font=("Microsoft YaHei", 14)
        ).pack(side="left", padx=5)
        
        entry = ctk.CTkEntry(
            frame,
            textvariable=path_var,
            width=400,
            font=("Microsoft YaHei", 12)
        )
        entry.pack(side="left", padx=5, fill="x", expand=True)
        
        ctk.CTkButton(
            frame,
            text="浏览",
            width=60,
            command=lambda: self._browse_file(path_var),
            fg_color="#FF9166",
            hover_color="#FF9166",
            font=("Microsoft YaHei", 12)
        ).pack(side="left", padx=5)
    
    def _browse_file(self, path_var):
        path = filedialog.askopenfilename(
            filetypes=[("JSON文件", "*.json")],
            initialdir=os.getcwd()
        )
        if path:
            path_var.set(path)
            self.status_label.configure(text=f"已选择文件: {os.path.basename(path)}")
    
    def _convert(self):
        # 输入验证
        if not all([self.zh_json_path.get(), self.en_json_path.get()]):
            show_error_dialog("请先选择中英文文件！")
            return
        
        # 执行转换
        self.status_label.configure(text="正在处理...", text_color="#FF9166")
        self.update()
        
        success, result = convert_bilingual(
            self.zh_json_path.get(),
            self.en_json_path.get(),
            self.output_ce.get(),
            self.output_ec.get()
        )
        
        # 显示结果
        if success:
            self.status_label.configure(text=f"成功处理 {result} 个节点", text_color="#00FF00")
            CTkMessagebox(
                title="完成",
                message=f"已生成双语文件至：\n{self.output_ce.get()} 和 {self.output_ec.get()}",
                icon="check",
                button_color="#FF9166"
            )
        else:
            self.status_label.configure(text="处理失败", text_color="#FF0000")
            show_error_dialog(f"错误: {result}")

    def _open_url(self, url):
        import webbrowser
        webbrowser.open(url)

# ====================== 工具函数 ======================
def show_error_dialog(message):
    CTkMessagebox(
        title="错误",
        message=message,
        icon="cancel",
        button_color="#FF9166",
        font=("Microsoft YaHei", 14)
    )

if __name__ == "__main__":
    app = BilingualUI()
    app.mainloop()