from imageGeneration import generate_image
from input import get_input
from download import download_image
import webbrowser



def main():
    prompt, quality = get_input()
    image_url = generate_image(prompt, quality)
    download_image(image_url, prompt)

    webbrowser.open(image_url)
    main()


if __name__ == "__main__":
    main()