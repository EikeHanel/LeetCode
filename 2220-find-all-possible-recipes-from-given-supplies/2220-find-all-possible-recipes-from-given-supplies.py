class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {s: True for s in supplies} # r -> True/False
        recipe_index = {r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False    
            can_cook[r] = False

            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False

            can_cook[r] = True
            return can_cook[r]

        return [r for r in recipes if dfs(r)]
        
        # # O(n^2 * m)
        # supplies = set(supplies)
        # res = []

        # while True:
        #     for i in range(len(recipes)):
        #         can_make = False
        #         for ing in ingredients[i]:
        #             if ing not in supplies:
        #                 break
        #         else:
        #             can_make = True

        #         if can_make:
        #             new_item = recipes.pop(i)
        #             ingredients.pop(i)
        #             res.append(new_item)
        #             supplies.add(new_item)
        #             break
        #     else:
        #         break
        # return res
            
