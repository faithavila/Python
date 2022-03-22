
# Description of Program: This program converts english units to metric and vice versa to the third decimal place.
def Project1():
    #introduction section
    print("")
    print("Welcome to the English/Metric conversion utility.")
    print("")
    print("This utility allows you to convert between English units \
    (miles, feet, inches) and metric units (kilometers, meters, \
    centimeters).")
    print("")
    print("------------------------------------------------------------")
    print("")


    #asking intro
    while True:
        print("Which direction would you like to convert:")
        print("   For English to Metric type: 1")
        print("   For Metric to English type: 2")
        print("   To Quit type:               3")
        print("")
        numin = input("Input your answer (1, 2, or 3): ")

    #first possible option
        #asking for initial
        if numin == "1":
            while True:
                print("")
                print("Select English units to convert to metric equivalent:")
                print("   For miles type:  1")
                print("   For feet type:   2")
                print("   For inches type: 3")
                print("")

                engnum = (input("   Choose English units to convert (1, 2 or 3): "))

                #labeling of engnum
                if engnum == "1":
                    engnum = "miles"
                    break
                elif engnum == "2":
                    engnum = "feet"
                    break
                elif engnum == "3":
                    engnum = "inches"
                    break
                else:
                    print("")
                    print("ERROR: Answer must be 1, 2, or 3. Try again.")

                #asking for second
            while True:
                print("")
                print("Convert to which metric units:")
                print("   For kilometers type:  1")
                print("   For meters type:      2")
                print("   For centimeters type: 3")
                print("")

                secnum = (input("   Choose target metric units (1, 2 or 3): "))
                print("")

                #labeling of secnum
                if secnum == "1":
                    secnum = "kilometers"
                    break
                elif secnum == "2":
                    secnum = "meters"
                    break
                elif secnum == "3":
                    secnum = "centimeters"
                    break
                else:
                    print("")
                    print("ERROR: Answer must be 1, 2, or 3. Try again.")

            #asking for quantity
            third = eval(input("Enter the number of " + engnum + " to convert to " + secnum + ": "))
            print("")
            
            #conversion to meters from feet
            if engnum == "miles":
                new = (third * 5280 * .3048)
            elif engnum == "feet":
                new = (third * .3048)
            elif engnum == "inches":
                new = ((third / 12) * .3048)

            #conversion of meters to final
            if secnum == "kilometers":
                final = new / 1000
            elif secnum == "meters":
                final = new
            elif secnum == "centimeters":
                final == new * 1000

            print("RESULT:", third, engnum, "=", format(final, "0.3f"), secnum)
            print("")
            print("------------------------------------------------------------")
            print("")

    #option 2
        #asking for initial
        elif numin == "2":
            while True:
                print("")
                print("Select metric units to convert to English equivalent:")
                print("   For kilometers type:  1")
                print("   For meters type:      2")
                print("   For centimeters type: 3")
                print("")

                metric = (input("   Choose metric units to convert (1, 2 or 3): "))

                #translation
                if metric == "1":
                    metric = "kilometers"
                    break
                elif metric == "2":
                    metric = "meters"
                    break
                elif metric == "3":
                    metric = "centimeters"
                    break
                else:
                    print("")
                    print("ERROR: Answer must be 1, 2, or 3. Try again.")

            #asking for second
            while True:
                print("")
                print("Convert to which English units:")
                print("   For miles type:  1")
                print("   For feet type:   2")
                print("   For inches type: 3")
                print("")

                secnum = (input("   Choose target English units (1, 2 or 3): "))
                print("")

                #translation
                if secnum == "1":
                    secnum = "miles"
                    break
                elif secnum == "2":
                    secnum = "feet"
                    break
                elif secnum == "3":
                    secnum = "inches"
                    break
                else:
                    print("")
                    print("ERROR: Answer must be 1, 2, or 3. Try again.")

            #asking for quantity
            third = eval(input("Enter the number of " + metric + " to convert to " + secnum + ": "))
            print("")
            
            #conversion from meters to feet
            if metric == "kilometers":
                new = (third * 1000 * 3.28084)
            elif metric == "meters":
                new = (third * 3.28084)
            elif metric == "centimeters":
                new = ((third / 100) * 3.28084)

            #conversion of feet to final
            if secnum == "miles":
                final = new / 5280
            elif secnum == "feet":
                final = new
            elif secnum == "inches":
                final = new * 12

            #print final result
            print("RESULT:", third, metric, "=", format(final, "0.3f"), secnum)
            print("")
            print("------------------------------------------------------------")
            print("")

        elif numin == "3":
            print("")
            print("Thanks for using our convertor. Goodbye!")
            print("")
            break

    #neither nor
        else:
            print("")
            print("ERROR: Answer must be 1, 2, or 3. Try again.")
            print("")
            print("------------------------------------------------------------")
            print("")

Project1()   


