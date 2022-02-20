def black_box(page: int):
    if page <= 7922400:
        return True
    else:
        return False

def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_box) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.
    
    Уточнение:
        black_box возвращает True, если страница последняя
                  возвращает False, если страница не последняя.
    
    
    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # application of binary search. Algorithm complexity is O(log n)
    left, right = 0, 1e7
    while left < right:
        mid = (left + right) // 2
        if black_box(mid):
            print(f"Volume of the book is {mid} pages")
            return mid
        else:
            right = mid - 1


if __name__ == '__main__':
    main()

