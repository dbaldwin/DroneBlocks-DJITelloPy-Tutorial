from djitellopy import Tello
import numpy as np


class DroneBlocksTello(Tello):

    def __init__(self):
        super().__init__()
        self.colors = {
            'red': 'r',
            'blue': 'b',
            'purple': 'p'
        }

    def _display_pattern(self, pattern_matrix):
        pattern = ''.join(pattern_matrix.flatten().tolist())
        return self.send_command_with_return(f"EXT mled g {pattern}")

    def tt_set_led_color(self, r: int, g: int, b: int, freq: float = 0.0) -> str:
        if freq > 0.0:
            if freq > 2.5:
                freq = 2.5
            return self.send_command_with_return(f"EXT led br {freq} {r} {g} {b}")
        else:
            return self.send_command_with_return(f"EXT led {r} {g} {b}")

    def tt_blink_led_color(self, r1: int, g1: int, b1: int, r2: int = 0, g2: int = 0, b2: int = 0,
                           freq: float = 0.1) -> str:
        return self.send_command_with_return(f"EXT led bl {freq} {r1} {g1} {b1} {r2} {g2} {b2}")

    @classmethod
    def tt_get_display_matrix(cls):
        return np.full((8,8), '0', dtype=str)

    def _up_arrow_matrix(self, display_color='p'):
        up = DroneBlocksTello.tt_get_display_matrix()
        up[0, 3:5] = display_color
        up[1, 2:6] = display_color
        up[2, 1:7] = display_color
        up[3, 0:8] = display_color
        up[4, 3:5] = display_color
        up[5, 3:5] = display_color
        up[6, 3:5] = display_color
        up[7, 3:5] = display_color
        return up

    def display_up_arrow(self, color='purple'):
        display_color = self.colors[color]
        up = self._up_arrow_matrix(display_color)
        return self._display_pattern(up)

    def display_down_arrow(self, color='purple'):
        display_color = self.colors[color]
        up = self._up_arrow_matrix(display_color)
        down = np.flipud(up)
        return self._display_pattern(down)

    def display_left_arrow(self, color='purple'):
        display_color = self.colors[color]
        up = self._up_arrow_matrix(display_color)
        left = np.rot90(up)
        return self._display_pattern(left)

    def display_right_arrow(self, color='purple'):
        display_color = self.colors[color]
        up = self._up_arrow_matrix(display_color)
        left = np.rot90(up)
        right = np.fliplr(left)
        return self._display_pattern(right)

    def clear_display(self) -> str:
        display = DroneBlocksTello.tt_get_display_matrix()
        return self._display_pattern(display)

    def display_message(self, message, color='purple', rate=2.5):
        if len(message) > 70:
            message = message[0:70]

        display_color = self.colors[color]
        return self.send_command_with_return(f"EXT mled l {display_color} {rate} {message}")

    def display_heart(self, color='purple'):
        display_color = self.colors[color]
        return self.send_command_with_return(f"EXT mled s {display_color} heart")

    def display_smile(self, color='purple'):
        display_color = self.colors[color]
        smile = DroneBlocksTello.tt_get_display_matrix()
        smile[0, 2] = display_color
        smile[0, 5] = display_color
        smile[2, 3:5] = display_color
        smile[3, 3:5] = display_color
        smile[4, 1] = display_color
        smile[4, 6] = display_color
        smile[5, 1] = display_color
        smile[5, 6] = display_color
        smile[6, 2] = display_color
        smile[6, 5] = display_color
        smile[7, 3:5] = display_color
        return self._display_pattern(smile)

if __name__ == '__main__':
    test_drone = DroneBlocksTello()
    test_drone.connect()

    test_matrix = test_drone.tt_get_display_matrix()

    test_drone.display_smile()

    # up = test_drone.up_arrow_matrix()
    # print(up)
    #
    # down = np.flipud(up)
    # print(down)
    #
    # left = np.rot90(up)
    # print(left)
    #
    # right = np.fliplr(left)
    # print(right)
