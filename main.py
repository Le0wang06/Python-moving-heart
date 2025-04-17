import turtle
import math
import time

# List of "I love you" in different languages
languages = [
    "I love you", "Te amo", "Je t'aime", "Ich liebe dich",
    "Ti amo", "Eu te amo", "Ik hou van je", "Я тебя люблю",
    "愛してる", "사랑해", "我爱你", "أنا أحبك",
    "मैं तुमसे प्यार करता हूँ", "Seni seviyorum", "Σ' αγαπώ",
    "Jag älskar dig", "Jeg elsker deg", "Kocham Cię",
    "Te iubesc", "Volim te", "Mahal kita", "Nakupenda",
    "Aloha wau iā ʻoe", "T'estimo", "Szeretlek"
]

def draw_heart():
    # Set up screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Multilingual Love Heart")
    screen.setup(800, 600)
    
    # Create and set up the turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    screen.tracer(0)
    
    # Pink color gradient
    colors = [
        "#FF69B4",  # Hot Pink
        "#FFB6C1",  # Light Pink
        "#FFC0CB",  # Pink
        "#FFCCD5"   # Soft Pink
    ]
    
    def draw_text_heart(angle):
        pen.clear()
        
        # Calculate points around a heart shape
        for i in range(len(languages)):
            # Calculate position on heart curve
            t = (i * 2 * math.pi / len(languages)) + math.radians(angle)
            
            # Heart curve equations
            x = 16 * math.sin(t) ** 3
            y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
            
            # Scale the heart
            x *= 10
            y *= 10
            
            # Position and write text
            pen.up()
            pen.goto(x, y)
            pen.color(colors[i % len(colors)])
            
            # Rotate text to follow heart curve
            angle_to_center = math.degrees(math.atan2(y, x))
            pen.setheading(angle_to_center)
            
            # Write the text
            pen.write(languages[i], align="center", font=("Arial", 12, "normal"))
    
    # Animation loop
    angle = 0
    try:
        while True:
            draw_text_heart(angle)
            screen.update()
            angle += 0.5
            time.sleep(0.02)
            
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    draw_heart()
