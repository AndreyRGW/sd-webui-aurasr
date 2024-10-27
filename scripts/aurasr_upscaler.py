from dataclasses import dataclass
from modules.upscaler import Upscaler, UpscalerData
from modules import devices
from scripts.aurasr_tools import runAuraSR

@dataclass
class Fields:
    scale: int

# AuraSR supports only 4x upscaling
data = [
    Fields(4),
]

class BaseClass(Upscaler):
    def __init__(self, dirname, fields: Fields = None):
        if fields is None:
            self.scalers = []
            return
        self.name = "AuraSR"
        self.fields = fields
        self.scalers = [UpscalerData(f'AuraSR {self.fields.scale}x', None, self, self.fields.scale)]
        super().__init__()

    def do_upscale(self, img, selected_model):
        # Get the appropriate device for AuraSR
        device = devices.get_device_for('aurasr')
        return runAuraSR(img, device)

class Class0(BaseClass, Upscaler):
    def __init__(self, dirname):
        super().__init__(dirname, data[0])
