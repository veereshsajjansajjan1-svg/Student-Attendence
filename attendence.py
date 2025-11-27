import sys
if len(sys.argv) != 3:
    print("Usage: python attendance_tracker.py <classes_held> <classes_attended>")
    sys.exit(1)

classes_held = int(sys.argv[1])
classes_attended = int(sys.argv[2])

if classes_held <= 0 or classes_attended < 0 or classes_attended > classes_held:
    print("Error: Invalid input. Make sure classes held > 0 and attended ≤ held.")
    sys.exit(1)

attendance_percentage = (classes_attended / classes_held) * 100

print("\n--- Student Attendance Tracker ---")
print(f"Classes Held: {classes_held}")
print(f"Classes Attended: {classes_attended}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
