from telebot import TeleBot
from telebot import types


qqq = ('Radeon RX 7900 XTX — топовая десктопная видеокарта на архитектуре RDNA 3.0 и техпроцессе 5 нм, рассчитанная на геймеров. 4 '

'Некоторые характеристики:'

'частота ядра (игровая/турбо): 2270/2500 МГц; 1'
'количество универсальных процессоров: 6144 (12288); 1'
'количество текстурных блоков: 384; 1'
'количество блоков блендинга: 192; 1'
'эффективная частота памяти: 20 ГГц; 1'
'тип памяти: GDDR6; 1'
'шина памяти: 384 бит; 1'
'объём памяти: 24 ГБ; 1'
'пропускная способность памяти: 960 ГБ/с; 1'
'вычислительная производительность (FP32): до 61,4 терафлопс; 1'
'теоретическая максимальная скорость закраски: 480 гигапикселей/с; 1'
'теоретическая скорость выборки текстур: 960 гигатекселей/с; 1'
'шина PCI Express 4.0 x16; 1'
'разъёмы: один HDMI 2.1b, два DisplayPort 2.1 и один USB Type C; 1'
'энергопотребление: до 355 Вт; 1'
'дополнительное питание: два 8-контактных разъёма; 1'
'число слотов, занимаемых в системном корпусе: 2,5. 1'
'Длина референсной версии — 287 мм.' 
)

www = ('Некоторые характеристики видеокарты Radeon RX 7800 XT:'

'Графический процессор: Navi 32 в варианте Navi 32 XT. 2'
'Объём памяти: 16 ГБ, тип памяти — GDDR6. 2'
'Ширина шины: 256 бит. 2'
'Частота графического процессора: 1295 МГц, которая может быть увеличена до 2430 МГц. 2'
'Эффективная частота памяти: 19,5 ГГц. 4'
'Пропускная способность памяти: 624 ГБ/с. 4'
'Вычислительная производительность (FP32): до 37,3 терафлопс. 4'
'Энергопотребление: до 263 Вт. 4'
'Разъёмы: один HDMI 2.1b, два DisplayPort 2.1 и один USB Type C. 4'
'Размеры: 267 мм x 111 мм x 50 мм. 2'
)

eee = ('Некоторые характеристики видеокарты AMD Radeon RX 7700 XT:'

'Графический процессор: Navi 32 в варианте Navi 32 XL. 1'
'Объём памяти: 12 ГБ, тип памяти — GDDR6. 1'
'Частота графического процессора: 1435 МГц, которая может быть увеличена до 2544 МГц. 1'
'Эффективная частота памяти: 18 ГГц. 3'
'Энергопотребление: до 245 Вт. 3'
'Разъёмы: один HDMI 2.1b, два DisplayPort 2.1 и один USB Type C. 3'
'Интерфейс: PCI-Express 4.0 x16. 1'
'Размеры: 267 мм x 135 мм x 50 мм. 1'
)

rrr = ('Некоторые характеристики видеокарты AMD Radeon RX 6750 GRE:'

'Версия Radeon RX 6750 GRE 10GB. Графический процессор Navi 22 с 36 исполнительными блоками, 2304 потоковыми процессорами и 36 блоками ускорения трассировки лучей. Базовая частота GPU — 2189 МГц, в режиме Boost чип работает на частоте до 2340 МГц. Энергопотребление — 170 Вт. Карта получила 10 Гбайт памяти GDDR6 с поддержкой 160-битной шины и скоростью 16 Гбит/с на контакт. В составе GPU — 80 Мбайт дополнительной кеш-памяти Infinity Cache. 1'
'Версия Radeon RX 6750 GRE 12GB. В составе чипа 40 исполнительных блоков с 2560 потоковыми процессорами, а также 40 блоков ускорения трассировки лучей. Базовая частота GPU — 2439 МГц, в режиме Boost чип работает на частоте 2581 МГц. Энергопотребление — 230 Вт. Карта получила 12 Гбайт памяти GDDR6 с поддержкой 192-битной шины и скоростью 16 Гбит/с на контакт. Дополнительно — 96 Мбайт кеш-памяти Infinity Cache.'
)

