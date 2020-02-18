import zipfile

input_file = 'txt.txt'
output_zip = 'txt.zip'

jungle_zip = zipfile.ZipFile(output_zip, 'w')
jungle_zip.write(input_file, compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()