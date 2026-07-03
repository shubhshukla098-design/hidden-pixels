from PIL import Image
try:
    Image_name=input("enter the name of the picture file also add extension (eg- jpg,png): ")
    img=Image.open(Image_name)
    Secret_message = input("Enter the secret message you want to hide: ")
    Secret_message=Secret_message+"#"
    l = len(Secret_message)
    binary_form = []
    for letter in Secret_message:
        ASCII_value = ord(letter)
        Binary_value = format(ASCII_value, '08b')
        for i in Binary_value:
            binary_form.append(i)

    img = img.convert("RGB")
    pixel=img.load()
    y,x=img.size
    bit_index=0
    for i in range(0,y):
        for j in range(0,x):
            (r,g,b)=pixel[i,j]
            Binary_r=""
            Binary_b=""
            Binary_g=""
            if bit_index<len(binary_form)and(bit_index+1 < len(binary_form))and(bit_index+2 < len(binary_form)):
                Binary_r=format(r,'08b')
                Binary_g=format(g,'08b')
                Binary_b=format(b,'08b')
                new_red_bin=Binary_r[:-1] + binary_form[bit_index]
                bit_index+=1
                new_green_bin=Binary_g[:-1] + binary_form[bit_index]
                bit_index += 1
                new_blue_bin=Binary_b[:-1] + binary_form[bit_index]
                bit_index += 1
                new_red=int(new_red_bin,2)
                new_green=int(new_green_bin,2)
                new_blue=int(new_blue_bin,2)
                pixel[i,j]=(new_red,new_green,new_blue)
            elif (bit_index<len(binary_form))and(bit_index+1 < len(binary_form)) :
                Binary_r = format(r, '08b')
                Binary_g = format(g, '08b')
                new_red_bin = Binary_r[:-1] + binary_form[bit_index]
                bit_index += 1
                new_green_bin = Binary_g[:-1] + binary_form[bit_index]
                bit_index += 1
                new_red = int(new_red_bin, 2)
                new_green = int(new_green_bin, 2)
                new_blue=b
                pixel[i, j] = (new_red, new_green, new_blue)
            elif bit_index<len(binary_form) :
                Binary_r = format(r, '08b')
                new_red_bin = Binary_r[:-1] + binary_form[bit_index]
                bit_index += 1
                new_red = int(new_red_bin, 2)
                new_green=g
                new_blue=b
                pixel[i, j] = (new_red, new_green, new_blue)
            else:
                new_red=r
                new_green=g
                new_blue=b
                pixel[i,j]=(new_red,new_green,new_blue)
    output_name=input("Enter the name of the output file: ")
    img.save(output_name+".png")

except FileNotFoundError:
    print("Error file not found please check weather the file exit or not.")
    print("please ensure that the file is in the same folder in which the script is.")

