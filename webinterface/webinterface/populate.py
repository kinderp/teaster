import os 

# configure the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webinterface.settings')

import django
django.setup()

import random
from core.models import ProductType, Product, Bug, BugStatusType, BugProductStatus
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()


def create_product_type(product_type):
    data = {}
    for p in product_type:
        value = ProductType.objects.get_or_create(name=p)[0] 
        data[p] = value
    return data 

def create_product(product, product_type):
    products_list = []
    # before that we have to create product type
    product_type_dict = create_product_type(product_type)
    for product_type_name,product_type_obj in product_type_dict.items():
        if product_type_name in product:
            for p in product[product_type_name]:
                name = p['name']
                version = p['version']
                new_p = Product.objects.get_or_create(product_type=product_type_obj, name=name, version=version)[0]
                products_list.append(new_p)

    return products_list


def create_bug_status_type():
    s_open = BugStatusType.objects.get_or_create(name='OPEN', description='bug is open')[0]
    s_closed = BugStatusType.objects.get_or_create(name='CLOSED', description='bug is closed')[0]
    s_need_info = BugStatusType.objects.get_or_create(name='NEEDINFO', description='bug needs info')[0]
    return [s_open, s_closed, s_need_info]


def create_bugs_for_products(product_list):
    # before that we have to create bug status
    bugs_status_obj_list = create_bug_status_type()

    for product in product_list:
        # num of bugs for a product
        n_bugs = random.randint(1,101)
        for bug_number in range(1,n_bugs):
            name = fakegen.linux_platform_token()
            description = ''
            c_date = fakegen.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
            user = User.objects.get(username='antonio')

            current_bug = Bug.objects.get_or_create(name=name, description=description, c_date=c_date, user=user)[0]
            #current_bug.product.add(product)
            # through='BugProductStatus'
            status = random.choice(bugs_status_obj_list)
            bsc = str(fakegen.pyint(min=0, max=999999, step=1))
            BugProductStatus.objects.get_or_create(status=status, bug=current_bug, product=product, bsc=bsc)[0]


if __name__ == '__main__':
    print("populating...")

    product_type = ['suse','opensuse','fedora','redhat','debian','ubuntu']

    product = {
        'suse': [{'name':'suse','version':'15'},{'name':'suse','version':'12'}],
        'opensuse': [{'name':'tumbleweed','version':'latest'},{'name':'leap','version':'15.1'}]
    }

    # create product
    import pdb
    pdb.set_trace()
    product_obj_list = create_product(product, product_type)
    # create bug for product
    create_bugs_for_products(product_obj_list)
    

