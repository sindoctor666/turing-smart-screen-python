import library.lcd_comm as lcd
from library import config

THEME_DATA = config.THEME_DATA
CONFIG_DATA = config.CONFIG_DATA


class StaticDisplay:
    @staticmethod
    def initialize_display():
        # Clear screen (blank)
        lcd.Clear(config.lcd_comm)

        # Set brightness
        lcd.SetBrightness(config.lcd_comm)

    @staticmethod
    def display_static_images():
        if THEME_DATA['static_images']:
            for image in THEME_DATA['static_images']:
                print(f"Drawing Image: {image}")
                lcd.DisplayBitmap(
                    ser=config.lcd_comm,
                    bitmap_path=THEME_DATA['PATH'] + THEME_DATA['static_images'][image].get("PATH"),
                    x=THEME_DATA['static_images'][image].get("X", 0),
                    y=THEME_DATA['static_images'][image].get("Y", 0),
                    width=THEME_DATA['static_images'][image].get("WIDTH", 0),
                    height=THEME_DATA['static_images'][image].get("HEIGHT", 0)
                )

    @staticmethod
    def display_static_text():
        if THEME_DATA['static_text']:
            for text in THEME_DATA['static_text']:
                print(f"Drawing Text: {text}")
                lcd.DisplayText(
                    ser=config.lcd_comm,
                    text=THEME_DATA['static_text'][text].get("TEXT"),
                    x=THEME_DATA['static_text'][text].get("X", 0),
                    y=THEME_DATA['static_text'][text].get("Y", 0),
                    font=THEME_DATA['static_text'][text].get("FONT", "roboto/Roboto-Regular.ttf"),
                    font_size=THEME_DATA['static_text'][text].get("FONT_SIZE", 10),
                    font_color=THEME_DATA['static_text'][text].get("FONT_COLOR", (0, 0, 0)),
                    background_color=THEME_DATA['static_text'][text].get("BACKGROUND_COLOR", (255, 255, 255)),
                    background_image=THEME_DATA['PATH'] + THEME_DATA['static_text'][text].get("BACKGROUND_IMAGE", None)
                )