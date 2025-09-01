from django.db import migrations


# def migrate_todo_status(apps, schema_editor):
#     Todo = apps.get_model('todo', 'Todo')
#     Status = apps.get_model('todo', 'Status')
#
#
#     statuses = {s.name: s for s in Status.objects.all()}
#
#     for todo in Todo.objects.all():
#         old_status = str(todo.status_id)
#         status_obj = statuses.get(old_status, statuses.get('pending'))
#         todo.status = status_obj
#         todo.save()


class Migration(migrations.Migration):
    dependencies = [
        ('todo', '0004_status_name_alter_todo_status'),
    ]

    operations = [
        # migrations.RunPython(migrate_todo_status),
    ]