ttt = ('AMD Radeon RX 7900 XT — видеокарта энтузиастского класса от AMD, выпущенная 3 ноября 2022 года. 2'

'Некоторые характеристики:'

'Графический процессор: Navi 31 в варианте Navi 31 XT. 2'
'Объём памяти: 20 ГБ GDDR6 с 320-битной шиной и пропускной способностью 800 ГБ/с. 1'
'Вычислительная мощность: достигает 51,6 Гфлопс. 1'
'Частота ядра: 2025/2400 МГц. 3'
'Разъёмы: один HDMI 2.1b, два DisplayPort 2.1 и один USB Type C. 3'
'Энергопотребление: до 300 Вт. 3'
'Размеры: 276 мм x 110 мм x 51 мм. '
)
yyy = ('Некоторые характеристики видеокарты Sapphire PULSE Radeon RX 550 4GB:'

'графический процессор: AMD Radeon RX 550; 1'
'объём памяти: 4 ГБ GDDR5; 1'
'интерфейс памяти: 128 бит; 1'
'частота GPU: 1100 МГц (базовая), 1206 МГц (турбо); 1'
'количество ядер Stream: 512; 1'
'поддержка DirectX 12; 1'
'порты вывода: HDMI, DisplayPort, DVI-D; 1'
'максимальное поддерживаемое разрешение: 5120x2880; 2'
'количество поддерживаемых мониторов: 4; 2'
'длина: 158 мм; 2'
'размеры: 158 x 112 x 28 мм; 2'
'мощность: 50 Вт; 2'
'рекомендуемая мощность БП: 400 Вт'
)
uuu = ('Некоторые характеристики видеокарты GIGABYTE Radeon RX 6700 XT:'

'Техпроцесс: 7 нм. 4'
'Тип подключения: PCI Express 4.0. 4'
'Количество поддерживаемых мониторов: 4. 4'
'Максимальное разрешение: 7680x4320. 4'
'Частота видеопроцессора: 2424 МГц. 4'
'Частота памяти: 16000 МГц. 4'
'Объём видеопамяти: 12 ГБ. 4'
'Тип памяти: GDDR6. 4'
'Разрядность шины памяти: 192 бит. 4'
'Рекомендуемая мощность блока питания: 650 Вт. 4'
'TDP: 250 Вт. 4'
'Дизайн системы охлаждения: кастомный, количество вентиляторов — 3. 4'
'Длина: 282 мм. 4'
'Высота: 113 мм. 4'
'Толщина: 40 мм. 4'
'Количество занимаемых слотов: 2.' 
)
iii = ('екоторые характеристики видеокарты ASUS DUAL Radeon RX 580 OC 8GB (DUAL-RX580-O8G):'

'Объём видеопамяти: 8 ГБ. 4'
'Пиковая частота: 1380 МГц. 4'
'Тип видеопамяти: GDDR5. 4'
'Разрядность шины видеопамяти: 256 бит. 4'
'Видеоразъёмы: DisplayPort — 2, DVI — 1, HDMI — 2. 4'
'Интерфейс подключения: PCI-e 3.0. 4'
'Рекомендуемая мощность блока питания: 500 Вт. 4'
'Потребляемая мощность: 185 Вт. 4'
'Количество одновременно подключаемых мониторов: 4. 4'
'Максимальное разрешение: 7680x4320. 4'
'Система охлаждения: активная воздушная, количество вентиляторов — 2. 4'
'Размеры и вес: длина — 242 мм, ширина — 128,9 мм, толщина — 38 мм, вес — 1000 г. '
)
ooo = ('Некоторые характеристики видеокарты AMD Radeon RX 6800:'

'Частота графического процессора: 1925 МГц (2155 МГц, в режиме Boost). 1'
'Техпроцесс: 7 нм. 1'
'Объём видеопамяти: 16 ГБ GDDR6. 1'
'Частота видеопамяти: 16000 МГц. 1'
'Разрядность шины видеопамяти: 256 бит. 1'
'Разъёмы: Display Port х 3, HDMI х 1. 1'
'Питание: 8+8 pin, рекомендовано 650 Вт. 1'
'Максимальное энергопотребление: 250 Вт. 1'
'Размеры: длина видеокарты — 324 мм, высота — 140 мм, толщина — 55 мм. 1'
)

