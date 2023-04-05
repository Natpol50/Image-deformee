class Faudio_lite:
    """
    Version lite (ayant toutes les commandes inutiles pour Fimg retirée) de la classe Faudio qui peux être trouvée dans https://github.com/Natpol50/Musique-deformee
    """
    def __init__(self,notes):
        self.res = len(notes)
        self.file =  {}
        count = 1
        for i in range(0, self.res):
            self.file[f"{count}/{self.res}"] = notes[i]
            count += 1
    
    def value(self, pos, res):
        pos = 2*pos-1
        res_2 = 2*res
        for i in range(0, self.res):
            if (i+1)/self.res < pos/res_2:
                True
            elif (i+1)/self.res > pos/res_2:
                return self.file[f"{(i+1)}/{self.res}"]
            elif (i+1)/self.res == pos/res_2:
                return 0
    
    def changement_de_resolution(self, m):
        self.new = {}
        count2 = 1
        for i in range(0, m):
            self.new[f"{count2}/{m}"] = self.value(count2, m)
            count2 += 1
        self.file = self.new
        self.res = m


class Fimg:
    """
    Classe python représentant une image dans le cadre de l'édition 2023 du TFJM²

    Pour créer une nouvelle image, il faut faire comme ceci : 

>>> i = Fimg([[1,2,3],[4,5,6],[7,8,9]])

    Pour afficher la résolution d'un image, il faut faire comme ceci :
    
>>> i.show_resolution()

3 x 3

    Pour afficher une image, il faut faire comme ceci : 

>>>i.show()

1 2 3
4 5 6
7 8 9

    Pour changer la résolution d'un image, il faut faire comme ceci : 
    
>>> i.scale(2,2)


"""
    
    def __init__(self, img):
        self.img = img
        self.height = len(img)
        self.width = len(img[0])
        
    def rotation(self,lst):
        n = len(lst)
        m = len(lst[0])
        rtd_lst = [[0 for j in range(n)] for i in range(m)]
        for i in range(n):
            for j in range(m):
                rtd_lst[m-j-1][i] = lst[i][j]
        return rtd_lst
    
    def scale(self, new_height, new_width):
        for i in range (0,len(self.img)):
            f = Faudio_lite(self.img[i])
            f.changement_de_resolution(new_width)
            j = []
            for val in f.file.values():
                j.append(val)
                self.img[i] = j
        self.img = self.rotation(self.img)
        for i in range (0,len(self.img)):
            f = Faudio_lite(self.img[i])
            f.changement_de_resolution(new_height)
            j = []
            for val in f.file.values():
                j.append(val)
                self.img[i] = j
            
        
    def show(self):
        for row in self.img:
            for pixel in row:
                print(pixel, end=' ')
            print()

    def show_resolution(self):
        print(f"{self.width}x{self.height}")

