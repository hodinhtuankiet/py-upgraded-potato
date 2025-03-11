import zipfile

def compress_file(file_name, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_name)

# Nhập tên tệp và tên tệp nén
file_name = input("Enter the file name to compress: ")
zip_name = input("Enter the name for the compressed file: ")

# Nén tệp
compress_file(file_name, zip_name)
print(f"The file '{file_name}' has been compressed into '{zip_name}'.")
