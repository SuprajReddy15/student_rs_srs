
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
    ('adminapp', '0004_faculty'),
    # Add any other dependencies here if needed
]
    operations = [
        migrations.AlterModelTable(
            name="facultycoursemapping",
            table="facutlycoursemapp_table",
        ),
    ]
