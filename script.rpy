﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('Мага', color="#c8ffc8")
define c = Character('Клауд', color="#1f2b5e")
define author = Character(None, kind=nvl)
define z = Character('Запись', color="#34b7eb")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
init:
    $ left2 = Position(xalign =-0.2, yalign = 1.1)
    $ right2 = Position(xalign =1.2, yalign = 1.1)
# Игра начинается здесь:
label start:

    scene bg dark

    '''Пролог'''
    '''{cps=25}Подросток Мага долгое время мечтал стать магом. Его путь только начинается и чтобы погрузиться в жизнь настоящего мага, он решил исследовать руины бывшего храма.'''
    scene bg 2
    with fade

    show maga1
    with dissolve

    m "Что это?"

    "Мага кладет камень в сумку и идет к магу, который проживает в его деревушке."

    hide maga1
    with dissolve

    scene bg 1
    with fade

    "Мага посещает избу мага по прозвищу Клауд."

    show maga2 at left2
    with dissolve

    m "Ох, зря я сюда полез..."

    show cloud3 at right2
    with dissolve

    c "Не часто я встречаю гостей. Для чего ты сюда пришел, мой дорогой друг?"

    m "Эээ... Здравствуйте, меня зовут Мага."

    "Клауд смеется, Мага чувствует себя неловко."

    c "Ого! А что это за камень у тебя в сумочке?"

    m "Вот как раз за этим я к вам и пришел! Я нашел его в руинах храма Каер. {w}Я подумал, может вы сможете подсказать мне как я могу его использовать... Ну или возможно он будет нужным вам"

    c "Ох, мой дорогой друг. Этот камень помогает использовать магию данных. {w}Я вижу что тебя это определенно интересует, что ты пошел аж в далекий храм. Хочешь я обучу тебя?"

    m "Было бы славно!"

    c "Начнем с простого. Бери камень и пойдем со мной."

    hide cloud3
    with moveoutright

    hide maga2
    with moveoutright

    scene bg dark
    with fade

    "Мага и Клауд приходят в сад."

    scene bg 3
    with fade

    show cloud3 at right2
    with moveinright

    show maga1 at left2
    with moveinleft

    c "Для начала тебе нужно научиться собирать и анализировать данные. Возьми мою книгу о растениях и направь энергию на этот сад. {w}Используя список и полученные данные, предскажи какие растения здесь будут процветать при здешних условиях."

    "Мага направляет энергию на небольшой участок и получает условия которые присутвуют там - редкие дожди, достаточное корневое питание, благоприятный режим воздушного питания"
    "Открывается список растений, Мага выбирает данные условия."

    hide maga1
    with dissolve

    hide cloud3
    with dissolve

    scene bg book
    with fade

    "Список сокращается до трех растений."

    m "Я понял! Здесь могут расти глазороза, тигродуванчик и драконий хвост!"

    c "Молодец, Мага! Ты справился со своей задачей, дальше нас ждет больше работы."

    #hide maga1
    #with dissolve
    #hide cloud3
    #with dissolve

    scene bg dark
    with fade

    jump act1

    return

