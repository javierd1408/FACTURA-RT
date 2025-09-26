```bash
#!/usr/bin/env bash
set -euo pipefail
mkdir -p backups
TS=$(date +"%Y%m%d-%H%M%S")
docker compose -f docker/compose.yml exec -T db pg_dump -U ${POSTGRES_USER:-app} ${POSTGRES_DB:-facturas} > backups/pg_${TS}.sql
echo "Backup creado en backups/pg_${TS}.sql"
```