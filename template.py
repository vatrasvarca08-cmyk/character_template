import random
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    count_card=int(input("сколько карточек вы хотите создать: "))
    os.makedirs('characters',exist_ok=True)
    for number in range(count_card):
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('template.html')
        clases_base={
            'маг':{
                'skills':['Стрела ледяного огня','Снятие проклятие','Огненный взрыв','Обледенение','Ледяное копье''Конус холода', 'Прилив сил', 'Морозный доспех'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence': 15,
                'luck':random.randint(1,3),
                'temper':random.randint(1,3),
                'image':'../images/wizard.png'
            },
            'воин': {
                'skills':['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                'strength':15,
                'agility':random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck':random.randint(1,3),
                'temper':random.randint(1,3),
                'image':'../images/warrior.png'
            },
            'лучник': {
                'skills':['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                'strength':random.randint(1,3),
                'agility':15,
                'intelligence': random.randint(1,3),
                'luck':random.randint(1,3),
                'temper':random.randint(1,3),
                'image':'../images/archer.png'
            },
            'асассин': {
                'skills':['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck':15,
                'temper':random.randint(1,3),
                'image':'../images/assasin.png'
            },
            'бард': {
                'skills':['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                'strength':random.randint(1,3),
                'agility':random.randint(1,3),
                'intelligence': random.randint(1,3),
                'luck':random.randint(1,3),
                'temper':15,
                'image':'../images/bard.webp'
            }

            }
        character_name=input("введите имя персонажа: ")
        races=["орк","человек","эльф"]
        character_race=int(input("выберите расу 1.орк 2. человек 3. эльф:" ))
        classes=["лучник","асассин","бард","воин","маг" ]
        character_class=int(input("выберите класс 1.лучник 2.асассин 3.бард 4.воин 5. маг:" ))
        skills=clases_base[classes[character_class-1]]["skills"]
        skills_sample=random.sample(skills,3)
        rendered_page = template.render(
            name=character_name,
            race=races[character_race-1],
            character_class=classes[character_class-1],
            strength=clases_base[classes[character_class-1]]["strength"],
            agility=clases_base[classes[character_class-1]]["agility"],
            intelligence=clases_base[classes[character_class-1]]["strength"],
            luck=clases_base[classes[character_class-1]]["luck"],
            temper=clases_base[classes[character_class-1]]["temper"],
            image=clases_base[classes[character_class-1]]["image"],
            first_skill=skills_sample[0],
            second_skill=skills_sample[1],
            third_skill=skills_sample[2],
        )





        with open(f'characters/index{number+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()