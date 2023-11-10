import re

def replace_placeholders(file_path, placeholders):
    with open(file_path, 'r') as file:
        content = file.read()

    for placeholder, value in placeholders.items():
        content = re.sub(fr'{placeholder}\b', value, content)

    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    yaml_file_path = 'your-deployment.yaml'  # Replace with your actual YAML file path

    # Define placeholders and their corresponding values
    placeholders = {
        'YOUR_APP_NAME': 'your-app-deployment',
        'YOUR_IMAGE_NAME': 'your-registry/your-app:latest'
        # Add more placeholders as needed
    }

    replace_placeholders(yaml_file_path, placeholders)
