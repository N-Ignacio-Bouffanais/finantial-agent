from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFPlumberLoader
import os

pdf_directory = os.path.join('../pdf/')
def process_pdf(uploaded_file):

  pdf_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pdf'))
  os.makedirs(pdf_directory, exist_ok=True)

  file_path = os.path.join(pdf_directory, uploaded_file.name)

  with open(file_path, 'wb') as f:
      f.write(uploaded_file.getbuffer())

      loader = PDFPlumberLoader(file_path)
      documents = loader.load()
      text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 200, add_start_index=True)
      return text_splitter.split_documents(documents)
    