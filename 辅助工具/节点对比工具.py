import json
from datetime import datetime

def compare_nodes(old_file, new_file, output_txt="node_changes.txt"):
    """生成简洁版节点变更报告（仅清单模式）"""
    
    def load_nodes(filename):
        """加载并过滤节点数据"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return {k: v for k, v in data.items() if k.startswith("Node_")}

    # 加载数据
    old_data = load_nodes(old_file)
    new_data = load_nodes(new_file)

    # 计算三类变更
    added = sorted(new_data.keys() - old_data.keys())
    modified = sorted(k for k in new_data.keys() & old_data.keys() 
                     if new_data[k] != old_data[k])
    deleted = sorted(old_data.keys() - new_data.keys())

    # 构建报告
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = [
        f"节点变更清单报告 ({timestamp})",
        f"旧版本：{old_file}",
        f"新版本：{new_file}",
        "="*50,
        f"总变更数：[+{len(added)}] [~{len(modified)}] [-{len(deleted)}]",
        "="*50
    ]

    # 按类别输出清单
    def add_section(title, items, symbol):
        if items:
            report.extend([
                f"\n[{symbol} {title} ({len(items)})]",
                *[f"{i+1}. {item}" for i, item in enumerate(items)]
            ])

    add_section("新增节点", added, "+")
    add_section("修改节点", modified, "~")
    add_section("删除节点", deleted, "-")

    # 无变更处理
    if not any([added, modified, deleted]):
        report.append("\n▷ 无任何节点变更")

    # 写入文件
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"报告已生成：{output_txt}")

# 使用示例
if __name__ == "__main__":
    compare_nodes(
        old_file="old-nodes.json",
        new_file="new-nodes.json",
        output_txt="对比报告.txt"
    )
