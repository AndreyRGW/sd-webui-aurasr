from aura_sr import AuraSR
from PIL import Image
import requests
from huggingface_hub import hf_hub_download
import torch

def get_aura_sr_model():
    model_name = "fal/AuraSR-v2"
    model_path = hf_hub_download(model_name, "model.safetensors")
    config_path = hf_hub_download(model_name, "config.json")
    return AuraSR.from_pretrained(model_path, use_safetensors=True)

def runAuraSR(img: Image.Image) -> Image.Image:
    try:
        # Get the AuraSR model
        aura_sr = get_aura_sr_model()
        
        # Upscale the input image using AuraSR
        upscaled_image = aura_sr.upscale_4x_overlapped(img.convert('RGB'))
        
        # Return the upscaled image directly
        return upscaled_image
    
    finally:
        try:
            del aura_sr
            torch.cuda.empty_cache()
        except:
            pass
