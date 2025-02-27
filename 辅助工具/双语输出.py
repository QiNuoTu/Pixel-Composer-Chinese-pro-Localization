import json
import os
import copy

def convert_to_bilingual(input_json_path="nodes.json",
                         output_folder_ce="ce-zh",
                         output_folder_ec="ec-zh"):
    # 创建输出目录
    os.makedirs(output_folder_ce, exist_ok=True)
    os.makedirs(output_folder_ec, exist_ok=True)

    # 读取原始数据
    with open(input_json_path, 'r', encoding='utf-8') as f:
        original_data = json.load(f)
    
    # 创建副本数据
    data_ce = copy.deepcopy(original_data)
    data_ec = copy.deepcopy(original_data)

    # 处理每个节点
    for node_key in original_data:
        if node_key.startswith("Node_"):
            # 提取英文名称
            english = node_key.replace("Node_", "", 1).replace("_", " ")
            # 提取中文名称
            chinese = original_data[node_key].get("name", "")
            
            # 智能拼接逻辑
            if chinese == english:
                # 中英文相同时不拼接
                combined_name = chinese
            else:
                # 正常拼接
                combined_name_ce = f"{chinese}_{english}"
                combined_name_ec = f"{english}_{chinese}"

            # 更新数据
            data_ce[node_key]["name"] = combined_name if chinese == english else combined_name_ce
            data_ec[node_key]["name"] = combined_name if chinese == english else combined_name_ec

    # 保存结果
    with open(f"{output_folder_ce}/nodes.json", 'w', encoding='utf-8') as f:
        json.dump(data_ce, f, ensure_ascii=False, indent=2)
    
    with open(f"{output_folder_ec}/nodes.json", 'w', encoding='utf-8') as f:
        json.dump(data_ec, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    convert_to_bilingual()
