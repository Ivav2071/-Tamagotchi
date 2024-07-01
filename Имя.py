print("        ／＞　   フ\n\
　　　　| 　_　 _|\n\
　 　　／`ミ _x 彡\n\
　　 /　　　 　 |\n\
　  /　 ヽ　　 ﾉ\n\
　／|　　 |　|　|\n\
 | (￣ヽ＿_ヽ_)_)\n\
 ＼二つ")
name1 = input("Привет,придумай мне имя: ")
class cat:
    def __init__ (self, name, health = 0):
        self.name = name
        self.health = health
    def feed(self,food):
        self.health += food
    def punish(self,hp):
        self.health -= hp

cat1 = cat(name1,1)
print(f"у кота", cat1.name,"здоровье равно",cat1.health)

while cat1.health > 0:
    print("1 - Покормить кота")
    print("2 - Наказать кота")
    print("3 - Узнать его здоровье")
    ans = input("Введите номер действия: ")
    if ans == "1":
        foodCount = int(input("На сколько покормит? "))
        cat1.feed(foodCount)
    elif ans == "2":
        painCount = int(input("На вы хотите наказать кота? "))
        cat1.punish(painCount)
    elif ans == "3":
        print(cat1.health)
print("Прости,мне очень жаль",cat1.name,"погиб\n\
       _______\n\
      (   |   )\n\
      | --|-- |\n\
      |   |   |\n\
      ----------")
end = int(input("Нажмите Enter чтобы попрощаться c котом"))



