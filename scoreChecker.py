from datetime import datetime

students = {
    "Tude": 90,
    "Ayu": 72,
    "Bima": 65,
    "Made": 55,
    "Gita": 83
}

def calculate_stats(data):
    avg = sum(data.values()) / len(data)
    return avg, max(data.values()), min(data.values())

def get_status(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else:
        return "Remedial"

try:
    avg, high, low = calculate_stats(students)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"--- Hasil Evaluasi ({now}) ---\n")

    with open("hasil.txt", "w") as f:
        f.write(f"--- Hasil Evaluasi ({now}) ---\n\n")
        for name, score in students.items():
            status = get_status(score)
            line = f"Nama: {name} | Nilai: {score} | Status: {status}"
            print(line)
            f.write(line + "\n")

        summary = f"\nRata-rata: {avg:.2f}\nNilai Tertinggi: {high}\nNilai Terendah: {low}\n"
        print(summary)
        f.write(summary)

except Exception as e:
    print("Terjadi kesalahan:", e)
