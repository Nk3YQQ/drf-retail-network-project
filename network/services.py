def get_all_objects(model):
    """Возвращает все объекты модели"""

    return model.objects.all()


def create_products_and_contact(product_model, contact_model, products_data, contact_data, network_node):
    """Функция создаёт для элемента сети продукты и контакт"""

    contact_model.objects.create(network_node=network_node, **contact_data)

    for product_data in products_data:
        product_model.objects.create(network_node=network_node, **product_data)


def update_products_and_contact(product_model, contact_model, products_data, contact_data, instance):
    """Функция обновляет у элемента сети продукты и контакт"""

    if contact_data:
        contact_model.objects.update_or_create(network_node=instance, defaults=contact_data)

    for product_data in products_data:
        product_id = product_data.get("id")

        if product_id:
            product = product_model.objects.get(id=product_id)
            product.name = product_data.get("name", product.name)
            product.model = product_data.get("model", product.model)
            product.on_market = product_data.get("on_market", product.on_market)

        else:
            product_model.objects.create(network_node=instance, **product_data)
