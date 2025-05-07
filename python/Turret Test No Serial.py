

import time

print("[TEST MODE] Turret controller started. Type angles in degrees (e.g., 45, -90).")

while True:
    try:
        # Read user input
        angle_str = input("Enter angle: ")
        if angle_str.lower() == "exit":
            print("Exiting test mode.")
            break

        angle = int(angle_str)

        # Convert to 2-byte signed int (as bytes)
        data = angle.to_bytes(2, byteorder='little', signed=True)

        # Simulate sending data
        print(f"[TEST] Would send bytes: {data.hex()} (angle {angle}°)")

    except ValueError:
        print("Please enter a valid integer or type 'exit' to quit.")
    except KeyboardInterrupt:
        print("\nExiting test mode.")
        break
