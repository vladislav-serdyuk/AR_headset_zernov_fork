from PIL import Image, ImageDraw, ImageFont
from dataclasses import dataclass

sans_font = ImageFont.truetype("applications/resources/sans-serif.ttf", 20)


@dataclass
class pane:
    """Тип данных объект интерфейса"""
    active: bool = None  # Shows object on next draw
    size: tuple[int, int] = (640, 380)
    destination: tuple[int, int] = (500, 500)
    button_timer: int = 0
    selected_menu: int = 1  # nothing
    message_text: str = "Выберите меню."

    @staticmethod
    def check_in_region(top_left, bottom_right, point):
        if top_left[1] < point[1] < bottom_right[1] and top_left[0] < point[0] < bottom_right[0]:
            # Check if point coordinates inside the region
            return True
        else:
            return False

    def main(self, config):
        self.image = Image.new('RGBA', self.size, (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rounded_rectangle(((0, 0), (640, 310)), 20, fill=(255, 255, 255, 230))
        self.draw.text((15, 15), "Настройки", (60, 60, 60, 10), font=sans_font)
        self.draw.line(((5, 50), (635, 50)), fill=(150, 150, 150, 120), width=5)
        self.draw.line(((200, 5), (200, 305)), fill=(150, 150, 150, 120), width=5)
        self.draw.rounded_rectangle(((10, 60), (190, 100)), 5, fill=(200, 200, 200, 200))
        self.draw.text((20, 70), "Камеры", (60, 60, 60, 10), font=sans_font)
        self.draw.rounded_rectangle(((10, 110), (190, 150)), 5, fill=(200, 200, 200, 200))
        self.draw.text((20, 120), "Приложения", (60, 60, 60, 10), font=sans_font)
        self.draw.rounded_rectangle(((10, 160), (190, 200)), 5, fill=(200, 200, 200, 200))
        self.draw.text((20, 170), "Цветокоррекция", (60, 60, 60, 10), font=sans_font)
        self.draw.rounded_rectangle(((10, 210), (190, 250)), 5, fill=(200, 200, 200, 200))
        self.draw.text((20, 220), "Трекинг рук", (60, 60, 60, 10), font=sans_font)
        self.draw.rounded_rectangle(((10, 260), (190, 300)), 5, fill=(200, 200, 200, 200))
        self.draw.text((20, 270), "DEBUG", (60, 60, 60, 10), font=sans_font)
        self.draw.line(((100, 330), (540, 330)), fill=(255, 255, 255, 230), width=10)
        match self.selected_menu:
            case 0:
                self.message_text = "Выберите меню."
                self.line_coords = ((0, 0), (0, 0))
            case 1:
                self.message_text = "Камеры. Настройка очков."
                self.line_coords = ((190, 80), (197, 80))
                self.draw.line(((220, 100), (600, 100)), fill=(200, 200, 200, 200), width=3)
                self.draw.text((220, 65),
                               "Настройка межзрачкового расстояния:" + config["Customize"]["distance_between_eyes"],
                               (60, 60, 60, 10), font=sans_font)
                self.draw.text((210, 90), "0", (60, 60, 60, 10), font=sans_font)
                self.draw.text((610, 90), "40", (60, 60, 60, 10), font=sans_font)
                self.draw.ellipse([(210 + int(config["Customize"]["distance_between_eyes"]) * 10 - 20, 90),
                                   (230 + int(config["Customize"]["distance_between_eyes"]) * 10 - 20, 110)],
                                  fill=(60, 60, 60, 10), width=50)

                self.draw.line(((220, 170), (600, 170)), fill=(200, 200, 200, 200), width=3)
                self.draw.text((220, 140), "Расстояние до интерфейса:" + config["Customize"]["to_interface_range"],
                               (60, 60, 60, 10), font=sans_font)
                self.draw.text((210, 160), "0", (60, 60, 60, 10), font=sans_font)
                self.draw.text((610, 160), "500", (60, 60, 60, 10), font=sans_font)
                self.draw.ellipse([(210 + int(config["Customize"]["to_interface_range"]), 160),
                                   (230 + int(config["Customize"]["to_interface_range"]), 180)], fill=(60, 60, 60, 10),
                                  width=50)
            case 2:
                self.message_text = "Управление приложениями."
                self.line_coords = ((190, 130), (197, 130))
            case 3:
                self.message_text = "Управление цветом и светом."
                self.line_coords = ((190, 180), (197, 180))
            case 4:
                self.message_text = "Управление трекингом рук."
                self.line_coords = ((190, 230), (197, 230))
            case 5:
                self.message_text = "Debug menu. Доп. функции."
                self.line_coords = ((190, 280), (197, 280))

        self.draw.line(self.line_coords, fill=(200, 200, 200, 200), width=10)
        self.draw.text((215, 15), self.message_text, (60, 60, 60, 10), font=sans_font)

        return self.image

    def controller(self, coordinates,
                   config):
        """
        Здесь пишем что исполняется по нажатию на кнопку.
        При этом coordinates - координата указательного пальца НА ПОЛОТНЕ ОБЪЕКТА (self.size)
        """
        if self.check_in_region((10, 60), (190, 100), coordinates):
            if self.button_timer > 5:
                self.button_timer = 0
                self.selected_menu = 1
            else:
                self.button_timer += 1
        elif self.check_in_region((10, 110), (190, 150), coordinates):
            if self.button_timer > 5:
                self.button_timer = 0
                self.selected_menu = 2
            else:
                self.button_timer += 1
        elif self.check_in_region((10, 160), (190, 200), coordinates):
            if self.button_timer > 5:
                self.button_timer = 0
                self.selected_menu = 3
            else:
                self.button_timer += 1
        elif self.check_in_region((10, 210), (190, 250), coordinates):
            if self.button_timer > 5:
                self.button_timer = 0
                self.selected_menu = 4
            else:
                self.button_timer += 1
        elif self.check_in_region((10, 260), (190, 300), coordinates):
            if self.button_timer > 5:
                self.button_timer = 0
                self.selected_menu = 5
            else:
                self.button_timer += 1
        elif self.check_in_region((230, 80), (610, 120), coordinates):
            if self.button_timer > 3:
                self.button_timer = 0
                config["Customize"]["distance_between_eyes"] = str((coordinates[0] - 220) // 10)
            else:
                self.button_timer += 1
        elif self.check_in_region((230, 150), (610, 190), coordinates):
            if self.button_timer > 3:
                self.button_timer = 0
                config["Customize"]["to_interface_range"] = str((coordinates[0] - 220))
            else:
                self.button_timer += 1
        else:
            if self.button_timer > 1:
                self.button_timer -= 2
        return "nothing"
