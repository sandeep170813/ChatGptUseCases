import yaml
import csv


def replace_placeholders_csv(csv_file):
    # Read the CSV file
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            deployment_name = row['deployment_name']
            container_image = row['container_image']
            cpu_limit = row['cpu_limit']
            memory_limit = row['memory_limit']
            cpu_request = row['cpu_request']
            memory_request = row['memory_request']
            # Read the YAML file
            with open("deployment.yaml") as f:
                deployment = yaml.safe_load(f)
# Replace the placeholders
            deployment["metadata"]["name"] = deployment_name
            deployment["spec"]["selector"]["matchLabels"]["app"] = deployment_name
            deployment["spec"]["template"]["metadata"]["labels"]["app"] = deployment_name
            deployment["spec"]["template"]["spec"]["containers"][0]["name"] = deployment_name
            deployment["spec"]["template"]["spec"]["containers"][0]["image"] = container_image
            deployment["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["cpu"] = cpu_limit
            deployment["spec"]["template"]["spec"]["containers"][0]["resources"]["limits"]["memory"] = memory_limit
            deployment["spec"]["template"]["spec"]["containers"][0]["resources"]["requests"]["cpu"] = cpu_request
            deployment["spec"]["template"]["spec"]["containers"][0]["resources"]["requests"]["memory"] = memory_request


            # Write the updated YAML file
            with open(f"deployment_{deployment_name}.yaml", "w") as f:
                yaml.dump(deployment, f)