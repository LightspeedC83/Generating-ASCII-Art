from PIL import Image

#opening the reference image
reference_name = "pheonix_cleaned_small"
reference_path = f"reference_images/{reference_name}.jpg"

reference_image = Image.open(reference_path)
reference_pixels = list(reference_image.getdata())
reference_size = reference_image.size # getting the refence image's size in (x-pixles,y-pixels) format


# making a greyscale version of the reference image
reference = []
for p in reference_pixels:
    avg = (p[0]+p[1]+p[2])/3
    reference.append((avg,avg,avg))

# defining the ascii characters that correspond to certain 'levels of grey' going from black --> white
raw = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
ascii_sorted = [x for x in raw]

output = """"""
output = ""
for y in range(reference_size[1]):
    if y % 2 == 0:
        continue
    for x in range(reference_size[0]):
        pixel = reference[reference_size[0]*y + x][0]
        output += ascii_sorted[round(pixel / 3.643) - 1]
    output += "\n"

# writing the output to a text file
with open(f"outputs/output_{reference_name}.txt","w") as f:
    f.write(output)

