const { execSync } = require('child_process')

const stopCommand = 'echo "y" | gcloud deployment-manager deployments stop deployment4 || true';
const deleteCommand = 'echo "y" | gcloud deployment-manager deployments delete deployment4 || true';
const createCommand = 'gcloud deployment-manager deployments create deployment4 --config config.yaml';
execSync(stopCommand, { stdio: 'inherit' });
execSync(deleteCommand, { stdio: 'inherit' });
execSync(createCommand, { stdio: 'inherit' });
