import os
import re

# 記事があるディレクトリ
TARGET_DIR = "content/post"

def add_slug_to_md(file_path):
    # 親フォルダ名を取得（これがSlugになる）
    dir_name = os.path.basename(os.path.dirname(file_path))
    
    # ファイルを読み込み
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 既に slug が設定されているかチェック
    has_slug = any(line.strip().startswith("slug:") for line in lines)
    if has_slug:
        print(f"[SKIP] Slug exists: {dir_name}")
        return

    # Front Matter の 'date:' の行を探して、その下に slug を追加する
    new_lines = []
    slug_added = False
    in_front_matter = False
    sep_count = 0

    for line in lines:
        new_lines.append(line)
        
        # Front Matterの区切り (---) をカウント
        if line.strip() == "---":
            sep_count += 1
        
        # date行の下に挿入（まだ追加しておらず、Front Matter内である場合）
        if not slug_added and sep_count == 1 and line.startswith("date:"):
            new_lines.append(f'slug: "{dir_name}"\n')
            slug_added = True
            print(f"[UPDATE] Added slug: {dir_name}")

    # ファイルに書き込み
    if slug_added:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

# メイン処理：ディレクトリを探索
if os.path.exists(TARGET_DIR):
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file == "index.md":
                add_slug_to_md(os.path.join(root, file))
else:
    print(f"Error: Directory {TARGET_DIR} not found.")
