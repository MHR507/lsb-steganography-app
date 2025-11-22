from stego.dataset import generate_dataset
from stego.detector import StegoDetector
from sklearn.model_selection import train_test_split

# Generate dataset with multiple stego images per cover
X, y = generate_dataset(
    cover_folder="images/cover",
    stego_folder="images/stego",
    bits=1,
    num_stego_per_cover=5,
    payload_length=50
)

# Split dataset into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train detector
detector = StegoDetector()
detector.train(X_train, y_train)

# Evaluate
detector.evaluate(X_test, y_test)

# Save trained model
detector.save("detector_model2.pkl")
print("Training completed. Model saved as detector_model1.pkl")
