import cv2
import numpy as np
import matplotlib.pyplot as plt


# ===============================
# Load dan preprocessing gambar
# ===============================
def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise Exception("Gambar tidak ditemukan: " + path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray


# ===============================
# Deteksi keypoints SIFT
# ===============================
def detect_sift(gray):
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors


# ===============================
# Visualisasi keypoints
# ===============================
def draw_keypoints(img, keypoints):
    return cv2.drawKeypoints(
        img, keypoints, None,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )


# ===============================
# Feature Matching + Lowe Ratio
# ===============================
def match_features(desc1, desc2, ratio=0.75):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(desc1, desc2, k=2)

    good = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append(m)

    return good


# ===============================
# Hitung similarity score
# ===============================
def similarity_score(good_matches, kp1):
    if len(kp1) == 0:
        return 0
    return (len(good_matches) / len(kp1)) * 100


# ===============================
# Visualisasi matching
# ===============================
def draw_matches(img1, kp1, img2, kp2, good_matches):
    return cv2.drawMatches(
        img1, kp1,
        img2, kp2,
        good_matches, None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )


# ===============================
# Tampilkan hasil
# ===============================
def show(title, image):
    plt.figure(figsize=(8,6))
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


# ===============================
# MAIN PROGRAM
# ===============================
def run_detection(img_path1, img_path2):

    # Load
    img1, gray1 = load_image(img_path1)
    img2, gray2 = load_image(img_path2)

    # Detect SIFT
    kp1, desc1 = detect_sift(gray1)
    kp2, desc2 = detect_sift(gray2)

    print("Keypoints Gambar 1 :", len(kp1))
    print("Keypoints Gambar 2 :", len(kp2))

    # Draw keypoints
    kp_img1 = draw_keypoints(img1, kp1)
    kp_img2 = draw_keypoints(img2, kp2)

    # Matching
    good_matches = match_features(desc1, desc2)

    print("Good Matches :", len(good_matches))

    # Similarity score
    score = similarity_score(good_matches, kp1)
    print("Similarity Score : %.2f%%" % score)

    # Draw matches
    match_img = draw_matches(img1, kp1, img2, kp2, good_matches)

    # Show results
    show("Keypoints Image 1", kp_img1)
    show("Keypoints Image 2", kp_img2)
    show("Feature Matching", match_img)

    # Kesimpulan otomatis
    if score > 40:
        print("KESIMPULAN: Kemungkinan gambar MIRIP / TERDAPAT PEMALSUAN")
    else:
        print("KESIMPULAN: Gambar BERBEDA")


# ===============================
# JALANKAN
# ===============================
if __name__ == "__main__":
    run_detection("p1.jpeg", "pp2.jpeg")
