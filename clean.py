import os

# 你的 index.html 所在的目录
target_dir = "docs"
bad_string = "https://polyfill.io/v3/polyfill.min.js?features=es6"

print("🧼 正在扫描 docs/ 文件夹下的所有 HTML 文件...")

cleaned_count = 0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 如果发现包含毒链接，直接全局替换掉
            if bad_string in content:
                content = content.replace(f'<script src="{bad_string}"></script>', "")
                # 兼容可能没有被引号包裹完全或者换行的情况
                content = content.replace(bad_string, "") 
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"✅ 成功清除毒链接: {file_path}")
                cleaned_count += 1

if cleaned_count == 0:
    print("✨ 检查完毕！HTML 中没有发现 polyfill.io 毒链接，网站很干净。")
else:
    print(f"🚀 清理完成！共处理了 {cleaned_count} 个文件。现在可以安全 Push 到 GitHub 了！")