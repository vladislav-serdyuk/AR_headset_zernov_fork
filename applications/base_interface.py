from PIL import Image, ImageDraw, ImageFont
from dataclasses import dataclass, field

@dataclass
class right_panel():
    """Тип данных объект интерфейса"""
    active: bool = None # Shows object on next draw
    size: int = (90, 400)
    destination: int = (1100, 500)
    button_timer: int = 0
    def check_in_region(self, top_left, bottom_right, point):
        if (point[1] > top_left[1] and point[1] < bottom_right[1] and point[0] > top_left[0] and point[0] < bottom_right[0]): # Check if point coordinates inside the region
            return True
        else:
            return False
    
    def __init__(self, active):
        self.active = active
        self.image = Image.new('RGBA', self.size, (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rounded_rectangle(((0, 0), self.size), 20, fill=(255,255,255,200))

        self.draw.rounded_rectangle(((10, 10), (80, 80)), 15, fill=(120,120,120,230))
        self.draw.ellipse([(20, 25), (30, 35)], fill=(60,60,60,10), width=10)
        self.draw.ellipse([(40, 25), (50, 35)], fill=(60,60,60,10), width=10)
        self.draw.ellipse([(60, 25), (70, 35)], fill=(60,60,60,10), width=10)
        self.draw.ellipse([(30, 40), (40, 50)], fill=(60,60,60,10), width=10)
        self.draw.ellipse([(50, 40), (60, 50)], fill=(60,60,60,10), width=10)
        self.draw.text((18, 55),"Меню",(60,60,60,10),font=ImageFont.truetype("applications/resources/sans-serif.ttf", 20))

        self.draw.rounded_rectangle(((10, 100), (80, 180)), 15, fill=(120,120,120,230))
        gear_image = Image.open('applications/resources/gear_icon.png')
        self.image.paste(gear_image, (14, 103), gear_image)
        self.draw.text((23, 165),"Настрой",(60,60,60,10),font=ImageFont.truetype("applications/resources/sans-serif.ttf", 12))

        self.draw.rounded_rectangle(((10, 200), (80, 280)), 15, fill=(120,120,120,230))

        self.draw.rounded_rectangle(((10, 300), (80, 380)), 15, fill=(120,120,120,230))
        self.draw.line(((20,310), (70,360)), fill=(60,60,60,10), width=5)
        self.draw.line(((70,310), (20,360)), fill=(60,60,60,10), width=5)
        self.draw.text((23, 360),"Выход",(60,60,60,10),font=ImageFont.truetype("applications/resources/sans-serif.ttf", 15))
        pass
        
    def main(self):

        return self.image
    def controller (self, coordinates): # Здесь пишем что исполняется по нажатию на кнопку. При этом coordinates - координата указательного пальца НА ПОЛОТНЕ ОБЪЕКТА (self.size)
        if (self.check_in_region([10,10], [80,80], coordinates)):
            if (self.button_timer > 7):
                self.button_timer = 0
                self.active = False
                return "run_appspanel"
            else:
                self.button_timer += 1
        elif (self.check_in_region((10, 100), (80, 180), coordinates)):
            if (self.button_timer > 7):
                self.button_timer = 0
                self.active = False
                return "run_settings"
            else:
                self.button_timer += 1
        elif (self.check_in_region((10, 300), (80, 380), coordinates)):
            if (self.button_timer > 7):
                self.button_timer = 0
                self.active = False
                return "exit"
            else:
                self.button_timer += 1
        else:
            if (self.button_timer > 1): self.button_timer -= 2
        return "nothing"