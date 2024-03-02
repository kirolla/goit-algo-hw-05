# Порівняльний аналіз швидкості виконання алгоритмів пошуку підрядка

Було проведено порівняльний аналіз швидкості виконання трьох алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа для двох наданих текстів:

## Результати для файлу article_1.txt:

Алгоритм Boyer-Moore:

Час для існуючого підрядка: 0.661 секунд

Час для вигаданого підрядка: 0.639 секунд

Алгоритм Knuth-Morris-Pratt:

Час для існуючого підрядка: 0.660 секунд

Час для вигаданого підрядка: 0.663 секунд

Алгоритм Rabin-Karp:

Час для існуючого підрядка: 0.0000397 секунд

Час для вигаданого підрядка: 0.0000401 секунд

## Результати для файлу article_2.txt:

Алгоритм Boyer-Moore:

Час для існуючого підрядка: 0.653 секунд

Час для вигаданого підрядка: 0.645 секунд

Алгоритм Knuth-Morris-Pratt:

Час для існуючого підрядка: 0.667 секунд

Час для вигаданого підрядка: 0.669 секунд

Алгоритм Rabin-Karp:

Час для існуючого підрядка: 0.0000393 секунд

Час для вигаданого підрядка: 0.0000402 секунд

## Висновки:

1. **Перший текст:**
    - Боєра-Мура: Швидкість для існуючого та вигаданого підрядків практично однакова, що свідчить про ефективність цього алгоритму незалежно від характеристик підрядка.
    - Кнута-Морріса-Пратта: Також спостерігається майже однакова швидкість для обох типів підрядків, що підтверджує ефективність алгоритму.
    - Рабіна-Карпа: Швидкість виконання цього алгоритму значно нижча порівняно з іншими для обох типів підрядків. Це може бути зумовлено додатковим обчисленням хеш-значень, що робить його менш ефективним в порівнянні з Боєра-Мура та Кнута-Морріса-Пратта.

2. **Другий текст:**
    - Боєра-Мура: Подібно до першого файлу, швидкість для існуючого та вигаданого підрядків майже однакова.
    - Кнута-Морріса-Пратта: Також спостерігається подібна швидкість для обох типів підрядків.
    - Рабіна-Карпа: Швидкість виконання залишається низькою, але в порівнянні з іншими алгоритмами для даного файлу вона залишається константною.

3. **В цілому:**
    - Боєра-Мура та Кнута-Морріса-Пратта: Ці алгоритми показують стабільну та подібну швидкість для обох типів підрядків у обох файлах. Вони можуть бути відмінними виборами для загального використання, оскільки показують стабільні результати незалежно від характеристик підрядків та тексту.
    - Рабіна-Карпа: Цей алгоритм показує низьку швидкість в порівнянні з іншими для обох файлів, що робить його менш практичним вибором у даному контексті.

Загалом, для обох текстів Боєра-Мура та Кнута-Морріса-Пратта демонструють схожу швидкість та можуть бути вибраними як ефективні алгоритми пошуку підрядка, тоді як Рабіна-Карпа має значно меншу ефективність в цьому контексті.