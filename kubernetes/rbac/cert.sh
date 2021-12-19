USER=cdn
NAMESPACE=cdn
SERVER_IP=85.208.253.129
scp ubuntu@$SERVER_IP:/etc/kubernetes/pki/ca.{crt,key} .
openssl genrsa -out $USER.key 2048
openssl req -new -key $USER.key -out $USER.csr -subj "/CN=$USER/O=$NAMESPACE"
openssl x509 -req -in $USER.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out $USER.crt -days 365
kubectl --kubeconfig $USER.kubeconfig config set-cluster kubernetes --server https://$SERVER_IP:6443 --certificate-authority=ca.crt
kubectl --kubeconfig $USER.kubeconfig config set-credentials $USER --client-certificate $USER.crt --client-key $USER.key
#kubectl --kubeconfig $USER.kubeconfig config set-cluster kubernetes --server https://$SERVER_IP:6443 --certificate-authority=ca.crt --embed certs=true
#kubectl --kubeconfig $USER.kubeconfig config set-credentials $USER --client-certificate $USER.crt --client-key $USER.key --embed certs=true
kubectl --kubeconfig $USER.kubeconfig config set-context $USER-kubernetes --cluster kubernetes --namespace $NAMESPACE --user $USER
kubectl create -f limit_to_namespace.yaml -n $NAMESPACE
#kubectl create rolebinding $USER-$NAMESPACE-rolebinding --role=$USER-$NAMESPACE --user=$USER --namespace $NAMESPACE
