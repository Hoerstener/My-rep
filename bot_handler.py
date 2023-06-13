from datetime import datetime
import telebot


# Получение меню на завтрак/обед/ужин для указанной программы и текущего времени дня
def get_menu(program, day_of_week, time_of_day):
    if program == 'Снижение веса':
        if day_of_week == 0:  # Понедельник
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Омлет из 2 яиц с овощами (помидоры, шпинат), греческий йогурт с орехами.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Запеченная куринная грудка с овощами (брокколи, морковь, цветная капуста).'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Паровая рыба с картофельным пюре и салатом из свежих овощей.'
        elif day_of_week == 1:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Миндальное молоко с овсянкой, ягоды (ежевика, малина), орехи. '
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Греческий салат с кускусом и фетой.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Куриные шашлыки с овощным грилем (паприка, цукини, лук).'
        elif day_of_week == 2:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Тост из цельнозернового хлеба с авокадо и яйцом, свежий апельсиновый сок. '
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Тушеные овощи с тушеным красным мясом (говядина).'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Омлет с шампиньонами и зеленью, салат из свежих овощей.'
        elif day_of_week == 3:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Зеленый смузи (шпинат, банан, морковь), яблоки. '
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Тушеные куриные грудки с овощным рагу (баклажаны, перцы, лук).'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Греческий йогурт с ягодами и медом.'
        elif day_of_week == 4:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Каша из гречки с орехами и сухофруктами.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Рисовые лепешки с тунцом и авокадо.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Тыквенный суп с курицей, овощной салат.'
        elif day_of_week == 5:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Омлет из белков с шпинатом, тост из цельнозернового хлеба.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Салат с тунцом, оливками, свежими овощами и лимонным соусом.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Тушеная рыба с овощами (брокколи, морковь).'
        elif day_of_week == 6:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Творог с ягодами и орехами. '
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Греческий салат с кускусом и креветками.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Куриные котлеты с овощным рататуем.'
    elif program == 'Набор массы':
        if day_of_week == 0:  # Понедельник
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Омлет из 3 яиц с овощами (шпинат, помидоры), цельнозерновый тост с авокадо.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Гриль-куринная грудка с картофельными ломтиками и овощным салатом.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Жареная рыба с киноа и запеченными овощами.'
        elif day_of_week == 1:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Греческий йогурт с орехами, ягодами и медом. '
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Стейк из говядины с картофельным пюре и овощами (брокколи, морковь).'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Паста из цельнозерновой муки с куриным филе и томатным соусом.'
        elif day_of_week == 2:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Бананово-шоколадный смузи с овсянкой и орехами.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Куриные котлеты с рисом и овощным рагу.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Стейк из лосося с картофельными кусочками и паровой брокколи.'
        elif day_of_week == 3:
            if time_of_day == 'завтрак':  # Завтрак
                menu = 'Завтрак: Тост из цельнозернового хлеба с кунжутной пастой и ломтиками курицы.'
            elif time_of_day == 'обед':  # Обед
                menu = 'Обед: Греческий салат с тунцом, оливками и фетой.'
            elif time_of_day == 'ужин':  # Ужин
                menu = 'Ужин: Говяжий гуляш с картофельным пюре и свежими овощами.'
        elif day_of_week == 4:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Омлет из 4 яиц с сыром и овощами (шпинат, перец, лук).'
            elif time_of_day == 'обед':
                menu = 'Обед: Тушеная индейка с киноа и овощным салатом.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Жареные креветки с картофельным гратеном и запеченными овощами.'
        elif day_of_week == 5:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Творожная запеканка с ягодами и медом.'
            elif time_of_day == 'обед':
                menu = 'Обед: Стейк из свинины с картофельными дольками и овощным грилем.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Рыбные котлеты с картофельным пюре и паровой брокколи.'
        elif day_of_week == 6:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Омлет с тунцом и овощами (помидоры, шпинат).'
            elif time_of_day == 'обед':
                menu = 'Обед: Говяжья пастрами с картофельным гратеном и овощным рагу.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Куриная грудка запеченная с овощами (цветная капуста, брокколи, морковь).'
    elif program == 'Поддержание формы':
        if day_of_week == 0:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Омлет из 2 яиц с овощами (помидоры, шпинат), цельнозерновый тост с маслом.'
            elif time_of_day == 'обед':
                menu = 'Обед: Куринная грудка на гриле с салатом из свежих овощей.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Треска запеченная в духовке с овощным гарниром (брокколи, морковь, цветная капуста).'
        elif day_of_week == 1:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Овсянка с ягодами и орехами.'
            elif time_of_day == 'обед':
                menu = 'Обед: Греческий салат с фетой и оливками.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Куриные шашлыки с овощным грилем (паприка, цукини, лук).'
        elif day_of_week == 2:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Тост из цельнозернового хлеба с авокадо и яйцом, свежий апельсиновый сок.'
            elif time_of_day == 'обед':
                menu = 'Обед: Паста из цельнозерновой муки с овощами (помидоры, шпинат) и лимонным соусом.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Тушеные овощи с красным мясом (говядина).'
        elif day_of_week == 3:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Греческий йогурт с ягодами и медом.'
            elif time_of_day == 'обед':
                menu = 'Обед: Салат с тунцом, свежими овощами и оливковым маслом.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Паровая рыба с овощным рагу (баклажаны, перцы, лук).'
        elif day_of_week == 4:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Каша из гречки с орехами и сухофруктами.'
            elif time_of_day == 'обед':
                menu = 'Обед: Цельнозерновые лепешки с курицей и авокадо.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Суп из овощей и курицы, свежий овощной салат.'
        elif day_of_week == 5:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Омлет из белков с шпинатом, тост из цельнозернового хлеба.'
            elif time_of_day == 'обед':
                menu = 'Обед: Салат с тунцом, оливками, свежими овощами и лимонным соусом.'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Тушеные овощи с куриным филе.'
        elif day_of_week == 6:
            if time_of_day == 'завтрак':
                menu = 'Завтрак: Творог с ягодами и орехами. '
            elif time_of_day == 'обед':
                menu = 'Обед: Куриная грудка на гриле с овощным гарниром (брокколи, морковь, цветная капуста).'
            elif time_of_day == 'ужин':
                menu = 'Ужин: Паровая рыба с свежими овощами и лимонным соусом.'
    return menu


