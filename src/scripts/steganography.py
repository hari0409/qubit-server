from PIL import Image

def encode(image_path, message,folder_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(c), '08b') for c in message) # Convert the message to binary
    if len(binary_message) > img.size[0]*img.size[1]*3: # Check if the message is too long to fit in the image
        return "Error: Message is too long to fit in the image"
    pixels = img.load()
    message_index = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            if message_index < len(binary_message):
                r = (r & 254) | int(binary_message[message_index])
                message_index += 1
            if message_index < len(binary_message):
                g = (g & 254) | int(binary_message[message_index])
                message_index += 1
            if message_index < len(binary_message):
                b = (b & 254) | int(binary_message[message_index])
                message_index += 1
            pixels[i, j] = (r, g, b)
            if message_index >= len(binary_message):
                break
        if message_index >= len(binary_message):
            break
    img.save(folder_path+'/encoded_image.png')
