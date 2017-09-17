def num_add(a,b):
    return a+b

def num_sub(a,b):
    return a-b

def num_mul(a,b):
    return a*b

def num_div(a,b):
    return a/b

def num_floor(a,b):
    return a//b

def num_rem(a,b):
    return a%b

def ingredient_exists(ingr, dict):
    if dict.has_key(ingr):
        return True

# def fatten_pancakes(dict):


IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {"flour" : 2, "eggs" : 4, "milk" : 200, "butter": False, "salt": 0.001}
