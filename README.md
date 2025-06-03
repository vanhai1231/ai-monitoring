# AI Monitoring Project

## 🧠 Mục tiêu
Giám sát inference time của AI model bằng Prometheus & Grafana. Dùng AI Agent để tự động cảnh báo nếu inference quá chậm.

## 🔧 Cách chạy local
```bash
docker-compose up --build
```

Truy cập:
- API: http://localhost:5000/predict
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 🤖 Chạy AI Agent thủ công
```bash
python agent.py
```

## 🚀 Chạy GitHub Actions
- Tự động gửi request tới model
- Phân tích log và upload alert
- Kiểm tra tại tab Actions trên GitHub
