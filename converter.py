from docx2pdf import convert
import os

def convert_docx_to_pdf(docx_path, output_path=None):
    """
    Converts a .docx file to .pdf
    
    :param docx_path: Path of the input .docx file
    :param output_path: Optional output folder
    """
    
    if not docx_path.endswith(".docx"):
        raise ValueError("Input file must be a .docx file")

    if not os.path.exists(docx_path):
        raise FileNotFoundError("File does not exist")

    try:
        if output_path:
            convert(docx_path, output_path)
        else:
            convert(docx_path)

        print("✅ Conversion completed successfully")

    except Exception as e:
        print("❌ Error during conversion:", e)
if __name__ == "__main__":
    convert_docx_to_pdf("sample.docx")