ppp = ('AMD Radeon RX 6600 XT — это высокопроизводительная видеокарта от AMD, выпущенная 30 июля 2021 года. 2'

'Некоторые характеристики:'

'Графический процессор: Navi 23 в варианте Navi 23 XT. 2'
'Техпроцесс: 7 нм. 2'
'Объём памяти: 8 ГБ, тип памяти — GDDR6. 2'
'Частота графического процессора: от 1968 (базовая) до 2589 МГц (турбо). 5'
'Энергопотребление: до 160 Вт. 5'
'Разъёмы: один HDMI 2.1, три DisplayPort 1.4a. 5'
'Подключение: к остальной части системы с помощью интерфейса PCI-Express 4.0 x8. 2'
'Размеры: 190 мм x 110 мм x 40 мм'
)
aaa = ('Некоторые характеристики видеокарты AMD Radeon RX 6800 XT:'

'Графический процессор: Navi 21, 7-нм техпроцесс. 14'
'Конфигурация ядра: 72 вычислительных блока по 64 шейдерных процессора (4608 всего), 72 блока трассировки лучей, 288 блоков выборки текстур, 128 блоков растеризации. 1'
'Объём видеопамяти: 16 ГБ GDDR6, ширина шины — 256 бит. 1'
'Кэш-память: 128 МБ кэш-памяти Infinity Cache. 1'
'Пропускная способность памяти: до 512 ГБ/с. 1'
'Вычислительная производительность: до 20,7 Тфлопс (FP32) и до 41,5 Тфлопс (FP16). 1'
'Энергопотребление: до 300 Вт. 2'
'Разъёмы: один HDMI 2.1, два DisplayPort 1.4a и один USB Type C. 2'
'Подключение: PCI-E 4.0 x 16. 1'
'Размеры: 267 мм x 120 мм x 50 мм'
)
sss =('Некоторые характеристики видеокарты AMD Radeon RX 6800'
'Частота ядра: игровая — 1815 МГц, пиковая — 2105 МГц. 2'
'Количество универсальных процессоров: 3840. 2'
'Количество текстурных блоков: 240. 2'
'Количество блоков блендинга: 96. 2'
'Эффективная частота памяти: 16 ГГц. 2'
'Тип памяти: GDDR6. 2'
'Шина памяти: 256-бит. 2'
'Объём памяти: 16 ГБ. 2'
'Пропускная способность памяти: 512 ГБ/с. 2'
'Вычислительная производительность (FP16): до 32,3 терафлопс. 2'
'Вычислительная производительность (FP32): до 16,2 терафлопс. 2'
'Теоретическая максимальная скорость закраски: 202 гигапикселей/с. 2'
'Теоретическая скорость выборки текстур: 505 гигатекселей/с. 2'
'Шина PCI Express 4.0. 2'
'Разъёмы: один HDMI 2.1, два DisplayPort 1.4a и один USB Type C. 2'
'Энергопотребление: до 250 Вт. 2'
'Дополнительное питание: два 8-контактных разъёма. 2'
'Число слотов, занимаемых в системном корпусе: 2'
)
ddd = ('Radeon RX 6900 XT — видеокарта энтузиастского класса от AMD, выпущенная 28 октября 2020 года. 1'

'Некоторые характеристики:'

'Графический процессор: Navi 21, 7-нм техпроцесс. 1'
'Объём памяти: 16 ГБ, тип памяти — GDDR6. 1'
'Частота графического процессора: 1825 МГц, которая может быть увеличена до 2250 МГц. 1'
'Энергопотребление: до 300 Вт. 2'
'Разъёмы: один HDMI 2.1, два DisplayPort 1.4a и один USB Type C. 2'
'Размеры: 267 мм x 120 мм x 50 мм. 1'
'Система охлаждения: с тремя слотами.'
)
qqq1 = 'Некоторые характеристики процессора AMD Ryzen 5 7600:Количество ядер: 6. 13Количество потоков: 12. 13Базовая частота: 3,8 ГГц. 13Максимальная частота в режиме Turbo: 5,1 ГГц. 3Объём кэша L2: 6 МБ. 1Объём кэша L3: 32 МБ. 13Тип памяти: DDR5. 14Максимальный объём памяти: 128 ГБ. 14Базовая мощность процессора: 105 Вт. 1Максимальная температура процессора: 95 °C. 1Интегрированное графическое ядро: есть, модель AMD Radeon Graphics, максимальная частота графического ядра — 2200 МГц'
www1 = 'Ryzen 9 7900 - десктопный процессор от компании AMD для сокета AM5, который имеет 12 ядер и 24 потока. Его базовая частота – 3700 МГц, но поддержка технологии Turbo Core позволяет автоматически разгоняться до 5400 МГц. Данный чип имеет интегрированную графику Radeon Graphics (Ryzen 7000), а размер кэша 3-го уровня составляет 64 МБ.'

eee1 = 'Некоторые характеристики процессора AMD Ryzen 5 5600X:Архитектура: Vermeer. 1Техпроцесс: 7 нм. 1Количество физических ядер: 6. 1Количество виртуальных потоков: 12. 1Диапазон рабочих частот: от 3,7 до 4,6 ГГц. 1Максимальный объём оперативной памяти: 128 ГБ типа DDR4. 1Встроенный контроллер PCI-E: версии 4.0. 1Максимальное тепловыделение: 65 Вт. Температура при максимальной нагрузке может достигать 95 °C. 1Поддержка систем охлаждения: модель поддерживает различные системы водяного и воздушного охлаждения'

rrr1 = 'Некоторые характеристики процессора AMD Ryzen 9 7950X:Ядро и архитектура: архитектура Zen, количество ядер — 16, количество потоков — 32. 1Кэш L3: 64 МБ. 1Техпроцесс: 5 нм. 1Интегрированное графическое ядро: есть, модель — Radeon Graphics, максимальная частота — 2200 МГц. 2Оперативная память: тип — DDR5, максимальный объём ОЗУ — 128 ГБ, максимальная частота оперативной памяти — 5200 МГц. 1Тепловыделение: 170 Вт. 1Максимальная рабочая температура процессора: 95 °C. 1Поддержка интерфейсов: PCI-E 5 поколения. 1Установка на материнскую плату: при помощи сокета AM5'


