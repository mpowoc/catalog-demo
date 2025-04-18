docker-compose up -d localstack --no-recreate
docker-compose up -d catalog-postgres --no-recreate

tflocal -chdir=../gitops/terraform/env/local init
tflocal -chdir=../gitops/terraform/env/local apply \
    -target="module.sqs_catalog_events" \
    -target="module.opensearch" \
    --auto-approve