# Получение задачи для тренировки для указанной программы и текущего дня недели
def get_training_task(program, day_of_week):
    if program == 'Снижение веса':
        if day_of_week == 0:
            task = 'День 1: Кардио и силовые тренировки\n- 30-40 минут интенсивной кардио-тренировки, такой как бег, плавание или езда на велосипеде.\n- 20-30 минут силовых упражнений для всех основных групп мышц (например, приседания, отжимания, подтягивания и упражнения на пресс).'
        elif day_of_week == 1:
            task = 'День 2: Аэробные упражнения и йога\n- 40-60 минут аэробных упражнений на выбор: бег, ходьба быстрым шагом, зумба или эллиптический тренажер.\n- 30-40 минут йоги или пилатеса для растяжки и силы.'
        elif day_of_week == 2:
            task = 'День 3: Отдых\n- Позволь своему организму восстановиться и отдохнуть. Можешь сделать легкую прогулку или заняться другими активностями низкой интенсивности, чтобы оставаться в движении.'
        elif day_of_week == 3:
            task = 'День 4: Кардио и функциональные тренировки\n- 30-40 минут кардио-тренировки: бег, прыжки на скакалке или велосипедная тренировка.\n- 20-30 минут функциональных упражнений, таких как выпады, подтягивания на перекладине, подъемы ног или планка.'
        elif day_of_week == 4:
            task = 'День 5: Интервальная тренировка и йога\n- 30-40 минут интервальной тренировки: чередуй высокоинтенсивные упражнения (например, скакалка, бурпи или бег на месте) с короткими периодами активного отдыха.\n- 30-40 минут йоги для растяжки и укрепления мышц.'
        elif day_of_week == 5:
            task = 'День 6: Кардио и силовые тренировки\n- 40-60 минут кардио-тренировки на выбор: бег, плавание или езда на велосипеде.\n- 20-30 минут силовых упражнений для всех основных групп мышц, таких как приседания, жимы, подтягивания и упражнения на пресс.'
        elif day_of_week == 6:
            task = 'День 7: Активный отдых и растяжка\n- Проведи день на активном отдыхе, например, семейная прогулка, пеший туризм или игры на открытом воздухе. - Закончи день растяжкой и релаксационными упражнениями для мышц и суставов.'
    elif program == 'Поддержание формы':
        if day_of_week == 0:
            task = 'День 1: Кардио и силовые тренировки\n- 30-40 минут интенсивной кардио-тренировки, такой как бег, плавание или езда на велосипеде.\n- 20-30 минут силовых упражнений для всех основных групп мышц (например, приседания, отжимания, подтягивания и упражнения на пресс).'
        elif day_of_week == 1:
            task = 'День 2: Аэробные упражнения и гибкость\n- 40-60 минут аэробных упражнений на выбор: бег, ходьба быстрым шагом, зумба или эллиптический тренажер.\n- 20-30 минут гибкостных упражнений, таких как йога или пилатес, для растяжки и улучшения гибкости.'
        elif day_of_week == 2:
            task = 'День 3: Отдых и релаксация\n- Позвольте своему организму восстановиться и отдохнуть. Можете заняться легкой прогулкой, медитацией или другими активностями, которые помогут вам расслабиться.'
        elif day_of_week == 3:
            task = 'День 4: Комбинированные тренировки\n- 20-30 минут кардио-тренировки: бег, прыжки на скакалке или велосипедная тренировка\n- 20-30 минут силовых упражнений с использованием гантелей или собственного веса тела.\n- 10-15 минут упражнений на силу и гибкость для мышц кора (core), таких как планка или вращения туловища.'
        elif day_of_week == 4:
            task = 'День 5: Активный отдых\n- Займитесь активными видами отдыха, такими как прогулка на природе, велосипедная поездка или игры на свежем воздухе.'
        elif day_of_week == 5:
            task = 'День 6: Кардио и силовые тренировки\n- 30-40 минут кардио-тренировки на выбор: бег, плавание или езда на велосипеде.\n- 20-30 минут силовых упражнений для всех основных групп мышц.'
        elif day_of_week == 6:
            task = 'День 7: Йога и растяжка\n- 40-60 минут йоги или пилатеса для улучшения гибкости, силы и релаксации.'
    elif program == 'Набор массы':
        if day_of_week == 0:
            task = 'День 1: Силовые тренировки верхней части тела\n- Жим штанги на грудь: 3-4 подхода по 8-10 повторений.\n- Тяга штанги в наклоне: 3-4 подхода по 8-10 повторений.\n- Армейский жим: 3-4 подхода по 8-10 повторений.\n- Шаги со штангой: 3-4 подхода по 10-12 повторений.\n- Разгибания рук со штангой: 3-4 подхода по 10-12 повторений.'
        elif day_of_week == 1:
            task = 'День 2: Кардио и ноги\n- 20-30 минут интенсивной кардио-тренировки, такой как бег, эллиптический тренажер или скакалка.\n- Приседания со штангой: 3-4 подхода по 8-10 повторений.\n- Жим ноги на тренажере: 3-4 подхода по 8-10 повторений.\n- Жим на икры: 3-4 подхода по 10-12 повторений.\n- Ходьба на подъеме: 3-4 подхода по 10-12 повторений.'
        elif day_of_week == 2:
            task = 'День 3: Отдых\n- Позвольте своему организму восстановиться и отдохнуть. Можете сделать легкую прогулку или заняться другими активностями низкой интенсивности, чтобы оставаться в движении.'
        elif day_of_week == 3:
            task = 'День 4: Силовые тренировки нижней части тела\n- Жим ногами на Smith-тренажере: 3-4 подхода по 8-10 повторений.\n- Выпады со штангой: 3-4 подхода по 8-10 повторений.\n- Румынская тяга со штангой: 3-4 подхода по 8-10 повторений.\n- Жим на икры на тренажере: 3-4 подхода по 10-12 повторений.'
        elif day_of_week == 4:
            task = 'День 5: Кардио и верхняя часть тела\n- 20-30 минут интенсивной кардио-тренировки, такой как бег, плавание или велосипед.\n- Жим штанги на грудь: 3-4 подхода по 8-10 повторений.\n- Тяга штанги в наклоне: 3-4 подхода по 8-10 повторений.\n- Армейский жим: 3-4 подхода по 8-10 повторений.\n- Разгибания рук со штангой: 3-4 подхода по 10-12 повторений.'
        elif day_of_week == 5:
            task = 'День 6: Отдых и растяжка\n- Позвольте своему организму восстановиться и отдохнуть. Можете сделать легкую прогулку или заняться другими активностями низкой интенсивности, чтобы оставаться в движении.\n- Посвятите время растяжке и гибкостным упражнениям, чтобы улучшить гибкость и снизить мышечное напряжение.'
        elif day_of_week == 6:
            task = 'День 7: Силовые тренировки всего тела\n- Жим штанги на грудь: 3-4 подхода по 8-10 повторений.\n- Тяга штанги в наклоне: 3-4 подхода по 8-10 повторений.\n- Приседания со штангой: 3-4 подхода по 8-10 повторений.\n- Подтягивания или тяга вертикальной тяги: 3-4 подхода по максимальному количеству повторений, чтобы развить силу верхней части тела.\n- Разгибания ног и сгибания на тренажере: 3-4 подхода по 10-12 повторений.'
    return task


