from django.core.management.base import BaseCommand
from django.core.management import call_command
from django_tenants.utils import tenant_context
from customers.models import Client

class Command(BaseCommand):
    help = "Create a superuser for a specifice tenant"

    def add_arguments(self, parser):
        parser.add_argument("-s", "--schema_name", type=str, help="Schema name of the tenant")    
    def handle(self, *args, **options):
        schema_name = options["schema_name"]

        try:
            tenant = Client.objects.get(schema_name=schema_name)
        except Client.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Tenant with schema '{schema_name}' doesn't exists "))       
            return     
        
        with tenant_context(tenant):
            self.stdout.write(self.style.SUCCESS(f"Creating superuser for tenant: {schema_name}"))
            call_command("createsuperuser")
            self.stdout.write(self.style.SUCCESS(f"Superuser create successfully for tenant: {schema_name}"))