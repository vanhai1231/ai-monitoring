from flask import Flask, request, jsonify
from prometheus_client import Counter, Summary, generate_latest
import time, random, logging

app = Flask(__name__)
logging.basicConfig(filename='inference.log', level=logging.INFO)

INFER_COUNT = Counter('inference_requests_total', 'Total inference requests')
INFER_TIME = Summary('inference_duration_seconds', 'Inference time')

@app.route('/predict', methods=['POST'])
@INFER_TIME.time()
def predict():
    INFER_COUNT.inc()
    data = request.json
    start = time.time()
    time.sleep(random.uniform(0.1, 0.5))
    pred = random.choice(['positive', 'negative'])
    duration = time.time() - start
    logging.info(f"Inference done in {duration:.3f}s, prediction={pred}")
    return jsonify({"prediction": pred, "duration": duration})

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)