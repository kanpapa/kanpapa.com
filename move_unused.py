import os
import re
import shutil
import urllib.parse

# 設定
CONTENT_DIR = "content"
BACKUP_DIR = "unused_images"  # ここに移動されます
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp', '.tiff'}

def get_all_files(directory, extensions=None):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if extensions:
                _, ext = os.path.splitext(file)
                if ext.lower() not in extensions:
                    continue
            file_list.append(os.path.join(root, file))
    return file_list

def find_used_images(content_dir):
    used_images = set()
    md_files = get_all_files(content_dir, {'.md'})

    # Markdownの画像記法 ![alt](url)
    # HTMLのimgタグ <img src="url">
    # Front Matterの image: url
    patterns = [
        re.compile(r'!\[.*?\]\((.*?)\)'),
        re.compile(r'<img.*?src=["\'](.*?)["\']'),
        re.compile(r'image:\s*["\']?([^"\']+\.[a-zA-Z0-9]+)["\']?'), # image: xxx.jpg
        re.compile(r'avatar:\s*["\']?([^"\']+\.[a-zA-Z0-9]+)["\']?') # avatar: xxx.jpg
    ]

    print(f"Checking {len(md_files)} markdown files...")

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        md_dir = os.path.dirname(md_file)

        for pattern in patterns:
            for match in pattern.findall(content):
                # URLデコード (例: image%201.jpg -> image 1.jpg)
                url = urllib.parse.unquote(match.strip())
                
                # 外部URLやルートパス(/static等)は除外
                if url.startswith('http') or url.startswith('//'):
                    continue
                
                # パス解決（Markdownファイルからの相対パスと仮定）
                # ../ などが含まれる場合も解決する
                abs_path = os.path.abspath(os.path.join(md_dir, url))
                used_images.add(abs_path)

    return used_images

def move_unused_images():
    # 1. 使用されている画像を特定
    used_images_paths = find_used_images(CONTENT_DIR)
    print(f"Found {len(used_images_paths)} referenced images.")

    # 2. 存在する全画像をリストアップ
    all_images = get_all_files(CONTENT_DIR, IMAGE_EXTS)
    print(f"Found {len(all_images)} total images in content directory.")

    moved_count = 0
    
    # 3. 比較して移動
    for img_path in all_images:
        abs_img_path = os.path.abspath(img_path)
        
        # 使われていない場合
        if abs_img_path not in used_images_paths:
            # 移動先のパスを作成 (階層構造を維持)
            rel_path = os.path.relpath(abs_img_path, os.getcwd())
            target_path = os.path.join(BACKUP_DIR, rel_path)
            
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            try:
                shutil.move(img_path, target_path)
                print(f"[MOVED] {rel_path}")
                moved_count += 1
            except Exception as e:
                print(f"[ERROR] Could not move {rel_path}: {e}")

    print(f"\nDone! Moved {moved_count} unused images to '{BACKUP_DIR}/'.")

if __name__ == "__main__":
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: {CONTENT_DIR} directory not found.")
    else:
        move_unused_images()
