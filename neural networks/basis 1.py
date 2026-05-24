from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="generated_image.png"):
    """
    Generates an image from a given text prompt using Stable Diffusion.

    Parameters:
        prompt (str): The text prompt to generate the image.
        output_path (str): Path to save the generated image.

    Returns:
        None: Saves the generated image to the specified path.
    """
    # Load the Stable Diffusion pipeline
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
    pipeline = pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate the image
    image = pipeline(prompt).images[0]

    # Save the image
    image.save(output_path)
    print(f"Image generated and saved at {output_path}")

if __name__ == "__main__":
    # Get input from the user
    user_prompt = input("Enter a text prompt to generate an image: ")
    output_file = "output_image.png"

    # Generate the image
    generate_image(user_prompt, output_file)
