from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
import os

# UI Design
KV = '''
MDScreen:
    md_bg_color: [0.1, 0.1, 0.1, 1]
    
    MDLabel:
        text: "Panjtan CS - Vocal Isolator"
        halign: "center"
        pos_hint: {"center_y": 0.8}
        font_style: "H4"
        theme_text_color: "Custom"
        text_color: [1, 1, 1, 1]

    MDRaisedButton:
        text: "SELECT VIDEO"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.open_file_manager()

    MDLabel:
        id: status_label
        text: "Status: Waiting for file..."
        halign: "center"
        pos_hint: {"center_y": 0.3}
        theme_text_color: "Hint"
'''

class PanjtanApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        return Builder.load_string(KV)

    def open_file_manager(self):
        self.file_manager.show(os.path.expanduser("~"))  # Opens home directory

    def select_path(self, path):
        self.exit_manager()
        self.root.ids.status_label.text = f"Processing: {os.path.basename(path)}"
        self.process_video(path)

    def exit_manager(self, *args):
        self.file_manager.close()

    def process_video(self, video_path):
        # یہاں ہم پروسیسنگ فنکشن کال کریں گے
        try:
            import processing
            output = processing.extract_vocals(video_path)
            self.root.ids.status_label.text = f"Success! Saved: {output}"
        except Exception as e:
            self.root.ids.status_label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    PanjtanApp().run()
