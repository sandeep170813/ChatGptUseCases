apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ deployment_name }}
spec:
  replicas: {{replicas}}
  selector:
    matchLabels:
      app: {{ deployment_name }}
  template:
    metadata:
      labels:
        app: {{ deployment_name }}
    spec:
      containers:
      - name: {{ deployment_name }}
        image: {{ container_image }}:{{container_tag}}
        ports:
        - containerPort: {{container_port}}
cpu: "{{cpu_limit}}"
            memory: "{{memory_limit}}"
          requests:
            cpu: "{{cpu_request}}"
            memory: "{{memory_request}}"
---
apiVersion: v1
kind: Service
metadata:
  name: {{ deployment_name }}-svc
spec:
  selector:
    app: {{ deployment_name }}
  ports:
  - name: {{service_name}}
    port: {{service_port}}
    targetPort: {{container_port}}
  type: {{service_type}}
----------------------
apiVersion: autoscaling/v2beta2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ deployment_name }}-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ deployment_name }}
  minReplicas: {{min_replicas}}
  maxReplicas: {{max_replicas}}
  metrics:
  - type: Resource
    resource:
      name: {{metric_name}}
      targetAverageUtilization: {{target_average_utilization}}