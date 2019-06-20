import os 
import pdb

# configure the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webinterface.settings')

import django
django.setup()

from core.models import ProductType, Product, Bug, BugStatusType, BugProductStatus

n_product_type = ProductType.objects.all().count()
n_product = Product.objects.all().count()
n_bug_status_type = BugStatusType.objects.all().count()
n_bug = Bug.objects.all().count()
n_bug_product_status = BugProductStatus.objects.all().count()


BugProductStatus.objects.all().delete()
Product.objects.all().delete()
ProductType.objects.all().delete()
Bug.objects.all().delete()
BugStatusType.objects.all().delete()

n_product_type_after = ProductType.objects.all().count()
n_product_after = Product.objects.all().count()
n_bug_status_type_after = BugStatusType.objects.all().count()
n_bug_after = Bug.objects.all().count()
n_bug_product_status = BugProductStatus.objects.all().count()

pdb.set_trace()