label act1:

    "Глава 1. Обучение."

    "На следующий день Мага вернулся к Клауду чтобы продолжить обучение."

    scene bg 4
    with fade

    show cloud3 at right2
    with dissolve

    show maga2 at left2
    with dissolve

    c "Молодой маг, сегодня наше почти первое магическое занятие. Я научу тебя, как применять магию данных."

    m "Кажется интересно, но я ничего не знаю об обработке данных. Как мне начать?"

    c "Не волнуйся, я научу тебя. Представь, что у нас есть огромная база данных с информацией о монстрах, которые населяют этот мир."

    c "Наша задача - определить слабое место каждого монстра и выбрать подходящее заклинание для победы. Начни с изучения данных о сильных и слабых сторонах монстров."

    m "А как я это сделаю?"

    c "Вот перед тобой компьютер с программой, которая позволит тебе анализировать данные. Используй методы машинного обучения, чтобы выявить закономерности и сделать выводы о слабых сторонах каждого монстра. Затем выбери подходящий заклинание для битвы."

    m "Понял, начну анализировать данные и выберу лучшие заклинания для битв. Спасибо за помощь!"

    hide maga2

    hide cloud3

    scene bg comp
    with fade
    
    "— Перед Магой открывается программа с тремя монстрами —"

    "— 1-ый монстр Паровик, 2-ой монстр Стеклянное сердце, 3-ий монстр Огромный тролль—"

    m "Так... Паровик - монстр превращающийся в пар... Атакует быстро с разных сторон. Ага... Тогда нужно себя максимально обезопасить и в первую очередь использовать заклинание защиты!"

    "—Мага вводит в компьютер 'Заклинания защиты', вылезают два заклинания с уровнем 'легкие'—"

    m "Заклинания 'Кристальная оболочка' - защита в виде шара вокруг и 'Щит духа Рыцаря' - защита в виде щита направленного в сторону взгляда."

    m "Раз Паровик может нападать с разных сторон, то лучше использовать защиту вокруг. Так, это заклинание называлось..."

    "—перед игроком выбор между 'Кристальная оболочка' и 'Щит духа Рыцаря'—"

    m "Затем надо использовать заклинание чтобы остановить Паровика и вернуть его в простое состояние."

    m "Посмотрю оглушающую атаку..."

    "—Мага вводит оглушающие атаки—"

    "—Выходит заклинание 'Парадоксо' - обездвиживает противника и делает его уязвимым к атакам.—"

    m "Я понял! Нужно использовать защищающее заклинание, чтобы обезопасить себя, а затем атаковать оглушающей атакой! А после можно уже использовать любые заклинания для атаки."

    m "Посмотрим про Стеклянное сердце."

    "—Описание: монстр в виде каменного голема с ледяным сердцем.—"

    m "Тогда надо просто атаками целиться в сердце!"

    "—Мага вводит точные атаки, выходит заклинание 'Маленькая звезда' - быстрая и точная атака.—"

    "—Мага вводит Огромный тролль—"

    "—Большой тролль на маленьких ножках—"

    m "Ага! Надо использовать заклинания чтобы сбить его с ног — поиск сильных заклинаний, выходит 'Воздушное цунами' - очень сильный порыв ветра в определенную область."

    scene bg 4
    
    show maga2 at left2
    with dissolve

    show cloud3 at right2
    with dissolve

    m "Прекрасно! Теперь я знаю что надо использовать в сражении с тремя монстрами!"

    c "Молодец! Ты быстро учишься, на сегодня твое занятие завершается, иди домой и передохни. Встретимся завтра."

    hide maga2
    with moveoutleft

    hide cloud3
    with moveoutright

    scene bg tropinka
    with fade

    show maga1 at left2
    with moveinleft

    "—Мага идет домой по тропинке и навстречу к нему выбегает гоблин с большой головой—"

    show goblin at right2
    with moveinright

    "—Гоблин злобно смотрит на Магу—"

    m "О нет... Это же северный гоблин, в нашей округе немало людей пострадало от их проделок. {w}Эти гоблины очень умные, но почти неподвижные из-за своей головы и вместо простой атаки их цель - грабеж."

    m "Надо что-то придумать..."

    menu:
        "Что делать?"

        "Он очень медленный и у него слишком большая голова, может попробовать попасть по ней камнем...":
            
            "Мага поднимает камень и кидает прямо в голову гоблина, гоблин падает без сознания."
            
            hide goblin
            with dissolve

            m "Я смог правильно оценить ситуацию и после анализа противника я успешно одолел его!"

        "Я залезу на дерево!":
            
            "Мага залезает на дерево, но гоблин закидывает его камнями, Мага падает после чего Гоблин крадет его сбережения..."
            
            hide goblin
            with dissolve

            m "Видимо мне предстоит еще многому научится.. На эти деньги я хотел купить себе еды!"

    "—Мага возвращается домой—"
    
    scene bg dark
    with fade

    "На следующий день..."

    scene bg 5
    with fade

    show cloud5 at right2
    with dissolve

    show maga4 at left2
    with dissolve

    c "Привет, юный маг! Сегодня я продолжу учить тебя, как использовать магию."

    c "Давай начнем с примера. Представь, что у нас есть огромный набор данных о погоде в разных регионах. Мы хотим предсказать, будет ли завтра дождь. Каким образом мы можем это сделать?"

    m "Данные о погоде собираются каждый день, может можно использовать их?"

    c "Верно! Ты можешь использовать эти данные для обучения модели, которая сможет предсказывать погоду на основе различных факторов, таких как температура, влажность и атмосферное давление."

    c "Но сегодня мы будем не этим, это была просто проверка твоих знаний."

    c "Недавно мои коллеги подарили мне несколько артефактов. Сегодня мы будем заниматься классификацией магических артефактов с помощью магии данных. Ты можешь научиться отличать добрые артефакты от злых по их характеристикам и влиянию на окружающую среду."

    c "Поищи записи об этих артефактах в моем компьютере, может быть ты найдешь что-то."

    m "Ну что ж, приступим!"

    hide maga4
    with dissolve

    hide cloud5
    with dissolve

    scene bg comp
    with fade

    "Мага садится за компьютер."

    m "Первый артефакт называется 'Лунная лампа', посмотрим..."

    "Мага вводит название и видит одну запись..."

    "Запись от Величайшего Колдуна Кузя Лакомкин"
    z "Нашел эту лампу в пещере кристаллов, вокруг нее было много растений, мне понравилось как она светит и я забрал ее к себе домой, ведь у меня почти нет света..."

    z "Странно что на следующий день у меня дома на месте, где находилась эта лампа выросли цветы, у меня не получалось их вывести 5 лет!"

    z "Может эта лампа несет удачу или магический свет? Я положил эту лампу в пещеру с полной темнотой и вокруг раскинул зерна моей любимой кукурузы, через 3 дня я нашел урожай моей хрустящей кукурузы!'"

    scene bg 5
    with fade

    show cloud5 at right2
    with dissolve
    
    show maga4 at left2
    with dissolve

    menu:
        m "Наверное, этот артефакт..."

        "Позволяет выращивать растения в темноте.":

            m "Учитель, я понял, эта лампа - артефакт, который позволяет выращивать растения в темноте!"

            c "Точно! Вчера в моем сундуке проросли ростки хотя там абсолютная темнота, спасибо, Мага!"

            m "Пожалуйста, учитель! Посмотрю следующий артефакт."

        "Приносит удачу.":
            
            m "Учитель, я понял, эта лампа - артефакт, который приносит удачу!"

            c "Оу, это точно не так! Вчера я провел весь день с этой лампой за поясом, но несмотря на удачу про которую ты говоришь, я не смог выиграть в денежное колесо, когда был в таверне! Мало того, вчера я три раза споткнулся у порога своего дома!"

            m "Извините, учитель... Со следующим артефактом я поработаю получше!"

    "Мага берет в руки следующий артефакт."


    return