ttt1 ='Ryzen 7 8700G - десктопный процессор от компании Amd для сокета AM5, который имеет 8 ядер и 16 потоков. Его базовая частота – 4300 МГц, но поддержка технологии Turbo Core позволяет автоматически разгоняться до 5100 МГц. Данный чип имеет интегрированную графику Radeon 780M, а размер кэша 3-го уровня составляет 16 МБ.'

yyy1 ='Ryzen 5 8600G - десктопный процессор от компании Amd для сокета AM5, который имеет 6 ядер и 12 потоков. Его базовая частота – 4300 МГц, но поддержка технологии Turbo Core позволяет автоматически разгоняться до 5000 МГц. Данный чип имеет интегрированную графику Radeon 760M, а размер кэша 3-го уровня составляет 16 МБ.'


uuu1 = 'Процессор разблокирован для оверклокинга. Общее количество ядер - 96, потоков - 192. Максимальная тактовая частота процессора - 5.1 GHz. Максимальная температура - 95°C. Технологический процесс - 5 nm. Размер кэша: L1 - 64 KB (per core), L2 - 1 MB (per core), L3 - 384 MB (shared).'

iii1 = 'Некоторые характеристики процессора AMD Ryzen 5 7500F OEM:Сокет: AM5. 14Ядро: Raphael. 1Число ядер: 6. 1Число потоков: 12. 1Базовая частота: 3,7 ГГц. 1Максимальная частота: 5 ГГц. 1Частота оперативной памяти: 3600, 5200 МГц. 1Максимальный объём ОЗУ: 128 ГБ. 1Тип памяти: DDR5. 1Техпроцесс: 5 нм. 1Объём кэша L1: 384 КБ. 1Объём кэша L2: 6 МБ. 1Объём кэша L3: 32 МБ. 1TDP (тепловыделение): 65 Вт. 1Максимальная температура: 95 °C. 1Система охлаждения: не включена. 1Поддержка ОС: RHEL x86, 64-разрядная, Ubuntu x86, 64-разрядная, Windows 10, 64-разрядная версия, Windows 11, 64-разрядная версия.'


ooo1 = 'Некоторые характеристики процессора AMD Ryzen 5 7600 OEM: Ядро: AMD Raphael. 1Количество ядер: 6. 1Количество потоков: 12. 1Базовая частота: 3,8 ГГц. 1Частота в режиме Turbo: 5,1 ГГц. 1Объём кэша L2: 6 МБ. 1Объём кэша L3: 32 МБ. 1Тип памяти: DDR 5. 1Максимальное число каналов памяти: 2. 1Максимальная пропускная способность памяти: 41,6 ГБ/с. 1Максимальный объём памяти (зависит от типа памяти): 128 ГБ. 1Базовая мощность процессора: 105 Вт. 1Максимальная температура процессора: 95 °C. 1Интегрированное графическое ядро: есть, модель AMD Radeon Graphics. 1Максимальная частота графического ядра: 2200 МГц.'


ppp1 = 'Ryzen 9 7950X3D Ryzen 9 7950X Ядра 16 16 Потоки 32 32 Частота, ГГц 4,2-5,7 4,5-5,7 TDP, Вт 120 170 Макс. потребление, Вт 162 230 L3-кеш, Мбайт 96+32 32+32 Память DDR5-5200 DDR5-5200 Встроенная графика RDNA 2 (2Cu) RDNA 2 (2Cu) PCIe 24 × PCIe 5.0 24 × PCIe 5.0 Сокет AM5 AM5 Стартовая цена $699 $699 Впрочем, на практике частотная формула Ryzen 9 7950X3D всё-таки хуже, чем у классического Ryzen 9 7950X.'

aaa1 = 'Процессор AMD Ryzen 3 4100 AM4, 4 x 3800 МГц. На Маркете: socket: AM4, линейка процессоров: AMD Ryzen 3, количество ядер: 4, техпроцесс: 7 нм, частота процессора: 3800 МГц, тип памяти: DDR4, ядро: Renoir, Объем кэша L3: 4 МБ, тепловыделение: 65 Вт, игровой. Общие характеристики. Q2 2022 Ядро. Zen 2 8 128 2 шт. Частота. 4000 МГц Кэш. 256 КБ 2 МБ Дополнительно. 95 C 3.0. SSE / Streaming SIMD Extensions.'

