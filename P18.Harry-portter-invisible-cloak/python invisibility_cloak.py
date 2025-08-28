import cv2
import numpy as np

def get_background(cap, frames=60):
    """Capture a stable background frame."""
    bg = None
    for _ in range(frames):
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)  # mirror for a natural webcam feel
        bg = frame
    return bg

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    print("➡️ Make sure the scene is empty, then press 'b' to capture background.")
    print("➡️ Press 'q' to quit.")

    background = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        if background is None:
            cv2.putText(frame, "Press 'b' to capture background", (20, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Invisibility Cloak", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('b'):
                print("📸 Capturing background...")
                background = get_background(cap)
                print("✅ Background captured.")
            elif key == ord('q'):
                break
            continue

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red color range in HSV
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        # ✅ Combine masks correctly
        red_mask = cv2.bitwise_or(mask1, mask2)

        # Clean the mask
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN,
                                    np.ones((3, 3), np.uint8), iterations=2)
        red_mask = cv2.dilate(red_mask, np.ones((3, 3), np.uint8), iterations=1)
        red_mask = cv2.GaussianBlur(red_mask, (5, 5), 0)

        inverse_mask = cv2.bitwise_not(red_mask)

        current_no_cloak = cv2.bitwise_and(frame, frame, mask=inverse_mask)
        cloak_area_from_bg = cv2.bitwise_and(background, background, mask=red_mask)

        final = cv2.addWeighted(current_no_cloak, 1, cloak_area_from_bg, 1, 0)

        cv2.putText(final, "Press 'b' to recapture background | 'q' to quit",
                    (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2, cv2.LINE_AA)

        cv2.imshow("Invisibility Cloak", final)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            print("📸 Re-capturing background...")
            background = get_background(cap)
            print("✅ Background updated.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
