import cv2
import numpy as np

class FeatureDetector:
    def __init__(self, method='SIFT'):
        if method == 'SIFT':
            self.detector = cv2.SIFT_create()
        elif method == 'ORB':
            self.detector = cv2.ORB_create()
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def detect_and_compute(self, image):
        keypoints, descriptors = self.detector.detectAndCompute(image, None)
        return keypoints, descriptors

class HomographyCalculator:
    def __init__(self):
        self.matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    
    def find_homography(self, src_image, dst_image, method='SIFT'):
        # Detect keypoints and compute descriptors
        detector = FeatureDetector(method)
        kp1, des1 = detector.detect_and_compute(src_image)
        kp2, des2 = detector.detect_and_compute(dst_image)
        
        # Match descriptors
        matches = self.matcher.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        
        # Extract matched keypoints
        src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        
        # Compute homography matrix
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        return H, mask

def main():
    # Load images
    src_image = cv2.imread('source_image.jpg', cv2.IMREAD_GRAYSCALE)
    dst_image = cv2.imread('destination_image.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Calculate homography
    calculator = HomographyCalculator()
    H, mask = calculator.find_homography(src_image, dst_image, method='SIFT')
    
    # Print the homography matrix
    print("Homography Matrix:")
    print(H)

if __name__ == "__main__":
    main()