ssd1 = 'Socket: AM4Количество ядер: 6Тактовая частота: 3600 МГцЧастота процессора в режиме Turbo: 4100 МГцЯдро: RenoirОбъём кэша L2: 3 МбОбъём кэша L3: 8 МбТехнологический процесс: 7 нмТипичное тепловыделение: 65 Вт'

ddd1 = 'Некоторые характеристики процессора AMD Ryzen 5 5500:Архитектура: Zen 3. 23Количество ядер: 6. 23Базовая тактовая частота: 3,6 ГГц. 23 Может быть увеличена с помощью технологии Precision Boost до 4,2 ГГц. 2Объём кэша L2: 3 МБ. 2Объём кэша L3: 16 МБ. 2Поддержка технологии SMT: есть, что позволяет процессору обрабатывать больше задач одновременно. 2Тип сокета: AM4. 3Техпроцесс: 7 нм. 23Максимальный объём памяти: 128 ГБ. 3Базовая мощность процессора: 65 Вт. Мощность в режиме Turbo — 88 Вт. 3Максимальная температура процессора: 90 °C'

hhh1 = 'Некоторые характеристики процессора AMD Ryzen 5 7600X:Количество ядер: 6. 24Количество потоков: 12. 24Базовая частота: 4,7 ГГц. 4Максимальная частота: 5,3 ГГц. 4Объём кэша L1: 384 Кб. 4Объём кэша L2: 6 Мб. 4Объём кэша L3: 32 Мб. 4Максимальный объём оперативной памяти: 128 ГБ. 24Поддерживаемая частота оперативной памяти: 5200 МГц. 4Интегрированное графическое ядро: есть, модель Radeon Graphics, максимальная частота 2200 МГц. 34Тепловыделение: 105 Вт. 34Критическая температура: 95 °С'

fff1 = 'Некоторые характеристики процессора AMD Ryzen 7 7700X:Назначение: настольный ПК. 1Ядро: Raphael. 1Техпроцесс: 5 нм с транзисторами FinFET. 1Частота работы: 4,5 ГГц или до 5,4 ГГц в режиме Precision Boost. 1Количество ядер: 8. 1Количество потоков: 16. Кэш L1: 64 Кб x8. 1Кэш L2: 1024 Кб x8. 1Кэш L3: 32 Мб. 1Максимальный объём оперативной памяти: 128 Гб. 1Поддержка ECC: есть. 1Рассеиваемая мощность: 105 Вт. 1Критическая температура: 95 °С. 1Встроенная видеокарта: видеоядро процессора AMD Radeon Graphics (Raphael), частота видеопроцессора — максимум 2200 МГц'

hh11 = 'Серия:AMD Ryzen 7Тип разъема (Socket):AM4Ядро:Vermeer (Zen 3)Количество ядер:8 ядерКоличество потоков:16 потоковЧастота в турбо режиме (ГГц):4.7 ГГцНоминальная частота (ГГц):3.8 ГГцТехпроцесс:7 НмНоминальный множитель:38Кэш L1:8x32, 8x32 КбКэш L2:8x512 КбКэш L3:32 МбГрафическое ядро:нетРассеиваемая мощность:105 Вт'


jjj1 = 'Ryzen 7 3800X - десктопный процессор от компании Amd для сокета AM4, который имеет 8 ядер и 16 потоков. Его базовая частота – 3900 МГц, но поддержка технологии Turbo Core позволяет автоматически разгоняться до 4500 МГц. Данный чип не имеет интегрированной графики, а размер кэша 3-го уровня составляет 32 МБ.'


kkk1 = 'Некоторые характеристики процессора AMD Ryzen 7 PRO 3700:Архитектура: Matisse. 1Количество ядер: 8. 14Количество потоков: 16. 14Базовая частота: 3,6 ГГц. 14Максимальная частота: 4,4 ГГц. 4Объём кэша L1: 512 КБ. 4Объём кэша L2: 4 МБ. 4Объём кэша L3: 32 МБ. 4Тип поддерживаемой оперативной памяти: DDR4. 3Максимальный объём памяти: 128 ГБ. 3Поддерживаемая частота оперативной памяти: 1600–3200 МГц. Максимальная рабочая температура: 95 °C. 4Тепловыделение (TDP): 65 Вт'

lll1 = 'Некоторые характеристики процессора AMD Ryzen 5 5600X:Архитектура: Vermeer, техпроцесс 7 нм. 1Количество физических ядер: 6. 1Количество виртуальных потоков: 12. 1Диапазон рабочих частот: от 3,7 до 4,6 ГГц. 1Максимальный объём оперативной памяти: 128 ГБ типа DDR4. 1Встроенный контроллер PCI-E: версия 4.0. 1Максимальное тепловыделение: 65 Вт. 1Температура при максимальной нагрузке: может достигать 95 °C. '

