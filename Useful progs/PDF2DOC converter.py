from pdf2docx import Converter
from docx import Document

def convert_pdf_to_doc(pdf_file, doc_file):
    # Конвертация PDF в DOCX
    cv = Converter(pdf_file)
    cv.convert(doc_file, start=0, end=None)
    cv.close()

    # Преобразование DOCX в DOC
    docx_file = doc_file.replace('.doc', '.docx')
    doc = Document(docx_file)
    doc.save(doc_file)

    # Удаление временного файла DOCX
    import os
    os.remove(docx_file)

if __name__ == "__main__":
    pdf_file = r"C:\Users\endovitskiy.a\Downloads\Delete\PDF2DOC\PDF\1.pdf"  # Путь к вашему PDF файлу
    doc_file = r'C:\Users\endovitskiy.a\Downloads\Delete\PDF2DOC\DOC\DOC.doc' # Имя файла DOC, в который будет сохранен результат
    convert_pdf_to_doc(pdf_file, doc_file)
    print("Конвертация завершена.")
