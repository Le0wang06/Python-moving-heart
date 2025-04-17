import turtle
import math
import time

# Extended list of "I love you" in different languages
languages = [
    "I love you", "Te amo", "Je t'aime", "Ich liebe dich", "Ti amo",
    "Eu te amo", "Ik hou van je", "Я тебя люблю", "愛してる", "사랑해",
    "我爱你", "أنا أحبك", "मैं तुमसे प्यार करता हूँ", "Seni seviyorum", "Σ' αγαπώ",
    "Jag älskar dig", "Jeg elsker deg", "Kocham Cię", "Te iubesc", "Volim te",
    "Mahal kita", "Nakupenda", "Aloha wau iā ʻoe", "Mən səni sevirəm", "T'estimo",
    "Szeretlek", "Miluji tě", "Ես քեզ սիրում եմ", "Мен сені сүйемін", "Мін цябе кахаю",
    "Tá grá agam duit", "Tha gaol agam ort", "Rwy'n dy garu di", "אני אוהב אותך", "دوستت دارم",
    "ฉันรักคุณ", "Tôi yêu bạn", "Saya cinta padamu", "እወድሃለሁ", "Ndiyakuthanda",
    "Mo ni fe", "Mina rakastan sinua", "Es mīlu tevi", "Aš tave myliu", "Të dua",
    "Volim te", "Ek het jou lief", "Ndinokuda", "Ngikhuthanda", "Ngiyakuthanda"
]

def create_heart_text():
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(1000, 800)
    screen.bgcolor("black")
    screen.title("Multilingual Love Heart")
    screen.tracer(0)  # Disable automatic updates
    
    # Create and configure the turtle
    text = turtle.Turtle()
    text.hideturtle()
    text.speed(0)
    
    # Pre-calculate heart points
    def get_heart_points(size, num_points):
        points = []
        for i in range(num_points):
            t = i * 2 * math.pi / num_points
            x = size * 16 * math.sin(t) ** 3
            y = size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            points.append((x, y))
        return points
    
    # Define colors with smooth gradient
    colors = [
        "#FF1493", "#FF69B4", "#FFB6C1", "#FFC0CB",
        "#FFD7E4", "#FFE4E1", "#FFFFFF", "#FFE4E1",
        "#FFD7E4", "#FFC0CB", "#FFB6C1", "#FF69B4"
    ]
    
    def draw_rotating_heart(angle, heart_points):
        text.clear()
        
        # Pre-calculate rotation values
        cos_angle = math.cos(math.radians(angle))
        sin_angle = math.sin(math.radians(angle))
        
        for i, (x, y) in enumerate(heart_points):
            # Rotate point with smooth interpolation
            rotated_x = x * cos_angle - y * sin_angle
            rotated_y = x * sin_angle + y * cos_angle
            
            text.up()
            text.goto(rotated_x, rotated_y)
            
            # Smooth color transition
            color_index = (i + int(angle / 15)) % len(colors)
            text.color(colors[color_index])
            
            # Calculate text angle for smooth orientation
            point_angle = math.degrees(math.atan2(rotated_y, rotated_x))
            text.setheading(point_angle)
            
            # Write text with anti-aliasing effect
            text.write(languages[i], align="center", font=("Arial", 10, "normal"))
    
    # Pre-calculate heart points with more density
    heart_points = get_heart_points(10, len(languages))
    angle = 0
    
    try:
        while True:
            draw_rotating_heart(angle, heart_points)
            screen.update()
            
            # Adjusted rotation speed and frame timing
            angle += 0.15  # Slightly faster rotation
            
            if angle >= 360:
                angle = 0
            
            # Shorter delay for higher frame rate
            time.sleep(0.02)  # Increased frame rate (50 FPS)
            
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    create_heart_text()
