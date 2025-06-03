with open("inference.log") as f:
    lines = f.readlines()[-20:]

slow = [l for l in lines if "Inference" in l and float(l.split()[3][:-1]) > 0.4]

with open("alert.txt", "w") as out:
    if slow:
        out.write("⚠️ Cảnh báo inference chậm:\n")
        out.writelines(slow)
    else:
        out.write("✅ Không có cảnh báo nào.")