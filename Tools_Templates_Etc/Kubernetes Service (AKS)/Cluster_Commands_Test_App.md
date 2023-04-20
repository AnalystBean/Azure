az aks get-credentials --resource-group aks1 --name cluster1
kubectl get nodes
git clone https://github.com/cloudacademy/configuring-aks.git
cd configuring-aks
kubectl apply -f azure-vote.yaml
kubectl get service azure-vote-front