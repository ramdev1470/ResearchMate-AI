"""Upload Papers Page - ResearchMate AI"""

import streamlit as st
from ui.layouts import layout_header_section
from ui.theme import Icons

def render_upload_page():
    """Render upload papers page."""
    layout_header_section("Upload Research Papers", "Add and process your PDF files", Icons.UPLOAD)
    
    # Instructions
    with st.expander("📖 How to Upload", expanded=False):
        st.markdown("""
        1. **Select Files** - Choose one or more PDF files
        2. **Upload** - Click the upload button
        3. **Process** - Click 'Process Files (OpenAI)'
        4. **Wait** - Processing takes 3-5 seconds per paper
        5. **Done** - Papers are stored and indexed
        """)
    
    st.markdown("---")
    
    # File uploader
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type="pdf",
        accept_multiple_files=True,
        help="Upload one or more research papers in PDF format"
    )
    
    if uploaded_files:
        st.markdown("### 📋 Selected Files")
        
        # Display file info
        total_size = 0
        for idx, file in enumerate(uploaded_files):
            size_mb = file.size / (1024 * 1024)
            total_size += size_mb
            
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"{Icons.PDF} {file.name}")
            with col2:
                st.caption(f"{size_mb:.1f} MB")
            with col3:
                # Show if already uploaded
                existing_names = {doc.filename for doc in st.session_state.get("uploaded_documents", [])}
                if file.name in existing_names:
                    st.caption("⚠️ Already uploaded")
                else:
                    st.caption("✅ Ready")
        
        st.markdown(f"**Total Size:** {total_size:.1f} MB")
        
        st.markdown("---")
        
        # Process button
        if st.button("⚡ Process Files (OpenAI)", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                from src.pdf_loader import PDFLoader
                
                pdf_loader = PDFLoader()
                processed = 0
                skipped = 0
                
                # Build set of already-uploaded filenames for duplicate detection
                if "uploaded_documents" not in st.session_state:
                    st.session_state.uploaded_documents = []
                existing_names = {doc.filename for doc in st.session_state.uploaded_documents}
                
                for idx, file in enumerate(uploaded_files):
                    status_text.text(f"Processing {idx + 1}/{len(uploaded_files)}: {file.name}")
                    
                    # Skip duplicates
                    if file.name in existing_names:
                        skipped += 1
                        progress = (idx + 1) / len(uploaded_files)
                        progress_bar.progress(progress)
                        continue
                    
                    # Save temporarily
                    import os
                    os.makedirs("temp", exist_ok=True)
                    temp_path = os.path.join("temp", file.name)
                    with open(temp_path, "wb") as f:
                        f.write(file.getbuffer())
                    
                    # Load PDF
                    doc = pdf_loader.load(temp_path)
                    
                    # Add to session state
                    st.session_state.uploaded_documents.append(doc)
                    existing_names.add(file.name)
                    processed += 1
                    
                    # Update progress
                    progress = (idx + 1) / len(uploaded_files)
                    progress_bar.progress(progress)
                
                # Show results
                if skipped > 0:
                    status_text.text(f"✅ Processed {processed} file(s), skipped {skipped} duplicate(s)")
                    st.warning(f"⚠️ Skipped {skipped} file(s) that were already uploaded")
                else:
                    status_text.text(f"✅ Successfully processed {processed} file(s)!")
                
                if processed > 0:
                    st.success(f"✅ {processed} new file(s) processed successfully!")
                    st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    else:
        st.info("📚 Please select PDF files to upload")
    
    st.markdown("---")
    
    # Tips
    st.markdown("### 💡 Tips")
    st.markdown("""
    - **Supported Format:** PDF only
    - **File Size:** Up to 50 MB per file
    - **Multiple Files:** Upload up to 10 files at once
    - **Processing Time:** ~2-3 seconds per paper
    """)