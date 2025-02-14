File = input("File name:").strip()

if File.endswith(".gif"):
    print("Image.gif")
elif File.endswith(".jpg"):
    print("Image.jpg")
elif File.endswith(".jpeg"):
    print("Image/jpeg")
elif File.endswith(".pdf"):
    print("Document/pdf")
elif File.endswith(".txt"):
    print("text/plain")
elif File.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
