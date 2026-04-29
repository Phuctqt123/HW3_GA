import time
from ga import run_ga
from plot import plot

start_time = time.time()

print("Đang chạy Genetic Algorithm... Vui lòng đợi.")
best, history = run_ga()

# 3. Ghi lại thời điểm kết thúc
end_time = time.time()

# 4. Tính toán tổng thời gian
execution_time = end_time - start_time

print("-" * 30)
print(f"Hoàn thành sau: {execution_time:.2f} giây")
print(f"Tổng số thế hệ: {len(history)}")
print("-" * 30)

print("Best schedule:")
# Sắp xếp lại lịch học theo Thứ và Tiết cho dễ nhìn
best.sort(key=lambda x: (x["day"], x["slot"]))

for g in best:
    # In ra định dạng dễ đọc hơn
    print(f"Thứ {g['day']} | Tiết {g['slot']} | Môn {g['course']['id']} | Lớp {g['section']} | GV {g['prof']} | Phòng {g['room']['id']}")

plot(history)