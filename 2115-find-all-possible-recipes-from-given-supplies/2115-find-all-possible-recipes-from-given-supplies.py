class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        res = []

        while True:
            for i in range(len(recipes)):
                can_make = False
                for ing in ingredients[i]:
                    if ing not in supplies:
                        break
                else:
                    can_make = True

                if can_make:
                    new_item = recipes.pop(i)
                    ingredients.pop(i)
                    res.append(new_item)
                    supplies.add(new_item)
                    break
            else:
                break
        return res
            
