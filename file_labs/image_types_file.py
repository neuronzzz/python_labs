import io

from PIL import Image

with open('1.png', 'rb') as f:
    print(f.read(20))

image = Image.open('1.png')

print(image.tobytes()[:20])

bytes_io = io.BytesIO()

image.save(bytes_io, 'png')

print(bytes_io.getvalue())

