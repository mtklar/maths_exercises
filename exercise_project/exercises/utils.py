from pdf2image import convert_from_path


def convert_pdf_to_png(pdf_path, dest):
    image = convert_from_path(pdf_path)
    image[0].save(dest, "PNG")
