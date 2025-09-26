```bash
#!/usr/bin/env bash
set -euo pipefail
FILE="${1:-}"
[ -z "$FILE" ] && echo "Uso: $0 backups/pg_YYYYmmdd-HHMMSS.sql" && exit 1
docker compose -f docker/compose.yml exec -T db psql -U ${POSTGRES_USER:-app} ${POSTGRES_DB:-facturas} < "$FILE"
echo "Restore completo desde $FILE"
```