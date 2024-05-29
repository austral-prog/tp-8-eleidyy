# sets_categories_data.py
ALCOHOLS = {
    'vodka', 'gin', 'rum', 'tequila', 'whiskey', 'bourbon', 'scotch', 'brandy', 
    'cognac', 'liqueur', 'vermouth', 'triple sec', 'absinthe', 'schnapps', 'wine', 
    'beer', 'champagne', 'sake'
}

# main script
from sets_categories_data import ALCOHOLS

# 2.1. Limpiar los ingredientes repetidos del plato
def clean_ingredients(dish_name, ingredients):
    unique_ingredients = set(ingredients)
    return (dish_name, unique_ingredients)

# 2.2. Clasificar Cócteles y Mocktails
def check_drinks(drink_name, ingredients):
    for ingredient in ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"

# Ejemplos de uso
print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))
# Debería imprimir: ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})

print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
# Debería imprimir: 'Honeydew Cucumber Mocktail'

print(check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']))
# Debería imprimir: 'Shirley Tonic Cocktail'
