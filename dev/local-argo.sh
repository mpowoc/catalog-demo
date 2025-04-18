minikube start --driver=docker -p argocd-helm

tflocal -chdir=../gitops/terraform/env/local init
tflocal -chdir=../gitops/terraform/env/local apply \
    -target="helm_release.argocd" \
    --auto-approve

# Forwarding argo console port to localhost. Log in at localhost:8081
# 
# Find local admin secret here:
#   - kubectl get secrets argocd-initial-admin-secret -o yaml -n argocd
minikube kubectl port-forward svc/argocd-server -n argocd 8081:80