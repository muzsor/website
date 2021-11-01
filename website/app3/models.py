from django.db import connections, models


def dictfetchall(cursor) -> list:
    """
    從 cursor 獲取的資料行轉換成元素為字典的列表
    [
        {
            'column1': '...',
            'column2': '...',
            ...': '...',
        },
        {
            'column1': '...',
            'column2': '...',
            '...': '...',
        },
    ]
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def execute_raw_database(sql, params) -> dict:
    with connections['third'].cursor() as cursor:
        cursor.execute(sql, params)
        return dictfetchall(cursor)


class Table(models.Model):
    column0 = models.IntegerField(blank=False, db_column='c0', primary_key=True)
    column1 = models.CharField(max_length=50, db_column='c1')
    column2 = models.DecimalField(blank=False, db_column='c2', decimal_places=2, max_digits=4)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
