class Fimg:
    def __init__(self, img):
        self.img = img
        self.height = len(img)
        self.width = len(img[0])

    def scale(self, new_height, new_width):
        new_img = []
        for i in range(new_height):
            row = []
            for j in range(new_width):
                # trouver les coordonnées du pixel correspondant dans l'image originale
                x = int((j + 0.5) * self.width / new_width)
                y = int((i + 0.5) * self.height / new_height)
                if x >= self.width - 1 or y >= self.height - 1:
                    row.append(0)
                else:
                    # vérifier si le pixel est situé exactement entre deux pixels dans l'image originale
                    if abs((j + 0.5) * self.width / new_width - x - 0.5) < 0.001 and abs((i + 0.5) * self.height / new_height - y - 0.5) < 0.001:
                        row.append(0)
                    else:
                        # calculer la valeur du pixel dans l'image redimensionnée en interpolant les pixels adjacents
                        a = (j + 0.5) * self.width / new_width - x - 0.5
                        b = (i + 0.5) * self.height / new_height - y - 0.5
                        value = (1 - a) * (1 - b) * self.img[y][x] + a * (1 - b) * self.img[y][x + 1] + (1 - a) * b * self.img[y + 1][x] + a * b * self.img[y + 1][x + 1]
                        row.append(int(value))
            new_img.append(row)
        self.img = new_img
        self.height = new_height
        self.width = new_width
        
    def show(self):
        for row in self.img:
            for pixel in row:
                print(pixel, end=' ')
            print()

    def show_resolution(self):
        print(f"{self.width}x{self.height}")
