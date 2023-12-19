import tkinter as tk
from tkinter import filedialog
import fitz

def split_pdf_to_a4(input_pdf, output_pdf):
    # （前のスクリプトと同じ関数をここにコピー）

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def split_pdf():
    input_pdf = file_entry.get()
    output_pdf = output_entry.get()
    if input_pdf and output_pdf:
        split_pdf_to_a4(input_pdf, output_pdf)
        status_label.config(text="変換完了: " + output_pdf)
    else:
        status_label.config(text="エラー: ファイル名を入力してください")

# GUIの設定
root = tk.Tk()
root.title("PDF Splitter")

# ファイル選択エントリ
file_entry = tk.Entry(root, width=40)
file_entry.pack()
open_button = tk.Button(root, text="ファイルを選択", command=open_file_dialog)
open_button.pack()

# 出力ファイル名エントリ
output_entry = tk.Entry(root, width=40)
output_entry.pack()
output_label = tk.Label(root, text="出力ファイル名:")
output_label.pack()

# 分割ボタン
split_button = tk.Button(root, text="PDFを分割", command=split_pdf)
split_button.pack()

# ステータスラベル
status_label = tk.Label(root, text="")
status_label.pack()

# GUIを開始
root.mainloop()
