from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.image import AsyncImage
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

__all__ = ("AKLabelLoader", "AKImageLoader")

Builder.load_string(
    """

<AKLabelLoader>:
    canvas.before:
        Color:
            rgba: root.theme_cls.bg_darkest
            a: root.fr_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(20), ]
        Color:
            rgba: root.theme_cls.bg_dark
            a: root.bg_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(20), ]


<AKImageLoader>:
    source: " "
    canvas.before:
        Color:
            rgba: root.theme_cls.bg_darkest
            a: root.fr_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(self.size[0] / 2), ] if root.circle else [dp(20), ]
        Color:
            rgba: root.theme_cls.bg_dark
            a: root.bg_rec_opacity
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(self.size[0] / 2, self.size[1] / 2), ] if root.circle else [dp(20), ]
"""
)


class AKLabelLoader(MDLabel):

    bg_rec_opacity = NumericProperty(0)
    fr_rec_opacity = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_anim = None
        Clock.schedule_once(self.on_text)

    def _check_text(self, text):
        if not text:
            return False
        else:
            return True

    def _start_animate(self):
        self.bg_rec_opacity = 1
        self.fr_rec_opacity = 1
        self.start_anim = Animation(
            bg_rec_opacity=1, t="in_quad", duration=0.8
        ) + Animation(bg_rec_opacity=0, t="out_quad", duration=0.8)
        self.start_anim.repeat = True
        self.start_anim.start(self)

    def _stop_animate(self):

        if self.start_anim:
            self.start_anim.cancel_all(self)

        if self.bg_rec_opacity != 0 and self.fr_rec_opacity != 0:
            self.stop_anim = Animation(
                fr_rec_opacity=0, t="out_quad", duration=0.3
            )
            self.stop_anim &= Animation(
                bg_rec_opacity=0, t="out_quad", duration=0.3
            )
            self.stop_anim.start(self)

    def on_text(self, *args):
        if self._check_text(self.text):
            self._stop_animate()
        else:
            self._start_animate()


class AKImageLoader(ThemableBehavior, AsyncImage):

    bg_rec_opacity = NumericProperty(0)
    fr_rec_opacity = NumericProperty(0)
    circle = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.start_anim = None

    def _check_source(self, source):
        if not source or len(source.strip()) == 0:
            self.source = " "
            return False
        else:
            return True

    def _start_animate(self):
        self.bg_rec_opacity = 1
        self.fr_rec_opacity = 1
        self.color = [1, 1, 1, 0]
        self.start_anim = Animation(
            bg_rec_opacity=1, t="in_quad", duration=0.8
        ) + Animation(bg_rec_opacity=0, t="out_quad", duration=0.8)
        self.start_anim.repeat = True
        self.start_anim.start(self)

    def _stop_animate(self):

        self.color = [1, 1, 1, 1]
        if self.start_anim:
            self.start_anim.cancel_all(self)
            self.stop_anim = Animation(
                fr_rec_opacity=0, t="out_quad", duration=0.3
            )
            self.stop_anim &= Animation(
                bg_rec_opacity=0, t="out_quad", duration=0.3
            )
            self.stop_anim.start(self)

    def on_source(self, *args):
        if self._check_source(self.source):
            self._start_animate()
        else:
            self._stop_animate()
    def on_load(self, *args):
        ''' called when the image has loaded'''
        print(f'====================== the images {self.source} has loaded ====================')
       
        self._stop_animate()
        self.adjust_size()
    def adjust_size(self, *args):
        if not self.parent or not self.texture:
            return

        (par_x, par_y) = self.parent.size

        if par_x == 0 or par_y == 0:
            with self.canvas:
                self.canvas.clear()
            return

        par_scale = par_x / par_y
        (img_x, img_y) = self.texture.size
        img_scale = img_x / img_y

        if par_scale > img_scale:
            (img_x_new, img_y_new) = (img_x, img_x / par_scale)
        else:
            (img_x_new, img_y_new) = (img_y * par_scale, img_y)

        crop_pos_x = (img_x - img_x_new) / 2
        crop_pos_y = (img_y - img_y_new) / 2

        subtexture = self.texture.get_region(
            crop_pos_x, crop_pos_y, img_x_new, img_y_new
        )

        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1)
            Rectangle(texture=subtexture, pos=self.pos, size=(par_x, par_y))

