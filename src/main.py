import argparse
import json
import os
from src.make_a_cake import generate_cake

# Load the default customizations
def load_customizations(file_path="src/utils/customizations.json"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Customizations file not found: {file_path}")
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="AV bday cake")
    parser.add_argument(
        "command",
        choices=["generate"],
        help="brb chicken kween is too busy helping others"
    )

    # Allow plant decorations to be customized via CLI
    parser.add_argument(
        "-p", "--plants", 
        type=str, 
        nargs='+', 
        help="Optional plant decorations you would like to see (e.g. daisies, cacti, spider ferns)"
    )
    # Allow user to name generated PNG file if they want
    parser.add_argument(
        "-f", "--filename",
        type=str,
        help="Optional filename for the generated image (e.g., 'Bruce-and-Bryan-must-have-made-this-one.png')."
    )


    args = parser.parse_args()

    if args.command == "generate":
        # TODO(mvn) -- Can we make this message funnier? 
        print("Generating the birthday cake...")

        default_customizations = load_customizations()

        # Override default plant decorations if provided
        customizations = default_customizations.copy()
        if args.plants:
            customizations["plants_decorations"] = args.plants

        print(f"Customizations being applied: {json.dumps(customizations, indent=4)}")

        generate_cake(customizations)

if __name__ == "__main__":
    main()
