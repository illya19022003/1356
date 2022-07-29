import classShop

def test_describe_shop():
    assert {
        shop = classShop('Полисся', 'Продуктовий', 10)
        shop.describe_shop == f'Назва: {shop.shop_name}. Тип: {shop.store_type}'
    }


def test():
    assert 'py'.upper() == 'PY'
