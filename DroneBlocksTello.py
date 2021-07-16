from djitellopy import Tello
import numpy as np

class DroneBlocksTello(Tello):

    def __init__(self):
        super().__init__()

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

    def tt_get_display_matrix(self):
        myArray = np.chararray((8,8))
        myArray[:] = 0
        myArray.reshape((8,8))
        return myArray

    def tt_clear_display(self) -> str:
        display = self.tt_get_display_matrix()
        return self.send_command_with_return(f"EXT mled g {display.tostring()}")
