# Хэсэг 2: Энгийн Тооны Машин Программ

# Цэс интерфэйстэй ĸомандын мөрийн тооны машин хэрэгжүүлэх
# Дараах үйлдлүүдийг дэмжих:
# - Нэмэх
# - Хасах
# - Үржүүлэх
# - Хуваах (тэгээр хуваахыг зөв боловсруулах)
# - Зэрэгт дэвшүүлэх
# - Квадрат язгуур
# - Үлдэгдэл
# Хэрэглэгчид хоёр тоо оруулж, үйлдэл сонгох боломж олгох
# Үр дүнг тохирох форматтайгаар харуулах
# Буруу оролтуудыг зөв боловсруулах
# Тухайн ажиллагааны үеэр тооцооллын түүхийг хадгалах
# Тооцооллын түүхийг харах сонголт олгох
# Түүхийг цэвэрлэх сонголт оруулах
# Хэрэглэгчид программаас гарах боломж олгох

# Техниĸийн Шаардлагууд:

# Үйлдэл бүрт фунĸц ашиглах
# Зөв алдаа боловсруулалт хэрэгжүүлэх
# Тооцооллын түүхийг тохиромжтой өгөгдлийн бүтцэд хадгалах
# Уншихад хялбар болгох форматлалт хийх
# Тохиромжтой тайлбарууд оруулах
# Хэрэглэгчид ээлтэй гаралтын тулд тэмдэгт мөрийн форматлалт ашиглах

first_num = float(input("Та эхний тоогоо оруулна уу? "))
character = input("Та хийх тэмдэг ээ оруулна уу? ")
second_num = float(input("Та дараагийн тоогоо оруулна уу? "))

if character == "+":
    result = float(first_num + second_num)
    print(f"{first_num} + {second_num} = {result}")
elif character == "-":
    result = float(first_num - second_num)
    print(f"{first_num} - {second_num} = {result}")
elif character == "*":
    result = float(first_num * second_num)
    print(f"{first_num} * {second_num} = {result}")
elif character == "/":
    result = float(first_num / second_num)
    print(f"{first_num} / {second_num} = {result}")
elif character == "**":
    result = float(first_num ** second_num)
    print(f"{first_num} ** {second_num} = {result}")
elif character == "//":
    result = float(first_num // second_num)
    print(f"{first_num} // {second_num} = {result}")
elif character == "%":
    result = float(first_num % second_num)
    print(f"{first_num} % {second_num} = {result}")
else:
    result = "Тэмдэгт буруу байна"
