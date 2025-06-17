def calculate_discount(total_sales):
    """
    Возвращает процент скидки в зависимости от объёма продаж.
    """
    if total_sales >= 300000:
        return 15
    elif total_sales >= 50000:
        return 10
    elif total_sales >= 10000:
        return 5
    return 0 