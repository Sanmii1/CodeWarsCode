# Fungsi bikin tangga denga huruf I
def draw_stairs(n):
    text = ""
    stairs = "I\n"
    space = " "
    for i in range(n) :
        text += space*i + stairs

    return text[:-1]
