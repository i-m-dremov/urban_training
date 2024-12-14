from time import sleep

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст.
    """
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    """
    Класс Видео, содержащий атрибуты: заголовок. Продолжительность, секунда остановки, ограничение по возрасту.
    """
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    """
    Класс пользователя, содержащий атрибуты: список объектов User, список объектов Video, текущий пользователь.
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

# Метод log_in, принимает на вход аргументы: nickname, password и пытается найти пользователя в users
# с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

#Метод register, принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
# пользователя не существует(с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
# уже существует". После регистрации, вход выполняется автоматически.

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        self.users.append(User(nickname, password, age))
        self.current_user = User(nickname, password, age)

#Метод log_out для сброса текущего пользователя на None.

    def log_out(self):
        self.current_user = None

#Метод add, который принимает неограниченное количество объектов класса Video и все добавляет в videos, если с таким \
# же названием видео ещё не существует. В противном случае ничего не происходит.

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

#Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
# слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best'(не учитывать регистр).

    def get_videos(self, find_text: str):
        list_title = []
        for video in self.videos:
            if find_text.lower() in video.title.lower():
                list_title.append(video.title)
        return list_title

#Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.

    def watch_video(self, name_video: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for j in self.videos:
            if j.title == name_video:
                if j.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for t in range(1, j.duration + 1):
                    sleep(1)
                    print(t, end=' ')
                sleep(1)
                print('Конец видео')

if __name__ == '__main__':

#Код для проверки:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200) #Добавляем первое видео в список
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True) #Добавляем второе видео в список
# Добавление видео
    ur.add(v1, v2)
# Проверка поиска
    print(ur.get_videos('лучший')) # ['Лучший язык программирования 2024 года']
    print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13) # Вам нет 18 лет, пожалуйста покиньте страницу
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25) # Войдите в аккаунт, чтобы смотреть видео
    ur.watch_video('Для чего девушкам парень программист?') # 12345678910 # Конец видео
# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user) # Пользователь vasya_pupkin уже существует
# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

