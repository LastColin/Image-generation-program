



def get_input():
    prompt = input("Enter what you want to generate: ")
    if len(prompt) < 10:
        print("Invalid Prompt or Prompt too short!")
        print("Prompt must be at least 10 characters long")
        return get_input()

    quality = input("Select Quality (Standard or HD): ")
    if quality not in ["Standard", "standard", "HD", "hd"]:
        print("Invalid Quality")
        return get_input()
    
    return prompt, quality.lower()