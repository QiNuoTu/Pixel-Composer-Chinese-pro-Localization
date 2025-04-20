import json
import os
def escape_special_chars(s):
    """统一处理特殊字符转义"""
    return (
        s.replace('\\', '\\\\')  # 先转义反斜杠自身
         .replace('\n', '\\n')    # 换行符
         .replace('\r', '\\r')    # 回车符
         .replace('/', '\\/')     # 正斜杠
    )
def extract_values(data):
    values = []
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, (dict, list)):
                values.extend(extract_values(value))
            else:
                processed = escape_special_chars(str(value)) if isinstance(value, str) else str(value)
                values.append(processed)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                values.extend(extract_values(item))
            else:
                processed = escape_special_chars(str(item)) if isinstance(item, str) else str(item)
                values.append(processed)
    else:
        processed = escape_special_chars(str(data)) if isinstance(data, str) else str(data)
        values.append(processed)
    return values
def process_file(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    values = extract_values(data)
    
    base_name = os.path.basename(json_path)
    txt_path = os.path.splitext(base_name)[0] + '.txt'
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(values))
    
    print(f"已生成文件：{txt_path}")

# 处理三个文件
# process_file('text.json')
# process_file('UI.json')
# process_file('words.json')
process_file('nodes.json')