zzz1 = 'Некоторые характеристики процессора AMD Ryzen 5 3600X:Количество ядер и потоков: 6/12. 3Базовая частота: 3,8 ГГц. 2 В турборежиме частота возрастает до 4,4 ГГц. 4Объём кэш-памяти: L1 — 64 Кб, L2 — 3 Мб, L3 — 32 Мб. 1Поддержка памяти: DDR4-3200. Максимальный объём оперативной памяти — 128 ГБ. 3Техпроцесс: 7 нм. 3Тепловыделение (TDP): 95 Вт. 3Максимальная рабочая температура процессора: 95 °C'


xxx1 = 'Некоторые характеристики процессора AMD Ryzen 9 5950X:Оперативная память: тип — DDR4, максимальный объём ОЗУ — 128 ГБ, максимальная частота оперативной памяти — 3200 МГц. 1Ядро и архитектура: архитектура Zen, 16 ядер, 32 потока. 12Кэш L3: 64 МБ. 12Базовая частота: 3,4 ГГц. 12Турбо-частота: 4,9 ГГц. 12Тепловыделение: 105 Вт. 14Максимальная рабочая температура процессора: 90 °C. 1Поддержка памяти: DDR4, поддержка памяти ECC. 2Взаимодействие с другими компонентами компьютера: соединение PCI-Express Gen 4. 2Встроенная графика: отсутствует, потребуется отдельная видеокарта.' 

ccc1 = 'Некоторые характеристики процессора AMD Ryzen 5 5600X:Архитектура: Vermeer. 1Техпроцесс: 7 нм. 1Количество физических ядер: 6. 1Количество виртуальных потоков: 12. 1Диапазон рабочих частот: от 3,7 до 4,6 ГГц. 1Максимальный объём оперативной памяти: 128 ГБ типа DDR4. 1Встроенный контроллер PCI-E: версия 4.0. 1Максимальное тепловыделение: 65 Вт. 1Температура при максимальной нагрузке: может достигать 95 °C'

vvv1 = 'Некоторые характеристики процессора AMD Ryzen 7 5800X:Количество ядер: 8. 24Количество потоков: 16. 24Базовая частота: 3,8 ГГц. 24Частота в турбо-режиме: 4,7 ГГц. 2Объём кэша L3: 32 МБ. 2Тип памяти: DDR4, 3200 МБ. 2Заявленный TDP: 105 Вт. 2Поддержка интерфейса PCI-Express: PCI-E 4.0, 20 линий. 2Интегрированное графическое ядро: нет.' 

bbb1 = 'Некоторые характеристики процессора AMD Ryzen 9 5900X BOX:Количество ядер: 12. 13Количество потоков: 24. 13Базовая частота: 3,7 ГГц. 13Максимальная частота: 4,8 ГГц. 13Объём кэша L1: 768 КБ. 13Объём кэша L2: 6 МБ. 13Объём кэша L3: 64 МБ. 13Частота системной шины: 100 МГц. 1Тепловыделение (TDP): 105 Вт. 13Максимальная рабочая температура процессора: 90 °C. 3Максимальный объём оперативной памяти: 128 ГБ. 13Поддерживаемая частота оперативной памяти: 3200 МГц'


nnn1 = 'Некоторые характеристики процессора AMD Ryzen 9 5950X:Оперативная память: тип — DDR4, максимальный объём ОЗУ — 128 ГБ, максимальная частота оперативной памяти — 3200 МГц. 1Ядро и архитектура: архитектура Zen, 16 ядер, 32 потока. 1Кэш L3: 64 МБ. 1Техпроцесс: 7 нм. 1Базовая частота: 3,4 ГГц. 1Турбо-частота: 4,9 ГГц. 1Тепловыделение: 105 Вт. 1Максимальная рабочая температура процессора: 90 °C. 1Поддержка памяти: DDR4, поддержка памяти ECC. 2Встроенная графика: отсутствует. 3Поддержка PCIe: PCIe 4.0.' 





ggg1 = 'Некоторые характеристики процессора AMD Ryzen 7 5800X3D:Архитектура: Vermeer. 2Базовая частота: 3,4 ГГц. 2Турбо-частота: 4,5 ГГц. 2Количество ядер: 8. 2Количество потоков: 16. 2Кэш L3: 96 МБ. 2Техпроцесс: 7 нм. 2Кэш L1: 512 КБ. 2Кэш L2: 4000 КБ. 2Тепловыделение: 105 Вт. 2Максимальная рабочая температура процессора: 90 °С. 2Совместимость с оперативной памятью: DDR4, максимальная частота — 3200 МГц, объём — 128 ГБ. 2Наличие встроенной графики: нет.'

TOKEN = '7505424553:AAH-gnl9ZaxiISnOE2OukqAKePcWWy4GZL8'

bot = TeleBot(TOKEN)





