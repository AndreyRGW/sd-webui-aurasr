# AuraSR V2 Integration for Stable Diffusion WebUI

This extension integrates [AuraSR V2](https://huggingface.co/fal/AuraSR-v2), AI upscaling model, into [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui). AuraSR offers 4x upscaling, an open reproduction of the GigaGAN Upscaler.

## Features

- 4x upscaling
- Can be used in *hires fix*, *upscaler_for_img2img*, or in the *extras* tab
- Automatic model download from Hugging Face

![](/images/preview.png)
![](/images/upscaler.png)

## Installation

The extension will automatically download the AuraSR model from Hugging Face during the first run. No manual setup is required.

## Usage

Once installed, AuraSR will appear in the list of available upscalers in the WebUI.

## Platform Support

This extension is designed to work on platforms that support PyTorch and can run stable-diffusion-webui. It has been tested on Windows and will probably work on Linux as well.

## Notes

Personally, AuraSR doesn't interest me because its quality isn't impressive yet. There are much more interesting options, like Swin2SR. I also want to highlight the significant vram consumption of AuraSR specifically in WebUI. I wrote a separate interface in Gradio to run AuraSR, and its memory consumption there was around 1.7GB. However, for some reason, in the A1111 WebUI interface, its pure vram consumption is 6.1GB! I'm not sure what the reason is; perhaps it's a bug that only occurs for me, but I haven't been able to resolve it.

![Comparison image placeholder](/images/comparation.jpg)

## Issues and Contributions

If you encounter any issues or have suggestions for improvement, please feel free to open an issue.
