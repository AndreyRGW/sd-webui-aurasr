from aura_sr import AuraSR
from PIL import Image
import requests
from io import BytesIO
from huggingface_hub import hf_hub_download
import torch
import os
from tempfile import TemporaryDirectory

def get_aura_sr_model():
    # Define the model name
    model_name = "fal/AuraSR-v2"
    
    # Download the model and config files from the Hugging Face Hub
    model_path = hf_hub_download(model_name, "model.safetensors")
    config_path = hf_hub_download(model_name, "config.json")
    
    # Return the pretrained AuraSR model
    return AuraSR.from_pretrained(model_path, use_safetensors=True)

def runAuraSR(img: Image.Image) -> Image.Image:
    # Create temporary directories to store input and output files
    tmpInDir = TemporaryDirectory()
    tmpOutDir = TemporaryDirectory()
    
    try:
        # Define the input and output file paths
        fileIn = os.path.join(tmpInDir.name, 'file.jpg')
        fileOut = os.path.join(tmpOutDir.name, 'file.jpg')
        
        # Convert the input image to RGB and save it to the input file path
        img.convert('RGB').save(fileIn, quality=100)
        
        # Get the AuraSR model
        aura_sr = get_aura_sr_model()
        
        # Open the input image
        input_image = Image.open(fileIn)
        
        # Upscale the input image using AuraSR
        upscaled_image = aura_sr.upscale_4x_overlapped(input_image)
        
        # Save the upscaled image to the output file path
        upscaled_image.save(fileOut, quality=100)
        
        # Check if the output file exists
        if not os.path.exists(fileOut):
            raise Exception("AuraSR didn't process any image")
        
        # Return the output image
        return Image.open(fileOut)
    
    finally:
        # Clean up resources
        try:
            del aura_sr
            torch.cuda.empty_cache()  # Clear GPU memory
            tmpInDir.cleanup()
            tmpOutDir.cleanup()
        except:
            pass