keyboard = types.InlineKeyboardMarkup()
button_link = types.InlineKeyboardButton("Amd", callback_data="amd")
button_link2 = types.InlineKeyboardButton("Inte", callback_data="Inte")
keyboard.add(button_link,button_link2)



keyboard1 = types.InlineKeyboardMarkup()
button_link3 = types.InlineKeyboardButton("процесор", callback_data="romm")
button_link4 = types.InlineKeyboardButton("видокарта", callback_data="qaz")
keyboard1.add(button_link3,button_link4)


keyboard2 = types.InlineKeyboardMarkup()
button_link5 = types.InlineKeyboardButton("2024", callback_data="q")
button_link6 = types.InlineKeyboardButton("2023", callback_data="w")
button_link7 = types.InlineKeyboardButton("2022", callback_data="e")
button_link8 = types.InlineKeyboardButton("2021", callback_data="r")
button_link9 = types.InlineKeyboardButton("2020", callback_data="t")
keyboard2.add(button_link5, button_link6,button_link7,button_link8, button_link9)

keyboard99 = types.InlineKeyboardMarkup()
button_link013 = types.InlineKeyboardButton("2024", callback_data="q130")
button_link613 = types.InlineKeyboardButton("2023", callback_data="w1")
button_link713 = types.InlineKeyboardButton("2022", callback_data="e1")
button_link813 = types.InlineKeyboardButton("2021", callback_data="r1")
button_link913 = types.InlineKeyboardButton("2020", callback_data="t1")
keyboard99.add(button_link013, button_link613,button_link713,button_link813, button_link913)

keyboard299 = types.InlineKeyboardMarkup()
button_link51 = types.InlineKeyboardButton("AMD Ryzen 5 7600", callback_data="q11")
button_link61 = types.InlineKeyboardButton("AMD Ryzen 9 7900", callback_data="w11")
button_link81 = types.InlineKeyboardButton("AMD Ryzen 5 5600X", callback_data="e11")
button_link91 = types.InlineKeyboardButton("AMD Ryzen 9 7950X", callback_data="r11")
button_link101 = types.InlineKeyboardButton("AMD Ryzen 7 8700G", callback_data="t11")
button_link111 = types.InlineKeyboardButton("AMD Ryzen 5 8600G", callback_data="y11")
button_link121 = types.InlineKeyboardButton("AMD Ryzen Threadripper Pro 7995WX", callback_data="u11")
keyboard299.add(button_link51, button_link61,button_link81,button_link91, button_link101, button_link111, button_link121)

keyboard399 = types.InlineKeyboardMarkup()
button_link132 = types.InlineKeyboardButton("AMD Ryzen 5 7500F OEM", callback_data="i11")
button_link142 = types.InlineKeyboardButton("AMD Ryzen 5 7600 OEM", callback_data="o11")
button_link152 = types.InlineKeyboardButton("AMD Ryzen 9 7950X3D OEM", callback_data="p11")
keyboard399.add(button_link132, button_link142,button_link152)

keyboard499 = types.InlineKeyboardMarkup()
button_link141 = types.InlineKeyboardButton("AMD Ryzen 3 4100", callback_data="a11")
button_link151 = types.InlineKeyboardButton("AMD Ryzen 5 4500", callback_data="s11")
button_link161 = types.InlineKeyboardButton("AMD Ryzen 5 5500", callback_data="d11")
button_link171 = types.InlineKeyboardButton("AMD Ryzen 5 7600X.", callback_data="f11")
button_link181 = types.InlineKeyboardButton("AMD Ryzen 7 7700X", callback_data="g11")
button_link191 = types.InlineKeyboardButton("AMD Ryzen 7 5800X3D", callback_data="h11")
keyboard499.add(button_link141, button_link151,button_link161,button_link171, button_link181, button_link191)

keyboard599 = types.InlineKeyboardMarkup()
button_link201 = types.InlineKeyboardButton("Ryzen 7 5800X", callback_data="j11")
button_link211 = types.InlineKeyboardButton("Ryzen 7 3800X", callback_data="k11")
button_link221 = types.InlineKeyboardButton("Ryzen 7 PRO 3700", callback_data="l11")
button_link231 = types.InlineKeyboardButton("Ryzen 5 5600X", callback_data="z11")
button_link241 = types.InlineKeyboardButton("Ryzen 5 3600X", callback_data="x11")
button_link251 = types.InlineKeyboardButton("Ryzen 9 5950X", callback_data="c11")
keyboard599.add(button_link201, button_link211,button_link221,button_link231, button_link241)

keyboard699 = types.InlineKeyboardMarkup()
button_link261 = types.InlineKeyboardButton("Ryzen 5 5600X", callback_data="v11")
button_link271 = types.InlineKeyboardButton("Ryzen 7 5800X", callback_data="b11")
button_link281 = types.InlineKeyboardButton("Ryzen 7 5900X", callback_data="n11")
button_link291 = types.InlineKeyboardButton("Ryzen 9 5950X", callback_data="m11")
keyboard699.add(button_link261, button_link271,button_link281,button_link291)



