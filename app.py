from flask import Flask, render_template, jsonify
from ga import run_ga
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-ga')
def trigger_ga():
    start_time = time.time()
    best_schedule, history = run_ga()
    end_time = time.time()

    # Sắp xếp lịch trước khi gửi lên frontend
    best_schedule.sort(key=lambda x: (x["day"], x["slot"]))

    return jsonify({
        "schedule": best_schedule,
        "execution_time": round(end_time - start_time, 2),
        "generations": len(history),
        "history": history
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)