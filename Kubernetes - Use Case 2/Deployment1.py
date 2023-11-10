import yaml


def replace_placeholders(deployment_name, container_image, cpu_limit, memory_limit, cpu_request, memory_request):
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