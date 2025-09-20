# 📝 Text Analysis Tool

Ứng dụng web phân tích văn bản sử dụng NLTK và SpaCy để thực hiện Tokenization, POS Tagging và Named Entity Recognition.

## 🚀 Tính năng

- **Tokenization**: Tách văn bản thành các tokens sử dụng NLTK và SpaCy
- **Part-of-Speech Tagging**: Gắn nhãn từ loại cho mỗi token
- **Named Entity Recognition**: Nhận dạng các thực thể có tên (Person, Organization, Location, etc.)
- **Giao diện web thân thiện**: Sử dụng Streamlit để tạo giao diện trực quan
- **Thống kê văn bản**: Hiển thị các thống kê cơ bản về văn bản
- **Visualization**: Biểu đồ phân bố các loại entity

## 📋 Yêu cầu hệ thống

- Conda hoặc Miniconda
- Python 3.9+

## 🛠️ Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd Text-Analysis-Tool
```

### 2. Tạo conda environment
```bash
conda env create -f environment.yml
```

### 3. Kích hoạt environment
```bash
conda activate text-analysis-tool
```

### 4. Tải SpaCy model
```bash
python -m spacy download en_core_web_sm
```

## 🎯 Cách sử dụng

### Chạy ứng dụng
```bash
conda activate text-analysis-tool
streamlit run app.py
```

Ứng dụng sẽ mở trong trình duyệt tại địa chỉ `http://localhost:8501`

### Sử dụng ứng dụng

1. **Nhập văn bản**: Nhập văn bản cần phân tích vào ô text area bên trái
2. **Chọn phương pháp**: Chọn sử dụng NLTK, SpaCy hoặc cả hai
3. **Phân tích**: Nhấn nút "Phân tích văn bản" để xem kết quả

## 📊 Kết quả phân tích

### Tokenization
- Hiển thị danh sách các tokens được tách từ văn bản
- Số lượng tokens

### POS Tagging
- Bảng hiển thị từng token với nhãn từ loại tương ứng
- Giải thích ý nghĩa của các nhãn POS

### Named Entity Recognition
- Danh sách các entities được nhận dạng
- Phân loại entities (PERSON, ORG, LOC, DATE, etc.)
- Highlight entities trong văn bản gốc
- Biểu đồ phân bố các loại entity

### Thống kê văn bản
- Số ký tự
- Số từ
- Số câu
- Số entities

## 🔧 Cấu trúc dự án

```
Text-Analysis-Tool/
├── app.py                 # Ứng dụng Streamlit chính
├── environment.yml        # Conda environment file
└── README.md             # File hướng dẫn này
```

## 📚 Thư viện sử dụng

- **Streamlit**: Framework web app
- **SpaCy**: Thư viện NLP hiện đại
- **NLTK**: Natural Language Toolkit
- **Pandas**: Xử lý dữ liệu
- **Plotly**: Tạo biểu đồ tương tác

## 🎨 Giao diện

Ứng dụng có giao diện thân thiện với:
- Sidebar để nhập văn bản và tùy chọn
- Layout 2 cột để hiển thị kết quả
- Bảng dữ liệu có thể sắp xếp
- Biểu đồ trực quan
- Highlight entities trong văn bản

## 📝 Ví dụ sử dụng

**Văn bản mẫu:**
```
Apple Inc. was founded by Steve Jobs in California on April 1, 1976. 
The company is now worth over $3 trillion.
```

**Kết quả:**
- **Tokens**: ["Apple", "Inc.", "was", "founded", ...]
- **POS Tags**: [("Apple", "NNP"), ("Inc.", "NNP"), ("was", "VBD"), ...]
- **Entities**: 
  - Apple Inc. → ORG
  - Steve Jobs → PERSON
  - California → GPE
  - April 1, 1976 → DATE
  - $3 trillion → MONEY

## 🐛 Xử lý lỗi

Nếu gặp lỗi "SpaCy English model not found":
```bash
python -m spacy download en_core_web_sm
```

Nếu gặp lỗi với NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
```

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📄 License

Dự án này được phát hành dưới MIT License.

## 👨‍💻 Tác giả

Text Analysis Tool - Dự án học tập NLP
