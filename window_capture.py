import numpy as np
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from Quartz import CGDisplayBounds
from Quartz import CGImageGetHeight, CGImageGetWidth, NSMakeRect, CGRectContainsRect
from Quartz import CGWindowListCreateImage, kCGWindowImageDefault, CGImageGetDataProvider, CGDataProviderCopyData
from AppKit import NSApplication, NSRunningApplication, NSWorkspace
class WindowCapture:

    # Properties
    w = 0
    h = 0
    hwnd = None
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=None, width=1024, height=768):

        if window_name is None:
            self.hwnd = kCGNullWindowID
        else:
            window_infos = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
            for window_info in window_infos:
                window_title = window_info.get('kCGWindowName', '')
                if window_title == window_name:
                    self.hwnd = window_info['kCGWindowNumber']
                    break

            if not self.hwnd:
                raise Exception("Window not found: {}".format(window_name))

        # Define monitor dimensions
        self.w = width
        self.h = height

    def get_screenshot(self):
        window_rect = CGDisplayBounds(self.hwnd)
        image = CGWindowListCreateImage(window_rect, kCGWindowListOptionOnScreenOnly, self.hwnd, kCGWindowImageDefault)

        width = CGImageGetWidth(image)
        height = CGImageGetHeight(image)

        data_provider = CGImageGetDataProvider(image)
        bitmap_data = CGDataProviderCopyData(data_provider)

        np_image = np.frombuffer(bitmap_data, dtype=np.uint8)
        np_image.shape = (height, width, 4)

        img = np_image[..., :3]
        img = np.ascontiguousarray(img)

        return img

    @staticmethod
    def list_window_names():
        window_infos = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
        for window_info in window_infos:
            window_title = window_info.get('kCGWindowName', '')
            if window_title:
                print(hex(window_info['kCGWindowNumber']), window_title)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
