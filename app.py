import streamlit as st
import spacy
import nltk
import pandas as pd
import plotly.express as px
from collections import Counter
import re

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load SpaCy model
@st.cache_resource
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        st.error("SpaCy English model not found. Please install it with: python -m spacy download en_core_web_sm")
        return None

def tokenize_with_nltk(text):
    """Tokenize text using NLTK"""
    tokens = nltk.word_tokenize(text)
    return tokens

def pos_tag_with_nltk(tokens):
    """Perform POS tagging using NLTK"""
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

def analyze_with_spacy(text, nlp):
    """Analyze text using SpaCy"""
    if nlp is None:
        return None, None, None
    
    doc = nlp(text)
    
    # Extract tokens
    tokens = [token.text for token in doc]
    
    # Extract POS tags
    pos_tags = [(token.text, token.pos_) for token in doc]
    
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return tokens, pos_tags, entities

def get_pos_explanation(tag):
    """Get explanation for POS tags"""
    pos_explanations = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb'
    }
    return pos_explanations.get(tag, 'Unknown')

def get_ner_explanation(label):
    """Get explanation for NER labels"""
    ner_explanations = {
        'PERSON': 'People, including fictional',
        'NORP': 'Nationalities or religious or political groups',
        'FAC': 'Buildings, airports, highways, bridges, etc.',
        'ORG': 'Companies, agencies, institutions, etc.',
        'GPE': 'Countries, cities, states',
        'LOC': 'Non-GPE locations, mountain ranges, bodies of water',
        'PRODUCT': 'Objects, vehicles, foods, etc. (not services)',
        'EVENT': 'Named hurricanes, battles, wars, sports events, etc.',
        'WORK_OF_ART': 'Titles of books, songs, etc.',
        'LAW': 'Named documents made into laws',
        'LANGUAGE': 'Any named language',
        'DATE': 'Absolute or relative dates or periods',
        'TIME': 'Times smaller than a day',
        'PERCENT': 'Percentage, including "%"',
        'MONEY': 'Monetary values, including unit',
        'QUANTITY': 'Measurements, as of weight or distance',
        'ORDINAL': '"first", "second", etc.',
        'CARDINAL': 'Numerals that do not fall under another type'
    }
    return ner_explanations.get(label, 'Unknown')