bot = telebot.TeleBot('5781282342:AAE7AjPhxB7_UMGABAoqJa_loe2Of9nl5Og')

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, 'Привет! Я помогу тебе подобрать программу тренировок и меню на день.')

    # Отправка меню программ тренировок
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    reply_markup.add(telebot.types.KeyboardButton('Снижение веса'), telebot.types.KeyboardButton('Набор массы'), telebot.types.KeyboardButton('Поддержание формы'))
    bot.send_message(message.chat.id, 'Выберите программу тренировок:', reply_markup=reply_markup)
    bot.register_next_step_handler(message, handle_program_choice)

# Обработчик выбора программы тренировок
def handle_program_choice(message):
    program = message.text

    # Определение времени дня
    current_time = datetime.now()
    if current_time.hour < 12:
        time_of_day = 'завтрак'  # Утро
    elif current_time.hour < 18:
        time_of_day = 'обед'  # День
    else:
        time_of_day = 'ужин'  # Вечер

    # Отправка меню на завтрак/обед/ужин
    day_of_week = datetime.now().weekday()
    menu = get_menu(program, day_of_week, time_of_day)
    bot.send_message(message.chat.id, 'Меню на {}: {}'.format(time_of_day, menu))

    # Отправка задачи для тренировки на текущий день недели
    training_task = get_training_task(program, day_of_week)
    bot.send_message(message.chat.id, 'Задача для тренировки сегодня: {}'.format(training_task))

# Запуск бота
bot.polling()
