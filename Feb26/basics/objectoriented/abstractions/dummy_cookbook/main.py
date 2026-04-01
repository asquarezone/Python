from base import RecipeBase
from concrete import Avakai, Tea

class CookBook:
    def __init__(self):
        self.recipes: list[RecipeBase] = []

    def add_recipe(self, recipe:RecipeBase):
        self.recipes.append(recipe)

    def show_recipe(self, index: int):
        self.recipes[index].show_ingridents()
        self.recipes[index].procedure()
        



if __name__ == "__main__":
    ammama_ruchulu = CookBook()
    ammama_ruchulu.add_recipe(Tea())
    ammama_ruchulu.add_recipe(Avakai())
    ammama_ruchulu.show_recipe(1)