def main():
    st.set_page_config(
        page_title="Text Analysis Tool",
        page_icon="📝",
        layout="wide"
    )
    
    st.title("📝 Text Analysis Tool")
    st.markdown("Phân tích văn bản với Tokenization, POS Tagging và Named Entity Recognition")
    
    # Load SpaCy model
    nlp = load_spacy_model()
    
    # Sidebar for input
    st.sidebar.header("Nhập văn bản")
    
    # Text input
    text_input = st.sidebar.text_area(
        "Nhập văn bản cần phân tích:",
        value="Apple Inc. was founded by Steve Jobs in California on April 1, 1976. The company is now worth over $3 trillion.",
        height=200
    )
    
    # Analysis options
    st.sidebar.header("Tùy chọn phân tích")
    use_spacy = st.sidebar.checkbox("Sử dụng SpaCy (khuyến nghị)", value=True)
    use_nltk = st.sidebar.checkbox("Sử dụng NLTK", value=True)
    
    if st.sidebar.button("Phân tích văn bản", type="primary"):
        if not text_input.strip():
            st.error("Vui lòng nhập văn bản để phân tích!")
            return
        
        # Main content area
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.header("📊 Kết quả phân tích")
            
            # Tokenization
            if use_nltk:
                st.subheader("🔤 Tokenization (NLTK)")
                nltk_tokens = tokenize_with_nltk(text_input)
                st.write(f"**Số lượng tokens:** {len(nltk_tokens)}")
                st.write("**Tokens:**")
                st.write(nltk_tokens)
            
            if use_spacy and nlp:
                st.subheader("🔤 Tokenization (SpaCy)")
                spacy_tokens, _, _ = analyze_with_spacy(text_input, nlp)
                st.write(f"**Số lượng tokens:** {len(spacy_tokens)}")
                st.write("**Tokens:**")
                st.write(spacy_tokens)
        
        with col2:
            # POS Tagging
            if use_nltk:
                st.subheader("🏷️ POS Tagging (NLTK)")
                nltk_tokens = tokenize_with_nltk(text_input)
                nltk_pos = pos_tag_with_nltk(nltk_tokens)
                
                # Create DataFrame for better display
                pos_df = pd.DataFrame(nltk_pos, columns=['Token', 'POS Tag'])
                pos_df['Explanation'] = pos_df['POS Tag'].apply(get_pos_explanation)
                st.dataframe(pos_df, use_container_width=True)
            
            if use_spacy and nlp:
                st.subheader("🏷️ POS Tagging (SpaCy)")
                _, spacy_pos, _ = analyze_with_spacy(text_input, nlp)
                
                # Create DataFrame for better display
                spacy_pos_df = pd.DataFrame(spacy_pos, columns=['Token', 'POS Tag'])
                st.dataframe(spacy_pos_df, use_container_width=True)
        
        # Named Entity Recognition
        st.header("🎯 Named Entity Recognition")
        
        if use_spacy and nlp:
            _, _, entities = analyze_with_spacy(text_input, nlp)
            
            if entities:
                st.subheader("SpaCy NER Results")
                
                # Create DataFrame for entities
                entity_df = pd.DataFrame(entities, columns=['Entity', 'Label'])
                entity_df['Explanation'] = entity_df['Label'].apply(get_ner_explanation)
                
                # Display entities
                st.dataframe(entity_df, use_container_width=True)
                
                # Highlight entities in text
                st.subheader("Văn bản với entities được highlight")
                highlighted_text = text_input
                for entity, label in entities:
                    highlighted_text = highlighted_text.replace(
                        entity, 
                        f"**{entity}** ({label})"
                    )
                st.markdown(highlighted_text)
                
                # Entity statistics
                st.subheader("📈 Thống kê Entities")
                entity_counts = Counter([label for _, label in entities])
                
                if entity_counts:
                    # Create pie chart
                    fig = px.pie(
                        values=list(entity_counts.values()),
                        names=list(entity_counts.keys()),
                        title="Phân bố các loại Entity"
                    )
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Không tìm thấy entities nào trong văn bản.")
        
        # Text statistics
        st.header("📊 Thống kê văn bản")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Số ký tự", len(text_input))
        
        with col2:
            words = text_input.split()
            st.metric("Số từ", len(words))
        
        with col3:
            sentences = text_input.split('.')
            st.metric("Số câu", len([s for s in sentences if s.strip()]))
        
        with col4:
            if use_spacy and nlp:
                _, _, entities = analyze_with_spacy(text_input, nlp)
                st.metric("Số entities", len(entities))
            else:
                st.metric("Số entities", "N/A")
    
    # Footer
    st.markdown("---")
    st.markdown("**Text Analysis Tool** - Sử dụng NLTK và SpaCy để phân tích văn bản")
    
    # Instructions
    with st.expander("📖 Hướng dẫn sử dụng"):
        st.markdown("""
        ### Cách sử dụng:
        1. **Nhập văn bản** vào ô text area bên trái
        2. **Chọn phương pháp phân tích** (NLTK hoặc SpaCy)
        3. **Nhấn nút "Phân tích văn bản"**
        
        ### Các tính năng:
        - **Tokenization**: Tách văn bản thành các tokens
        - **POS Tagging**: Gắn nhãn từ loại cho mỗi token
        - **Named Entity Recognition**: Nhận dạng các thực thể có tên
        
        ### Cài đặt:
        ```bash
        pip install -r requirements.txt
        python -m spacy download en_core_web_sm
        ```
        
        ### Chạy ứng dụng:
        ```bash
        streamlit run app.py
        ```
        """)

if __name__ == "__main__":
    main()
