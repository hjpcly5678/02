import os
import glob

def format_ip443_files():
    # 获取 ip443/ 下所有 .txt 文件
    txt_files = glob.glob("ip443/*.txt")
    
    if not txt_files:
        print("No files found in ip443/")
        return
    
    for txt_file in txt_files:
        # 提取国家代码（从文件名）
        country_code = os.path.splitext(os.path.basename(txt_file))[0]
        temp_file = f"{txt_file}.tmp"
        
        # 读取原文件，写入新格式
        with open(txt_file, "r") as f_in, open(temp_file, "w") as f_out:
            for ip in f_in:
                ip = ip.strip()
                if ip:  # 忽略空行
                    formatted_ip = f"{ip}:443#{country_code}"
                    f_out.write(f"{formatted_ip}\n")
        
        # 替换原文件
        os.replace(temp_file, txt_file)
        print(f"Formatted {txt_file}")

if __name__ == "__main__":
    format_ip443_files()
