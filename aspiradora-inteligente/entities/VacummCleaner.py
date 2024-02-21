class VacummCleaner:
    def __init__(self, current_quadrant):
        self.mode = 1                               # 0 - dumb    //  1 - smart
        self.current_quadrant = current_quadrant

    def set_mode(self, mode):
        self.mode = mode

    def smart_cleaning(self):
        if not self.current_quadrant.is_cleaned:
            self.current_quadrant.clean()
            if self.current_quadrant.left_quadrant is not None:
                print("Cuadrante 2 limpiado")
            else:
                print("Cuadrante 1 limpiado")

        if self.current_quadrant.right_quadrant is not None and not self.current_quadrant.right_quadrant.is_cleaned:
            self.current_quadrant = self.current_quadrant.right_quadrant
            print("La aspiradora se ha movido al cuadrante 2")
            self.current_quadrant.clean()
            print("Cuadrante 2 limpiado")

        if self.current_quadrant.left_quadrant is not None and not self.current_quadrant.left_quadrant.is_cleaned:
            self.current_quadrant = self.current_quadrant.left_quadrant
            print("La aspiradora se ha movido al cuadrante 1")
            self.current_quadrant.clean()
            print("Cuadrante 1 limpiado")



    def dumb_cleaning(self):
        if self.current_quadrant.left_quadrant is not None:
            self.current_quadrant = self.current_quadrant.left_quadrant
            print("La aspiradora se ha movido al cuadrante 1")
            if not self.current_quadrant.is_cleaned:
                self.current_quadrant.clean()
                print("Cuadrante 1 limpiado")

        elif self.current_quadrant.right_quadrant is not None:
            self.current_quadrant = self.current_quadrant.right_quadrant
            print("La aspiradora se ha movido al cuadrante 2")
            if not self.current_quadrant.is_cleaned:
                self.current_quadrant.clean()
                print("Cuadrante 2 limpiado")

    def clear(self):
        if self.mode == 0:
            self.dumb_cleaning()
        else:
            self.smart_cleaning()