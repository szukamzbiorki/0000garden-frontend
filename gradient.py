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

def cubic_bezier_squeezed(t, p1x=0.37, p1y=0, p2x=1, p2y=0.35):
    # Simulates a squeezed cubic-bezier by adjusting control points
    return 3 * (1 - t) ** 2 * t * p1y + 3 * (1 - t) * t ** 2 * p2y + t ** 3

def generate_css_keyframes(steps, x, easing_function="cubic-bezier-squeezed"):
    easing_functions = {
        "linear": linear_ease,
        "ease-in": ease_in,
        "ease-out": ease_out,
        "ease-in-out": ease_in_out,
        "cubic-bezier-squeezed": cubic_bezier_squeezed,
    }

    ease_func = easing_functions.get(easing_function, linear_ease)

    css_code = ""
    for i in range(steps + 1):
        t = i / steps  
        eased_t = ease_func(t) 

        calculated = eased_t * (100 + x)
        
        gradient_start = round(-x + calculated, 12)
        gradient_end = round(calculated, 12)

        css_code += f"""
    {round(t * 100, 5)}% {{
        mask-image: linear-gradient(0, #00000000 {gradient_start}%, #000000ff {gradient_end}%);
    }}
    """

    return css_code

steps = 50           
x = 50             
easing_function = "cubic-bezier-squeezed"  
css = generate_css_keyframes(steps, x, easing_function)

with open("generated_css_keyframes.txt", "w") as file:
    file.write(css)

print("CSS keyframes have been saved to generated_css_keyframes.txt")