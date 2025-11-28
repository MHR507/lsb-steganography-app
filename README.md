# LSB Steganography App  
A powerful and user-friendly **Streamlit-based Python application** for performing:

LSB Image Steganography (Encode & Decode)  
LSB Steganography Detection using Image Analysis  

---

## Features

### 🔐 **1. Hide Text in Images (Encoding)**
- Upload any PNG/JPG image  
- Enter a secret message  
- App hides the text using **Least Significant Bit (LSB)** technique  
- Download the stego image instantly  
- No visible change in the image

### 🔍 **2. Extract Hidden Text (Decoding)**
- Upload a stego image  
- App extracts the LSB-encoded message  
- Works even if the image is slightly compressed

### 🕵️ **3. LSB Steganography Detector**
This feature helps detect whether **any image contains LSB-based hidden data**, even if you don’t know the original message.  
The detector uses:

- **Bit-plane analysis**
- **LSB noise pattern detection**
- **Pixel frequency randomness tests**
- **Histogram irregularity checks**

The output shows:
- ✔️ Probability of hidden data  
- ✔️ Visualized LSB plane  
- ✔️ Statistical analysis summary  

Useful for:
- Security audits  
- Digital forensics  
- Testing suspicious images  

### **4. Easy and Modern UI**
- Clean Streamlit interface  
- Works offline  
- Fast and GPU/CPU friendly

---

## Technologies Used
- **Python 3**
- **Streamlit**
- **Pillow (PIL)**
- **NumPy**
- **Matplotlib** (for detector visualization)

---

## Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MHR507/lsb-steganography-app.git
cd lsb-steganography-app
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv myenv
```

### 3️⃣ Activate Environment  
**Windows:**
```bash
myenv\Scripts\activate
```
**Linux/Mac:**
```bash
source myenv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open the link (usually `http://localhost:8501`).

---

## 📁 Project Structure

```
lsb-steganography-app/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
│
├── utils/
│   ├── encoder.py            # LSB encoding logic
│   ├── decoder.py            # LSB decoding logic
│   ├── detector.py           # LSB detection and analysis
│
└── README.md                 # Documentation
```

---

## How It Works

### LSB Encoding
- Converts message → binary  
- Embeds bits into image pixels  
- Only **1 bit per channel** is changed (invisible to human eyes)

### LSB Decoding
- Reads LSBs from modified pixels  
- Rebuilds the binary → converts to text

### LSB Detection Logic
The detector analyzes image LSB patterns:

**1. Bit Plane Visualization**  
Shows the last bit of each pixel as a black/white image —  
if it looks *too random*, the image likely contains hidden data.

**2. Statistical Tests**
- Chi-square randomness test  
- Pixel intensity anomalies  
- LSB uniformity evaluation  

**3. Confidence Score**
The app outputs:
```
Probability of Steganography: 0% - 100%
```
---

##  Contributing
Pull requests and feature suggestions are welcome!

---

## License
MIT License

---

## 👨‍💻 Author
**Muhammad Hussnain Raza**  
FAST NUCES Lahore  
BSSE — 2022
