class Quadrant:
    def __init__(self, left_quadrant=None, right_quadrant=None):
        self.is_cleaned = True
        self.left_quadrant = left_quadrant
        self.right_quadrant = right_quadrant

    def set_left_quadrant(self, left_quadrant):
        self.left_quadrant = left_quadrant

    def set_right_quadrant(self, right_quadrant):
        self.right_quadrant = right_quadrant

    def clean(self):
        self.is_cleaned = True

    def dirty(self):
        self.is_cleaned = False

    def is_cleaned(self):
        return self.is_cleaned

