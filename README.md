# AI Monitoring Project

## 📌 Mục tiêu dự án
- Giám sát mô hình AI theo thời gian thực bằng Prometheus & Grafana.
- Sử dụng AI Agent để tự động kiểm tra log, phát hiện lỗi và cảnh báo.
- Triển khai CI/CD với GitHub Actions để tự động hóa quá trình test, monitoring và gửi báo cáo.

---

## 🧱 Kiến trúc hệ thống

```
[Client Request] ---> [Flask AI Model] ---> [Prometheus Exporter /metrics]
                                    |               |
                                    |               v
                                [inference.log]   [Prometheus Server] --> [Grafana Dashboard]
                                       |
                                       v
                                  [agent.py] ---> alert.txt / email / log warning
```

---

## 🛠️ Công nghệ sử dụng
- Python 3.10
- Flask
- Prometheus + Grafana
- Docker, Docker Compose
- GitHub Actions (CI/CD)

---

## 📂 Cấu trúc thư mục

```
ai-monitoring/
├── app.py                  # Flask AI model có metrics
├── agent.py                # AI Agent phân tích log
├── Dockerfile              # Dockerfile cho AI model
├── requirements.txt        # Thư viện cần thiết
├── prometheus.yml          # Cấu hình Prometheus
├── docker-compose.yml      # Khởi động toàn bộ hệ thống
├── inference.log           # Log sinh ra từ app.py (runtime)
├── alert.txt               # Báo cáo sinh ra từ agent.py
├── README.md               # Hướng dẫn chi tiết
└── .github/
    └── workflows/
        └── monitor.yml     # GitHub Actions workflow
```

---

## 🚀 Hướng dẫn chạy local

### Bước 1: Build và chạy hệ thống
```bash
docker-compose up --build
```

### Bước 2: Gửi request mẫu để sinh log
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "hi"}'
```

### Bước 3: Mở các giao diện
- Flask API: http://localhost:5000/predict
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (user: admin / pass: admin)

### Bước 4: Chạy AI Agent để phân tích log
```bash
python agent.py
cat alert.txt
```

---

## 🤖 Tự động hóa với GitHub Actions

Workflow `.github/workflows/monitor.yml` sẽ thực hiện:
- Tự động build project
- Gửi request test đến model
- Copy file `inference.log` ra host
- Phân tích bằng `agent.py`
- Tạo file cảnh báo `alert.txt`
- Upload kết quả vào mục Artifact

### Kích hoạt
- Push lên nhánh `main`
- Hoặc nhấn "Run workflow" tại tab **Actions** của repo

---

## 📊 Dashboard Grafana (tuỳ chọn)
Để cấu hình Dashboard đẹp:
1. Truy cập Grafana → `http://localhost:3000`
2. Đăng nhập: `admin / admin`
3. Add data source: Prometheus → `http://prometheus:9090`
4. Import Dashboard ID từ Grafana Hub (ví dụ: 1860 hoặc 11074)

---

## 📤 Kết quả đầu ra
- `alert.txt` chứa cảnh báo nếu inference > 0.4s
- Dashboard theo dõi số lượng request và thời gian infer
- Artifact upload sau mỗi lần chạy CI trên GitHub

---

