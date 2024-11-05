import pymupdf4llm

def to_text(file_path):
    md_text = pymupdf4llm.to_markdown(file_path)
    return md_text