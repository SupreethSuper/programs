import math
# taking input
first_digit = int(input("enter the first digit "))
second_digit = int(input("enter the second digit "))
third_digit = int(input("enter the third digit "))
# common difference checking
common_dif_val_check_one = second_digit - first_digit
common_dif_val_check_two = third_digit - second_digit
# common ratio checking
common_ratio_val_check_one = (second_digit / first_digit)
common_ratio_val_check_two = (third_digit / second_digit)
# checking weather it is an ap
if common_dif_val_check_two == common_dif_val_check_one and common_dif_val_check_two != 0 and common_ratio_val_check_one != 0:
    print("it is an ap")
    print("the cd is ", common_dif_val_check_two)
    ask_does_he_need_the_th_term_in_ap = input("do you want some th term (y/n) ").lower()
    if ask_does_he_need_the_th_term_in_ap == "y":
        ask_what_term = float(input("which term do you need "))
        print("the ", ask_what_term, "th is", first_digit + ((ask_what_term - 1) * common_dif_val_check_two))
    elif ask_does_he_need_the_th_term_in_ap == "n":
        asking_does_he_need_the_series_in_ap = input("do you need the series (y/n) ").lower()
        if asking_does_he_need_the_series_in_ap == "y":
            till_which_term_does_he_need_the_series = int(input("till what term do you need the series "))
            n = 0
            for i in range(till_which_term_does_he_need_the_series):
                print(first_digit + (n * common_dif_val_check_two))
                n = n + 1
        elif asking_does_he_need_the_series_in_ap == "n":
            asking_weather_he_needs_the_sum_of_the_series_in_ap = input(
                "do you need the sum of the series (y/n)? ").lower()
            if asking_weather_he_needs_the_sum_of_the_series_in_ap == "y":
                val_of_n = int(input("what is the number of terms"))
                new_val_of_n = val_of_n / 2
                in_brackets = ((2 * first_digit) + ((val_of_n - 1) * common_dif_val_check_one))
                sum_of_ap = new_val_of_n * in_brackets
                print("the sum of your ap till the value of ", val_of_n, "is: ", sum_of_ap)
            elif asking_weather_he_needs_the_sum_of_the_series_in_ap == "n":
                asking_hp = input("do you want hp (y/n)? ").lower()
                if asking_hp == "y":
                    print("first term = ", 1 / first_digit)
                    print("second term = ", 1 / second_digit)
                    print("third term = ", 1 / third_digit)
                    ask_nth_term_hp = input("do you want to know the nth term of this hp (y/n) ? ").lower()
                    if ask_nth_term_hp == "y":
                        n_th = int(input("what is the value of n "))
                        print("the characteristics of this hp are : ")
                        print("the ", n_th, " term is ", (1 / (first_digit + ((n_th - 1) * common_dif_val_check_two))))
                        difference_inverse = 1 / common_dif_val_check_two
                        numerator = (2 * first_digit) + (((2 * n_th) - 1) * common_dif_val_check_two)
                        denominator = (2 * first_digit) - common_dif_val_check_two
                        division = numerator / denominator
                        division_with_log = math.log10(division)
                        sum_n = difference_inverse * division_with_log
                        print("the sum of ", n_th, "of an hp is ", sum_n)
                        series_hp = input("do you want the series (y/n) ? ").lower()
                        if series_hp == "y":
                            till_which_term_does_he_need_the_series_hp = int(
                                input("till what term do you need the series "))
                            n = 0
                            for i in range(till_which_term_does_he_need_the_series_hp):
                                print(1 / (first_digit + (n * common_dif_val_check_two)))
                                n = n + 1
                        elif series_hp == "n":
                            print("there is nothing else")
                            exit()
                        else:
                            print("invalid input")
                elif asking_hp == "n":
                    print("there is nothing else")
                    exit()
                else:
                    print("invalid input")
            else:
                print("invalid input")

        else:
            print("invalid input")
    else:
        print("invalid input")
# checking weather its gp
if common_ratio_val_check_one == common_ratio_val_check_two and common_ratio_val_check_one != 1 and common_ratio_val_check_two != 1:
    print("it is a gp with common ratio ", common_ratio_val_check_one)
    ask_does_he_need_the_th_term_in_gp = input(
        "do you need the nth term of the series (y/n)? or press any other key for more options ").lower()
    if ask_does_he_need_the_th_term_in_gp == "y":
        val_of_nth_in_gp = int(input("what is the value of n "))
        val_of_new_nth_in_gp = val_of_nth_in_gp - 1
        print("the value of the ", val_of_nth_in_gp, " th term is ",
              first_digit * (common_ratio_val_check_one ** val_of_new_nth_in_gp))
    elif ask_does_he_need_the_th_term_in_gp == "n":
        sum_of_gp = input("do you need the value of n terms in gp (y/n)? ").lower()
        if sum_of_gp == "y":
            val_of_n_in_sn = int(input("what is the value of n in sn "))
            if common_ratio_val_check_one > 1 and common_ratio_val_check_two != 1:
                sn_of_gp = first_digit * (
                            ((common_ratio_val_check_two ** val_of_n_in_sn) - 1) / (common_ratio_val_check_two - 1))
                print("the sum of ", val_of_n_in_sn, " th terms in gp is ", sn_of_gp)
            elif common_ratio_val_check_two < 1 and common_ratio_val_check_two != 1:
                sn_of_gp = first_digit * (
                            (1 - (common_ratio_val_check_two ** val_of_n_in_sn)) / (1 - common_ratio_val_check_two))
                print("the sum of ", val_of_n_in_sn, " th terms in gp is ", sn_of_gp)
    else:
        any_other_options = input("do you want the series of the gp (y/n)? ").lower()
        if any_other_options == "y":
            val_of_n_in_gp = int(input("what is the val of n "))
            x = 0
            for i in range(val_of_n_in_gp):
                print(first_digit * (common_ratio_val_check_one ** x))
                x = x + 1
# constant progression
if first_digit == second_digit == third_digit:
    print("it is a constant progression")
    print('''here:
common difference = 0
common ratio = 1''')
# special series
else:
    print("special series")