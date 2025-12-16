while True:
    language = input("please select a language between persian and english, type pe, or persian for persian, type en, or english for english")
    if language.lower().strip() in ["en", "english"]:
        question = input("do you want to see when number will be count? type yes or no")
        counter = 0
        user_counts = input("if you press enter, number will be count, and for end, type end to end counting")
        if user_counts == "":
            counter += 1
            if question.lower().strip() == "yes":
                print(f"Current count: {counter}")
        while True:
            user_counts = input("")
            if user_counts.strip() == "":
                counter += 1
                if question.lower().strip() == "yes":
                    print(f"Current count: {counter}")
            elif user_counts.strip() == "end":
                print(f"Final result is {counter}")
                break
        finish = input("Counter is finished, type 'exit' to close: ")
        while finish.strip() != "exit":
            finish = input("Please type 'exit' to close: ")
        print("Program closed!")
        break
    elif language.lower().strip()in ["pe", "persian"]:
        question = input("آیا دوست دارید شمارش اعداد رو در همون لحظه ببینید؟ بله یا خیر رو توی این ادیت باکس تایپ کنید")
        counter = 0
        user_counts = input("اگر اینتر بزنید، عدد شمارش میشه، و برای پایان شمارش، پایان رو بنویسید")
        if user_counts == "":
            counter += 1
            if question.strip() == "بله":
                print(f"شمارش کنونی، {counter}")
        while True:
            user_counts = input("")
            if user_counts.strip() == "":
                counter += 1
                if question.strip() == "بله":
                    print(f"شمارش کنونی، {counter}")
            elif user_counts.strip() == "پایان":
                print(f"نتیجه ی شمارش نهایی {counter} هست")
                break
        finish = input("شمارنده تمام شد، خروج رو برای بستن بنویسید")
        while finish.strip() != "خروج":
            finish = input("لطفاً خروج رو برای بسته شدن بنویسید")
        print("برنامه بسته شد!")
        break
    else:
        print("please just choose english or persian languages, and don't type other things, in this edit box")
    print("لطفاً فقط زبان فارسی یا انگلیسی رو انتخاب کنید و چیز دیگه ای ننویسید")