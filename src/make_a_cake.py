# This script will contain the logic for generating the cake using Stable Diffusion.

import json
from datetime import datetime
from diffusers import StableDiffusionPipeline
import torch

def load_customizations(file_path="src/utils/customizations.json"):
    """Load default customizations from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def make_cake(cli_customizations=None, output_dir="cakes/", filename=None):
    """
    Generate a cake image using Stable Diffusion with customizations.
    Arguments:
        cli_customizations: Dictionary of CLI-provided customizations to override defaults.
        output_dir: Directory to save the generated images.
        filename: Optional filename for the output image.
    """
    # Step 1: Load default customizations
    customizations = load_customizations()

    # Step 2: Integrate CLI-provided overrides
    if cli_customizations:
        customizations.update(cli_customizations)

    # Step 3: Construct the prompt
    prompt = (
        f"A birthday cake with a {customizations['color_scheme_cake']} color scheme, "
        f"set in a {customizations['setting_type']} with a {customizations['color_scheme_background']} background. "
        f"The cake is decorated with {', '.join(customizations['plants_decorations'])} and "
        f"{', '.join(customizations['other_decorations'])}. "
        f"It features a design with {', '.join(customizations['design_on_cake'])} "
        f"and the message '{customizations['message_on_cake']}' written on it."
    )

    print(f"Using prompt: {prompt}")

    # Step 4: Load Stable Diffusion model
    print("Loading Stable Diffusion model...")
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    pipeline = pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

    # Step 5: Generate the image
    print("Generating the image...")
    image = pipeline(prompt).images[0]  # Get the first generated image

    # Step 6: Determine filename
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cake__{timestamp}.png"
    output_path = f"{output_dir}{filename}"

    # Step 7: Save the generated image
    print(f"Saving the image to {output_path}...")
    image.save(output_path)
    print("Cake generation completed!")
