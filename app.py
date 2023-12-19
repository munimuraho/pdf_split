import streamlit as st
import fitz
import os
from io import BytesIO

def split_pdf_to_a4(input_pdf):
    # A4サイズの寸法 (ポイント単位)
    a4_width, a4_height = fitz.paper_size('a4')

    # メモリ内でPDFを操作
    doc = fitz.open(stream=input_pdf, filetype="pdf")
    new_doc = fitz.open()

    for page in doc:
        rect = page.rect
        for y in range(int(rect.height / a4_height) + 1):
            subrect = fitz.Rect(0, y * a4_height, a4_width, (y + 1) * a4_height)
            new_page = new_doc.new_page(width=a4_width, height=a4_height)
            new_page.show_pdf_page(new_page.rect, doc, page.number, clip=subrect)

    # バイトストリームとしてPDFを保存
    output_stream = BytesIO()
    new_doc.save(output_stream)
    output_stream.seek(0)

    # ドキュメントを閉じる
    doc.close()
    new_doc.close()

    return output_stream

# Streamlitのウェブページ設定
st.title('PDF Splitter')
st.write('縦長のPDFをA4サイズに分割します。')

uploaded_file = st.file_uploader("PDFファイルをアップロードしてください", type="pdf")
if uploaded_file is not None:
    output_pdf = split_pdf_to_a4(uploaded_file)
    st.download_button(
        label="分割されたPDFをダウンロード",
        data=output_pdf,
        file_name="split_output.pdf",
        mime="application/octet-stream"
    )
