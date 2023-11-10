import yaml


def replace_placeholders(deployment_name, container_image):
    # Read the YAML file
    with open("deployment.yaml") as f:
        deployment = yaml.safe_load(f)


    # Replace the placeholders
    deployment["metadata"]["name"] = deployment_name
    deployment["spec"]["selector"]["matchLabels"]["app"] = deployment_name
    deployment["spec"]["template"]["metadata"]["labels"]["app"] = deployment_name
    deployment["spec"]["template"]["spec"]["containers"][0]["name"] = deployment_name
    deployment["spec"]["template"]["spec"]["containers"][0]["image"] = container_image


    # Write the updated YAML file
    with open("deployment.yaml", "w") as f:
        yaml.dump(deployment, f)
