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

class HeartAnimation:
    def __init__(self):
        # Initialize screen
        self.screen = turtle.Screen()
        self.screen.setup(1000, 800)
        self.screen.bgcolor("black")
        self.screen.title("Multilingual Love Heart")
        self.screen.tracer(0)  # Disable automatic updates
        
        # Create main turtle for drawing
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.speed(0)
        
        # Animation properties
        self.angle = 0
        self.heart_points = self.get_heart_points(10, len(languages))
        self.frame_delay = 1/60  # Target 60 FPS
        self.rotation_speed = 0.15
        
        # Color gradient for smooth transitions
        self.colors = [
            "#FF69B4", "#FF74B9", "#FF7FBE", "#FF8AC3",
            "#FF95C8", "#FFA0CD", "#FFABD2", "#FFB6D7",
            "#FFC1DC", "#FFCCE1", "#FFD7E6", "#FFE2EB",
            "#FFEDFF", "#FFE2EB", "#FFD7E6", "#FFCCE1",
            "#FFC1DC", "#FFB6D7", "#FFABD2", "#FFA0CD",
            "#FF95C8", "#FF8AC3", "#FF7FBE", "#FF74B9"
        ]
        
    def get_heart_points(self, size, num_points):
        points = []
        for i in range(num_points):
            t = i * 2 * math.pi / num_points
            x = size * 16 * math.sin(t) ** 3
            y = size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            points.append((x, y))
        return points
    
    def draw_frame(self):
        self.text.clear()
        
        # Pre-calculate rotation values
        cos_angle = math.cos(math.radians(self.angle))
        sin_angle = math.sin(math.radians(self.angle))
        
        # Draw each point
        for i, (x, y) in enumerate(self.heart_points):
            # Smooth rotation
            rotated_x = x * cos_angle - y * sin_angle
            rotated_y = x * sin_angle + y * cos_angle
            
            self.text.up()
            self.text.goto(rotated_x, rotated_y)
            
            # Get color with smooth transition
            color_index = (i + int(self.angle / 2)) % len(self.colors)
            self.text.color(self.colors[color_index])
            
            # Calculate text orientation
            point_angle = math.degrees(math.atan2(rotated_y, rotated_x))
            self.text.setheading(point_angle)
            
            # Write text
            self.text.write(languages[i], align="center", font=("Arial", 10, "normal"))
    
    def animate(self):
        try:
            last_frame_time = time.time()
            
            while True:
                current_time = time.time()
                elapsed = current_time - last_frame_time
                
                if elapsed >= self.frame_delay:
                    # Update animation
                    self.draw_frame()
                    self.screen.update()
                    
                    # Update angle
                    self.angle = (self.angle + self.rotation_speed) % 360
                    
                    # Update frame timing
                    last_frame_time = current_time
                else:
                    # Small sleep to prevent CPU overload
                    time.sleep(0.001)
                    
        except turtle.Terminator:
            pass

def main():
    animation = HeartAnimation()
    animation.animate()

if __name__ == "__main__":
    main()