keyboard3 = types.InlineKeyboardMarkup()
button_link10 = types.InlineKeyboardButton("Radeon RX 7900 XTX", callback_data="z")
button_link11 = types.InlineKeyboardButton("Radeon RX 7800 XT", callback_data="x")
button_link12 = types.InlineKeyboardButton("Radeon RX 7700 XT", callback_data="c")
keyboard3.add(button_link10, button_link11, button_link12)

keyboard4 = types.InlineKeyboardMarkup()
button_link13 = types.InlineKeyboardButton("AMD Radeon RX 6750 GRE", callback_data="a")
keyboard4.add(button_link13)

keyboard5 = types.InlineKeyboardMarkup()
button_link14 = types.InlineKeyboardButton("RX 7900 XT ", callback_data="s")
keyboard5.add(button_link14)

keyboard6 = types.InlineKeyboardMarkup()
button_link15 = types.InlineKeyboardButton("Radeon RX 550 4GB", callback_data="d")
button_link16 = types.InlineKeyboardButton("Radeon RX 6700 XT", callback_data="f")
button_link17 = types.InlineKeyboardButton("ASUS DUAL Radeon RX 580 OC 8GB", callback_data="g")
button_link18 = types.InlineKeyboardButton("AMD Radeon RX 6800", callback_data="h")
button_link19 = types.InlineKeyboardButton("AMD Radeon RX 6600 XT", callback_data="j")
keyboard6.add(button_link15, button_link16, button_link17, button_link18, button_link19)

keyboard7 = types.InlineKeyboardMarkup()
button_link20 = types.InlineKeyboardButton("Radeon RX 6800 XT", callback_data="k")
button_link21 = types.InlineKeyboardButton("Radeon RX 6800", callback_data="l")
button_link22 = types.InlineKeyboardButton("Radeon RX 6900 XT", callback_data="m")
keyboard7.add(button_link20, button_link21, button_link22)




@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id, 
        'Нажмите кнопку, чтобы показать информацию:', 
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "amd":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта или процесор", reply_markup=keyboard1)
    if call.data == "qaz":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите год", reply_markup=keyboard2)

    if call.data == "q":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта", reply_markup=keyboard3)
    if call.data == "w":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта", reply_markup=keyboard4)
    if call.data == "e":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта", reply_markup=keyboard5)
    if call.data == "r":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта", reply_markup=keyboard6)
    if call.data == "t":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите видокарта", reply_markup=keyboard7)
    if call.data == "z":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{qqq}')
    if call.data == "x":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{www}')
    if call.data == "c":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{eee}')
    if call.data == "a":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{rrr}')
    if call.data == "s":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ttt}')
    if call.data == "d":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{yyy}')
    if call.data == "f":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{uuu}')
    if call.data == "g":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{iii}')
    if call.data == "h":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ooo}')
    if call.data == "j":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ppp}')
    if call.data == "k":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{aaa}')
    if call.data == "l":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{sss}')
    if call.data == "m":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ddd}')
     

    if call.data == "romm":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите год", reply_markup=keyboard99)
    if call.data == "q130":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите процесор", reply_markup=keyboard299)
    if call.data == "w1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите процесор", reply_markup=keyboard399)
    if call.data == "e1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите процесор", reply_markup=keyboard499)
    if call.data == "r1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите процесор", reply_markup=keyboard599)
    if call.data == "t1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text="выбирите процесор", reply_markup=keyboard699)
    
    if call.data == "q11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{qqq1}')
    if call.data == "w11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{www1}')
    if call.data == "e11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{eee1}')
    if call.data == "r11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{rrr1}')
    if call.data == "t11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ttt1}')
    if call.data == "y11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{yyy1}')
    if call.data == "u11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{uuu1}')
   
    if call.data == "i11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{iii1}')
    if call.data == "o11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ooo1}')
    if call.data == "p11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ppp1}')
    
    
    if call.data == "a11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{aaa1}')
    if call.data == "s11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ssd1}')
    if call.data == "d11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ddd1}')
    if call.data == "f11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{hhh1}')
    if call.data == "g11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{fff1}')
    if call.data == "h11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ggg1}')
        
    if call.data == "j11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{hh11}')
    if call.data == "k11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{jjj1}')
    if call.data == "l11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{kkk1}')
    if call.data == "z11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{lll1}')
    if call.data == "x11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{zzz1}')
    if call.data == "c11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{xxx1}')

    if call.data == "v11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{ccc1}')
    if call.data == "b11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{vvv1}')
    if call.data == "n11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{bbb1}')
    if call.data == "m11":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                         text=f'{nnn1}')


print('Сервер запущен')
bot.polling()