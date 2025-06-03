with open("inference.log") as f:
    lines = f.readlines()[-20:]

slow = []
for l in lines:
    if "Inference" in l:
        try:
            duration_str = l.split()[3].replace('s', '')  # bỏ ký tự 's'
            duration = float(duration_str)
            if duration > 0.4:
                slow.append(l)
        except ValueError:
            continue  # Bỏ qua nếu lỗi định dạng

with open("alert.txt", "w") as out:
    if slow:
        out.write("Cảnh báo inference chậm:\n")
        out.writelines(slow)
    else:
        out.write("Không có cảnh báo nào.")
