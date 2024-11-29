from PIL import Image, ImageDraw, ImageFont

# Open an image
image = Image.open("example.jpg")

# Resize image
image_resized = image.resize((300, 300))
image_resized.save("resized_example.jpg")

# Crop image
image_cropped = image.crop((100, 100, 400, 400))
image_cropped.save("cropped_example.jpg")

# Draw text on an image
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Hello, World!", font=font, fill="white")
image.save("text_image.jpg")

# Rotate the image
image_rotated = image.rotate(90)
image_rotated.save("rotated_example.jpg")