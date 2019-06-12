from kubernetes import client, config
import subprocess

config.load_kube_config()
v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    if i.metadata.labels["release"] == "ccproject":
        name = i.metadata.name
        subprocess.Popen(f"powershell kubectl logs pod/{name} -f", creationflags=subprocess.CREATE_NEW_CONSOLE)
        print(i.metadata.labels["module"], i.metadata.name)
        
