# enjson.py 完整修改版
import json
import os
def unescape_special_chars(s):
    """反转义特殊字符（必须按此顺序处理）"""
    return (
        s.replace('\\n', '\n')      # 先处理换行符
         .replace('\\r', '\r')      # 再处理回车符
         .replace('\\/', '/')       # 处理正斜杠转义
         .replace('\\\\', '\\')     # 最后处理反斜杠自身
    )
def parse_value(txt_value, original_type):
    """类型转换逻辑"""
    try:
        if original_type == bool:
            return txt_value.lower() == 'true'
        elif original_type == type(None):
            return None if txt_value == 'None' else txt_value
        elif original_type == int:
            return int(txt_value)
        elif original_type == float:
            return float(txt_value)
        else:
            return str(txt_value)
    except:
        return txt_value  # 类型转换失败时保持原始字符串
def convert_value(txt_value, original_type):
    """主转换函数"""
    if isinstance(txt_value, str) and original_type is str:
        # 只有字符串类型需要反转义
        unescaped = unescape_special_chars(txt_value)
        return parse_value(unescaped, original_type)
    else:
        return parse_value(txt_value, original_type)
def rebuild_structure(lines, structure_template):
    """递归重建数据结构"""
    if isinstance(structure_template, dict):
        keys = list(structure_template.keys())
        new_dict = {}
        for i, key in enumerate(keys):
            if i < len(lines):
                original_type = type(structure_template[key])
                new_dict[key] = convert_value(lines[i], original_type)
        return new_dict
    elif isinstance(structure_template, list):
        return [convert_value(line, type(item)) for line, item in zip(lines, structure_template)]
    else:
        return convert_value(lines[0], type(structure_template))
def restore_json(txt_path, json_template_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    
    with open(json_template_path, 'r', encoding='utf-8') as f:
        template = json.load(f)
    
    restored_data = rebuild_structure(lines, template)
    
    output_path = os.path.splitext(txt_path)[0] + '.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(restored_data, f, indent=2, ensure_ascii=False)
    
    print(f"已恢复文件：{output_path}")
def process_file(filename):
    json_name = filename.replace('.txt', '.json')
    restore_json(filename, json_name)

# 使用示例
process_file('text.txt')
# process_file('UI.txt')
# process_file('words.txt')
# process_file('nodes.json')
