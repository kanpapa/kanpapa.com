import os
import glob
import yaml
import collections

# 設定
CONTENT_DIR = "content"
THRESHOLD = 20  # この記事数以下のカテゴリを抽出
PLAN_FILE = "category_plan.yaml"

def parse_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Front Matter (--- で囲まれた部分) を抽出
    try:
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            return fm
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    return None

def main():
    print("Scanning content...")
    category_counts = collections.defaultdict(int)
    
    # 全ファイルをスキャンしてカテゴリをカウント
    files = glob.glob(os.path.join(CONTENT_DIR, "**/*.md"), recursive=True)
    
    for file_path in files:
        fm = parse_front_matter(file_path)
        if fm and 'categories' in fm:
            cats = fm['categories']
            # 文字列ならリスト化
            if isinstance(cats, str):
                cats = [cats]
            
            if cats:
                for cat in cats:
                    category_counts[cat] += 1

    print(f"Found {len(category_counts)} unique categories.")

    # 閾値以下のカテゴリを抽出してプランを作成
    plan = {}
    sorted_cats = sorted(category_counts.items(), key=lambda x: x[1])
    
    count_small = 0
    for cat, count in sorted_cats:
        if count <= THRESHOLD:
            # 提案データの作成
            plan[cat] = {
                'count': count,
                'new_category': cat,      # デフォルトは変更なし
                'add_tags': [cat]         # デフォルトで元のカテゴリ名をタグに追加
            }
            count_small += 1

    # YAMLファイルとして保存
    with open(PLAN_FILE, 'w', encoding='utf-8') as f:
        f.write("# カテゴリ統廃合プラン\n")
        f.write("# count: 現在の記事数\n")
        f.write("# new_category: 移動先のカテゴリ（変更しなければそのまま）\n")
        f.write("# add_tags: 追加するタグのリスト（不要なら [] にする）\n")
        f.write("# --------------------------------------------------\n\n")
        yaml.dump(plan, f, allow_unicode=True, sort_keys=False)

    print(f"\nDone! Found {count_small} small categories.")
    print(f"Please edit '{PLAN_FILE}' to define your cleanup strategy.")

if __name__ == "__main__":
    main()
