import time
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ga import run_ga

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Trình duyệt sẽ gọi endpoint này để tải giao diện"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/run-ga")
async def trigger_ga():
    """
    Endpoint này ghép nối toàn bộ logic từ main.py cũ:
    Đo thời gian, chạy GA, và sắp xếp kết quả.
    """
    print("Đang chạy Genetic Algorithm... Vui lòng đợi.")

    start_time = time.time()

    best_schedule, history = run_ga()

    end_time = time.time()

    execution_time = round(end_time - start_time, 2)
    generations = len(history)

    best_schedule.sort(key=lambda x: (x["day"], x["slot"]))

    print(f"Hoàn thành sau: {execution_time} giây")
    print(f"Tổng số thế hệ: {generations}")

    return {
        "schedule": best_schedule,
        "execution_time": execution_time,
        "generations": generations,
        "history": history
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)