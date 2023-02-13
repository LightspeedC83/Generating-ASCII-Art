from PIL import Image

#opening the reference image
reference = "mustache.jpg"
reference_path = f"reference_images/{reference}"

reference_image = Image.open(reference_path)
reference_pixels = list(reference_image.getdata())
reference_size = reference_image.size # getting the refence image's size in (x-pixles,y-pixels) format


# making a greyscale version of the reference image
reference_greyscale = []
for p in reference_pixels:
    avg = (p[0]+p[1]+p[2])/3
    reference_greyscale.append((avg,avg,avg))

# defining the ascii characters that correspond to certain 'levels of grey' going from white --> black
raw = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
ascii_sorted = [x for x in raw[::-1]]

