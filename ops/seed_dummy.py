import os
import random
from decimal import Decimal, ROUND_HALF_UP
from sqlalchemy import text
from app.db import engine


# Este seed solo inserta texto plano de ejemplo en tablas si existieran.
# En esta versión de scaffold, sirve como placeholder para mostrar enfoque.


def q(x):
return Decimal(x).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)


def main():
with engine.begin() as conn:
# Ejemplo: crear empresa y clientes ficticios (ajusta cuando definas modelos)
conn.execute(text("SELECT 1"))
print("Seed demo ejecutado (placeholder). Define modelos y rehaz este script).")


if __name__ == "__main__":
main()