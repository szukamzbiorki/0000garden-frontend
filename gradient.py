import math

def linear_ease(t):
    return t

def ease_in(t):
    return t * t

def ease_out(t):
    return t * (2 - t)

def ease_in_out(t):
    return (t ** 3) * (4 - 3 * t)  # stronger ease-in-out effect
    # return t * t * (3 - 2 * t)

def generate_css_keyframes(steps, x, easing_function="ease-in-out"):
    easing_functions = {
        "linear": linear_ease,
        "ease-in": ease_in,
        "ease-out": ease_out,
        "ease-in-out": ease_in_out,
    }

    ease_func = easing_functions.get(easing_function, linear_ease)

    css_code = ""
    for i in range(steps + 1):
        t = i / steps  
        eased_t = ease_func(t) 
        
        gradient_start = round(-x + eased_t * (100 + x), 12)
        gradient_end = round(eased_t * (100 + x), 12)

        css_code += f"""
    {round(t * 100, 5)}% {{
        mask-image: linear-gradient(0, #00000000 {gradient_start}%, #000000ff {gradient_end}%);
    }}
    """

    return css_code

steps = 50           
x = 50             
easing_function = "ease-in-out"  
css = generate_css_keyframes(steps, x, easing_function)
print(css)