from PIL import Image

#opening the reference image
reference_name = "mustache_small"
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
index = 0
for pixel in reference:
    # figuring out what line of the image we are on (we are only going to do every other vertical line)
    line = index % reference_size[0]
    if line % 2 == 0:
        if index % reference_size[0] == 0:
            output += "\n"
        else:
            shade = pixel[0]
            output += ascii_sorted[round(shade/3.643)-1]
            
    index += 1

# writing the output to a text file
with open(f"output_{reference_name}.txt","w") as f:
    f.write(output)

